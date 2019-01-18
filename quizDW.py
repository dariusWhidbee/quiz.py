# Variables
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
# questions ---------------------------------------------------------
#q1 
q1c = False
q1t = str("""Which gas is formed when a hydrogen bomb is detonated?

1) Oxygen
2) Methane
3) Neon
4) Helium""")
q1r = 4

#q2
q2c = False
q2t = str("""Anyone know any jokes about sodium?

1) Na
2) Ok
3) No
4) Ca""")
q2r = 1

#q3
q3c = False
q3t = str("""If Rn has an atomic number of 86 and looses 15 electrons
what's Rn's charge?

1) -15
2) +15
3) 86
4) -86""")
q3r = 2

#q4
q4c = False
q4t = str("""Noble gases are inert because they have completed outer
electron shells. Which of these elements isn't a noble gas?

1) Helium 
2) Argon
3) Chlorine
4) Krypton
""")
q4r = 3

#q5
q5c = False
q5t = str("""Three of the most common states of
matter are solids, liquids, and gases. A liquid has:

1) a defined volume, but not a defined shape
2) a definite shape, but no defined volume
3) a definite volume and shape
4) no defined volume or shape
""")
q5r = 1

#q6
q6c = False
q6t = str("""Can you light a diamond on fire?
1) yes
2) no""")
q6r = 1

#q7
q7c = False
q7t = str("""Does electronegativity increase or decrease
down a group?
1) increase
2) decrease""")
q7r = 2

#q8
q8c = False
q8t = str("""Whats the Scientific Notation of
12,000,600,000?

1) 1.20006 * 10^8
2) 1.2006 * 10^10
3) 1.20006 * 10^10
4) 1.206 * 10^9
""")
q8r = 3

#q9
q9c = False
q9t = str("""Whats Oxygens Electron Configuration?
1) 1s^2, 2s^2, 2s^4
2) 1s^2, 2s^2, 2p^4
3) 1s^2, 2p^2, 2p^6
4) 1d^2, 2s^2, 2p^6
""")
q9r = 2

#q10
q10c = False
q10t = str("""90 ML to L
( K, H, D, B, D, C, M)

1) 9.0 ML to L
2) 000.9 ML to L
3) 9.00 ML to L
4) 0.90 ML to L
""")
q10r = 4
#-------------------------------------------------------------------
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
print("Your score",grade + 0,"/10")


