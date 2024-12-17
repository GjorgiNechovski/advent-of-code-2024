def exec(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()

    regA = int(lines[0].split(":")[1].strip())
    regB = int(lines[1].split(":")[1].strip())
    regC = int(lines[2].split(":")[1].strip())

    program = list(map(int, lines[4].split(":")[1].strip().split(",")))

    def findRegister(code):
        if code <= 3:
            return code
        elif code == 4:
            return regA
        elif code == 5:
            return regB
        elif code == 6:
            return regC

    pointer = 0
    output = []

    while pointer < len(program):
        code = program[pointer]
        operand = program[pointer + 1] if pointer + 1 < len(program) else None

        if code == 0:  # adv
            regA //= 2 ** findRegister(operand)

        elif code == 1:  # bxl
            regB ^= operand

        elif code == 2:  # bst
            regB = findRegister(operand) % 8

        elif code == 3:  # jnz
            if regA != 0:
                pointer = operand
                continue

        elif code == 4:  # bxc
            regB ^= regC

        elif code == 5:  # out
            output.append(findRegister(operand) % 8)

        elif code == 6:  # bdv
            regB = regA // (2 ** findRegister(operand))

        elif code == 7:  # cdv
            regC = regA // (2 ** findRegister(operand))

        pointer += 2

    return ",".join(map(str, output))


file = '1.txt'
result = exec(file)
print(result)
