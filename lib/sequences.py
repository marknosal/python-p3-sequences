#!/usr/bin/env python3

# def print_fibonacci(length):
#     if length == 0:
#         print([])
#     elif length == 1:
#         print([0])
#     else:
#         fib_list = [0,1]

#         while len(fib_list) < length:
#             next_int = fib_list[-1] + fib_list[-2]
#             fib_list.append(next_int)

#         print(fib_list)


# Much better code:
def print_fibonacci(length):
    if length == 0:
        fib_list = []
    elif length == 1:
        fib_list = [0]
    else:
        fib_list = [0,1]
        for _ in range(length - 2):
            fib_list.append(sum(fib_list[-2:]))
    print(fib_list)