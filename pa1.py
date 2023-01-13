'''
Author: Mihir Rao
Purpose: Grading Script for Programming Assignment 1 for CS260 with Dr. Osmanlioglu
'''

# PACKAGE IMPORTS

import gradeMaterials
import os
import subprocess

# TEACHING ASSISTANT INFORMATION VARIABLES

ta_name = "Mihir Rao" # Change if need be
ta_email_address = "mr3554@drexel.edu" # Change if need be

# PROGRAMMING ASSIGNMENT VARIABLES

pa_number = 1
pa_name = "PA" + str(pa_number)
pa_tests_dict = gradeMaterials.pa1_test_cases_dict
pa_score_per_test = 10 # Change if need be
pa_number_of_test_cases = len(pa_tests_dict)
pa_max_score = pa_score_per_test * pa_number_of_test_cases

# FUNCTIONS INVOLVED IN GRADING (You do not need to change anything below this point in the program)

def gradeProgrammingAssignment(student_id):
    print("")
    print("Grading " + student_id + "'s assignment ...")
    print("")

    f = open(pa_name + "Grades" + "/" + student_id + ".txt", "w")
    f.write("---PROGRAMMING ASSIGNMENT " + str(pa_number) + " FEEDBACK---\n")
    f.write("Student ID\t:\t" + student_id + "\n")
    f.write("\n")

    compile_process = subprocess.run(["gcc", pa_name + "/" + student_id + ".c"])

    score = 0

    if (compile_process.returncode != 0):
        f.write("Your program failed to compile.\n")
        f.write("\n")
        f.write("[GRADE]\n")
        f.write("\n")
        f.write("Total score\t:\t" + str(score) + "/" + str(pa_max_score) + "\n")
        f.write("Graded by\t:\t" + ta_name)
        f.write("\n")
        f.write("Comments\t:\tPlease reach out to me at " + ta_email_address + " for any questions about your grade.")

        f.close()
        return score

    f.write("[TEST CASES]\n")
    f.write("\n")

    test_case_number = 1
    test_case_passed = False
    for input_string in pa_tests_dict.keys():
        t = open(str(test_case_number) + ".txt", "w")
        t.write(input_string)
        t.close()

        f.write("TEST CASE " + str(test_case_number) + "\t")

        run_process = subprocess.run(["./a.out", str(test_case_number) + ".txt"], stdout = subprocess.PIPE, stderr = subprocess.DEVNULL, timeout = 5)

        if (run_process.returncode != 0):
            f.write("{FAILED | 0/" + str(pa_score_per_test) + "}\n")
            f.write("\n")
            f.write("Input:\n")
            f.write(input_string)
            f.write("\n\n")
            f.write("Correct ouput:\n")
            f.write(pa_tests_dict[input_string])
            f.write("\n")
            f.write("Your program was unable to produce an ouput for this test case.\n")
            f.write("\n")
            test_case_number += 1
            continue
        
        output_string = run_process.stdout.decode()

        if (output_string == pa_tests_dict[input_string]):
            score += pa_score_per_test
            test_case_passed = True

        if (test_case_passed):
            f.write("{PASSED | " + str(pa_score_per_test) + "/" + str(pa_score_per_test) + "}\n")
        else:
            f.write("{FAILED | 0/" + str(pa_score_per_test) + "}\n")

        f.write("\n")
        f.write("Input:\n")
        f.write(input_string)
        f.write("\n\n")
        f.write("Correct ouput:\n")
        f.write(pa_tests_dict[input_string])
        f.write("\n")
        f.write("Your program's ouput:\n")
        f.write(output_string)
        f.write("\n")

        test_case_number += 1
        test_case_passed = False


    f.write("[GRADE]\n")
    f.write("\n")
    f.write("Total score\t:\t" + str(score) + "/" + str(pa_max_score) + "\n")
    f.write("Graded by\t:\t" + ta_name)
    f.write("\n")
    f.write("Comments\t:\tPlease reach out to me at " + ta_email_address + " for any questions about your grade.")

    f.close()

    return score

def writeGradeReport(student_score_dict):
    gr = open(pa_name + "GradeReport.txt", "w")

    gr.write("---PROGRAMMING ASSIGNMENT " + str(pa_number) + " REPORT---\n")
    gr.write("\n")
    gr.write("[INFORMATION]\n")
    gr.write("\n")
    gr.write("Number of test cases\t:\t" + str(pa_number_of_test_cases) + "\n")
    gr.write("Points per test case\t:\t" + str(pa_score_per_test) + "\n")
    gr.write("Maximum points possible\t:\t" + str(pa_max_score) + "\n")
    gr.write("\n")
    gr.write("[GRADES]\n")
    gr.write("\n")

    min_score = pa_max_score
    max_score = 0
    sum_of_scores = 0

    for student_id in student_score_dict.keys():
        gr.write(student_id + "\t:\t" + str(student_score_dict[student_id]) + "\n")
        sum_of_scores += student_score_dict[student_id]
        min_score = min(min_score, student_score_dict[student_id])
        max_score = max(max_score, student_score_dict[student_id])

    gr.write("\n")
    gr.write("[STATISTICS]\n")
    gr.write("\n")
    gr.write("Average\t:\t" + str(int(sum_of_scores / len(student_score_dict))) + "\n")
    gr.write("Maximum\t:\t" + str(max_score) + "\n")
    gr.write("Minimum\t:\t" + str(min_score) + "\n")

    gr.close()

def cleanUp():
    for i in range(1, pa_number_of_test_cases + 1):
        if (os.path.isfile(str(i) + ".txt")):
            os.remove(str(i) + ".txt")

    if (os.path.isfile("a.out")):
        os.remove("a.out")

if __name__ == "__main__":

    if (str(pa_name + "Grades") not in os.listdir()):
        os.mkdir(pa_name + "Grades")

    pa_submissions_list = [submission for submission in os.listdir(pa_name) if submission.endswith(".c")]

    student_score_dict = {}
    for student_id in gradeMaterials.student_id_list:
        if (student_id + ".c") in pa_submissions_list:
            student_score_dict[student_id] = gradeProgrammingAssignment(student_id)
        else:
            student_score_dict[student_id] = 0

            f = open(pa_name + "Grades" + "/" + student_id + ".txt", "w")
            f.write("---PROGRAMMING ASSIGNMENT " + str(pa_number) + " FEEDBACK---\n")
            f.write("Student ID\t:\t" + student_id + "\n")
            f.write("\n")

            f.write("No submission.\n")
            f.write("\n")
            f.write("[GRADE]\n")
            f.write("\n")
            f.write("Total score\t:\t" + str(student_score_dict[student_id]) + "/" + str(pa_max_score) + "\n")
            f.write("Graded by\t:\t" + ta_name)
            f.write("\n")
            f.write("Comments\t:\tPlease reach out to me at " + ta_email_address + " for any questions about your grade.")

            f.close()
            

    writeGradeReport(student_score_dict)

    cleanUp()

