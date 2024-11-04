import streamlit as st
from services.ai_assistant_service import AssistantService
from services.ai_prompts_service import PromptType
from services.data_ingestion_service import fake_system_data_workout_plan_creation


st.title("Workout Plan Creation")
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.session_history_summary = ""
    st.session_state.first_response_called = False
    st.session_state.discussion_finished = False

running_level, running_reason, dedication_level, user_input,  = None, None, None, None

assistant_svc = AssistantService(st.session_state.messages)
system_prompt_data = {"user_data":fake_system_data_workout_plan_creation["user_data"]}

goal_option = st.selectbox(
    "Ready to set an exciting new running goal together? Let's make it happen.",
    ("I have a goal in mind", "I'm looking for some support to find my goal"),
    index=None,
    placeholder="Please choose an option..",
)


if goal_option == "I'm looking for some support to find my goal":
    
    running_level = st.selectbox(
    "How would you describe your current running level?",
    ("Amateur/beginner (expectations or requirements)", "Intermediate (expectations or requirements)","Advanced (expectations or requirements)","Not sure (further explanation)","I'm not sure (asisstant will help you decide)"),
    index=None,
    placeholder="Please choose an option..")

    if running_level:
        running_reason = st.selectbox(
        "Let's set your goal together! Can you describe why you want to take on running?",
        ("I'd love to set a new personal record for a specific distance", "I'm looking to take part/join a race","I want to run a longer distance that I've never ran before","Have a different reason in mind? Share it here!"),
        index=None,
        placeholder="Please choose an option..")
        
        if running_reason == "Have a different reason in mind? Share it here!":
                running_reason = st.text_input("Write your reason for running here...")
        
        if running_reason:
            dedication_level = st.selectbox(
            "How dedicated are you?",
            ("Casually improve my run (1/3 intensity)", "I am up for a challenge (2/3 intensity)","Reach my full potential (3/3 intensity)"),
            index=None,
            placeholder="Please choose an option..")
        
        if dedication_level:
            user_input = f"""

            User's Goal type: {goal_option}
            User's running level: {running_level}
            User's reason for running training: {running_reason}
            The user's current dedication level: {dedication_level}
            """
            
            if st.session_state.first_response_called == False:
                with st.chat_message("assistant"):
                    box = st.empty()
                    result = assistant_svc.send_input(user_input, box, PromptType.LIFESTYLE_DISCUSSION, system_prompt_data)
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.messages.append({"role": "assistant", "content": result})
                    st.session_state.first_response_called = True

            if st.session_state.messages != []:
                user_response = st.chat_input("Share your thoughts...")
                if user_response:
                    with st.chat_message("assistant"):
                        box = st.empty()
                        assistant_result = assistant_svc.send_input(user_response, box, PromptType.LIFESTYLE_DISCUSSION, system_prompt_data)
                
                        st.session_state.messages.append({"role": "user", "content": user_response})
                        st.session_state.messages.append({"role": "assistant", "content": assistant_result})
                
                if st.session_state.discussion_finished == False:
                    if st.button("Finish discussion and generate recommendations"):
                        st.session_state.discussion_finished = True
                

                if st.session_state.discussion_finished == True:
                    with st.chat_message("assistant"):
                        box = st.empty()
                        result = assistant_svc.send_input(user_input, box, PromptType.RUNNING_FREQUENCY_RECOMMENDATION, system_prompt_data)
                        st.session_state.messages.append({"role": "user", "content": user_input})
                        st.session_state.messages.append({"role": "assistant", "content": result})
                        st.session_state.first_response_called = True

                        

