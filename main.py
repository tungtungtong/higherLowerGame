import random
import logo
import data

listData = data.data
isTrue = True
score = 0
compareCase1 = {}
compareCase2 = {}

# Function: print
def questionPrint():
    print(logo.logo)
    if isTrue:
        print(f"Current score: {score}")
    print(f"Compare A: {compareCase1['name']}, {compareCase1['description']}, from {compareCase1['country']}")
    print(logo.vs)
    print(f"Compare B: {compareCase2['name']}, {compareCase2['description']}, from {compareCase2['country']}")

# Function: Take random index
def randomCase():
    global compareCase1
    global compareCase2

    # Take random Index
    compareCase1 = random.choice(listData)
    compareCase2 = random.choice(listData)

    # Check in Case 1 == Case 2
    if compareCase1 == compareCase2:
        compareCase2 = random.choice(listData)

def continueAsk():
    global isTrue
    global score
    
    continueRequest = input("Do you want to restart: y or n? ")
    if continueRequest == "y":
        print(chr(27) + "[2J")
        isTrue = True
        score = 0
    else:
        print("Game Over")

# Clear Screen
print(chr(27) + "[2J")

while isTrue:
    # Random index
    randomCase()

    # Print Questions
    questionPrint()

    # Input player choice
    compareChoice = input("Who have more follower: 'A' or 'B'? ")
    compareResult = "A"

    # Take follower
    followerA = int(compareCase1['follower_count'])
    followerB = int(compareCase2['follower_count'])

    # Compare
    if followerA > followerB:
        compareResult = "A"
    else:
        compareResult = "B"

    # Result
    print(chr(27) + "[2J")
    if compareChoice == compareResult:
        score += 1
    else:
        isTrue = False
        print(logo.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        continueAsk()