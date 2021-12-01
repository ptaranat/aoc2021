def solution1(input_file: str):
    with open(input_file, "r") as f:
        count = -1  # first one doesn't count
        last = 0
        for line in f:
            num = int(line)
            if num > last:
                count += 1
            last = num
        print(f"day 01 q1: {count}")


def solution2(input_file: str):
    with open(input_file, "r") as f:
        arr = [int(i) for i in f.readlines()]
        count = -1
        last = 0
        for i in range(len(arr) - 2):
            if sum(arr[i : i + 3]) > last:
                count += 1
            last = sum(arr[i : i + 3])
        print(f"day 01 q2: {count}")


try:
    solution1("input.txt")
    solution2("input.txt")
except FileNotFoundError:
    print("No input file!")
