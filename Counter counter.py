import time
variables = {}
variables["0"] = 0
x = 0
delayTime = None
while True:
    delayTime = input("How many seconds do you want to wait for a counter to change? ")
    try:
        delayTime = float(delayTime)
        break
    except:
        print("\033[F\033[K", end="")
while True:
    countTime = input("After how many counts should a new counter start? ")
    try:
        countTime = int(countTime)
        break
    except:
        print("\033[F\033[K", end="")
while True:
    values = [str(variables[var_name]) for var_name in variables]
    print(" ".join(values))
    variables[str(x)] += 1
    for _ in range(len(variables)):
        if variables[str(x)] == countTime:
            x += 1
            if not str(x) in variables:
                variables[str(x)] = 0
            variables[str(x)] += 1
    while not x == 0:
        x -= 1
        variables[str(x)] = 0
    time.sleep(delayTime)
    print("\033[A", end='')