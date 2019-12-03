import turtle as t
import random as r

def navega():
    xd = True
    while xd:
        char = input('Digite um caracter que define o movimento: ')
        if char == 'A':
            t.fd(20)
        if char == 'E':
            t.lt(90)
        if char == 'D':
            t.rt(90)
        if char == 'R':
            t.bk(20)
        if char == 0:
            t.exit()

navega()