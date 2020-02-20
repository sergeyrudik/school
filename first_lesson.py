import string
import random

st = input("Введите строку: ")


def first_func(st):
    for i in range(int(st)):
        print('#' * (i+1))

    return first_func


def second_func(st):
    sum = 0
    for s in st:
        if s.isdigit():
            sum += int(s)
    return sum


def third_func(*args):
    sum_args = 0
    for i in args:
        sum_args += i

    return sum_args


def four_func(st):

    arr = []
    for s in st:
        a = (st.index(s)+1, s)
        arr.append(a)
    return arr


def fifth_func():
    minimum = input('Введите минимум: ')
    maximum = input('Введите максимум: ')
    length = input('Введите длина: ')

    a = [random.choice([i for i in range(int(minimum), int(maximum))]) for j in range(int(length))]

    return a


init = list(string.ascii_lowercase)
init.append(' ')


def six_func(len_st):
    st = ''
    for i in range(0, len_st):
        rand = random.randint(0, len(init)-1)
        st += init[rand]
    return st
