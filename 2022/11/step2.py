import sys

inp = sys.stdin.read()
monk = inp.split("\n\n")


multi = 1
monkeys = list()
for m in monk:
    monkey = dict()
    lines = m.splitlines()
    si = lines[1].split("Starting items: ")[1].split(", ")
    monkey["items"] = list(map(int, si))
    monkey["operation"] = lines[2].split("Operation: new = ")[1]
    monkey["test"] = int(lines[3].split("Test: divisible by ")[1])
    monkey["true"] = int(lines[4].split("If true: throw to monkey ")[1])
    monkey["false"] = int(lines[5].split("If false: throw to monkey ")[1])
    monkey["inspect"] = 0
    multi *= monkey["test"]
    monkeys.append(monkey)


for r in range(10000):
    for m in monkeys:
        while len(m["items"]):
            m["inspect"] += 1
            old = m["items"].pop(0)
            new = eval(m["operation"])
            new = new % multi
            if new % m["test"] == 0:
                dest = m["true"]
            else:
                dest = m["false"]
            monkeys[dest]["items"].append(new)

inspects = [m["inspect"] for m in monkeys]
inspects = sorted(inspects)
print(inspects[-1] * inspects[-2])
