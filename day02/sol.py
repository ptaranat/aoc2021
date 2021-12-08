def solution1(input_file: str):
    with open(input_file, "r") as f:
        pos, depth = 0, 0
        for line in f:
            cmd = line.split()
            direction = cmd[0]
            value = int(cmd[1])
            if direction == "forward":
                pos += value
            else:
                if direction == "down":
                    depth += value
                else:
                    depth -= value

        print(f"day 02 q1: {pos*depth}")


def solution2(input_file: str):
    with open(input_file, "r") as f:
        pos, depth, aim = 0, 0, 0
        for line in f:
            cmd = line.split()
            direction = cmd[0]
            value = int(cmd[1])
            if direction == "forward":
                pos += value
                depth += aim * value
            else:
                if direction == "down":
                    aim += value
                else:
                    aim -= value

        print(f"day 02 q2: {pos*depth}")


try:
    solution1("input.txt")
    solution2("input.txt")
except FileNotFoundError:
    print("No input file!")
