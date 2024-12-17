def exec(initialA, program, memo):
    if initialA in memo:
        return memo[initialA]

    regA = initialA
    regB = 0
    regC = 0
    pointer = 0
    output = []

    def findRegister(code):
        if code <= 3:
            return code
        elif code == 4:
            return regA
        elif code == 5:
            return regB
        elif code == 6:
            return regC

    seen_states = set()
    while pointer < len(program):
        state = (pointer, regA, regB, regC)
        if state in seen_states:
            break
        seen_states.add(state)

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

    memo[initialA] = output
    return output


def readAndExec(file):
    with open(file, 'r') as file:
        lines = file.read().strip().splitlines()

    program = list(map(int, lines[4].split(":")[1].strip().split(",")))

    initialA = 200000000000000
    memory = {}

    while True:
        output = exec(initialA, program, memory)
        if output == program:
            return initialA
        initialA += 1


file = '2.txt'
result = readAndExec(file)
print(result)
