import random


print("Snake, Water, Gun Game")

def game(a, b):
    if a == b:
        return None
    elif a == 's':
        if b == 'w':
            return False
        elif b == 'g':
            return True
    elif a == 'w':
        if b == 'g':
            return False
        elif b == 's':
            return True
    elif a == 'g':
        if b == 's':
            return False
        elif b == 'w':
            return True

print("Computer's turn: Press Snake(s), Water(w) and Gun(g)")
compSelection = random.randint(1, 3)
# print(compSelection)
if compSelection == 1:
    comp = "s"
elif compSelection == 2:
    comp = "w"
elif compSelection == 3:
    comp = "g"

you = input("Your turn: Press Snake(s), Water(w) and Gun(g) ")

gameResult = game(comp, you)
print("Computer choose = " + comp)
print("You choose = " + you)
if gameResult == None:
    print("Game Tied")
elif gameResult:
    print("you Win")
else:
    print("you Lose")
