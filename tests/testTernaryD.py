from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 1
print("Negative edge trigger" if fPos == 0 else "Positive edge trigger")

# Create a flip-flop controller
FFC = FlipFlopController()

# Reset the flip-flops
resetResD = FFC.resetFF(fPos, 'DFF', 2)  # 2: number of flip-flops
clk, x1, x2 = resetResD[0], resetResD[1], resetResD[2]
print(f"Initial state -> clk={clk}, x1={x1}, x2={x2}")

# Generate 10 clock cycles and update the flip-flop states
for ir in range(10):  # Repeat for 10 clock cycles
    for ic in range(2):  # Each clock has two states (0 and 1)
        clk = 1 - clk    # Toggle the clock signal
        d1 = int(x2)
        d2 = int(not x1 and not x2)
            
        # Update flip-flop states
        x1 = FFC.dff(fPos, 0, clk, d1)  # DFF1
        x2 = FFC.dff(fPos, 1, clk, d2)  # DFF2
        print(f"clk={clk}, x1={x1}, x2={x2}")
