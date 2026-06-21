import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0 
    
    print("--- Welcome to the Number Guessing Game! ---")
    print("I have thought of a number between 1 and 100. Can you guess it?")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1 
        
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number.")
            print(f"It took you {attempts} attempts.")
            break
        elif guess < secret_number:
            print("📉 Uh-oh! Your guess is low. Try a bigger number.")
        else:
            print("📈 Oh! Your guess is high. Try a smaller number.")

start_game()