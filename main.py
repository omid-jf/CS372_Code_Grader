#  ============================================================
#  This file is part of the CS372_Code_Grader project.
#
#  Author: Omid Jafari - omidjafari.com
#  Copyright (c) 2022
#
#  For the full copyright and license information, please view
#  the LICENSE file that was distributed with this source code.
#  ============================================================

from pathlib import Path
import subprocess
import pandas as pd
import sys
import importlib.util


def convert_list_to_cli(in_list: list) -> list:
    output = []

    for elem in in_list:
        if isinstance(elem, int):
            output.append(str(elem))

        elif isinstance(elem, list):
            if isinstance(elem[0], list):  # 2d list
                tmp = "["
                for dim_idx, dim in enumerate(elem):
                    tmp += "["
                    tmp += ",".join(map(str, dim))
                    tmp += "]" if dim_idx == len(elem) - 1 else "],"
                tmp += "]"
                output.append(tmp)

            elif isinstance(elem[0], int):  # 1d list of ints
                output.append(",".join(map(str, elem)))

        elif isinstance(elem, str):
            output.append(elem)

    return output


assignment_no = int(sys.argv[1])
submissions_path = Path(sys.argv[2]).absolute()
exec_args_list = []
results = []

for student_path in submissions_path.glob("*_800*"):
    student_result = {"name": str(student_path.name)}
    print("===================================")
    print(str(student_path.name))

    if Path(student_path, f"assignment{assignment_no}.py").exists():
        # Python
        print("Python")
        exec_args_list = [
            "python",
            Path("Python", f"assignment{assignment_no}_caller.py").absolute(),
            Path(student_path, f"assignment{assignment_no}.py").absolute()
        ]

    elif Path(student_path, f"assignment{assignment_no}.cpp").exists():
        # CPP
        print("CPP")
        cpp_caller_path = Path("CPP").absolute()

        # Compilation
        try:
            # compiles and creates assignmentX_compiled/assignmentX.exe
            Path(student_path, f"assignment{assignment_no}_compiled").mkdir(exist_ok=True)

            subprocess.run([
                "g++",
                Path(cpp_caller_path, f"assignment{assignment_no}_caller.cpp").absolute(),
                Path(cpp_caller_path, "utils.cpp").absolute(),
                Path(student_path, f"assignment{assignment_no}.cpp").absolute(),
                "-I",
                Path(student_path).absolute(),
                "-I",
                Path(cpp_caller_path).absolute(),
                "-o",
                Path(student_path, f"assignment{assignment_no}_compiled", f"assignment{assignment_no}").absolute()
            ], check=True)

        except Exception as e:
            student_result["is_correct"] = False
            student_result["question"] = 0
            student_result["errors"] = repr(e)
            results.append(student_result)
            print(repr(e))
            continue

        exec_args_list = [
            Path(student_path, f"assignment{assignment_no}_compiled", f"assignment{assignment_no}.exe").absolute()
        ]

    elif Path(student_path, f"assignment{assignment_no}.java").exists():
        # Java
        print("Java")
        java_caller_path = Path("Java", "src").absolute()

        # Compilation
        try:
            # compiles and creates assignmentX_compiled folder with all compiled classes inside
            subprocess.run([
                "javac",
                Path(java_caller_path, f"assignment{assignment_no}_caller.java").absolute(),
                Path(java_caller_path, "utils.java").absolute(),
                Path(student_path, f"assignment{assignment_no}.java").absolute(),
                "-d",
                Path(student_path, f"assignment{assignment_no}_compiled").absolute()
            ], check=True)

        except Exception as e:
            student_result["is_correct"] = False
            student_result["question"] = 0
            student_result["errors"] = repr(e)
            results.append(student_result)
            print(repr(e))
            continue

        exec_args_list = [
            "java",
            "-cp",
            Path(student_path, f"assignment{assignment_no}_compiled").absolute(),
            f"assignment{assignment_no}_caller"
        ]

    else:
        raise Exception("No submission.")

    spec = importlib.util.spec_from_file_location("questions", Path("Tests", f"assignment{assignment_no}.py"))
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    for q_idx, question in enumerate(foo.questions):
        print(f"Question {q_idx + 1}:")

        for text_idx, test in enumerate(question):
            student_result = {"name": str(student_path.name), "question": q_idx + 1, "test": text_idx + 1}
            print(f"Test {text_idx + 1}/{len(question)}:")

            cli_args = convert_list_to_cli(test["inputs"])
            output_args_str = " ".join(convert_list_to_cli(test["outputs"]))

            try:
                program_out = subprocess.run(exec_args_list + [f"question{q_idx + 1}"] + cli_args,
                                             capture_output=True,
                                             text=True,
                                             check=True)
            except Exception as e:
                student_result["is_correct"] = False
                student_result["errors"] = repr(e)
                results.append(student_result)
                print(repr(e))
                continue

            program_out_str = program_out.stdout.strip().split(f'Question{q_idx + 1}: ')[1]

            print(f"Desired output: {output_args_str}")
            print(f"Student output: {program_out_str}")

            if program_out_str in map(str, test["outputs"]):
                print("CORRECT")
                student_result["is_correct"] = True

            else:
                print("FALSE")
                student_result["is_correct"] = False

            student_result["cli_args"] = cli_args
            student_result["desired_out"] = output_args_str
            student_result["student_out"] = program_out_str

            results.append(student_result)

df = pd.DataFrame(results)
df.to_csv(f"assignment{assignment_no}_grades_details.csv", index=False)

df2 = df.groupby(["name", "question"]).apply(
    lambda dff: pd.Series({
        "false_count": sum(dff.is_correct == False),
        "total_count": dff.is_correct.count()
    })
)

df2.to_csv(f"assignment{assignment_no}_grades.csv", index=True)

print("DONE")
