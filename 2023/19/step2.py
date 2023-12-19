import sys
import math


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
    part = map(lambda x: (x[0], range(int(x[2:]), int(x[2:]) + 1)), part)
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


def process_state(workflows, state_parts):
    state, parts = state_parts

    workflow = workflows[state]

    for w in workflow[:-1]:
        w, next_state = w.split(":")
        p, op, val = w[0], w[1], int(w[2:])
        if op == ">":
            if parts[p][-1] <= val:
                continue
            if parts[p][0] > val:
                yield (next_state, parts)
                return
            out_parts = parts.copy()
            out_parts[p] = range(val + 1, parts[p][-1] + 1)
            yield (next_state, out_parts)
            parts[p] = range(parts[p][0], val + 1)
            continue

        # if op == "<":
        if parts[p][0] >= val:
            continue
        if parts[p][-1] < val:
            yield (next_state, parts)
            return
        out_parts = parts.copy()
        out_parts[p] = range(parts[p][0], val)
        yield (next_state, out_parts)
        parts[p] = range(val, parts[p][-1] + 1)

    yield (workflow[-1], parts)


def accepted_parts(workflows, parts):
    state_parts = ("in", parts)
    todo = [state_parts]
    out = 0
    while todo:
        state_parts = todo.pop()
        next_state_parts = process_state(workflows, state_parts)
        for s_p in next_state_parts:
            state, parts = s_p
            if state == "R":
                continue
            if state == "A":
                out += math.prod([len(x) for x in parts.values()])
                continue
            todo.append(s_p)
    return out


workflows, parts = sys.stdin.read().split("\n\n")

workflows = parse_workflows(workflows)
parts = parse_parts(parts)
out = 0
for p in parts:
    if accepted_parts(workflows, p) == 1:
        out += sum([x[0] for x in p.values()])
print("Part 1:", out)

parts = {
    "x": range(1, 4001),
    "m": range(1, 4001),
    "a": range(1, 4001),
    "s": range(1, 4001),
}
print("Part 2:", accepted_parts(workflows, parts))
