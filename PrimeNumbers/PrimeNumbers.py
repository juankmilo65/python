def is_prime(number):
    count = 0

    for i in range(1, number+1):
        if i == 1 or i == number:
            continue
        if number % 1 == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


def run():
    number = int(input('Type a number'))
    if is_prime(number):
        print('Is prime')
    else:
        print('Is no prime')


if __name__ == "__main__":
    run()
