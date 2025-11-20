# Student Grade Management System

## Problem Statement
Manual handling of students' academic records, particularly their marks for different subjects, is error-prone, time-consuming. Even for tracking student performance, computing class averages, or identifying bright students, one has to do boring calculations repeatedly. Moreover, charting such data in order to get an instant picture of overall class performance or of any single student's standing itself is bulky without special tools.  

## Scope of the project
This project is a Python-based application that deals with the basic requirements of classroom grade management. It concentrates on locally storing data regarding students' names and marks during runtime. The scope covers the fundamental "CRUD" operations: Adding, Reading, Updating, and Deleting of student records.
Beyond data storage, the project is particularly concerned with the visualization of data. It utilizes the matplotlib library in converting plain numbers to understandable graphs, such as bar charts and pie charts. It’s meant to be a standalone command-line tool that runs on a teacher's local machine.

## Target users
*   **Teachers and Professors:** These are people who want a quick way of recording and analyzing marks for a batch of students.
*   **Teaching Assistants (TAs):** Who help in grading and need to generate reports or checking the class average.
*   **Class Representatives:** To keep a rough record of class performance with regard to internal assessments.
*   
## Features of the project
*   **Student Management:** You have the option to add new students along with their marks, or you may update them in case of mistakes. You can also delete a particular student from your record upon their dropout.
*   **Data Visualization:** This is a key feature. The system can generate three types of graphs:
    *   Bar Graphs (for comparing students side-by-side).
    *   Pie Charts (to see the distribution).
    *   Scatter Plots.
*   **Statistical Insights:** The system calculates the average of the class and marks the topper (highest marks) on its own, thus leaving no need for mathematical calculations by the teacher.
*   **View All:** : A simple option to dump the whole list of students and marks to the screen for a quick check.
