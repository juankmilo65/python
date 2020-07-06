import random


def run():
    random_number = random.randint(1, 100)
    number = int(input("Type a number between 1 and 100: "))
    while number != random_number:
        if number < random_number:
            print('Seek a larger number')
        else:
            print('Seek a smaller number')
        number = int(input("Type a number: "))
    print('You Won!')


if __name__ == "__main__":
    run()
