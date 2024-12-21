# Single-Phase Synchronous Logic Circuit Simple Simulator

## 1. **Overview**

By using the methods provided in the `binarylogicroutine` library, single-phase synchronous logic circuit simulations can be easily performed with Python.

This library is designed to enable students with visual impairments to conveniently simulate single-phase synchronous logic circuits using flip-flops in a text-based environment.

The `binarylogicroutine` library allows users to perform single-phase synchronous logic circuit simulations with ease, requiring no additional libraries beyond downloading this package and using Python.

## 2. **Usage Example**

### 2.1 Example Program

An example program simulates a ternary counter circuit using negative edge triggered JK flip-flops, where the state `(x, y)` transitions cyclically as `(0, 0) → (0, 1) → (1, 0)`.  
In this example, output variables are not used; the program prints the clock (`clk`) and state variables (`x`, `y`).

```python
# demoprogram.py
from binarylogicroutine import resetFF, FF2, JKFF

# Initialization Section:
## Initial Settings
fPos = 0  # Negative edge trigger
## Reset the flip-flops
clk, x, y = resetFF(fPos, JKFF, 2)  # JKFF: flip-flop type, 2: number of flip-flops
    # clk: clock, 
    # x and y: the outputs of JKFF1 and JKFF2, respectively.
print(f"Initial state -> clk={clk}, x={x}, y={y}")

# Clock Cycle Setting Section:
## Generate 10 clock cycles and update the flip-flop states
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
```

### 2.2 Execution Result
```
Initial state -> clk=0, x=0, y=0
clk=1, x=0, y=0
clk=0, x=0, y=1
clk=1, x=0, y=1
clk=0, x=1, y=0
clk=1, x=1, y=0
clk=0, x=0, y=0
clk=1, x=0, y=0
clk=0, x=0, y=1
clk=1, x=0, y=1
clk=0, x=1, y=0
clk=1, x=1, y=0
clk=0, x=0, y=0
clk=1, x=0, y=0
clk=0, x=0, y=1
clk=1, x=0, y=1
clk=0, x=1, y=0
clk=1, x=1, y=0
clk=0, x=0, y=0
clk=1, x=0, y=0
clk=0, x=0, y=1
```

## 3. **Installation**

Python>=3.8 

Download `binarylogicroutine.py`.

## 4. **Usage**

Create a program for simulations.  
For example, create the demoprogram for section 3.1.

Run the following command to start the program (demoProgram.py):

```
python demoProgram.py
```

## 5. **Detail Description of the Simulation Library**

### 5.1 Constraints

The flip-flops(FFs) are unified as either positive-edge triggered or negative-edge triggered, and the following constraints are applied:  

    1. Feedback loops that do not pass through FFs do not exist.
    2. The delay time caused by various arithmetic elements in combinational circuits is not considered. (Processing is executed in the order described in the program)
    3. The number of fan-ins and fan-outs is not considered.  

Users must not use global variables defined in the library within their programs.
These global variables are used to retain the value of the clock just before it was called and the output of the FF, as follows:  
For Clock value storage:   
`__clkJKFFnp__`, `__clkSRFFnp__`, `__clkRSFFnp__`, `__clkDFFnp__`, `__clkTFFnp__`  
For FF output storage:  
`__QJKFFnp__`, `__QSRFFnp__`, `__QRSFFnp__`, `__QDFFnp__`, `__QTFFnp__`

### 5.2 Types of Flip-flops

The library implements four types of FFs, with the following function names:
- JK flip-flop: `JKFF`
- SR or RS flip-flop: `SRFF` or `RSFF`
- D flip-flop: `DFF`
- T flip-flop: `TFF`

### 5.3 Creating Combinational Logic Circuits

Although the library is not required for combinational logic circuits, its usage is sometimes necessary when used within sequential logic circuits.
The usage is explained below:

Logical operators are written using Python's logical expressions.
Specifically, logical AND is represented by `and`, logical OR by `or`, and logical NOT by `not`.
Logical variables are written on the left side, and logical expressions on the right side.
When writing multiple statements, already defined values should be used.  
For example:  

- Writing in one statement:  
  `a = b and c or d`  
- Writing in two statements:  
  ```python
  e = b and c
  a = e or d
  ```  
  However, the following is not allowed because `e` has not yet been defined at the time it is referenced:  
  ```python
  a = e or d
  e = b and c
  ```

If necessary, the `int()` function can be used to convert `TRUE` and `FALSE` to `1` and `0`, respectively.
Conversely, `1` and `0` are treated as `TRUE` and `FALSE` in Python.
Furthermore, the priority of operators in Python is the same as in general logical expressions: `not > and > or`.

### 5.4 Creating Sequential Logic Circuits

The program can consist of two parts: the "**initialization section**" and the "**clock cycle setting section**" which is repeated for the number of simulation clock cycles.

#### **Initialization Section**:
In the initialization section, functions to be used are imported, edge-trigger type is set, and FFs are initialized.

1. **Importing Functions**  
   For example, if two FFs synchronized with clock triggers are used, both of which are JKFFs, the following code is used:  
   ```python
   from binarylogicroutine import resetFF, FF2, JKFF
   ```  
   Similarly, if three FFs are used, all of which are DFFs:  
   ```python
   from binarylogicroutine import resetFF, FF3, DFF
   ```  
   A combination of multiple types of FFs can also be used.

2. **Setting the Edge Trigger Type**  
   For example, if the edge-trigger type is represented by the variable `fPos`, set `fPos=1` for positive-edge triggering or `fPos=0` for negative-edge triggering.

3. **Initializing FFs**  
   A reset function for the FF outputs, `ResetFF()`, can be used.  
   The `resetFF()` function is used with the arguments: edge trigger type (`flagPositive`), FF name (`ffName`), and the number of FFs (`numFF`).  
   ```python
   resetFF(flagPositive, ffName, numFF)
   ```  
   The return values are the clock value immediately after the edge trigger (1 for positive-edge triggering, 0 for negative-edge triggering) and the output values of the FFs (initially set to 0).

#### Clock Cycle Setting Section:
1. **Setting External Inputs and Logical Expressions**  
   If necessary, provide external inputs and write logical expressions for the input variables of FFs.

2. **Describing Functions According to the Number of FFs**  

   Functions named from `FF1()` to `FF16()` are provided, corresponding to the number of FFs operating in synchronization with the clock trigger.

   For example, if there are two flip-flops (FFs) synchronized with the clock trigger, the `FF2()` function is used.  

   When the type of FF is a JKFF, the function can be written as follows:  
   ```python
   newQ1, newQ2 = FF2(fPos, clk, JKFF, J1, K1, JKFF, J2, K2)
   ```
   Here:  
   - `fPos` specifies whether it is a positive-edge-triggered FF (flag).  
   - `clk` provides the clock value (0 or 1).  
   - `J1` and `K1` are the inputs for the first specified FF (JKFF).  
   - `J2` and `K2` are the inputs for the second specified FF (JKFF).  

   If the type of FF is a DFF, which has only one input, the second input can be omitted as follows:  
   ```python
   newQ1, newQ2 = FF2(fPos, clk, f1=DFF, f1i1=D1, f2=DFF, f2i1=D2)
   ```

   The order of inputs (fni1 and fni2) depends on the type of nth FF. For example:  
   - For JKFF, the first input is `J` and the second is `K`.  
   - For SRFF, the inputs are `S` and `R`.  
   - For RSFF, the inputs are `R` and `S`.  
   - For DFF and TFF, there is only one input, which is `D` and `T`, respectively.  

   The return values of the `FFn()` function are the output values of the flip-flops in order, from the first FF to the nth FF.

3. **Setting Output Variables**  
   If necessary, set the values of output variables using logical expressions of combinational circuits.  

## 6. **License**

This project is licensed under the MIT License. See the LICENSE file for details.

## 7. **Contact**
SEKITA, Iwao  
sekita@cs.k.tsukuba-tech.ac.jp
