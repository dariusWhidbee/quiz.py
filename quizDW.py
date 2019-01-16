# Fix Errors

# Variables
score = 0
q1r = False 
q1a = 1

score = 0
q2r = False 
q2a = 2

# Introduction, asks the user 1 question
print(" Hello, this program runs a quiz with 10 questions."
      " based on the options under each question. Choose your"
      " best response")
print()
print("""I start off dry but come out wet. I go in light and come out heavy.
What am I?

1) A teabag
2) A penis
3) A cookie 
4) A spoon""")

# While loop
while q1r == False:
    try:
        print()
        q1a = int(input("Choose the wisely. > "))
         # scoreect answer "3"
        if q1a == 1:
            score += 1
            # if the user answers the question right the boolean turns true
            # and gets out of the while loop
            q1r = True
        elif 0 < q1a < 5:
            q1r = True
            # If the user doesn't respond with a interger between 1 to 4
        else:
            print("please choose an interger from 1 to 4")
            # If the user doesn't respond with a interger
    except ValueError:
         print("Invalid response.Please choose either option 1, 2, 3 or 4")


print()
print("""When I point up, it’s bright. When I point down, it’s dark.
What am I?
1) A flashlight
2) A light switch
3) A lamp
4) The sun and moon""")

while q2r == False:
    try:
        print()
        q2a = int(input("Choose the wisely. > "))
         # scoreect answer "3"
        if q2a == 2:
            score += 1
            # if the user answers the question right the boolean turns true
            # and gets out of the while loop
            q2r = True
        elif 0 < q2a < 5:
            q2r = True
            # If the user doesn't respond with a interger between 1 to 4
        else:
            print("please choose an interger from 1 to 4")
            # If the user doesn't respond with a interger
    except ValueError:
         print("Invalid response.Please choose either option 1, 2, 3 or 4")
         
print()
print("Your score",score + 0,"/10")
