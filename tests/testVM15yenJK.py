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
resetResJK = FFC.resetFF(fPos, 'JKFF', 2)
clk, xJK, yJK = resetResJK[0], resetResJK[1], resetResJK[2]
print(f"Initial state JKFF -> clk={clk}, x={xJK}, y={yJK}")

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

        J0 = int(ii and not yJK or jj and yJK)
        K0 = int(ii or jj)
        J1 = int(not xJK and jj)
        K1 = int(ii or jj)
        print(f'J0 = {J0}, K0 = {K0}, J1 = {J1}, K1 = {K1}', end=', ')
        xJK = FFC.jkff(fPos, 0, clk, J0, K0)  # JKFF0
        yJK = FFC.jkff(fPos, 1, clk, J1, K1)  # JKFF1
        print(f'xJK = {xJK}, yJK = {yJK}')

        JuiceJK = yJK and ii or xJK and jj or xJK and ii
        FiveYenJK = xJK and not yJK and ii and not jj
        JuiceJK = int(JuiceJK and (clk ^ fPos))  # ^ is bitwise XOR, but for variables that take 0 or 1, it has the same meaning as logical XOR between variables.
        FiveYenJK = int(FiveYenJK and (clk ^ fPos))
        print(f'JuiceJK = {JuiceJK}, FiveYenJK = {FiveYenJK}')
