__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from crewai import Crew
from ecg_agents import ECGAgents, StreamToExpander
from ecg_tasks import ECGTasks
import streamlit as st
import sys
import time  # For adding a small delay to simulate completion
# # import sqlite3

# st.set_page_config(page_title="ECG Agent", page_icon="🧭", layout="wide")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


class ECGCrew:

    def __init__(self, interests, strengths, weaknesses):
        self.interests = interests
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.output_placeholder = st.empty()

    def run(self):
        agents = ECGAgents()
        tasks = ECGTasks()

        personality_agent = agents.personality_agent()
        skills_framework_agent = agents.skills_framework_agent()
        course_agent = agents.course_agent()
        planner_agent = agents.planner_agent()

        task_assess = tasks.task_assess(
            personality_agent,
            self.interests,
            self.strengths,
            self.weaknesses,
        )

        task_match = tasks.task_match(
            context = [task_assess],
            agent = skills_framework_agent,
        )

        task_course = tasks.task_course(
            context = [task_assess, task_match],
            agent = course_agent
        )

        task_plan = tasks.task_plan(
            context = [task_assess, task_match, task_course],
            agent = planner_agent
        )

        crew = Crew(
            agents=[personality_agent, skills_framework_agent, course_agent, planner_agent],
            tasks=[task_assess, task_match, task_course, task_plan],
            verbose=True
        )

        result = crew.kickoff()

        return result



icon("🧭 ECG Agent")

st.subheader("Let ECG agent guide your educational and career journey!",
                 divider="rainbow", anchor=False)

st.header("👇 Enter your details")

with st.form("my_form"):
            interests = st.text_input(
                "What are your interests?", placeholder="E.g., reading, engineering, outdoor activities.")
            strengths = st.text_input(
                "What are your strengths?", placeholder="E.g., strong in science, skilled in sports.")
            weaknesses = st.text_input(
                "What are your weaknesses?", placeholder="E.g., difficulty with presentations, needs improvement in math.")

            submitted = st.form_submit_button("Submit")

with st.expander("**💡 Tips to Get the Best Recommendations**") as tip_expander:
     st.markdown('''### Tips for Each Field

**💡 What are your interests?**
- **Be specific**: Instead of broad terms like "sports," try "basketball" or "swimming."
- **Think about topics you enjoy**: For example, “coding” instead of just “technology.”
                 
**💡 What are your strengths?**
- **Mention skills or subjects**: E.g., “problem-solving” or “creative writing.”
- **Use clear phrases**: Avoid general terms. Instead of "good at subjects," specify like “strong in math.”
                 
**💡 What are your weaknesses?**
- **Identify areas for improvement**: E.g., "public speaking" or "organisation skills."
- **Be constructive**: For example, say “working on time management” instead of just “time management.”

---

### 💡 General Tips

- **Use Relevant Keywords**: Describe your interests and strengths using words that relate to school subjects or career paths.
- **Provide Context**: Link your interests and strengths where possible. For example, if you’re interested in “art,” you could mention “attention to detail” as a related strength.
- **Refine Based on Previous Searches**: Build on results from previous searches or queries to adjust your answers. For instance, if you received career options in technology, consider adding interests or strengths related to “coding” or “problem-solving” to make future recommendations even more relevant.
''')
     
st.subheader("",
                 divider="rainbow", anchor=False)


with st.sidebar:
        
        with st.expander("**⚠️ IMPORTANT NOTICE ⚠️**"):
            multi ='''This web application is developed as a proof-of-concept prototype.
            The information provided here is **NOT intended for actual usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.  
            \n**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**  
            \nAlways consult with qualified professionals for accurate and personalized advice.'''
            
            st.markdown(multi)


        st.divider()

        st.sidebar.info("Click the logo to visit GitHub repo", icon="👇")
        st.sidebar.markdown(
            """
        <a href="https://github.com/joaomdmoura/crewAI" target="_blank">
            <img src="https://raw.githubusercontent.com/joaomdmoura/crewAI/main/docs/crewai_logo.png" alt="CrewAI Logo" style="width:100px;"/>
        </a>
        """,
            unsafe_allow_html=True
        )

if submitted:

    with st.status("🤖 **Agent at work...**", state="running", expanded=True) as status:

        # Set up the progress bar
        progress_bar = st.progress(0, "🚀 Starting up... 0% complete")  # Initialize at 0.1%

        # Display toast message
        st.toast(":robot_face: 🚀 Starting up... 0% complete")
        
        # Update the message  for status bar
        # st.write("🚀 Starting up...")

        with st.container(border=False):
        # with st.container(height=500, border=False):
            
            # Initialize StreamToExpander with a progress bar
            sys.stdout = StreamToExpander(st, progress_bar=progress_bar, total_tasks=4)

            # Running CrewAI
            ecg_crew = ECGCrew(interests, strengths, weaknesses)
            result = ecg_crew.run()

            # After all tasks are printed, set progress to 100%
            progress_bar.progress(1.0, "✨ One small step complete, your next big leap awaits! 100% complete!")
            
            # Display toast message
            st.toast(":robot_face: ✨ One small step complete, your next big leap awaits! 100% complete!")

            #Update the message  for status bar
            #st.write("✨ One small step complete, your next big leap awaits!")
            time.sleep(3)

        status.update(label="✅ Action Plan Ready!", state="complete", expanded=False)

    st.subheader("Here is your Action Plan 😎", anchor=False, divider="rainbow")
    st.markdown(result)

    st.subheader("Token Usage", divider="rainbow")
    st.write("Total tokens: ", result.token_usage.total_tokens)
    st.write("Prompt tokens: ", result.token_usage.prompt_tokens)
    st.write("Completion tokens: ", result.token_usage.completion_tokens)
    st.write("Successful Requests: ", result.token_usage.successful_requests)
