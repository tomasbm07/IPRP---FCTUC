import random as r
import turtle as t


def random_number(n):
    movement_file = open('movement_file.txt', 'w+')
    for i in range(n):
        moves = [r.randint(1, 6), r.randint(1, 6)]
        movement_file.write('{} {}\n'.format(moves[0], moves[1]))
    movement_file.close()


def movement():
    movement_file = open('movement_file.txt', 'r')
    line = movement_file.readlines()
    nums = [0 for i in range(len(line))]
    movement_file.close()
    for i in range(len(line)):
        line[i] = line[i].strip('\n')
        nums[i] = line[i].split(' ')

    t.setworldcoordinates(0, 0, 7, 7)
    for i in range(len(nums)):
        t.goto(int(nums[i][0]), int(nums[i][1]))

    print(nums)


t.speed(0)
t.pu()
t.goto(1, 1)
t.pd()
random_number(1000)
movement()
t.exitonclick()
