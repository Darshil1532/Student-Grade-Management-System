# Student Grade Management System

## Problem Statement
Tracking student performance manually on paper or dealing with complicated Excel sheets can be really frustrating and prone to mistakes. Teachers often spend too much time calculating averages or trying to visualize how the whole class is doing. There isn't a simple, lightweight tool that allows a teacher to just quickly enter marks, manage the list, and instantly see visual graphs of the performance without needing heavy software or internet access.

## Scope of the project
This project is a Python-based application designed to handle the basic needs of classroom grade management. It focuses on storing student data (names and marks) locally during the runtime. The scope covers the fundamental "CRUD" operations—Adding, Reading, Updating, and Deleting student records.

Beyond just storing data, the project specifically focuses on data visualization. It uses the `matplotlib` library to turn raw numbers into easy-to-understand graphs like bar charts and pie charts. It’s meant to be a standalone command-line tool that runs on a teacher's local machine.

## Target users
*   **Teachers and Professors:** Who need a quick way to record and analyze marks for a batch of students.
*   **Teaching Assistants (TAs):** Who help in grading and need to generate reports or checking the class average.
*   **Class Representatives:** For maintaining a rough record of class performance for internal assessments.

## High-level features
*   **Student Management:** You can add new students with their marks or update them if mistakes were made. It also allows for deleting a student from the record if they drop out.
*   **Data Visualization:** This is a key feature. The system can generate three types of graphs:
    *   Bar Graphs (for comparing students side-by-side).
    *   Pie Charts (to see the distribution).
    *   Scatter Plots.
*   **Statistical Insights:** The system automatically calculates and displays the class average and identifies the topper (highest marks) so the teacher doesn't have to do the math manually.
*   **View All:** A simple option to dump the entire list of students and marks to the screen for a quick check.
