import random
import logo
import data

listData = data.data
isTrue = True
score = 0

while isTrue:
    # Compare case Index
    compareCase1Int = random.randint(0, len(listData))
    compareCase2Int = random.randint(0, len(listData))
    while compareCase1Int == compareCase2Int:
        compareCase2Int = random.randint(0, len(listData))

    # Print Questions
    print(logo.logo)
    print(f"Compare A: {listData[compareCase1Int]['name']}, {listData[compareCase1Int]['description']}, from {listData[compareCase1Int]['country']}")
    print(logo.vs)
    print(f"Compare B: {listData[compareCase2Int]['name']}, {listData[compareCase2Int]['description']}, from {listData[compareCase2Int]['country']}")

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
        print(f"You're right! Current score: {score}")
    else:
        isTrue = False
        print(f"Sorry, that's wrong. Final score: {score}")
        print(score)
