import sys
import math


def parse_module(line):
    out = dict()
    line = line.strip()
    inp, outp = line.split(" -> ")
    out["output"] = tuple(outp.split(", "))
    out["input"] = tuple()
    if inp == "broadcaster":
        out["type"] = "b"
        return inp, out
    if inp[0] == "&":
        out["type"] = "&"
        return inp[1:], out
    if inp[0] == "%":
        out["type"] = "%"
        return inp[1:], out
    raise Exception()


def get_inputs(modules):
    for mod in modules:
        for o in modules[mod]["output"]:
            if o not in modules:
                continue
            modules[o]["input"] = modules[o]["input"] + (mod,)
    return


def get_init_state(modules):
    for mod in modules.values():
        if mod["type"] == "b":
            mod["state"] = ()
            continue
        if mod["type"] == "%":
            mod["state"] = (False,)
            continue
        if mod["type"] == "&":
            mod["state"] = (False,) * len(mod["input"])
            continue
        raise Exception()
    return


def process_pulse(modules, fr, end):
    todo = [(False, "broadcaster", fr)]
    found = False

    step = 0
    while todo:
        step += 1
        pulse, fr, mod = todo.pop(0)
        if mod == end and pulse:
            found = True
        if not pulse and mod == "rx":
            found = True
        if mod not in modules:
            continue
        module = modules[mod]
        if module["type"] == "b":
            for m in module["output"]:
                todo.append((pulse, mod, m))
            continue
        if module["type"] == "%":
            if pulse:
                continue
            next_pulse = not module["state"][0]
            module["state"] = (next_pulse,)
            for m in module["output"]:
                todo.append((next_pulse, mod, m))
            continue
        if module["type"] == "&":
            state = list(module["state"])
            state[module["input"].index(fr)] = pulse
            module["state"] = tuple(state)
            if all(module["state"]):
                next_pulse = False
            else:
                next_pulse = True
            for m in module["output"]:
                todo.append((next_pulse, mod, m))
            continue
    return found


def find_pulse(modules, fr, end):
    step = 0
    while not process_pulse(modules, fr, end):
        step += 1
    return step + 1


def print_graph(modules):
    print("digraph G {")
    for i in modules:
        for j in modules[i]["output"]:
            print(i, "->", j)
    print("}")


def get_fewest(modules):
    for m in modules:
        if modules[m]["output"] == ("rx",):
            end = m
            break
    least = 1
    for m in modules["broadcaster"]["output"]:
        least = math.lcm(least, find_pulse(modules, m, end))

    return least


modules = dict()
lines = sys.stdin.readlines()
modules = dict(map(parse_module, lines))

get_inputs(modules)
get_init_state(modules)

print("Part 2:", get_fewest(modules))

# 243221023462303
