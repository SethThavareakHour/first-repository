import random

def generate_number():
  return random.randint(1, 100)

def get_user_guess():
  guess = input("Guess a number between 1 and 100: ")
  while not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
    print("Invalid input. Please enter a number between 1 and 100.")
    guess = input("Guess a number between 1 and 100: ")
  return int(guess)

def is_correct_guess(number, guess):
  return number == guess

def main():
  number = generate_number()
  guess_count = 0
  while not is_correct_guess(number, guess_count):
    guess = get_user_guess()
    guess_count += 1
    if is_correct_guess(number, guess):
      print("Congratulations! You guessed the correct number in {} guesses.".format(guess_count))
    else:
      if guess < number:
        print("Your guess is too low.")
      else:
        print("Your guess is too high.")

if __name__ == "__main__":
  main()
