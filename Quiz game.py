#Quiz Game 
print("Welcome to my computer quiz!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":  #We used playing.lower() because if an individual type yes in capital letters such as Yes,YES,YeS then 
    quit()  #after putting .lower() every capital letters will be converted into small letters 

print("Okay! Let's play :) ")
score = 0

answer = input("What does CPU stands for? ")

if answer =="central processing unit":
    print("correct !")
    score += 1
else:
    print("incorrect!")

answer = input("What does GPU stands for? ")
if answer == "graphics processing unit":
    print("Correct !")
    score += 1
else:
    print("Incorrect!")

answer = input("Name capital city of India? ")
if answer == "New Delhi":
    print('Correct !')
    score += 1
else:
    print("Incorrect!")

answer = input("Name Capital city of Rajasthan? ")
if answer == "Jaipur":
    print('Correct !')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
          

