rules = []
ret = 0


def check_rules(pages):
    for page in pages:
        for l, r in rules:
            if int(l) == int(page) and int(r) in pages:
                # print("page:", page, "rule:", l, r)
                # print(pages.index(int(r)), pages.index(int(l)))
                if pages.index(int(r)) <= pages.index(int(l)):
                    print("break", page, l, r)
                    return False
    else:
        return True


def part_two_sort(pages):
    n = len(pages)
    swapped = True

    # bubble sort 😭
    while swapped:
        swapped = False
        for i in range(n - 1):
            need_swap = False
            for l, r in rules:
                if int(l) == pages[i + 1] and int(r) == pages[i]:
                    need_swap = True
                    break

            if need_swap:
                pages[i], pages[i + 1] = pages[i + 1], pages[i]
                swapped = True

    return pages


p = []

with open("input.txt", "r") as file:

    for line in file:
        if "|" in line:
            rules.append(list(line.strip().split("|")))

        elif "," in line:
            p.append(list(map(int, line.split(","))))
            # print(p)

            # print(l, r, page, int(l) == int(page), int(r) == int(page))

            # if page in rules:
            # print("hello")

# print(rules)
print(p)

c = 0
c2 = 0
for p2 in p:
    print(p2)
    if check_rules(p2):
        c = c + p2[len(p2) // 2]
    else:
        d = part_two_sort(p2)
        print(d)
        c2 = c2 + d[len(d) // 2]
        print("d:", part_two_sort(p2))
        print("s")
    # c.append(check_rules(p2))

print(c)
print(c2)
