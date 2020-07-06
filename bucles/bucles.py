def run():
    LIMIT = 10
    count = 0
    for_count = 1
    rise_2 = 2**count
    while rise_2 < LIMIT:
        print('2 reised to ' + str(count) + ' is: ' + str(rise_2))
        count = count+1
        rise_2 = 2**count

    for for_count in range(LIMIT+1):
        print(for_count)

    sentence = input('Type a sentence: ')
    for character in sentence:
        print(character.upper())

    for count in range(10):
        if count % 2 != 0:
            continue
        print(count)

    for i in range(5):
        print(i)
        if i == 3:
            break


if __name__ == '__main__':
    run()
