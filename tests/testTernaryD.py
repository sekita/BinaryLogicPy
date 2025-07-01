from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 1
print("Negative edge trigger" if fPos == 0 else "Positive edge trigger")

# Create a flip-flop controller
FFC = FlipFlopController()

# Reset the flip-flops
resetResD = FFC.resetFF(fPos, 'DFF', 2)  # 2: number of flip-flops
clk, x0, x1 = resetResD[0], resetResD[1], resetResD[2]
print(f"Initial state -> clk={clk}, x0={x0}, x1={x1}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk    # Toggle the clock signal
        d0 = int(x1)
        d1 = int(not x0 and not x1)
            
        # Update flip-flop states
        x0 = FFC.dff(fPos, 0, clk, d0)  # DFF0
        x1 = FFC.dff(fPos, 1, clk, d1)  # DFF1
        print(f"clk={clk}, x0={x0}, x1={x1}")
