import streamlit as st

st.markdown("# 🧑🏻‍🏫 About Us")

multi1 = '''
# **Project Title**  
## **ECG Agent: Personalised Education and Career Guidance for Secondary School Students** '''

st.markdown(multi1)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Project Overview, Scope & Objectives", "📊 Data Sources", "🔑 Key Features", "📈 Use Cases", "👥 Impact & Project Users"])

# tab1.header("📋 Project Overview, Scope & Objectives")
tab1.markdown('''
### 📋 Project Overview

**ECG Agent** is a query-based application designed to provide personalised educational and career guidance to secondary school students. Developed as an individual initiative, this project aims to bridge the gap between general guidance and specific, actionable steps, allowing users to enter information about their **interests, strengths, and weaknesses** to receive tailored recommendations.

While the primary function is to serve as a self-guided tool for students, **ECG Agent** can also be used by teachers, ECG counsellors, and parents as a toolkit. This enables educators and parents to efficiently guide students with accurate, structured information on course options, prerequisites, and career sectors, supporting them in offering informed, personalised guidance.

- **Application Type**: Query-based, self-guided educational guidance  
- **Primary Audience**: Secondary school students, teachers, ECG counsellors, and parents who need a structured toolkit to facilitate educational and career guidance.

---

### 📋 Project Scope

The scope of **ECG Agent** is to develop a **query-based guidance tool** that enables secondary school students, teachers, ECG counsellors, and parents to enter or access information about interests, strengths, and weaknesses. The application then analyses this information to provide personalised career sector suggestions and educational pathways at three institutions (two polytechnics and one ITE). This initial phase will validate the feasibility of the application, laying the groundwork for potential future scaling to more institutions and additional guidance features.

**Core Functionalities**:
- **Query Input**: Users (students, teachers, counsellors, and parents) can enter or access details on students’ strengths, interests, and weaknesses to receive personalised recommendations.
- **Career Sector Recommendations**: Based on input data, the application suggests potential career sectors.
- **Course Listings with Prerequisites**: Presents relevant courses and prerequisites from the two selected polytechnics and one ITE.

---

### 📋 Objectives

The objectives of **ECG Agent** are to:

1. **Simplify Educational Decision-Making**: Provide students with structured, easy-to-understand guidance that matches their individual profiles, reducing the complexity of educational planning.
2. **Equip Teachers, Counsellors, and Parents with a Guidance Toolkit**: Provide educators, ECG counsellors, and parents with an efficient tool to guide students with accurate, structured information on educational and career pathways.
3. **Bridge Guidance with Action**: Move beyond general advice by offering clear, actionable steps for students to qualify for their desired courses.
4. **Test Feasibility for Future Scaling**: Focus initially on three institutions (two polytechnics and one ITE) to ensure feasibility and user engagement, setting the stage for future expansion.

''')

#tab2.header("📊 Data Sources")
tab2.markdown('''
### 📊 Data Sources

To generate meaningful recommendations, **ECG Agent** will use the following data sources:
1. **Institutional Course Data**:
   - **Polytechnic and ITE Data** for the three selected institutions, including:
     - **Course names** and **course codes**
     - **Subject prerequisites and minimum grade requirements** for each course.
2. **Career Sector Information from Skills Frameworks by SkillsFuture Singapore**:
   - Career sector information is sourced from the **Skills Frameworks** by **SkillsFuture Singapore**, which provides:
     - **Sector**: Different industries and sectors available for career exploration.
     - **Track**: Specific tracks within each sector, showing various specialisation paths.
     - **Job Roles**: Common job roles within each track, offering insight into potential career positions.
     - **Job Descriptions**: Detailed descriptions for each job role, including required skills and responsibilities.
   - This structured information enables ECG Agent to suggest suitable sectors and career tracks, providing students with a clear picture of relevant roles and pathways aligned with their interests and strengths.
''')

#tab3.header("🔑 Key Features")
tab3.markdown('''
### 🔑 Key Features

#### 1. Self-Discovery and Query Input
   - **Description**: Users can enter information about students' **interests, strengths, and weaknesses**. This data is then processed to build a profile that matches students with potential career sectors and educational paths.
   - **Purpose**: To provide a foundational understanding of each student’s unique qualities, guiding them towards educational choices that align with their profiles.

#### 2. Career Sector Recommendations
   - **Description**: Based on the input provided, the application suggests relevant career sectors that align with the student’s strengths and interests.
   - **Purpose**: To help students focus on career fields that are compatible with their strengths and interests, providing a targeted approach to career exploration.

#### 3. Course Listings with Prerequisites
   - **Description**: Once a career sector is chosen, ECG Agent presents a list of relevant courses from the selected polytechnics and ITE. Each course listing includes subject prerequisites and minimum grade requirements.
   - **Purpose**: This feature connects students’ interests to specific academic paths and provides them with clear eligibility requirements.

#### 4. Personalised Action Plan - Skill Gaps and Academic Prerequisites
   - **Description**: The application generates a **personalised action plan** outlining the necessary steps for students to qualify for their chosen courses. This plan addresses **skill gaps** and **academic prerequisites**, providing clear, actionable guidance to help students achieve their educational goals.
   - **Purpose**: To offer students a tailored roadmap, showing them precisely which areas to focus on and the steps required to meet eligibility for their desired courses.
''')

#tab4.header("📈 Use Cases")
tab4.markdown('''
### 📈 Use Cases

#### Use Case 1: Student Exploring Career Options and Course Eligibility
   - **Scenario**: A student is interested in STEM fields but isn’t sure which specific career or education path to pursue. They are also uncertain about the eligibility requirements for courses in these fields.
   - **Process**: The student enters their interests and strengths (e.g., proficiency in Maths and Science) into ECG Agent. Based on this input, ECG Agent suggests career sectors like Engineering or Information Technology and lists relevant courses in these fields at the selected polytechnics and ITE, along with the necessary subject prerequisites and minimum grade requirements.
   - **Outcome**: The student gains clarity on suitable career sectors and receives specific course recommendations with clear eligibility criteria. This allows them to focus on the prerequisites needed to qualify, providing a structured plan for their academic efforts.

#### Use Case 2: Educators Using ECG Agent as a Guidance Toolkit
   - **Scenario**: A teacher is responsible for providing basic educational and career guidance to a group of students but has limited time for researching course options and prerequisites across different institutions.
   - **Process**: The teacher uses ECG Agent as a toolkit to quickly access relevant course information, eligibility requirements, and career sector recommendations. The tool provides structured, data-driven guidance, cutting down the time the teacher would otherwise spend on manual research.
   - **Outcome**: The teacher can efficiently deliver accurate and personalised guidance to students, helping them explore suitable career paths and educational opportunities without needing extensive preparation time.

#### Use Case 3: ECG Counsellors Supporting In-Depth Career Guidance
   - **Scenario**: An ECG counsellor is working with students who need detailed guidance on aligning their strengths and interests with suitable career and educational paths.
   - **Process**: The counsellor uses ECG Agent to access personalised course recommendations, career sector options, and eligibility details based on each student’s profile. By using the app, the counsellor can focus on providing deeper, individualised advice rather than spending time gathering information manually.
   - **Outcome**: Students receive well-researched, personalised guidance from the ECG counsellor, allowing the counsellor to spend more time on meaningful discussions and strategic advice tailored to each student’s unique profile.

#### Use Case 4: Parents Supporting Their Child’s Career and Education Planning
   - **Scenario**: A parent wants to help their child explore future educational and career options that align with their interests and strengths. The parent is looking for guidance on course options, prerequisites, and potential career paths but is unfamiliar with current educational pathways.
   - **Process**: The parent uses ECG Agent to enter their child’s interests and strengths, such as proficiency in the arts or a strong interest in science. ECG Agent then provides a list of recommended career sectors, along with suitable courses at polytechnics and ITEs, including prerequisites and any skills the child may need to develop.
   - **Outcome**: The parent gains insights into their child’s possible educational and career options and becomes more informed about the necessary steps for qualification. This helps the parent have meaningful, supportive discussions with their child about future planning and identify specific academic areas or skills the child may need to focus on.
''')

#tab5.header("👥 Impact & Project Users")
tab5.markdown('''
### 👥 Impact

**ECG Agent** is expected to have a positive impact on students’ approach to educational decision-making and to support educators, counsellors, and parents in guiding students effectively:

1. **Improved Decision-Making**: By offering targeted course recommendations, ECG Agent simplifies the planning process and enhances students’ confidence in their educational choices.
   
2. **Actionable Guidance**: The app gives students specific action items through eligibility and prerequisite requirements, guiding them to focus on areas for improvement.
   
3. **Time-Saving**: Students, parents, and educators receive relevant recommendations without having to sift through extensive information, reducing preparation and research time.

4. **Empowerment in Education and Career Planning**: ECG Agent bridges the gap between guidance and action, helping students gain clarity on the steps required to achieve their goals.

5. **Toolkit for Educators and Parents**: Teachers, counsellors, and parents can use ECG Agent to complement their guidance sessions, enabling students to approach these sessions with a more focused plan and enhancing the quality of personalised guidance.

---

### 👥 Project Users

This project is developed as an **individual initiative**, with no external sponsors.

**Primary Users**:
- **Secondary school students** are the main users of ECG Agent. They benefit from personalised recommendations on course options and subject prerequisites based on their strengths and academic profiles.
- **Teachers, ECG Counsellors, and Parents** can utilise ECG Agent as a toolkit. It enables them to provide structured, data-driven guidance efficiently, making their counselling sessions and discussions with students more productive and focused.

**Secondary Users**:
- **School counsellors** and **teachers** can use the app as a supplementary tool, allowing students to come prepared with personalised advice and enabling counsellors to provide more in-depth, tailored guidance.
''')



multi = '''
# **Project Title**  
## **ECG Agent: Personalised Education and Career Guidance for Secondary School Students**

---

### 1. Project Overview

**ECG Agent** is a query-based application designed to provide personalised educational and career guidance to secondary school students. Developed as an individual initiative, this project aims to bridge the gap between general guidance and specific, actionable steps, allowing users to enter information about their **interests, strengths, and weaknesses** to receive tailored recommendations.

While the primary function is to serve as a self-guided tool for students, **ECG Agent** can also be used by teachers, ECG counsellors, and parents as a toolkit. This enables educators and parents to efficiently guide students with accurate, structured information on course options, prerequisites, and career sectors, supporting them in offering informed, personalised guidance.

- **Application Type**: Query-based, self-guided educational guidance  
- **Primary Audience**: Secondary school students, teachers, ECG counsellors, and parents who need a structured toolkit to facilitate educational and career guidance.

---

### 2. Project Scope

The scope of **ECG Agent** is to develop a **query-based guidance tool** that enables secondary school students, teachers, ECG counsellors, and parents to enter or access information about interests, strengths, and weaknesses. The application then analyses this information to provide personalised career sector suggestions and educational pathways at three institutions (two polytechnics and one ITE). This initial phase will validate the feasibility of the application, laying the groundwork for potential future scaling to more institutions and additional guidance features.

**Core Functionalities**:
- **Query Input**: Users (students, teachers, counsellors, and parents) can enter or access details on students’ strengths, interests, and weaknesses to receive personalised recommendations.
- **Career Sector Recommendations**: Based on input data, the application suggests potential career sectors.
- **Course Listings with Prerequisites**: Presents relevant courses and prerequisites from the two selected polytechnics and one ITE.

---

### 3. Objectives

The objectives of **ECG Agent** are to:

1. **Simplify Educational Decision-Making**: Provide students with structured, easy-to-understand guidance that matches their individual profiles, reducing the complexity of educational planning.
2. **Equip Teachers, Counsellors, and Parents with a Guidance Toolkit**: Provide educators, ECG counsellors, and parents with an efficient tool to guide students with accurate, structured information on educational and career pathways.
3. **Bridge Guidance with Action**: Move beyond general advice by offering clear, actionable steps for students to qualify for their desired courses.
4. **Test Feasibility for Future Scaling**: Focus initially on three institutions (two polytechnics and one ITE) to ensure feasibility and user engagement, setting the stage for future expansion.

---

### 4. Data Sources

To generate meaningful recommendations, **ECG Agent** will use the following data sources:
1. **Institutional Course Data**:
   - **Polytechnic and ITE Data** for the three selected institutions, including:
     - **Course names** and **course codes**
     - **Subject prerequisites and minimum grade requirements** for each course.
2. **Career Sector Information from Skills Frameworks by SkillsFuture Singapore**:
   - Career sector information is sourced from the **Skills Frameworks** by **SkillsFuture Singapore**, which provides:
     - **Sector**: Different industries and sectors available for career exploration.
     - **Track**: Specific tracks within each sector, showing various specialisation paths.
     - **Job Roles**: Common job roles within each track, offering insight into potential career positions.
     - **Job Descriptions**: Detailed descriptions for each job role, including required skills and responsibilities.
   - This structured information enables ECG Agent to suggest suitable sectors and career tracks, providing students with a clear picture of relevant roles and pathways aligned with their interests and strengths.

---

### 5. Key Features

#### 1. Self-Discovery and Query Input
   - **Description**: Users can enter information about students' **interests, strengths, and weaknesses**. This data is then processed to build a profile that matches students with potential career sectors and educational paths.
   - **Purpose**: To provide a foundational understanding of each student’s unique qualities, guiding them towards educational choices that align with their profiles.

#### 2. Career Sector Recommendations
   - **Description**: Based on the input provided, the application suggests relevant career sectors that align with the student’s strengths and interests.
   - **Purpose**: To help students focus on career fields that are compatible with their strengths and interests, providing a targeted approach to career exploration.

#### 3. Course Listings with Prerequisites
   - **Description**: Once a career sector is chosen, ECG Agent presents a list of relevant courses from the selected polytechnics and ITE. Each course listing includes subject prerequisites and minimum grade requirements.
   - **Purpose**: This feature connects students’ interests to specific academic paths and provides them with clear eligibility requirements.

#### 4. Personalised Action Plan - Skill Gaps and Academic Prerequisites
   - **Description**: The application generates a **personalised action plan** outlining the necessary steps for students to qualify for their chosen courses. This plan addresses **skill gaps** and **academic prerequisites**, providing clear, actionable guidance to help students achieve their educational goals.
   - **Purpose**: To offer students a tailored roadmap, showing them precisely which areas to focus on and the steps required to meet eligibility for their desired courses.

---

### 6. Use Cases

#### Use Case 1: Student Exploring Career Options and Course Eligibility
   - **Scenario**: A student is interested in STEM fields but isn’t sure which specific career or education path to pursue. They are also uncertain about the eligibility requirements for courses in these fields.
   - **Process**: The student enters their interests and strengths (e.g., proficiency in Maths and Science) into ECG Agent. Based on this input, ECG Agent suggests career sectors like Engineering or Information Technology and lists relevant courses in these fields at the selected polytechnics and ITE, along with the necessary subject prerequisites and minimum grade requirements.
   - **Outcome**: The student gains clarity on suitable career sectors and receives specific course recommendations with clear eligibility criteria. This allows them to focus on the prerequisites needed to qualify, providing a structured plan for their academic efforts.

#### Use Case 2: Educators Using ECG Agent as a Guidance Toolkit
   - **Scenario**: A teacher is responsible for providing basic educational and career guidance to a group of students but has limited time for researching course options and prerequisites across different institutions.
   - **Process**: The teacher uses ECG Agent as a toolkit to quickly access relevant course information, eligibility requirements, and career sector recommendations. The tool provides structured, data-driven guidance, cutting down the time the teacher would otherwise spend on manual research.
   - **Outcome**: The teacher can efficiently deliver accurate and personalised guidance to students, helping them explore suitable career paths and educational opportunities without needing extensive preparation time.

#### Use Case 3: ECG Counsellors Supporting In-Depth Career Guidance
   - **Scenario**: An ECG counsellor is working with students who need detailed guidance on aligning their strengths and interests with suitable career and educational paths.
   - **Process**: The counsellor uses ECG Agent to access personalised course recommendations, career sector options, and eligibility details based on each student’s profile. By using the app, the counsellor can focus on providing deeper, individualised advice rather than spending time gathering information manually.
   - **Outcome**: Students receive well-researched, personalised guidance from the ECG counsellor, allowing the counsellor to spend more time on meaningful discussions and strategic advice tailored to each student’s unique profile.

#### Use Case 4: Parents Supporting Their Child’s Career and Education Planning
   - **Scenario**: A parent wants to help their child explore future educational and career options that align with their interests and strengths. The parent is looking for guidance on course options, prerequisites, and potential career paths but is unfamiliar with current educational pathways.
   - **Process**: The parent uses ECG Agent to enter their child’s interests and strengths, such as proficiency in the arts or a strong interest in science. ECG Agent then provides a list of recommended career sectors, along with suitable courses at polytechnics and ITEs, including prerequisites and any skills the child may need to develop.
   - **Outcome**: The parent gains insights into their child’s possible educational and career options and becomes more informed about the necessary steps for qualification. This helps the parent have meaningful, supportive discussions with their child about future planning and identify specific academic areas or skills the child may need to focus on.

---

### 7. Impact

**ECG Agent** is expected to have a positive impact on students’ approach to educational decision-making and to support educators, counsellors, and parents in guiding students effectively:

1. **Improved Decision-Making**: By offering targeted course recommendations, ECG Agent simplifies the planning process and enhances students’ confidence in their educational choices.
   
2. **Actionable Guidance**: The app gives students specific action items through eligibility and prerequisite requirements, guiding them to focus on areas for improvement.
   
3. **Time-Saving**: Students, parents, and educators receive relevant recommendations without having to sift through extensive information, reducing preparation and research time.

4. **Empowerment in Education and Career Planning**: ECG Agent bridges the gap between guidance and action, helping students gain clarity on the steps required to achieve their goals.

5. **Toolkit for Educators and Parents**: Teachers, counsellors, and parents can use ECG Agent to complement their guidance sessions, enabling students to approach these sessions with a more focused plan and enhancing the quality of personalised guidance.

---

### 8. Project Users

This project is developed as an **individual initiative**, with no external sponsors.

**Primary Users**:
- **Secondary school students** are the main users of ECG Agent. They benefit from personalised recommendations on course options and subject prerequisites based on their strengths and academic profiles.
- **Teachers, ECG Counsellors, and Parents** can utilise ECG Agent as a toolkit. It enables them to provide structured, data-driven guidance efficiently, making their counselling sessions and discussions with students more productive and focused.

**Secondary Users**:
- **School counsellors** and **teachers** can use the app as a supplementary tool, allowing students to come prepared with personalised advice and enabling counsellors to provide more in-depth, tailored guidance.

'''

#st.markdown(multi)