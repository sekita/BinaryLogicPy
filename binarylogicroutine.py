#coding: utf-8
# Last updated on 2024.05.14
__maxFF__= 100
__clkJKFFnp__ = [[1]*__maxFF__, [0]*__maxFF__]
__clkRSFFnp__ = [[1]*__maxFF__, [0]*__maxFF__]
__clkSRFFnp__ = [[1]*__maxFF__, [0]*__maxFF__]
__clkDFFnp__ = [[1]*__maxFF__, [0]*__maxFF__]
__clkTFFnp__ = [[1]*__maxFF__, [0]*__maxFF__]
__QJKFFnp__ = [[0]*__maxFF__ for i in range(2)]
__QRSFFnp__ = [[0]*__maxFF__ for i in range(2)]
__QSRFFnp__ = [[0]*__maxFF__ for i in range(2)]
__QDFFnp__ = [[0]*__maxFF__ for i in range(2)]
__QTFFnp__ = [[0]*__maxFF__ for i in range(2)]

def JKFF(ipos, iKnd, iP2, iJ, iK):
    """
    int JKFF(int ipos, int iKnd, int iP2, int iJ, int iK)
    Simulates a JK flip-flop (FF) operation.
    
    Parameters:
        ipos (int): Edge type (1 for positive edge, 0 for negative edge).
        iKnd (int): Type of FF (range: 0 to __maxFF__).
        iP2 (int): New clock state to transition to.
        iJ (int): J input signal.
        iK (int): K input signal.
    
    Returns:
        int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
    
    Notes:
        - The clock state transitions from __clkJKFFnp__[ipos][iKnd] to iP2.
        - The value of __clkJKFFnp__[ipos][iKnd] will be updated accordingly.
    """

    if iKnd >= __maxFF__ :
        print("*** ERR: kind of JK-FF(%d) must be >=0 and <%d. ***" % (iKnd, __maxFF__))
        return -1
    if((ipos == 0 and __clkJKFFnp__[ipos][iKnd] == 1 and iP2 == 0)
       or (ipos == 1 and __clkJKFFnp__[ipos][iKnd] == 0 and iP2 == 1)) :
        if iJ==1 and iK==0:
            __QJKFFnp__[ipos][iKnd] = 1
        if iJ==0 and iK==1:
             __QJKFFnp__[ipos][iKnd] = 0
        if iJ==1 and iK==1:
             __QJKFFnp__[ipos][iKnd] = int(not  __QJKFFnp__[ipos][iKnd])
    __clkJKFFnp__[ipos][iKnd] = iP2
    return  __QJKFFnp__[ipos][iKnd]


def SRFF(ipos, iKnd, iP2, iS, iR):
    """
    int SRFF(int ipos, int iKnd, int iP2, int iS, int iR)
    Simulates an SR flip-flop (FF) operation.
    
    Parameters:
        ipos (int): Edge type (1 for positive edge, 0 for negative edge).
        iKnd (int): Type of FF (range: 0 to __maxFF__).
        iP2 (int): New clock state to transition to.
        iS (int): S input signal (Set).
        iR (int): R input signal (Reset).
    
    Returns:
        int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
    
    Notes:
        - The clock state transitions from __clkSRFFnp__[ipos][iKnd] to iP2.
        - The value of __clkSRFFnp__[ipos][iKnd] will be updated accordingly.
    """
 
    if iKnd >= __maxFF__ :
        print("*** ERR: kind of SR-FF(%d) must be >=0 and <%d. ***" % (iKnd, __maxFF__))
        return -1
    if((ipos == 0 and __clkSRFFnp__[ipos][iKnd] == 1 and iP2 == 0) 
       or (ipos == 1 and __clkSRFFnp__[ipos][iKnd] == 0 and iP2 == 1)) :
        if iR==1 and iS==0:
            __QSRFFnp__[ipos][iKnd] = 0
        if iR==0 and iS==1:
            __QSRFFnp__[ipos][iKnd] = 1
        if iR==1 and iS==1:
            print(f"*** ERR: S={iS} and R={iR} is not permitted. ***")
            return -1
    __clkSRFFnp__[ipos][iKnd] = iP2
    return __QSRFFnp__[ipos][iKnd]


def RSFF(ipos, iKnd, iP2, iR, iS):
    """
    int RSFF(int ipos, int iKnd, int iP2, int iR, int iS)
    Simulates an RS flip-flop (FF) operation.
    
    Parameters:
        ipos (int): Edge type (1 for positive edge, 0 for negative edge).
        iKnd (int): Type of FF (range: 0 to __maxFF__).
        iP2 (int): New clock state to transition to.
        iR (int): R input signal (Reset).
        iS (int): S input signal (Set).
    
    Returns:
        int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
    
    Notes:
        - The clock state transitions from __clkRSFFnp__[ipos][iKnd] to iP2.
        - The value of __clkRSFFnp__[ipos][iKnd] will be updated accordingly.
    """

    if iKnd >= __maxFF__ :
        print("*** ERR: kind of RS-FF(%d) must be >=0 and <%d. ***" % (iKnd, __maxFF__))
        return -1
    if((ipos == 0 and __clkRSFFnp__[ipos][iKnd] == 1 and iP2 == 0) 
       or (ipos == 1 and __clkRSFFnp__[ipos][iKnd] == 0 and iP2 == 1)) :
        if iR==1 and iS==0:
            __QRSFFnp__[ipos][iKnd] = 0
        if iR==0 and iS==1:
            __QRSFFnp__[ipos][iKnd] = 1
        if iR==1 and iS==1:
            print(f"*** ERR: R={iR} and S={iS} is not permitted. ***")
            return -1
    __clkRSFFnp__[ipos][iKnd] = iP2
    return __QRSFFnp__[ipos][iKnd]


def DFF(ipos, iKnd, iP2, iD, iDummy=0):
    """
    int DFF(int ipos, int iKnd, int iP2, int iD, int iDummy=0)
    Simulates a D flip-flop (FF) operation.
    
    Parameters:
        ipos (int): Edge type (1 for positive edge, 0 for negative edge).
        iKnd (int): Type of D-FF (range: 0 to __maxFF__).
        iP2 (int): New clock state to transition to.
        iD (int): D input signal (Data).
        iDummy (int, optional): Placeholder parameter; default is 0.
    
    Returns:
        int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
    
    Notes:
        - The clock state transitions from __clkDFFnp__[ipos][iKnd] to iP2.
        - The value of __clkDFFnp__[ipos][iKnd] will be updated accordingly.
        - `iDummy` is not used in the current implementation but is included for compatibility.
    """

    if iKnd >= __maxFF__:
        print("*** ERR: kind of D-FF(%d) must be >=0 and <%d. ***" % (iKnd, __maxFF__))
        return -1
    if((ipos == 0 and __clkDFFnp__[ipos][iKnd] == 1 and iP2 == 0)
       or (ipos == 1 and __clkDFFnp__[ipos][iKnd] == 0 and iP2 == 1)) :
        __QDFFnp__[ipos][iKnd] = int(iD)
    __clkDFFnp__[ipos][iKnd] = iP2
    #print("__clkDFFnp__=\n",__clkDFFnp__)
    #print("__QDFFnp__=\n",__QDFFnp__)
    return __QDFFnp__[ipos][iKnd]


def TFF(ipos, iKnd, iP2, iT, iDummy=0):
    """
    int TFF(int ipos, int iKnd, int iP2, int iT, int iDummy=0)
    Simulates a T flip-flop (FF) operation.

    Parameters:
        ipos (int): Edge type (1 for positive edge, 0 for negative edge).
        iKnd (int): Type of T-FF (range: 0 to __maxFF__).
        iP2 (int): New clock state to transition to.
        iT (int): T input signal (Toggle).
        iDummy (int, optional): Placeholder parameter; default is 0.

    Returns:
        int: The new Q (output) state of the flip-flop, or -1 if an error occurs.

    Notes:
        - The clock state transitions from __clkTFFnp__[ipos][iKnd] to iP2.
        - The value of __clkTFFnp__[ipos][iKnd] will be updated accordingly.
        - `iT` determines whether the flip-flop toggles or maintains its state.
        - `iDummy` is not used in the current implementation but is included for compatibility.
    """

    if iKnd >= __maxFF__ :
        print("*** ERR: kind of T-FF(%d) must be >=0 and <%d. ***" % (iKnd, __maxFF__))
        return -1
    if((ipos == 0 and __clkTFFnp__[ipos][iKnd] == 1 and iP2 == 0)
       or (ipos == 1 and __clkTFFnp__[ipos][iKnd] == 0 and iP2 == 1)):
        if iT==1:
            __QTFFnp__[ipos][iKnd] = int(not __QTFFnp__[ipos][iKnd])
    __clkTFFnp__[ipos][iKnd] = iP2
    return __QTFFnp__[ipos][iKnd]

def FF16(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0, f10=DFF, f10i1=0, f10i2=0, f11=DFF, f11i1=0, f11i2=0, f12=DFF, f12i1=0, f12i2=0, f13=DFF, f13i1=0, f13i2=0, f14=DFF, f14i1=0, f14i2=0, f15=DFF, f15i1=0, f15i2=0, f16=DFF, f16i1=0, f16i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2), f10(flagPositive, 9, clock, f10i1, f10i2), f11(flagPositive, 10, clock, f11i1, f11i2), f12(flagPositive, 11, clock, f12i1, f12i2), f13(flagPositive, 12, clock, f13i1, f13i2), f14(flagPositive, 13, clock, f14i1, f14i2), f15(flagPositive, 14, clock, f15i1, f15i2), f16(flagPositive, 15, clock, f16i1, f16i2)

def FF15(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0, f10=DFF, f10i1=0, f10i2=0, f11=DFF, f11i1=0, f11i2=0, f12=DFF, f12i1=0, f12i2=0, f13=DFF, f13i1=0, f13i2=0, f14=DFF, f14i1=0, f14i2=0, f15=DFF, f15i1=0, f15i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2), f10(flagPositive, 9, clock, f10i1, f10i2), f11(flagPositive, 10, clock, f11i1, f11i2), f12(flagPositive, 11, clock, f12i1, f12i2), f13(flagPositive, 12, clock, f13i1, f13i2), f14(flagPositive, 13, clock, f14i1, f14i2), f15(flagPositive, 14, clock, f15i1, f15i2)

def FF14(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0, f10=DFF, f10i1=0, f10i2=0, f11=DFF, f11i1=0, f11i2=0, f12=DFF, f12i1=0, f12i2=0, f13=DFF, f13i1=0, f13i2=0, f14=DFF, f14i1=0, f14i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2), f10(flagPositive, 9, clock, f10i1, f10i2), f11(flagPositive, 10, clock, f11i1, f11i2), f12(flagPositive, 11, clock, f12i1, f12i2), f13(flagPositive, 12, clock, f13i1, f13i2), f14(flagPositive, 13, clock, f14i1, f14i2)

def FF13(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0, f10=DFF, f10i1=0, f10i2=0, f11=DFF, f11i1=0, f11i2=0, f12=DFF, f12i1=0, f12i2=0, f13=DFF, f13i1=0, f13i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2), f10(flagPositive, 9, clock, f10i1, f10i2), f11(flagPositive, 10, clock, f11i1, f11i2), f12(flagPositive, 11, clock, f12i1, f12i2), f13(flagPositive, 12, clock, f13i1, f13i2)

def FF12(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0, f10=DFF, f10i1=0, f10i2=0, f11=DFF, f11i1=0, f11i2=0, f12=DFF, f12i1=0, f12i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2), f10(flagPositive, 9, clock, f10i1, f10i2), f11(flagPositive, 10, clock, f11i1, f11i2), f12(flagPositive, 11, clock, f12i1, f12i2)

def FF11(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0, f10=DFF, f10i1=0, f10i2=0, f11=DFF, f11i1=0, f11i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2), f10(flagPositive, 9, clock, f10i1, f10i2), f11(flagPositive, 10, clock, f11i1, f11i2)

def FF10(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0, f10=DFF, f10i1=0, f10i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2), f10(flagPositive, 9, clock, f10i1, f10i2)

def FF9(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0, f9=DFF, f9i1=0, f9i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2), f9(flagPositive, 8, clock, f9i1, f9i2)

def FF8(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0, f8=DFF, f8i1=0, f8i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2), f8(flagPositive, 7, clock, f8i1, f8i2)

def FF7(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0, f7=DFF, f7i1=0, f7i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2), f7(flagPositive, 6, clock, f7i1, f7i2)

def FF6(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0, f6=DFF, f6i1=0, f6i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2), f6(flagPositive, 5, clock, f6i1, f6i2)

def FF5(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0, f5=DFF, f5i1=0, f5i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2), f5(flagPositive, 4, clock, f5i1, f5i2)

def FF4(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0, f4=DFF, f4i1=0, f4i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2), f4(flagPositive, 3, clock, f4i1, f4i2)

def FF3(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0, f3=DFF, f3i1=0, f3i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2), f3(flagPositive, 2, clock, f3i1, f3i2)

def FF2(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0, f2=DFF, f2i1=0, f2i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2), f2(flagPositive, 1, clock, f2i1, f2i2)

def FF1(flagPositive, clock, f1=DFF, f1i1=0, f1i2=0):
    return f1(flagPositive, 0, clock, f1i1, f1i2)

def Separator(inum, nth):
    """
    int Separator(unsigned long int inum, int nth)
    Returns the value of the nth bit of the input number `inum`, using little-endian order.
    
    Parameters:
        inum (unsigned long int): Input number (unsigned integer).
        nth (int): Bit position to extract (0, 1, ...), counted from right to left.

    Returns:
        int: The value of the specified bit (0 or 1).
    
    Notes:
        - The bit order follows little-endian convention, with bit 0 being the least significant bit (LSB).
    """

    ione = 1
    inum = inum >> nth
    #  ival = (inum & ione ? 1 : 0);
    ival = inum & ione
    return ival

def resetFF(flagPositive, ffName, numFF):
    """
    resetFF(int flagPositive, function ffName, int numFF)
    Resets a specified number of flip-flops (FFs) to their initial state.

    Parameters:
        flagPositive (int): Specifies the clock edge type. Use 1 for a positive edge and 0 for a negative edge.
        ffName (function): A function object representing the flip-flop type. 
                           Acceptable values include: JKFF, RSFF, SRFF, DFF, or TFF.
                           Note: Do not enclose the function name in quotation marks.
        numFF (int): The number of flip-flops to reset.

    Returns:
        tuple:
            - int: The clock value when the edge is triggered.
            - list of int: A tuple containing `numFF` zeros, representing the Q (output) states of the flip-flops.
    Notes:
        - The `flagPositive` parameter determines whether the clock operates on a positive or negative edge.
        - The `ffName` parameter must be passed as a valid function object (e.g., JKFF, not "JKFF").
        - This function resets all specified flip-flops (`numFF`) to their initial state of zero.
    """

    clk = flagPositive
    if ffName.__name__ == 'RSFF':
        i1 = 1
    else:
        i1 = 0
    if ffName.__name__ =='TFF':
        for ii in range(2):
            for jj in range(__maxFF__):
                __QTFFnp__[ii][jj] = 0
    if numFF == 1:
        x1 = FF1(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1)
        x1 = FF1(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1)
        return clk, x1
    elif numFF == 2:
        x1, x2 = FF2(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1)
        x1, x2 = FF2(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1)
        return clk, x1, x2
    elif numFF == 3:
        x1, x2, x3 = FF3(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1)
        x1, x2, x3 = FF3(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1)
        return clk, x1, x2, x3
    elif numFF == 4:
        x1, x2, x3, x4 = FF4(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1)
        x1, x2, x3, x4 = FF4(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1)
        return clk, x1, x2, x3, x4
    elif numFF == 5:
        x1, x2, x3, x4, x5 = FF5(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1)
        x1, x2, x3, x4, x5 = FF5(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1)
        return clk, x1, x2, x3, x4, x5
    elif numFF == 6:
        x1, x2, x3, x4, x5, x6 = FF6(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1)
        x1, x2, x3, x4, x5, x6 = FF6(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6
    elif numFF == 7:
        x1, x2, x3, x4, x5, x6, x7 = FF7(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7 = FF7(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7
    elif numFF == 8:
        x1, x2, x3, x4, x5, x6, x7, x8 = FF8(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8 = FF8(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8
    elif numFF == 9:
        x1, x2, x3, x4, x5, x6, x7, x8, x9 = FF9(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9 = FF9(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9
    elif numFF == 10:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = FF10(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = FF10(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10
    elif numFF == 11:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 = FF11(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 = FF11(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11
    elif numFF == 12:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = FF12(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = FF12(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12
    elif numFF == 13:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13 = FF13(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13 = FF13(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13
    elif numFF == 14:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 = FF14(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1, f14=ffName, f14i1=i1, f14i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 = FF14(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1, f14=ffName, f14i1=i1, f14i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14
    elif numFF == 15:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = FF15(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1, f14=ffName, f14i1=i1, f14i2=1-i1, f15=ffName, f15i1=i1, f15i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = FF15(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1, f14=ffName, f14i1=i1, f14i2=1-i1, f15=ffName, f15i1=i1, f15i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15
    elif numFF == 16:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16 = FF16(flagPositive, 1-clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1, f14=ffName, f14i1=i1, f14i2=1-i1, f15=ffName, f15i1=i1, f15i2=1-i1, f16=ffName, f16i1=i1, f16i2=1-i1)
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16 = FF16(flagPositive, clk, f1=ffName, f1i1=i1, f1i2=1-i1, f2=ffName, f2i1=i1, f2i2=1-i1, f3=ffName, f3i1=i1, f3i2=1-i1, f4=ffName, f4i1=i1, f4i2=1-i1, f5=ffName, f5i1=i1, f5i2=1-i1, f6=ffName, f6i1=i1, f6i2=1-i1, f7=ffName, f7i1=i1, f7i2=1-i1, f8=ffName, f8i1=i1, f8i2=1-i1, f9=ffName, f9i1=i1, f9i2=1-i1, f10=ffName, f10i1=i1, f10i2=1-i1, f11=ffName, f11i1=i1, f11i2=1-i1, f12=ffName, f12i1=i1, f12i2=1-i1, f13=ffName, f13i1=i1, f13i2=1-i1, f14=ffName, f14i1=i1, f14i2=1-i1, f15=ffName, f15i1=i1, f15i2=1-i1, f16=ffName, f16i1=i1, f16i2=1-i1)
        return clk, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16
    else:
        print(f'*** ERROR: number of FF ({numFF}) should be <= 16 ***')
