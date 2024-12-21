from binarylogicroutine import resetFF, FF2, JKFF

# Initial Settings
fPos = 0  # Negative edge trigger
# Reset the flip-flops
clk, x, y = resetFF(fPos, JKFF, 2)  # clk: clock, JKFF: flip-flop type, 2: number of flip-flops
print(f"Initial state -> clk={clk}, x={x}, y={y}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk  # Toggle the clock signal
        j1 = y          # Input value J for JKFF1
        k1 = 1          # Input value K for JKFF1
        j2 = not x      # Input value J for JKFF2
        k2 = 1          # Input value K for JKFF2

        # Update flip-flop states
        x, y = FF2(fPos, clk, JKFF, j1, k1, JKFF, j2, k2)
        print(f"clk={clk}, x={x}, y={y}")
