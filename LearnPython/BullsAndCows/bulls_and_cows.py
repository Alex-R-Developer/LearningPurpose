from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("The computer has randomly generated three different numbers between 0 and 9.\n")
    return numbers


def take_guess():
    print("Enter your guess for each number, one at a time.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input("Enter the {} number: ".format(len(new_guess) + 1)))

        if new_num < 0 or new_num > 9:
            print("Invalid input. Number must be between 0 and 9.")
        elif new_num in new_guess:
            print("Invalid input. Number has already been guessed.")
        else:
            new_guess.append(new_num)

    return new_guess


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# Begin game
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("Congratulations! You guessed the numbers in {} tries.".format(tries))
