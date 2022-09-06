# CS372_Code_Grader
A script to grade students' submissions written in CPP, Java, and Python.

## Requirements:
Tested only on the following versions.
- python 3.10
- pandas 1.4
- g++ 12.1.0 (to compile C++ codes)
- javac and java 18 (to compile and run Java codes)

## How to run:
python main.py _<assignment_number>_ _<submissions_path>_

e.g.: python main.py 1 "D:\Submissions"

A sample submissions folder is provided.

## Output:
Two CSV files:
1. assignment1_grades.csv
   - contains the number of incorrect tests for each question.
2. assignment1_grades_details.csv
   - contains the students' codes outputs and the desired outputs for each test and each question.
