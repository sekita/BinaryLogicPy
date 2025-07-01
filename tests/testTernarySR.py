from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 1
print("Negative edge trigger" if fPos == 0 else "Positive edge trigger")

# Create a flip-flop controller
FFC = FlipFlopController()

# Reset the flip-flops
resetResSR = FFC.resetFF(fPos, 'SRFF', 2)  # 2: number of flip-flops
clk, x0, x1 = resetResSR[0], resetResSR[1], resetResSR[2]
print(f"Initial state -> clk={clk}, x0={x0}, x1={x1}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk    # Toggle the clock signal
        s0 = int(x1 and not x0)
        r0 = int(not s0)
        s1 = int(not x0 and not x1)
        r1 = int(not s1)

        # Update flip-flop states
        x0 = FFC.srff(fPos, 0, clk, s0, r0)  # SRFF0
        x1 = FFC.srff(fPos, 1, clk, s1, r1)  # SRFF1
        print(f"clk={clk}, x0={x0}, x1={x1}")
