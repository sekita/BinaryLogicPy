from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 1
print("Negative edge trigger" if fPos == 0 else "Positive edge trigger")

# Create a flip-flop controller
FFC = FlipFlopController()

# Reset the flip-flops
resetResSR = FFC.resetFF(fPos, 'SRFF', 2)  # 2: number of flip-flops
clk, x1, x2 = resetResSR[0], resetResSR[1], resetResSR[2]
print(f"Initial state -> clk={clk}, x1={x1}, x2={x2}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk    # Toggle the clock signal
        s1 = int(x2 and not x1)
        r1 = int(not s1)
        s2 = int(not x1 and not x2)
        r2 = int(not s2)

        # Update flip-flop states
        x1 = FFC.srff(fPos, 0, clk, s1, r1)  # SRFF2
        x2 = FFC.srff(fPos, 1, clk, s2, r2)  # SRFF1
        print(f"clk={clk}, x1={x1}, x2={x2}")
