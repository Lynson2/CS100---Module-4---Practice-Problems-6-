'''6. Write a program that stores a secret number in a variable (e.g., 7).
The program then peforms the following tasks:
• Ask the user for a guess.
• If the guess equals the secret number, print "Correct!".
• If the guess is too low, print "Too low.".
• Otherwise, print "Too high.".
Example Run:
Guess the secret number: 3
Too low.
Guess the secret number: 7
Correct!'''

guess_num = int(input("Enter your guess"))
secret_num = 17

if guess_num == secret_num:
    print("Correct!")
elif guess_num < secret_num:
    print("Too low.")
else:
    print("Too high.")
