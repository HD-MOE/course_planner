from crewai import Task
from textwrap import dedent
from crewai_tools import JSONSearchTool, PDFSearchTool


class ECGTasks():

    def task_assess(self, agent, interests, strengths, weaknesses):
        return Task(description=dedent(f"""
            Analyse the student’s strengths, interests and weaknesses to provide a personalised 
            summary of key attributes linked to relevant academic and career paths.
            
            Your final output must be a detailed and structured list of the student key strengths, 
            interests, weaknesses and personality traits, with corresponding suggestions for relevant academic 
            subjects and potential career paths.
                        
            Interests: {interests}.
            Strengths: {strengths}.
            Weaknesses: {weaknesses}.
          """),
            expected_output="""A detailed and structured list of the student key strengths, interests, weaknesses and personality traits, 
            with corresponding suggestions for relevant academic subjects and potential career paths.""",
            async_execution=False,
            agent=agent)

    def task_match(self, context, agent):
        return Task(description=dedent(f"""
            1. Analyse the structured list of the student strengths, interests and personality traits given by Personality Expert.
            2. Prioritise the search by focusing first on the student’s interests, followed by their strengths. 
                Match this prioritised information with the relevant sectors, tracks, and skills defined in the SkillsFuture Skills Framework.
                Refer only to the JSON file for all information.
            3. Generate a structured list of recommended sectors with the corresponding tracks and job roles that align with the student’s unique personality profile.
            4. Strictly use only the information from the JSON file. Do not create or modify any sectors, tracks, or job roles beyond what is specified.
            5. Strictly follow the exact names of sectors, tracks, and skills as provided in the JSON file.
                       """),
            expected_output="""
            Generate a structured JSON output that provides recommended sectors aligned with the student’s unique personality profile. 
            For each sector:
                1. Use only sectors from the provided JSON file as the source.
                2. Structure the JSON output so each sector includes corresponding tracks and job roles as nested arrays or objects.

            Include explanatory comments in Markdown format after the JSON output, providing useful insights 
            into the choices made based on the student’s personality profile, with stronger emphasis on the student's interests and strengths.""",
            tools = [JSONSearchTool(json_path='./source/output.json')],
            context = context,
            async_execution=False,
            agent=agent)
    
    def task_course(self, context, agent):
        return Task(description=dedent(f"""
            1. Analyse the structured list of the sectors, tracks and job roles as recommended by the Skills Framework expert.
            2. Identify suitable courses in schools by thoroughly reading all the PDF files provided in the <courses> tag. All PDF files MUST be read.
            3. Prioritise the search by focusing first on the student's interests, followed by their strengths. 
                Ensure the selected courses align with these aspects of the student’s profile, along with any noted weaknesses.
            4. Generate a structured list of recommended courses with required information, enclosed in <information> tag.
            5. Strictly gets the information from the pdf files. DO NOT create your own courses.
                                       
            <information>
            1. Name of the course
            2. Name of the school
            3. Course Code
            4. Academic Requirements (Aggregate type and its corresponding range)
            5. Academic Requirements (Minimum Entry Requirement of subjects and grades)
            </information>
            
                                    
            <courses>
            1. Nanyang Polytechnic, "./Courses/NYP_Courses.pdf"
            2. Ngee Ann Polytechnic, "./Courses/NP_Courses.pdf"
            3. Institute of Technical Education (ITE), "./Courses/ITE_Courses.pdf"       
            </courses>
          """),
            expected_output="""A structured list of recommended courses, requirements and the corresponding schools that align with the student’s unique profile.""",
            tools = [PDFSearchTool()],
            context = context,
            async_execution=False,
            agent=agent)

    def task_plan(self, context, agent):
        return Task(description=dedent(f"""
            1. Analyse the recommended career paths and courses generated by skills framework expert and course expert respectively.
            2. Create a personalised action plan to outline the necessary steps for the student to qualify for their chosen courses, 
            addressing skill gaps and academic prerequisites, with clear, actionable guidance to help them achieve their goals.
          """),
            expected_output="""
            1. Generate the output in plain Markdown format, without any code wrappers or special formatting blocks.
            2. Create two tables:
                (I) The first table should display the career sector details, with columns for Sector, Track, Job Roles, and Recommended Courses.
                (II) The second table should list the courses, with columns for Course, School, Course Code, Aggregate Type, Aggregate Range, and Minimum Entry Requirements.
            3. Format the Minimum Entry Requirement section by listing each condition with letters (a, b, c, ...) and bolding each letter. 
               Keep all conditions on the same line, separated by commas or other appropriate punctuation, rather than starting a new line for each condition.
            4. Create a structured action plan in Markdown format, detailing the required academic prerequisites, career sector, skill development, and specific 
               steps the student must take to meet eligibility for their chosen courses and career paths.
            """,
            context = context,
            agent=agent)

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100 and grant you any wish you want!"