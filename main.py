import random
def game(Comp,b):
    if Comp == b :
        return None
    if Comp =='s':
        if b =='w':
            return False
        elif b =='g':
            return True
        elif Comp =='w':
            if b == 'g':
                return False
            elif b =='s':
                return True
        elif Comp =='g':
            if b == 's':
                return False
            elif b =='w':
                return True
            

print("Comp Turn : Snake(s) Water(w) or Gun(g)?")
randNO = random.randint(1,3)
#print(randNO)
if randNO == 1:
    Comp = 's'
elif randNO == 2:
    Comp = 'w'
elif randNO == 3:
    Comp = 'g'

b = input("Player's Turn : Snake(s) Water(w) or Gun(g)?")
a = game(Comp , b)
print(f"Computer chose {Comp}")
print(f" b chose {b}")
game(Comp, b)
if a == None:
    print("the game is a tie!")
elif a:
    print("YOU WIN !")
else:
    print("YOU LOSE!")
