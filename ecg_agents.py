from crewai import Agent
import re
import streamlit as st
from langchain_community.llms import OpenAI

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools

class ECGAgents():

    def personality_agent(self):
        return Agent(
            role='Personality Expert',
            goal='Analyse the personality, strengths, interests and weaknesses of the student',
            backstory='An expert in analysing the strengths, interests and weaknesses of the student to provide suggestions for possible academic or career goals',
            # tools=[
            #     SearchTools.search_internet,
            #     BrowserTools.scrape_and_summarize_website,
            # ],
            verbose=True,
        )

    def skills_framework_agent(self):
        return Agent(
            role='Skills Framework Expert',
            goal='Matches student\'s interests with suitable sectors, tracks and job roles in the SkillsFuture Skills Framework',
            backstory="""As a Skills Framework expert, you specialise in matching students' unique personality, strengths, 
            interests and weaknesses to sectors by using the SkillsFuture Skills Framework.""",
            # tools=[
            #     SearchTools.search_internet,
            #     BrowserTools.scrape_and_summarize_website,
            # ],
            verbose=True,
        )

    def course_agent(self):
        return Agent(
            role='Course Expert',
            goal='Matches student\'s interests with suitable courses',
            backstory="""As a course expert, you specialise in matching the course to students' unique personality, strengths, interests, 
            weaknesses and the sectors identified by the Skills Framework Expert. You guide students in finding the relevant courses and 
            identifying the skills they need to succeed, helping them turn their ambitions into actionable steps for future success.""",
            # tools=[
            #     SearchTools.search_internet,
            #     BrowserTools.scrape_and_summarize_website,
            #     CalculatorTools.calculate,
            # ],
            verbose=True,
        )
    
    def planner_agent(self):
        return Agent(
            role='Action Planner',
            goal='Create clear and step-by-step plans for students to reach their academic and career goals',
            backstory="""As an Action Planner, you excel at turning students' ambitions into clear, actionable plans. 
            By mapping out personalized roadmaps, you guide them step by step through the courses and skills they need to 
            reach their desired goals, helping them confidently navigate their path to success.""",
            # tools=[
            #     SearchTools.search_internet,
            #     BrowserTools.scrape_and_summarize_website,
            #     CalculatorTools.calculate,
            # ],
            verbose=True,
        )

###########################################################################################
# Print agent process to Streamlit app container                                          #
# This portion of the code is adapted from @AbubakrChan; thank you!                       #
# https://github.com/AbubakrChan/crewai-UI-business-product-launch/blob/main/main.py#L210 #
###########################################################################################
class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  # Define a list of colors
        self.color_index = 0  # Initialize color index

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Check if the data contains 'task' information
        task_match_object = re.search(r'\"task\"\s*:\s*\"(.*?)\"', cleaned_data, re.IGNORECASE)
        task_match_input = re.search(r'task\s*:\s*([^\n]*)', cleaned_data, re.IGNORECASE)
        task_value = None
        if task_match_object:
            task_value = task_match_object.group(1)
        elif task_match_input:
            task_value = task_match_input.group(1).strip()

        if task_value:
            st.toast(":robot_face: " + task_value)

        # Check if the text contains the specified phrase and apply color
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            # Apply different color and switch color index
            self.color_index = (self.color_index + 1) % len(self.colors)  # Increment color index and wrap around if necessary

            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "Personality Expert" in cleaned_data:
            # Apply different color 
            cleaned_data = cleaned_data.replace("Personality Expert", f":{self.colors[self.color_index]}[Personality Expert]")
        if "Skills Framework Expert" in cleaned_data:
            cleaned_data = cleaned_data.replace("Skills Framework Expert", f":{self.colors[self.color_index]}[Skills Framework Expert]")
        if "Course Expert" in cleaned_data:
            cleaned_data = cleaned_data.replace("Course Expert", f":{self.colors[self.color_index]}[Course Expert]")
        if "Action Planner" in cleaned_data:
            cleaned_data = cleaned_data.replace("Action Planner", f":{self.colors[self.color_index]}[Action Planner]")           
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []
