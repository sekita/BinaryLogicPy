from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 0
print("Negative edge trigger" if fPos == 0 else "Positive edge trigger")

# Create a flip-flop controller
FFC = FlipFlopController()

# Reset the flip-flops
resetResJK = FFC.resetFF(fPos, 'JKFF', 2)  # 2: number of flip-flops
clk, x1, x2 = resetResJK[0], resetResJK[1], resetResJK[2]
print(f"Initial state -> clk={clk}, x1={x1}, x2={x2}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk    # Toggle the clock signal
        j1 = x2          # Input value J for JKFF1
        k1 = 1           # Input value K for JKFF1
        j2 = int(not x1) # Input value J for JKFF2 (convert bool to int)
        k2 = 1           # Input value K for JKFF2

        # Update flip-flop states
        x1 = FFC.jkff(fPos, 0, clk, j1, k1)  # JKFF1
        x2 = FFC.jkff(fPos, 1, clk, j2, k2)  # JKFF2
        print(f"clk={clk}, x1={x1}, x2={x2}")
