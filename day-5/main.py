rules = []
ret = 0


def check_rules(pages):
    for page in pages:
        for l, r in rules:
            if int(l) == int(page) and int(r) in pages:
                # print("page:", page, "rule:", l, r)
                # print(pages.index(int(r)), pages.index(int(l)))
                if pages.index(int(r)) <= pages.index(int(l)):
                    print("break")
                    return False
    else:
        return True


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
for p2 in p:
    print(p2)
    if check_rules(p2):
        c = c + p2[len(p2) // 2]
    # c.append(check_rules(p2))

print(c)
