file = open('primeiro.txt', 'r')
numbers = [str(p) for p in range(10)]

lines = file.readlines()
nums = []
print(lines)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in numbers:
            nums.append(int(lines[i][j]))

nums.sort()
print(nums)
print(list(set(nums)))

file.close()
