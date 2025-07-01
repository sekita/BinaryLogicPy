from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 0
print("Negative edge trigger" if fPos == 0 else "Positive edge trigger")

# Create a flip-flop controller
FFC = FlipFlopController()

# Reset the flip-flops
resetResJK = FFC.resetFF(fPos, 'JKFF', 2)  # 2: number of flip-flops
clk, x0, x1 = resetResJK[0], resetResJK[1], resetResJK[2]
print(f"Initial state -> clk={clk}, x0={x0}, x1={x1}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk    # Toggle the clock signal
        j0 = x1          # Input value J for JKFF0
        k0 = 1           # Input value K for JKFF0
        j1 = int(not x0) # Input value J for JKFF1 (convert bool to int)
        k1 = 1           # Input value K for JKFF1

        # Update flip-flop states
        x0 = FFC.jkff(fPos, 0, clk, j0, k0)  # JKFF0
        x1 = FFC.jkff(fPos, 1, clk, j1, k1)  # JKFF1
        print(f"clk={clk}, x0={x0}, x1={x1}")
