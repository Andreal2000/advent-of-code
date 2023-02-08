import os


def part_one(input):
    input = input.strip().splitlines()

    def AND(a, b): return find_signal(a) & find_signal(b)
    def OR(a, b): return find_signal(a) | find_signal(b)
    def LSHIFT(a, b): return (find_signal(a) << int(b)) & ((1 << 16)-1)
    def RSHIFT(a, b): return find_signal(a) >> int(b)

    operations = {"AND": AND, "OR": OR, "LSHIFT": LSHIFT, "RSHIFT": RSHIFT}

    wires = {}

    def find_signal(signal):
        i = 0

        if signal.isdecimal():
            return int(signal)

        if signal in wires.keys():
            return wires[signal]

        while not input[i].endswith(f" -> {signal}"):
            i += 1

        line = input[i].split()
        out = 0

        if len(line) == 3:
            if not line[0].isdecimal():
                return find_signal(line[0])
            out = line[0]

        elif len(line) == 4:
            out = ~find_signal(line[1])

        elif len(line) == 5:
            out = operations[line[1]](line[0], line[2])

        wires[signal] = int(out)
        return int(out)

    return find_signal("a")


def part_two(input):
    input_two = input.strip().splitlines()
    i = 0

    while not input_two[i].endswith(" -> b"):
        i += 1

    input_two[i] = f"{part_one(input)} -> b"

    return part_one("\n".join(input_two))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 3176
    print(part_two(input))  # 14710
