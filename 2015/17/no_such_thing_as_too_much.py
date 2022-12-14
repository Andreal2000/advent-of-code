import os


def part_one(input):
    input = sorted(map(int, input.strip().split("\n")), reverse=True)
    liters = 150

    def filler(containers, quantity):
        if quantity == 0:
            return 1

        if len(containers) == 1:
            return 1 if containers[0] == quantity else 0

        yes = (filler(containers[1:], quantity - containers[0])
               if quantity >= containers[0] else 0)

        no = (filler(containers[1:], quantity)
              if sum(containers[1:]) >= quantity else 0)

        return yes + no

    return filler(input, liters)


def part_two(input):
    input = sorted(map(int, input.strip().split("\n")), reverse=True)
    liters = 150

    def filler(containers, quantity, out=[]):
        if quantity == 0:
            return [out]

        if len(containers) == 1:
            return [out + containers if containers[0] == quantity else []]

        yes = (filler(containers[1:],
                      quantity - containers[0],
                      out + [containers[0]])
               if quantity >= containers[0] else [])

        no = (filler(containers[1:], quantity, out)
              if sum(containers[1:]) >= quantity else [])

        return yes + no

    out = [len(x) for x in filler(input, liters) if len(x) > 0]
    m = min(out)

    return sum([x == m for x in out])


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 654
    print(part_two(input))  # 57
