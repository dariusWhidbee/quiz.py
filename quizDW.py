# Variables
score = 0

def run_quest(quest, check, ansU, ansR):
    print(quest)
    while check == False:
        try:
            print()
            ansU = int(input("Responce. > "))
            # coreect answer "3"
            if ansU == 1:
                #global grade
                #grade += 1
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
print(" Hello there, new user. This program will run a quiz with 10 questions."
"Using  your prior knowledge, choose your best response. Good Luck!")
print()

#q1 
q1c = False
q1t = str("""Which gas is formed when a hydrogen bomb is detonated?
1) Oxygen
2) Methane
3) Neon
4) Helium""")
qlr = 4

# runs the question
run_quest(q1t, q1c, 0, qlr)


# score
#print()
#print("Your score",score + 0,"/10")


