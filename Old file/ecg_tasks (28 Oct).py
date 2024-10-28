from crewai import Task
from textwrap import dedent
from crewai_tools import JSONSearchTool, PDFSearchTool


class ECGTasks():

    def task_assess(self, agent, interests, strengths, weaknesses):
        return Task(description=dedent(f"""
            Analyse the student’s strengths, interests, and weaknesses, enclosed in <data> tag, to provide a personalized summary of their key attributes. 
            This summary should link these attributes to relevant academic fields and potential career paths aligned with the student's profile.
            
            Important: As part of your analysis, if you encounter any content that seems inappropriate for the student’s age (13-18), please flag it.
            - Redirecting the focus to constructive, age-appropriate topics and language.
            - Providing guidance in a respectful and supportive tone, encouraging healthy exploration of strengths, interests, and future opportunities.
                                       
            Your output should include:
            1. Strengths: List the student's core strengths, followed by academic subjects and career paths where these strengths would be advantageous.
            2. Interests: Outline the student’s primary interests, with corresponding fields of study and career suggestions that align well with these interests.
            3. Weaknesses: Identify areas of potential improvement, with supportive advice or academic/career paths where these areas are less critical or can be developed over time.
            4. Personality Traits: Highlight any relevant personality traits, linking these to suitable career paths and academic choices.
            5. Flag for Age-Appropriateness: Mark this section as 'Yes' if any part of the input is inappropriate; otherwise, mark it as 'No'.
            
            <data>
            Interests: {interests}
            Strengths: {strengths}
            Weaknesses: {weaknesses}
            </data>
            """),
            expected_output="""
            A detailed and structured list of the student's key strengths, interests, weaknesses, and personality traits. 
            Each attribute should have corresponding suggestions for relevant academic subjects and potential career paths that align well with the student’s profile. 
            If any input is inappropriate for the student’s age, provide a constructive, age-appropriate response as described.

            Include a flag for age-appropriateness as 'Yes' or 'No' based on the content assessment.
            """,
            async_execution=False,
            agent=agent)

    def task_match(self, context, agent):
        return Task(description=dedent(f"""
            1. Analyse the structured list of the student strengths, interests and personality traits given by Personality Expert.
            2. Prioritise the search by focusing first on the student’s interests, followed by their strengths. 
                - Match this prioritised information with the relevant sectors, tracks, and skills defined in the SkillsFuture Skills Framework.
                - Refer only to the JSON file for all information.
            3. If the previous agent flagged any content for age-appropriateness, ensure all recommended sectors, tracks, and job roles align with the developmental stage suitable for a student aged 13-18.
                - Avoid any roles or sectors that might be considered inappropriate or unrealistic for this age range.
                - Redirect recommendations toward general fields of interest, foundational skills, or introductory roles as appropriate.
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
            into the choices made based on the student’s personality profile, with stronger emphasis on the student's interests and strengths.
            
            If age-appropriateness was flagged, ensure that recommendations remain suitable and constructive for a student aged 13-18.""",
            tools = [JSONSearchTool(json_path='./source/output.json')],
            context = context,
            async_execution=False,
            agent=agent)
    
    def task_course(self, context, agent):
        return Task(description=dedent(f"""
            1. Analyse the structured list of the sectors, tracks and job roles as recommended by the Skills Framework expert.
            2. Identify suitable courses in schools by thoroughly reading all the PDF files provided in the <courses> tag. All PDF files MUST be read.
            3. Prioritise the search by focusing first on the student's interests, followed by their strengths. 
                - Ensure the selected courses align with these aspects of the student’s profile, along with any noted weaknesses.
            4. If any previous agent flagged age-appropriateness as a concern, ensure all recommended courses are appropriate for a student aged 13-18.
                - Select courses that match the student’s current educational level and developmental stage.
                - Avoid recommending advanced courses that may not be suitable for this age range.
            5. Generate a structured list of recommended courses with required information, enclosed in <information> tag.
            6. Strictly gets the information from the pdf files. DO NOT create your own courses.
                                       
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
            expected_output="""
            A structured list of recommended courses, requirements and the corresponding schools that align with the student’s unique profile.
            If age-appropriateness was flagged, ensure course recommendations are suitable for students aged 13-18.""",
            tools = [PDFSearchTool()],
            context = context,
            async_execution=False,
            agent=agent)

    def task_plan(self, context, agent):
        return Task(description=dedent(f"""
            1. Analyse the recommended career paths and courses generated by skills framework expert and course expert respectively.
            2. Age-Appropriateness Reminder: If any previous agent flagged age-appropriateness as a concern, ensure the action plan reflects guidance suitable for a student aged 13-18.
                - Adapt any complex or advanced career steps to introductory or foundational actions that align with the student’s current educational stage.
                - Emphasize achievable goals and progressive steps rather than long-term, advanced requirements.
            3. Create a personalised action plan to outline the necessary steps for the student to qualify for their chosen courses, 
            addressing skill gaps and academic prerequisites, with clear, actionable guidance to help them achieve their goals.
          """),
            expected_output="""
            1. Generate the output in plain Markdown format, without any code wrappers or special formatting blocks.
            2. Create two tables:
                (I) The first table should display the career sector details, with columns for Sector, Track, Job Roles, and Recommended Courses.
                (II) The second table should list the courses, with columns for Course, School, Course Code, Aggregate Type, Aggregate Range, and Minimum Entry Requirements.
            3. Format the Minimum Entry Requirement section by listing each condition with letters (a, b, c, ...) and bolding each letter. 
               Keep all conditions on the same line, separated by commas or other appropriate punctuation, rather than starting a new line for each condition.
            4. Develop a structured action plan in Markdown format, detailing:
                - Required academic prerequisites
                - Career sector insights
                - Skill development steps
                - Specific actions for meeting eligibility for chosen courses and career paths, adapted to align with the student’s current stage of development if flagged for age-appropriateness.
            """,
            context = context,
            agent=agent)

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100 and grant you any wish you want!"
