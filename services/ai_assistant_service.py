import os 
import openai
import streamlit as st
import time as t
from services.ai_prompts_service import AIPrompts,PromptType,InstructionType

openai.api_key = os.environ["OPENAI_API_KEY"]

class AssistantService:
    def __init__(self, chat_history: list) -> None:
        self.chat_history = chat_history
        self.llm = openai.OpenAI()
        self.session_history = chat_history
        self.session_history_summary = None
        self.adjustment_data = None

    def get_session_history(self) -> list:
        return self.session_history
    
    def validate_input(self,box, system_prompt_data: dict) -> str:
        system_prompt = AIPrompts.get_prompt(PromptType.VALIDATE_USER_INPUT,InstructionType.ASSISTANT,system_prompt_data)
        user_prompt = AIPrompts.get_prompt(PromptType.VALIDATE_USER_INPUT,InstructionType.USER,{"user_adjustments":self.adjustment_data})

        messages = [
            {"role":"system", "content":system_prompt},
            {"role":"user","content": user_prompt},
        ]

        response = self.llm.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True
        )

        collective_response = ""
        for chunk in response:
            if chunk.choices[0].finish_reason == "stop":
                break
            for c in chunk.choices[0].delta.content:
                collective_response += c
                t.sleep(.002)
                box.write(collective_response)

        return collective_response
    
    def summarize_session_history(self) -> str:

        system_prompt = AIPrompts.get_prompt(PromptType.SESSION_HISTORY_SUMMARIZATION_PROMPT,InstructionType.ASSISTANT,{})
        
        history_messages = self.session_history[-1] if self.session_history_summary else self.session_history

        user_prompt = AIPrompts.get_prompt(PromptType.SESSION_HISTORY_SUMMARIZATION_PROMPT,InstructionType.USER,{"messages":history_messages})

        messages = [
            {"role":"system", "content":system_prompt},
            {"role":"user","content": user_prompt},
        ]

        response = self.llm.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )

        if self.session_history_summary:
            self.session_history_summary = self.session_history_summary + '\n' + response.choices[0].message.content
        else:
            self.session_history_summary = response.choices[0].message.content
            
    def update_session_history(self) -> None:
        if len(self.chat_history) > 1:
            self.summarize_session_history()
            st.session_state.session_history_summary = self.session_history_summary
            self.session_history = self.session_history[-2:]
    
    def update_history(self, question: str, answer: str) -> None:
        self.chat_history.append((f"User: {question}", f"Assistant: {answer}"))
        self.session_history.append((f"User: {question}", f"Assistant: {answer}"))

        self.update_session_history()
    
    def send_input(self,user_input: str, box, prompt_type: PromptType ,system_prompt_data: dict) -> str:

        combined_history = [st.session_state.session_history_summary] + self.session_history

        system_prompt = AIPrompts.get_prompt(prompt_type,InstructionType.ASSISTANT,system_prompt_data)
        user_prompt = AIPrompts.get_prompt(prompt_type,InstructionType.USER,{"chat_history":combined_history,"user_input":user_input})

        messages = [
            {"role":"system", "content":system_prompt},
            {"role":"user","content": user_prompt},
        ]

        response = self.llm.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True
        )

        collective_response = ""
        for chunk in response:
            if chunk.choices[0].finish_reason == "stop":
                break
            for c in chunk.choices[0].delta.content:
                collective_response += c
                t.sleep(.002)
                box.write(collective_response)

        self.update_history(user_input,collective_response)        

        return collective_response
    