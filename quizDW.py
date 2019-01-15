# Fix Errors

# Variables
score = 0
q1r = False 
q1a = 3



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
print("Your score is", score + 0,"/ 10")
