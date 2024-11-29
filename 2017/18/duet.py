import os
import threading
import queue


def part_one(input):
    input = input.strip().splitlines()
    mem = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}
    snd = 0

    i = 0

    while 0 <= i < len(input):
        inst = input[i].split()
        if inst[0] == "snd":
            snd = mem[inst[1]] if inst[1].isalpha() else int(inst[1])
            i += 1
        elif inst[0] == "set":
            mem[inst[1]] = mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += 1
        elif inst[0] == "add":
            mem[inst[1]] += mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += 1
        elif inst[0] == "mul":
            mem[inst[1]] *= mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += 1
        elif inst[0] == "mod":
            mem[inst[1]] %= mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += 1
        elif inst[0] == "rcv":
            if mem[inst[1]] if inst[1].isalpha() else int(inst[1]) != 0:
                break
            i += 1
        elif inst[0] == "jgz":
            x = mem[inst[1]] if inst[1].isalpha() else int(inst[1])
            y = mem[inst[2]] if inst[2].isalpha() else int(inst[2])
            i += y if x > 0 else 1

    return snd


def part_two(input):
    input = input.strip().splitlines()
    queues = [queue.Queue(), queue.Queue()]
    sent = [0, 0]

    def computer(id):
        mem = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}
        mem["p"] = id

        i = 0

        while 0 <= i < len(input):
            inst = input[i].split()
            if inst[0] == "snd":
                queues[1 - id].put(mem[inst[1]] if inst[1].isalpha() else int(inst[1]))
                sent[id] += 1
                i += 1
            elif inst[0] == "set":
                mem[inst[1]] = mem[inst[2]] if inst[2].isalpha() else int(inst[2])
                i += 1
            elif inst[0] == "add":
                mem[inst[1]] += mem[inst[2]] if inst[2].isalpha() else int(inst[2])
                i += 1
            elif inst[0] == "mul":
                mem[inst[1]] *= mem[inst[2]] if inst[2].isalpha() else int(inst[2])
                i += 1
            elif inst[0] == "mod":
                mem[inst[1]] %= mem[inst[2]] if inst[2].isalpha() else int(inst[2])
                i += 1
            elif inst[0] == "rcv":
                try:
                    mem[inst[1]] = queues[id].get(timeout=1)
                    i += 1
                except queue.Empty:
                    return
            elif inst[0] == "jgz":
                x = mem[inst[1]] if inst[1].isalpha() else int(inst[1])
                y = mem[inst[2]] if inst[2].isalpha() else int(inst[2])
                i += y if x > 0 else 1

        return

    thread_0 = threading.Thread(target=computer, args=[0])
    thread_1 = threading.Thread(target=computer, args=[1])

    thread_0.start()
    thread_1.start()

    thread_0.join()
    thread_1.join()

    return sent[1]


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 3423
    print(part_two(input))  # 7493
