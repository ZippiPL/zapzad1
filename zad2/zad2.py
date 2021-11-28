names = ['denis', 'monika', 'marysia']
numbers = [1, 2, 3, 4, 5]


def print_hi(tab_names):
    for name in tab_names:
        print(name)


def print_numbers(tab_numbers):
    for number in tab_numbers:
        print("Table number:{}".format(number))


def count_numbers(tab_numbers):
    for number in tab_numbers:
        number = number*2
        print("Table number * 2 :{}".format(number))


def count_numbersv2():
    numbersv2 = [x for x in range(5, 10)]
    print(numbersv2)
    numbersv2 = [x*2 for x in numbersv2]
    print(numbersv2)


def shuffle_numbers():
    numbers_to_shuffle = [x for x in range(1, 10) if x % 2 == 0]
    print(numbers_to_shuffle)


def skipshuffle_numbers():
    numbers_skip = [x for x in range(1, 10, 2)]
    print(numbers_skip)


if __name__ == '__main__':
    print_hi(names)
    print_numbers(numbers)
    count_numbers(numbers)
    count_numbersv2()
    shuffle_numbers()
    skipshuffle_numbers()
