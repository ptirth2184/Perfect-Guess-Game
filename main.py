from random import randint
n = randint(1, 100)
a= -1
guesses  = 1
while(a != n):
    a = int(input("Guess a Number: "))

    if(a>n):
        print("Lower Number please")
    elif(a<n):
        print("Higher Number please")
    guesses += 1

print(f"You guess the correct number {n} in {guesses} attempt")