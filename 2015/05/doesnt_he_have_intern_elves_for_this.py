import os


def part_one(input):
    def is_nice(word):
        vowels = "aeiou"
        bad_str = ("ab", "cd", "pq", "xy")
        propertie_1 = sum([w in vowels for w in word]) >= 3
        propertie_2 = any([word[i] == word[i+1] for i in range(len(word)-1)])
        propertie_3 = not any([b in word for b in bad_str])
        return propertie_1 and propertie_2 and propertie_3

    return sum(map(is_nice, input.strip().splitlines()))


def part_two(input):
    def is_nice(word):
        propertie_1 = any([word[i:i+2] in word[i+2:]
                          for i in range(len(word)-3)])
        propertie_2 = any([word[i] == word[i+2]
                          for i in range(len(word)-2)])
        return propertie_1 and propertie_2

    return sum(map(is_nice, input.strip().splitlines()))


if __name__ == "__main__":
    input = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()
    print(part_one(input))  # 255
    print(part_two(input))  # 55
