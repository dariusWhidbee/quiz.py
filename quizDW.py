# Variables
from quizDataDW import *
grade = 0

def run_quest(quest, check, ansU, ansR):
    print(quest)
    while check == False:
        try:
            print()
            ansU = int(input("Responce. > "))
            print()
            # coreect answer "1"
            if ansU == ansR:
                global grade
                grade += 1
            # if the user answers the question right the boolean turns true
            # and gets out of the while loop
                check = True
            elif 0 < ansU < 5:
                check = True
            # If the user doesn't respond with a interger between 1 to 4
            else:
                print("please choose an interger from 1 to 4")
            # If the user doesn't respond with a interger
        except ValueError:
            print("Invalid response.Please choose either option 1, 2, 3 or 4")


# Introduction
print("""Hello there, new user. This program will run a quiz that consist of 10
questions about Chemistry. Using  your prior knowledge, choose your best
response. Good Luck!""")
print()

# runs the question
run_quest(q1t, q1c, 0, q1r)
run_quest(q2t, q2c, 0, q2r)
run_quest(q3t, q3c, 0, q3r)
run_quest(q4t, q4c, 0, q4r)
run_quest(q5t, q5c, 0, q5r)
run_quest(q6t, q6c, 0, q6r)
run_quest(q7t, q7c, 0, q7r)
run_quest(q8t, q8c, 0, q8r)
run_quest(q9t, q9c, 0, q9r)
run_quest(q10t, q10c, 0, q10r)
# grade
print()
print("Your score",grade * 10,"% / 100%")
if -1 < grade < 5:
    print("""Au, get out of here! You're no scientist
(Get it?)""")
elif 4 < grade < 8:
    print("""At least you tried. Just remember
Old chemists never die, they just stop reacting.""")
elif 7 < grade < 10:
    print(""" You know what? You'd be a good chemists""")
elif grade == 10:
    print(""" I should go to a chemist like you for my problems
since you have all the solutions""")
    





