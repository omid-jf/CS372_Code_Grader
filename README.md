# CS372_Code_Grader
A script to grade students' submissions written in CPP, Java, and Python.

## Requirements:
Tested only on the following versions.
- python 3.10
- pandas 1.4
- openpyxl 3.0
- g++ 12.1.0 (to compile C++ codes)
- javac and java 18 (to compile and run Java codes)

## How to run (from source):
1. Make sure all the requirements are installed.
2. Clone the Git repository.
3. Copy your folder (which contains your source code file) into the _Submissions_ folder. A sample folder (named _Doe_800123123_) is provided in the _Submissions_ folder.
4. Run the grader using:

   `python main.py <assignment_number> Submissions`

   example: `python main.py 1 Submissions`

## How to run (using Docker):
1. Make sure the Docker platform is installed on your machine. It can be installed from https://www.docker.com/
2. Build the image using the following command in Terminal / PowerShell / Command Prompt:
   
   `docker build -t cs372_code_grader .`
3. Copy your folder (which contains your source code file) into the _Submissions_ folder. A sample folder (named _Doe_800123123_) is provided in the _Submissions_ folder.
4. Run the image using the following command:
   - In Terminal and PowerShell:
   
   `docker run --rm -v ${PWD}:/app cs372_code_grader <assignment_number> Submissions`
   
   example: `docker run --rm -v ${PWD}:/app cs372_code_grader 1 Submissions`

   - In Command Prompt:

   `docker run --rm -v "%cd%":/app cs372_code_grader <assignment_number> Submissions`
   
   example: `docker run --rm -v "%cd%":/app cs372_code_grader 1 Submissions`
5. Remove the created image using the following command:

   `docker rmi cs372_code_grader`

## Output:
One Excel file (assignment1_grades.xlsx) with the following sheets:
1. grades
   - contains the number of incorrect tests for each question.
2. details
   - contains the students' codes outputs and the desired outputs for each test and each question.
