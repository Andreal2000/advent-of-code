import os


def computer(input, mem):
    def hlf(r): return r // 2
    def tpl(r): return r * 3
    def inc(r): return r + 1
    def jmp(_, offset): return offset
    def jie(r, offset): return jmp(0, offset) if r % 2 == 0 else 1
    def jio(r, offset): return jmp(0, offset) if r == 1 else 1

    instructions = {"hlf": hlf,
                    "tpl": tpl,
                    "inc": inc,
                    "jmp": jmp,
                    "jie": jie,
                    "jio": jio, }

    input = input.strip().replace(",", "").splitlines()

    i = 0

    while 0 <= i < len(input):
        inst = input[i].split()
        if inst[0].startswith("j"):
            i += instructions[inst[0]](mem.get(inst[-2]), int(inst[-1]))
        else:
            mem[inst[-1]] = instructions[inst[0]](mem[inst[-1]])
            i += 1

    return mem


def part_one(input):
    return computer(input, {"a": 0, "b": 0})["b"]


def part_two(input):
    return computer(input, {"a": 1, "b": 0})["b"]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 255
    print(part_two(input))  # 334
