import sys


def parse_workflow(workflow):
    workflow = workflow.strip()
    name, right = workflow.split("{")
    right = right[:-1]
    right = right.split(",")
    return name, right


def parse_workflows(workflows):
    workflows = workflows.splitlines()
    out = dict()
    for w in workflows:
        name, content = parse_workflow(w)
        out[name] = content
    return out


def parse_part(part):
    part = part.strip()
    part = part.strip("{}")
    part = part.split(",")
    part = map(lambda x: (x[0], int(x[2:])), part)
    return dict(part)


def parse_parts(parts):
    parts = parts.splitlines()
    parts = map(parse_part, parts)
    return tuple(parts)


def accepted_part(workflows, part):
    state = "in"
    while state not in ("A", "R"):
        workflow = workflows[state]

        for w in workflow[:-1]:
            w, next_state = w.split(":")
            p, op, val = w[0], w[1], int(w[2:])
            if op == ">":
                if part[p] > val:
                    state = next_state
                    break
            elif op == "<":
                if part[p] < val:
                    state = next_state
                    break
            else:
                print(op)
        else:
            state = workflow[-1]
    return state == "A"


workflows, parts = sys.stdin.read().split("\n\n")

workflows = parse_workflows(workflows)
parts = parse_parts(parts)
out = 0
for p in parts:
    if accepted_part(workflows, p):
        out += sum(p.values())
print("Part 1:", out)

out = 0
for x in range(1, 4001):
    for m in range(1, 4001):
        for a in range(1, 4001):
            for s in range(1, 4001):
                part = {
                    "x": x,
                    "m": m,
                    "a": a,
                    "s": s,
                }
                if accepted_part(workflows, part):
                    out += 1
print("Part 2:", out)
