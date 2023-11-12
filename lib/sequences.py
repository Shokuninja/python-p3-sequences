#!/usr/bin/env python3

def print_fibonacci(length):
    first = 0
    second = 1

    if length == 1:
        print([0])

    elif length > 1:
        fib_sequence = [first, second]
        length -= 2

        while length > 0:

            next_number = first + second
            fib_sequence.append(next_number)

            temp = second
            second = first + second
            first = temp

            length -= 1

        print(fib_sequence)
    else:
        print([])
