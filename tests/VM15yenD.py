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
resetResD = FFC.resetFF(fPos, 'DFF', 2)
clk, xD, yD = resetResD[0], resetResD[1], resetResD[2]
print(f"Initial state DFF -> clk={clk}, x={xD}, y={yD}")

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

        D0 = int(not xD and not yD and ii or yD and jj or xD and not ii and not jj)
        D1 = int(not xD and not yD and jj or yD and not ii and not jj)
        print(f'D0 = {D0}, D1 = {D1}', end=', ')
        # Update flip-flop states
        xD = FFC.dff(fPos, 0, clk, D0)  # DFF0
        yD = FFC.dff(fPos, 1, clk, D1)  # DFF1

        print(f'xD  = {xD}, yD  = {yD}')
        JuiceD = yD and ii or xD and jj or xD and ii
        FiveYenD = xD and not yD and ii and not jj
        JuiceD = int(JuiceD and (clk ^ fPos))  # ^ is bitwise XOR, but for variables that take 0 or 1, it has the same meaning as logical XOR between variables.
        FiveYenD = int(FiveYenD and (clk ^ fPos))
        print(f'JuiceD  = {JuiceD}, FiveYenD  = {FiveYenD}')

