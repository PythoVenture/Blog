count = 0

print("******QUIZ******")
print("(Please type only A, B or C as a answer)\n")

print("QUESTION #1")
print("What's the shortcut for new terminal?")
print(" A: Ctrl+Shift+`\n B: Alt+F4\n C: Ctrl+Shift+T")

quiz1 = input("Pleas type your answer:")

if quiz1 == "A":
    count += 1

print("\n")
print("QUESTION #2")
print("What type of data can be use in input?")
print(" A: Only stringA\n B: Only numbers\n C: Almost everything")

quiz2 = input("Pleas type your answer: ")

if quiz2 == "C":
    count += 1
else:
    pass

print(f" !!!Congratuation!!!\n   Your score is {count}!")