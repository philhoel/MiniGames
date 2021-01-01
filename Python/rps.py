import random

c = "sad"
print(c.capitalize())

def cpu():

    a = random.randint(1,4)
    if a == 1:
        return "Rock"
    elif a == 2:
        return "Paper"
    else:
        return "Scissors"

def player():
    b = input("Enter Rock, Paper or Scissors: ")
    #print(b.capitalize())
    if (b.capitalize() != "Rock" and b.capitalize() != "Paper" and b.capitalize() != "Scissors"):
        print("Needs to be rock, paper or scissors")
        player()
    else:
        return b.capitalize()

print("Rock!")
print("Paper!")
print("Scissors!")
p = player()
cpu = cpu()

if cpu == p:
    print(f"CPU: {cpu} || Player: {p}")
    print("Its a tie")

elif cpu == "Rock" and p == "Paper":
    print(f"CPU: {cpu} || Player: {p}")
    print("You Win!")

elif cpu == "Scissors" and p == "Paper":
    print(f"CPU: {cpu} || Player: {p}")
    print("You Loose!")

elif cpu == "Paper" and p == "Rock":
    print(f"CPU: {cpu} || Player: {p}")
    print("You Loose!")

elif cpu == "Paper" and p == "Scissors":
    print(f"CPU: {cpu} || Player: {p}")
    print("You Win!")

elif cpu == "Scissors" and p == "Rock":
    print(f"CPU: {cpu} || Player: {p}")
    print("You Win!")

elif cpu == "Rock" and p == "Scissors":
    print(f"CPU: {cpu} || Player: {p}")
    print("You Loose!")