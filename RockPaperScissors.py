# Orion Davis 3003072 ord4@zips.uakron.edu
# 2-Player Rock Paper Scissors

print("Your options are:\n1. Rock\n2. Paper\n3. Scissors")

playerOne = int(input("\nPlayer one please enter the number of your choice: "))
playerTwo = int(input("Player two please enter the number of your choice: "))
# Later come back and validate the inputs to make sure they are 1-3

# How can the logic be compressed to increase performance
if playerOne == 1:
    if playerTwo == 1:
        print("\nTie")
    elif playerTwo == 2:
        print("\nPlayer two wins!")
    else:
        print("\nPlayer one wins!")

elif playerOne == 2:
    if playerTwo == 1:
        print("\nPlayer one wins!")
    elif playerTwo == 2:
        print("\nTie")
    else:
        print("\nPlayer two wins!")

elif playerOne == 3:
    if playerTwo == 1:
        print("\nPlayer one wins!")
    elif playerTwo == 2:
        print("\nPlayer one wins!")
    else:
        print("\nTie")

print("\nThanks for playing!!\n")
