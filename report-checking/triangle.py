import random
secret = random.randint(1,500)
attempt = 0
max_attempt = 7
while attempt < max_attempt:
    guess = int(input("Enter Your Number "))
    attempt =- 1
    if guess == secret:
        print(f"Congratulation! You Guessed The Perfect Number!")
        break
    elif guess < secret:
        print(f"Too Low!")
    else:
        print(f"Too High!")


if attempt == max_attempt:
    print("Sorry Bro, You Are Out Of The Rules! The Secret Number Was {secret}")




                  
