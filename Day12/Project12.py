# Project 12
print('''╔══════════════════════════════════════════╗
║          NUMBER GUESSING GAME            ║
╠══════════════════════════════════════════╣
║                                          ║
║                                          ║
║        Can you guess it right?           ║
║                                          ║
║        Easy Mode  : 10 Attempts          ║
║        Hard Mode  : 5 Attempts           ║
╚══════════════════════════════════════════╝
''')
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
import random
num=random.choice(range(1,101))
difficulty=input("Choose a level. Type 'easy' or 'hard': ").lower()


if difficulty=="easy":
    chances=10
    
    print(f"you have {chances} attempts to guess the number.")
    guess=int(input("Make a guess: "))
    
    if guess!=num:
        while chances>0:
            if guess<num:
                print("Too low")
                chances-=1
            elif guess>num:
                print("Too high")
                chances-=1

            if chances==0:
                print("No attempts left. Game over!")
                break

            print(f"you have {chances} attempts to guess the number.")
            guess=int(input("Guess again: "))

            if guess==num:
                print("You guessed it right! You won!")
                break
    else:
        print("You guessed it right in your first attempt! You won!")


if difficulty=="hard":
    chances=5
    
    print(f"you have {chances} attempts to guess the number.")
    guess=int(input("Make a guess: "))
    
    if guess!=num:
        while chances>0:
            if guess<num:
                print("Too low")
                chances-=1
            elif guess>num:
                print("Too high")
                chances-=1

            if chances==0:
                print("No attempts left. Game over!")
                break

            print(f"you have {chances} attempts to guess the number.")
            guess=int(input("Guess again: "))

            if guess==num:
                print("You guessed it right! You won!")
                break
    else:
        print("You guessed it right in your first attempt! You won!")


        
        
                
            

