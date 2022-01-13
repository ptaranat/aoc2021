def solution1(input_file: str):
    with open(input_file, "r") as f:
        X = []
        for line in f:
            X.append(list(line.strip()))
        X = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
        gamma = ""
        epsilon = ""
        for line in X:
            ones = 0
            zeroes = 0
            for bit in line:
                if bit == "1":
                    ones += 1
                elif bit == "0":
                    zeroes += 1
            if ones > zeroes:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"

        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
        print(f"ans: {gamma * epsilon}")


try:
    solution1("input.txt")
except FileNotFoundError:
    print("No input file!")
