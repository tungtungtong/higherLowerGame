import random
import logo
import data

listData = data.data
isTrue = True
score = 0
compareCase1Int = 0
compareCase2Int = 0

# Function: print
def questionPrint():
    print(logo.logo)
    if isTrue:
        print(f"Current score: {score}")
    print(f"Compare A: {listData[compareCase1Int]['name']}, {listData[compareCase1Int]['description']}, from {listData[compareCase1Int]['country']}")
    print(logo.vs)
    print(f"Compare B: {listData[compareCase2Int]['name']}, {listData[compareCase2Int]['description']}, from {listData[compareCase2Int]['country']}")

# Function: Take random index
def randomCase():
    global compareCase1Int
    global compareCase2Int

    # Take random Index
    compareCase1Int = random.randint(0, len(listData)-1)
    compareCase2Int = random.randint(0, len(listData)-1)

    # Compare case Index
    while compareCase1Int == compareCase2Int:
        compareCase2Int = random.randint(0, len(listData))

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
    followerA = int(listData[compareCase1Int]['follower_count'])
    followerB = int(listData[compareCase2Int]['follower_count'])

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