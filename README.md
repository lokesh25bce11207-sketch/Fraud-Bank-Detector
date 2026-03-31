# Smart School Management System (Python and Pandas)


## Student Details
Name: Lokesh Kasana 
Roll Number: 25BCE11207   
Course: B.Tech CSE    


---

## Project Overview
The Smart School Management System is a console-based application designed to manage school administrative data efficiently.  

Unlike traditional menu-driven programs, this system uses a chatbot-style interface where users can interact using simple English commands.  

The system manages two main entities: Students and Teachers. It uses Python dictionaries for fast data handling and the Pandas library for structured and professional data display.

---

## Key Features
- Chatbot Interaction: Users can type commands like "Add a student" or "Show all teachers"  
- Data Visualization: Uses Pandas DataFrames for clean and structured table display  
- Student Records: Stores details like Admission Number, Roll Number, DOB, Gender, Class, Section, and Parent Information  
- Teacher Management: Stores Employee ID, Qualification, Subject, Date of Joining, and Designation  
- Search Functionality: Search records by Name, Class, Subject, or Address  
- Input Validation: Uses try-except blocks to handle invalid inputs  
- CRUD Operations: Add, View, Update, and Delete records  

---

## Technical Stack
Language: Python 3.x  

Libraries Used:  
pandas for data manipulation and display  
tabulate (via pandas to_markdown) for formatted tables  

Data Structure: Nested Dictionaries  

---

## How to Use
1. Run the Python script  
2. Use simple commands like:  
   Add: Add a student or Insert teacher  
   View: Show students or Display all teachers  
   Search: Find student or Search teacher  
   Update: Modify student or Change teacher details  
   Delete: Remove student or Delete teacher  
3. Type Exit or Quit to close the program  

---

## System Logic
Data Storage: Data is stored in dictionaries using Admission Number or Employee ID as unique keys  

Table Generation: Data is converted into a Pandas DataFrame and transposed for proper display  

Exception Handling: try-except blocks are used to handle invalid inputs without crashing the system  

---

## Project Note
This project is developed as a practical implementation of Python programming concepts including data structures, file handling, and basic AI-style interaction.