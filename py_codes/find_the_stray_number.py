# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)


def stray(number):
    for n in number:
        if n % 2 == 0 or n == 3:
            return n
        elif n % 2 == 1 and n >= 3:
            return n

number = [1, 1, 1, 1, 1, 1, 2]
number = [2, 3, 2, 2, 2]
number = [3, 2, 2, 2, 2]

print(stray(number))
print(stray(number))
print(stray(number))

"""
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
"""