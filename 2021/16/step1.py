import sys


def to_bin(hexs):
    out = ""
    for h in hexs:
        d = int(h, 16)
        out += "{0:b}".format(d).zfill(4)
    return out


def to_packet(bins):
    i = 0
    while i < len(bins) - 7:
        start = i
        packet = dict()
        packet["version"] = int(bins[i:i+3], 2)
        i += 3

        packet["type"] = int(bins[i:i+3], 2)
        i += 3

        if packet["type"] == 4:
            packet["data"] = list()
            while True:
                data = int(bins[i+1:i+5], 2)
                packet["data"].append(data)
                i += 5
                if bins[i-5] == "0":
                    v = 0
                    for j in packet["data"]:
                        v *= 16
                        v += j
                    packet["value"] = v
                    break
        else:
            packet["length_type_id"] = int(bins[i:i+1], 2)
            i += 1
            if packet["length_type_id"] == 0:
                packet["length"] = int(bins[i:i+15], 2)
                i += 15
            else:
                packet["n_packages"] = int(bins[i:i+11], 2)
                i += 11

        packet["content"] = bins[start:i]
        yield packet


for lines in sys.stdin.readlines():
    binstr = to_bin(lines.strip())
    v_sum = 0
    for p in to_packet(binstr):
        v_sum += p["version"]
    print(v_sum)
