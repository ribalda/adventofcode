import sys


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


def process_pulse(modules):
    todo = [(False, "button", "broadcaster")]
    n_low, n_high = 0, 0
    found = False

    while todo:
        pulse, fr, mod = todo.pop(0)
        if pulse:
            n_high += 1
        else:
            n_low += 1
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
    return n_low, n_high, found


modules = dict()
lines = sys.stdin.readlines()
modules = dict(map(parse_module, lines))

get_inputs(modules)
get_init_state(modules)

found = False
step = 0
out_low, out_high = 0, 0
while step < 1000 or not found:
    step += 1
    n_low, n_high, is_found = process_pulse(modules)
    out_low += n_low
    out_high += n_high
    if step == 1000:
        print("Part 1:", out_low * out_high)
    if is_found == 1000:
        print("Part 2:", step)
        found = True
