# Project Proposal

## 1. Project Identification
- **Project Title:**
- **Course:**
- **Term:**
- **Student Name(s):**
- **Primary Contact:**
- **Proposed Start Date:**
- **Proposed End Date:**

---

## 2. Project Selection & Motivation
Describe why you selected this project and why you are a good fit.

Include:
- Personal or professional motivation
- Alignment with career goals
- Relevant interests or prior exposure

---

## 3. Problem Statement
Clearly describe the problem, need, or opportunity this project addresses.

Answer:
- What problem exists?
- Who is affected?
- Why does this problem matter?

Limit to 1–2 focused paragraphs.

---

## 4. Proposed Solution Overview
Provide a high-level description of your proposed solution.

Include:
- What you intend to build, deploy, or configure
- Core features or capabilities
- Explicit exclusions (what the project will *not* include)

---

## 5. Technical Stack & Tools
List the technologies you expect to use.  Please note that this solution MUST live within the cpt.internal network and must be maintainable by future students.

- **Operating System(s):**
- **Programming Language(s):**
- **Frameworks / Libraries:**
- **Databases / Storage:**
- **Infrastructure (VMs, containers, etc.):**
- **Tools (Git, CI, monitoring, APIs, etc.):**

---

## 6. Prerequisite Knowledge & Skills
As the second project a lot of skills where honed and are now able to be used in this semesters project.
A pipeline for cleaning and formatting data as been implemented last time and also python web scraping was used to grab the PDF calendars. 
A SQL database was setup and queried and a cron job was drafted for automation. 
Therefore this E199 project builds on the skills we have used previously use, and allows us to practice them again.

Ayden – Python, Databases, Linux, GitHub/Git, APIs, Parsing Files, Automation.
Ian – Python, Web Scraping, Formatting, GUI, Bash, Linux, Automation.
Darian – SQL, DDL (database defining), DQL (database queries), Python, Formatting, Linux.


---

## 7. Project Scope & Deliverables
The scope of this project is to design and implement an automated solution for grabbing E199 data from online and parsing and formatting the data to be inserted into a database. Development will be on the fetching, parsing, formatting, and sending to the database.
Key considerations should be how the data is sent and in what format the end result should be in.
Deliverables for this project include a GitHub repository containing the completed proposal, all source code, database schema definitions, config files, and the documentation required to deploy and maintain the automated process.
A final live demonstration of the working pipeline will also be completed with each group member participating as required, with a complementary slideshow.

---

## 8. Milestones & Timeline
Phase 1: Plan and design what the required parts are for the project to be successful. This includes making the GitHub and completing the proposal.
Phase 2: Implement a system to go and fetch E199 data in a readable format and automate the collection of this information. 
Phase 3: Convert the data collected to the appropriate database schema and work to make sure the data is normalized in a clean and efficient way.
Phase 4: Connect to the database and send frames of the correctly formatted data. Insure that this process is automatic and will result in the output of a clean database with scraped information from E199.
Phase 5: Document the project and include everything required to run the project in a live environment and create a demo slideshow to present what the project can do. Ask for feedback from the professor and complete the implementation of the automated project in a live environment.

---

## 9. Risks, Constraints & Dependencies
Risks: Changes or inconsistencies in the source data format might be hard to work around. Limited time within the half semester project window. Database remade schema might contain constraints we need to work with. Wrong commands can wipe the database, and if any preexisting data is present, that would not be ideal.
Constraints: The automated solution must stay within the CPT department and also run on a minimal Linux host for easy deployment and preservation of system resources. The database is predefined and must require permission to access.
Dependencies: Linux VM, PostgreSQL database, Python (any package that may be needed). Our goal is to limit the footprint of packages, that way there are a minimal amount of packages required to run the project.

---

## 10. Security, Ethics & Safety Considerations
Authentication and Authorization:  Access to the data online might require some sort of API or account to properly fetch. The on premises database will require database credentials that will be stored in a secure .env file and not be uploaded onto GitHub.
Data Sensitivity: There will be no PHI or personal data as the information is purely informative and not governed by any privacy related laws.
Network Exposure: The network will be limited to the connection to the local database server and the internet for information scraping. There will be no exposure of internal services in this project.
Logging, Monitoring, or Automation Impact: Log files will be created and placed in a dedicated log file folder. Any information scraped will be logged and the whole process will be logged for troubleshooting purposes.
Ethical Considerations: The information being scraped is publicly available and ready to use, and will be gather with the intent of using the data in a useful way.

---

## 11. Team Structure (If Applicable)
If working in a group, describe:
- Team roles
- Communication plan
- Conflict resolution approach
- Workload distribution

---

## 12. Documentation & Knowledge Transfer Plan
Explain how this project will be documented.  Please note that this should include documentation in the UVDesk knowledgebase at the very least.  Programming projects should include readme.md files. 

Include:
- README or user documentation
- Deployment or maintenance guides
- How another student or administrator could continue the project

---

## 13. Faculty/cpt.internal Resources Requested
List any required resources:
- VM access
- Network access
- Credentials or APIs
- Special permissions
- Hardware (if applicable)

Please be sure to consider any future tickets you may need to submit to complete this work as those will need to be generated and assigned to the appropriate groups as soon as feasibly possible once the project kicks off to ensure timely delivery.  I will step in to help where required but you will likely be working with students in other classes so please be cognizant of their time!

---

## 14. Acknowledgement of Expectations
By submitting this proposal, I acknowledge that:
- This is a self-directed technical project
- I am responsible for research and troubleshooting
- Evaluation will consider process, documentation, and professionalism

**Signature (Name & Date):**

Student 1:  ____________________________ Date: _______________
Student 2:  ____________________________ Date: _______________
Student 3:  ____________________________ Date: _______________
Student 4:  ____________________________ Date: _______________

Instructor: ____________________________ Date: _______________
