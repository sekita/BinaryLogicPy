# A simulation of a vending machine that sells 15-yen juice 
# in a world where only 5-yen and 10-yen coins are used.

from binarylogicroutine import FlipFlopController

fPos = int(input('What type of edge trigger? 1: Positive-edge triggered, 0: Negative-edge triggered '))
print('Positive-edge triggered flip-flop') if fPos == 1 else print('Negative-edge triggered flip-flop')

# Create a flip-flop controller
FFC = FlipFlopController()

# Original main program implementation
print("=== Original Main Program ===")

print("Initializing the flip-flop")

# Reset the flip-flops
resetResSR = FFC.resetFF(fPos, 'SRFF', 2)
clk, xSR, ySR = resetResSR[0], resetResSR[1], resetResSR[2]
print(f"Initial state SRFF -> clk={clk}, x={xSR}, y={ySR}")    

while True:  # Infinite loop
    # Input
    inputData = input("Enter I and J separated by a space. '0 0' means 0 yen, '0 1' means 5 yen, '1 0' means 10 yen: ")
    iStr, jStr = inputData.split()
    ii = int(iStr)
    jj = int(jStr)

    # Execute one clock cycle
    for iclk in range(2):
        clk = 1 - clk  #Clock changes
        print(f'clk = {clk}', end=', ')

        S0 = int((ii and not ySR or jj and ySR) and not xSR)
        R0 = int((ii or jj) and xSR)
        S1 = int((not xSR and jj) and not ySR)
        R1 = int((ii or jj) and ySR)
        print(f'S0 = {S0}, R0 = {R0}, S1 = {S1}, R1 = {R1}', end=', ')
        xSR = FFC.srff(fPos, 0, clk, S0, R0)  # SRFF0
        ySR = FFC.srff(fPos, 1, clk, S1, R1)  # SRFF1

        print(f'xSR = {xSR}, ySR = {ySR}')
        JuiceSR = ySR and ii or xSR and jj or xSR and ii
        FiveYenSR = xSR and not ySR and ii and not jj
        JuiceSR = int(JuiceSR and (clk ^ fPos))  # ^ is bitwise XOR, but for variables that take 0 or 1, it has the same meaning as logical XOR between variables.
        FiveYenSR = int(FiveYenSR and (clk ^ fPos))
        print(f'JuiceSR = {JuiceSR}, FiveYenSR = {FiveYenSR}')
