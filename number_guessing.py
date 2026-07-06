Number = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
print(f"Guess any from this : {Number}\n")
import random
Lucky_Number = random.choice(Number)
Player = int(input("Guess the Lucky Number : "))
print(f"Player : {Player}\n")
print(f"Lucky Number : {Lucky_Number}\n")
if Lucky_Number == Player :
    print("Congratulation! You Won\n")
else :
    print("Better Luck Next Time\n")




