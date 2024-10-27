# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from crewai import Crew
from ecg_agents import ECGAgents, StreamToExpander
from ecg_tasks import ECGTasks
import streamlit as st
import sys
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

st.subheader("Let AI agents guide your educational and career journey!",
                 divider="rainbow", anchor=False)

with st.sidebar:
        st.header("👇 Enter your details")
        with st.form("my_form"):
            interests = st.text_input(
                "What are your interests?", placeholder="Programming")
            strengths = st.text_input(
                "What are your strengths?", placeholder="Good in Mathematics and Science")
            weaknesses = st.text_input(
                "What are your weaknesses?", placeholder="Not good in English")

            submitted = st.form_submit_button("Submit")

        st.divider()
        
        with st.expander("**⚠️ IMPORTANT NOTICE ⚠️**"):
            multi ='''This web application is developed as a proof-of-concept prototype.
            The information provided here is **NOT intended for actual usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.  
            \n**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**  
            \nAlways consult with qualified professionals for accurate and personalized advice.'''
            
            st.markdown(multi)


        st.divider()
        # Credits to joaomdmoura/CrewAI for the code: https://github.com/joaomdmoura/crewAI
        # st.sidebar.markdown(
        # """
        # Credits to [**@joaomdmoura**](https://twitter.com/joaomdmoura)
        # for creating **crewAI** 🚀
        # """,
        #     unsafe_allow_html=True
        # )

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
    with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
        with st.container(height=500, border=False):
            sys.stdout = StreamToExpander(st)
            ecg_crew = ECGCrew(interests, strengths, weaknesses)
            result = ecg_crew.run()
        status.update(label="✅ Action Plan Ready!",
                      state="complete", expanded=False)

    st.subheader("Here is your Action Plan 😎", anchor=False, divider="rainbow")
    st.markdown(result)

    st.subheader("Token Usage", divider="rainbow")
    st.write("Total tokens: ", result.token_usage.total_tokens)
    st.write("Prompt tokens: ", result.token_usage.prompt_tokens)
    st.write("Completion tokens: ", result.token_usage.completion_tokens)
    st.write("Successful Requests: ", result.token_usage.successful_requests)
