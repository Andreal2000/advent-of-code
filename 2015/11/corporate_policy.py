import os


def increment(word):
    if word == "z"*8:
        return "a"*8
    elif word[-1] == "z":
        return increment(word[:-1]) + "a"
    else:
        return (word[:-1] +
                chr(ord(word[-1]) +
                (1 if ord(word[-1]) not in [104, 107, 110] else 2)))


def part_one(input):
    def requirement_1(word):
        for i in range(len(word) - 2):
            if ord(word[i]) == ord(word[i+1])-1 == ord(word[i+2])-2:
                return True
        return False

    def requirement_2(word):
        for i in range(len(word)):
            if ord(word[i]) in [105, 108, 111]:
                return word[:i] + chr(ord(word[i])+1) + "a"*(len(word)-1-i)
        return word

    def requirement_3(word):
        pairs = 0
        i = 0
        while i < len(word)-1:
            if word[i] == word[i+1]:
                pairs += 1
                i += 1
            i += 1
        return pairs == 2

    input = requirement_2(input)

    while not (requirement_1(input) and requirement_3(input)):
        input = increment(input)

    return input


def part_two(input):
    return part_one(increment(part_one(input)))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # hxbxxyzz
    print(part_two(input))  # hxbxwxba
