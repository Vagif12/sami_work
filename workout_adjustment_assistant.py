import streamlit as st
from services.data_ingestion_service import fake_system_data_workout_and_skipping_assistant
from services.ai_assistant_service import AssistantService
from services.ai_prompts_service import PromptType

st.title("Workout Adjustment Assistant")
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.session_history_summary = ""

# Initial AI assistant service with user data
assistant_svc = AssistantService(st.session_state.messages)
system_prompt_data = {"user_data":fake_system_data_workout_and_skipping_assistant["user_data"],"goal":fake_system_data_workout_and_skipping_assistant["goal"],"existing_plan":fake_system_data_workout_and_skipping_assistant["existing_plan"]}

option = st.selectbox(
    "Help us personalize your workouts to your liking. What would you like to modify?",
    ("Workout Duration & Distance", "Workout Intensity", "Rest", "Run Type", "Pace", "I'd like to adjust something else"),
    index=None,
    placeholder="Please choose an option..",
)

st.write(f"summary: {st.session_state.session_history_summary}")

if option == "I'd like to adjust something else":
    with st.chat_message("assistant"):
        st.write("I'd love to help you with adjusting your workout plan. What would you like to adjust?")
        st.write("""For example, specific exercises, run type, duration, heart rate zones, pace, etc.""")
    
    user_input = st.chat_input("Share your thoughts...")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            box = st.empty()
            result = assistant_svc.send_input(user_input, box, PromptType.WORKOUT_ADJUSTMENT, system_prompt_data)
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": result})

else:
    if option == "Workout Duration & Distance":
        duration = st.slider("Adjust the desired workout duration **in minutes**.", 0, 360, 60)
        distance = st.slider("Adjust the desired workout distance **in kilometres**.", 0, 45, 5)

        assistant_svc.adjustment_data = f"""
        New desired workout duration in minutes: {duration}
        New desired workout distance in kilometres: {distance}
        """

    elif option == "Workout Intensity":
        intensity = st.slider("Adjust the desired **RPE** for your workouts.", 0, 10, 5)

        assistant_svc.adjustment_data = f"""
        New desired workout intensity in RPE: {intensity}
        """

    elif option == "Rest":
        rest_period = st.slider("Adjust the rest duration between intervals **in seconds**.", 0, 300, 5)

        assistant_svc.adjustment_data = f"""
        New desired workout rest duration between intervals in seconds: {rest_period}
        """

    elif option == "Run Type":
        run_type = st.selectbox("Select the type of run you wish to perform",("Base run", "Recovery run", "Long run","Tempo run","Interval run","Fartlek","Hill Repeats","Progression run","Easy run"),index=None,
        placeholder="Please choose an option..")

        assistant_svc.adjustment_data = f"""
        New desired type of run : {run_type}
        """

    elif option == "Pace":
        pace = st.selectbox("Select your desired workout pace",("Tempo run pace", "Recovery pace","Interval pace","Easy run pace","Custom pace"),index=None,
        placeholder="Please choose an option..")

        assistant_svc.adjustment_data = f"""
        New desired workout pace: {pace}
        """

        if pace == "Custom pace":
            custom_pace = st.text_input("Write your custom pace")

            assistant_svc.adjustment_data = f"""
            New desired workout pace: {custom_pace}
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
                assistant_result = assistant_svc.send_input(user_input, box, PromptType.WORKOUT_ADJUSTMENT, system_prompt_data)
        
                st.session_state.messages.append({"role": "user", "content": user_input})
                st.session_state.messages.append({"role": "assistant", "content": assistant_result})
        
        st.markdown("""<form action="/" ><input class="st-emotion-cache-1vt4y43" type="submit" value="Manual re-adjustment" /></form>""",unsafe_allow_html=True)

