import re

with open("input.txt", "r") as file:
    # print(file.read())

    content = file.read()

# regex = "mul\((\d{1,3}),(\d{1,3})\)" # part 1
regex = "mul\((\d{1,3}),(\d{1,3})\)|(do)(n't)?\(\)"  # part 2

s = re.findall(regex, content)

print(type(s[0]))

print(s)


def part_one(calcs):

    total = 0

    for pair in calcs:
        m = int(pair[0]) * int(pair[1])
        total = total + m

    return total


def part_two(calcs):
    total = 0
    allow_calc = True
    for pair in s:
        print(pair)

        if allow_calc and pair[3] != "n't" and pair[0] and pair[1]:
            m = int(pair[0]) * int(pair[1])
            total = total + m
        elif pair[3] == "n't":
            allow_calc = False
            continue
        elif pair[2] == "do":
            allow_calc = True
            continue
    return total


# print(part_one(s))
print(part_two(s))
