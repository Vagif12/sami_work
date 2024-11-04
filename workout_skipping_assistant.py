import streamlit as st
from services.data_ingestion_service import fake_system_data_workout_and_skipping_assistant
from services.ai_assistant_service import AssistantService
from services.ai_prompts_service import PromptType
from datetime import time, datetime

st.title("Workout Skipping Assistant")
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.session_history_summary = ""

# Initial AI assistant service with user data
assistant_svc = AssistantService(st.session_state.messages)
system_prompt_data = {"user_data":fake_system_data_workout_and_skipping_assistant["user_data"],"goal":fake_system_data_workout_and_skipping_assistant["goal"],"existing_plan":fake_system_data_workout_and_skipping_assistant["existing_plan"]}

st.write("Unable to do your workout today? No problem, we understand that life gets in the way. Just focus on yourself and let us help you stack on track with your running goals")
option = st.selectbox(
    "Are you unable to run due to one of the following reasons?",
    ("Injured? (Report the injury to Vortza can factor that into your workout plan)","Too tired or stressed? (You can postpone your run)","Busy? (You can postpone your run)"),
    index=None,
    placeholder="Please choose an option..",
)

if option == "Too tired or stressed? (You can postpone your run)":
    with st.chat_message("assistant"):
        st.write("I'd love to help you with adjusting your workout plan and give you more of a break. Would you like to share how you are feeling?")
    
    user_input = st.chat_input("Share your thoughts...")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            box = st.empty()
            result = assistant_svc.send_input(user_input, box, PromptType.WORKOUT_SKIPPING, system_prompt_data)
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": result})

else:
    if option == "Injured? (Report the injury to Vortza can factor that into your workout plan)":
        st.link_button("Injury report & pause plan","https://www.vortza.com/nl-NL")

    elif option == "Busy? (You can postpone your run)":
        workout_time = st.slider("Choose the time period for your next workout:",value=(time(11, 30), time(12, 45)))

        workout_date = st.date_input("Choose the date for your next workout:", datetime.now(),min_value=datetime.now())

        assistant_svc.adjustment_data = f"""
        New desired start time interval of next workout: Between {workout_time[0].strftime("%H:%M")} and {workout_time[1].strftime("%H:%M")}
        New desired start date of next workout: {workout_date}
        """

    if st.button("Continue"):
        with st.chat_message("assistant"):
            box = st.empty()
            result = assistant_svc.validate_input(box,system_prompt_data)

            st.session_state.messages.append({"role": "user", "content": assistant_svc.adjustment_data})
            st.session_state.messages.append({"role": "assistant", "content": result})
    

    if st.session_state.messages != []:
        user_input = st.chat_input("Share your thoughts...")
        if user_input:
            with st.chat_message("assistant"):
                box = st.empty()
                assistant_result = assistant_svc.send_input(user_input, box, PromptType.WORKOUT_SKIPPING, system_prompt_data)
        
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.session_state.messages.append({"role": "assistant", "content": assistant_result})
        
        st.markdown("""<form action="/" ><input class="st-emotion-cache-1vt4y43" type="submit" value="Manual re-adjustment" /></form>""",unsafe_allow_html=True)

