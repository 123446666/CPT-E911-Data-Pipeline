# Project Proposal

## 1. Project Identification
- Project Title: CPT E911 Data Pipeline
- Course: CPT 298
- Term: Spring 2028
- Student Name(s): Ayden Sturtevant, Ian Broshes, Darian Mongiovi
- Primary Contact: Discord
- Proposed Start Date: Pending Project Approval
- Proposed End Date: TBD

---

## 2. Project Selection & Motivation

This project was selected in response to a ticket request identifying a need for the CPT 166 PostGIS class. It is a strong fit for our 
group as it directly applies skills we have built throughout the program and in previous projects, such as Python scripting, REST APIs, and database management, 
while also having a real impact on other students who depend on this data.

---

## 3. Problem Statement

The State of Maine publishes its E911 roads dataset through a public ArcGIS feature service, but there is no automated process 
to load it into the internal PostgreSQL warehouse. Without this pipeline, CPT 166 students cannot reliably access the road 
geometry data needed for their PostGIS assignments.

---

## 4. Proposed Solution Overview

We will build a Python ETL script that pulls the Maine E911 roads dataset from the provided ArcGIS REST API, normalizes it for PostgreSQL compatibility, 
and loads it into the proper tables. The script will run on a monthly basis to keep the data current. The project will not include a web front end, 
real time streaming, or any changes to the source data beyond what is required for schema compatibility.

---

## 5. Technical Stack & Tools
List the technologies you expect to use.  Please note that this solution MUST live within the cpt.internal network and must be maintainable by future students.

- Operating System(s): Internal Linux VM
- Programming Language(s): Python, SQL
- Frameworks / Libraries: requests, psycopg2, geopandas, pandas, fiona
- Databases / Storage: PostgreSQL with PostGIS extension (existing cpt.internal warehouse)
- Infrastructure (VMs, containers, etc.):  Existing CPT internal Linux VM, cron for scheduling
- Tools (Git, CI, monitoring, APIs, etc.): Git and GitHub for version control, basic logging for monitoring and troubleshooting, environment variables for credential management

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

## 11. Team Structure
- Team roles
  Ian Broshes: Github setup
  Ayden Stutevent: Task Manager, Group Cordination
  Darian Mongiovi: SQL Test Server Setup
  
- Communication plan
  
  Discord: General communication (first line)
  
  Weekly Meetings: Online meetings to cordinate weekly goals, and testing timeline.
  
- Conflict resolution approach
  
  Vote
  
---

## 12. Documentation & Knowledge Transfer Plan
Our main documentation will be a README text file. This document will outline needed Python package files, SQL Documentation, instructions for automation, and a diagram of the directory tree. 

Include:
- Python Packages, APIs, OS
- Automation Script and CRON job specs.
- Instructions for manual deployment.

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

Student 1:  _Ian Broshes________________ Date: _4/03/2026_____
Student 2:  ____________________________ Date: _______________
Student 3:  ____________________________ Date: _______________
Student 4:  ____________________________ Date: _______________

Instructor: ____________________________ Date: _______________
