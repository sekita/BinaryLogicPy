# Single-Phase Synchronous Logic Circuit Simple Simulator

## 1. **Overview**

The binarylogicroutine library facilitates the simulation of single-phase synchronous logic circuits in Python.  
Designed with accessibility in mind, it allows students with visual impairments to model flip-flop-based circuits in a fully text-based environment.  
The library is self-contained and does not require any external dependencies beyond Python.  

## 2. **Usage Example**

### 2.1 Example Program

An example program simulates a ternary counter circuit using negative-edge-triggered JK flip-flops, 
where the state `(x0, x1)` transitions cyclically as `(0, 0) → (0, 1) → (1, 0)`.  
In this example, output variables are not used; instead, the program prints the clock (`clk`) and the state variables (`x0`, `x1`).  

```python
# testTernaryJK.py
from binarylogicroutine import FlipFlopController

# Initial Settings
fPos = 0  # Negative edge trigger
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
        j0 = x1          # Input value J to JKFF0
        k0 = 1           # Input value K to JKFF0
        j1 = int(not x0) # Input value J to JKFF1 (convert bool to int)
        k1 = 1           # Input value K to JKFF1

        # Update flip-flop states
        x0 = FFC.jkff(fPos, 0, clk, j0, k0)  # JKFF0
        x1 = FFC.jkff(fPos, 1, clk, j1, k1)  # JKFF1
        print(f"clk={clk}, x0={x0}, x1={x1}")
```

### 2.2 Execution Result

```
Negative edge trigger
Initial state -> clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
clk=1, x0=0, x1=1
clk=0, x0=1, x1=0
clk=1, x0=1, x1=0
clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
clk=1, x0=0, x1=1
clk=0, x0=1, x1=0
clk=1, x0=1, x1=0
clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
clk=1, x0=0, x1=1
clk=0, x0=1, x1=0
clk=1, x0=1, x1=0
clk=0, x0=0, x1=0
clk=1, x0=0, x1=0
clk=0, x0=0, x1=1
```

## 3. **Installation**

Python>=3.8  

```bash
pip install git+https://github.com/sekita/BinaryLogicPy.git
```

## 4. **Usage**

- In a Python program  
```bash
from binarylogicroutine import FlipFlopController

obj = FlipFlopController()  
obj.doSomething()
```

- Excecution Example  
```
# Ternary Counter
python testTernaryJK.py
python testTernaryD.py
python testTernarySR.py

# A simulation of a vending machine that sells 15-yen juice in a world where only 5-yen and 10-yen coins are used.
python testVM15YenJK.py
python testVM15YenD.py
python testVM15YenSR.py
```

## 5. **Detail Description of the Simulation Library**

### 5.1 Constraints

The flip-flops (FFs) are unified to be either positive-edge-triggered or negative-edge-triggered, and the following constraints are applied:  
1. Feedback loops that do not pass through flip-flops are not allowed.  
2. Delay times caused by arithmetic elements in the combinational circuits are not considered. Processing is performed in the order written in the program.  
3. Fan-in and fan-out limitations are not considered.  

### 5.2 Types and IDs of Flip-flops

The library implements four types of flip-flops, with the following function names:  
- JK flip-flop: `JKFF`
- SR (or RS) flip-flop: `SRFF` or `RSFF`
- D flip-flop: `DFF`
- T flip-flop: `TFF`

And each type of flip-flop has an FFID ranging from 0 to 99.  

### 5.3 Creating Combinational Logic Circuits

Although the library is not required for combinational logic circuits, its use may be necessary when working within sequential logic circuits.  
The usage is explained below:

Logical operators are written using Python’s logical expressions.  
Specifically, logical AND is represented by `and`, logical OR by `or`, and logical NOT by `not`.  
Logical variables appear on the left-hand side, and logical expressions on the right-hand side.  
When writing multiple statements, previously defined values should be reused.  

For example:  

- Writing as a single statement:  
  `a = b and c or d`  
- Writing as two statements:  
  ```python
  e = b and c
  a = e or d
  ```  
  However, the following is not allowed because `e` is referenced before it is defined:  
  ```python
  a = e or d
  e = b and c
  ```

If necessary, the `int()` function can be used to convert `True` and `False` to 1 and 0, respectively.  
Conversely, `1` and `0` are treated as `True` and `False` in Python.  
Furthermore, the precedence of logical operators in Python follows the standard order: not > and > or.  

### 5.4 Creating Sequential Logic Circuits

A program typically consists of two sections: an **initialization section**, 
and a **clock cycle section**, which is executed repeatedly for each simulation cycle.

#### **Initialization Section**:

In the initialization section, the FlipFlopController class should be imported,
the edge-trigger type should be set,
and the flip-flops should be initialized.

1. **Importing Class**  
   ```python
   from binarylogicroutine import FlipFlopController
   ```  

2. **Setting the Edge Trigger Type**  
   For example, if the edge-trigger type (`flagPositive`) is represented by a variable `fPos`,
   set `fPos = 1` for positive-edge triggering,
   or `fPos = 0` for negative-edge triggering.

   ```python
   fPos = 0  # 0 for negative-edge, 1 for positive-edge
   ```  

3. **Initializing flip-flops**  
   For example, if you create an object `FFC` from the `FlipFlopController` class,
   you can use its reset function for the flip-flop outputs: `FFC.resetFF()`.
   The `resetFF()` function is used with the following arguments: the edge trigger type (flagPositive),
   as shown above; the flip-flop type (ffType), which is one of the types listed in section 5.2;
   and the number of flip-flops (numFF).

   ```python
   FFC = FlipFlopController()
   FFC.resetFF(fPos, ffType, numFF)
   ```  

   The return values are the clock value immediately after the edge trigger (1 for positive-edge triggering, 0 for negative-edge triggering) 
   and the output values of the flip-flops (initially set to 0).

#### Clock Cycle Section:

1. **Setting External Inputs and Logical Expressions**  
   If necessary, provide external inputs, 
   and set all input variables of the flip-flops to the appropriate logic expressions derived from the combinational circuits.

2. **Caling flip-flop functions**  

   Flip-flop functions are called.  
   Inputs to a function are: a flagPositive, the FFID, the clock signal, and the input(s) to the flip-flop.  
   Output of a function is the Q output to the flip-flop.  

   For example, suppose there are two JK flip-flops (JKFFs) with flip-flop IDs (FFIDs) 0 and 1, both synchronized to the clock (clk) trigger.  
   When the type of flip-flop is JKFF, each flip-flop has an ID of 0 or 1, and the inputs for flip-flop n are labeled Jn and Kn (where n = 0 or 1).  

   ```python
   newQ1 = FFC.jkff(fPos, 0, clk, J1, K1)
   newQ2 = FFC.jkff(fPos, 1, clk, J2, K2)
   ```

   If the type of flip-flop is a DFF: 
   ```python
   newQ1 = FFC.dff(fPos, 0, clk, D1)
   newQ2 = FFC.dff(fPos, 1, clk, D2)
   ```

   If the type of flip-flop is a RSFF: 
   ```python
   newQ1 = FFC.rsff(fPos, 0, clk, R1, S1)
   newQ2 = FFC.rsff(fPos, 1, clk, R2, S2)
   ```

   If the type of flip-flop is a SRFF: 
   ```python
   newQ1 = FFC.srff(fPos, 0, clk, S1, R1)
   newQ2 = FFC.srff(fPos, 1, clk, S2, R2)
   ```

   If the type of flip-flop is a TFF: 
   ```python
   newQ1 = FFC.tff(fPos, 0, clk, T1)
   newQ2 = FFC.tff(fPos, 1, clk, T2)
   ```

3. **Setting Output Variables**  
   If necessary, set the values of output variables to the appropriate logic expressions derived from the combinational circuits.  

## 6. **License**

This project is licensed under the MIT License. See the LICENSE file for details.

## 7. **Contact**
SEKITA, Iwao  
sekita@cs.k.tsukuba-tech.ac.jp
