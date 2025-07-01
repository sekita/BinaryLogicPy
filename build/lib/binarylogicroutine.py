#coding: utf-8
# Last updated on 2024.05.14 - Modified to remove global variables

class FlipFlopController:
    """
    FlipFlopController manages the state of multiple flip-flops without using global variables.
    Each instance maintains its own state for up to maxFF flip-flops.
    """

    def __init__(self, maxFF=100):
        self.maxFF = maxFF
        # Clock states for each flip-flop type [positive/negative][ff_index]
        self.clkJKFF = [[1] * maxFF, [0] * maxFF]
        self.clkRSFF = [[1] * maxFF, [0] * maxFF]
        self.clkSRFF = [[1] * maxFF, [0] * maxFF]
        self.clkDFF = [[1] * maxFF, [0] * maxFF]
        self.clkTFF = [[1] * maxFF, [0] * maxFF]

        # Output states for each flip-flop type [positive/negative][ff_index]
        self.qJKFF = [[0] * maxFF for _ in range(2)]
        self.qRSFF = [[0] * maxFF for _ in range(2)]
        self.qSRFF = [[0] * maxFF for _ in range(2)]
        self.qDFF = [[0] * maxFF for _ in range(2)]
        self.qTFF = [[0] * maxFF for _ in range(2)]

    def jkff(self, ipos, iknd, ip2, ij, ik):
        """
        JK flip-flop simulation.

        Parameters:
            ipos (int): Edge type (1 for positive edge, 0 for negative edge).
            iknd (int): Type of FF (range: 0 to maxFF).
            ip2 (int): New clock state to transition to.
            ij (int): J input signal.
            ik (int): K input signal.

        Returns:
            int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
        """
        if iknd >= self.maxFF:
            print(f"*** ERR: kind of JK-FF({iknd}) must be >=0 and <{self.maxFF}. ***")
            return -1

        if ((ipos == 0 and self.clkJKFF[ipos][iknd] == 1 and ip2 == 0) or 
            (ipos == 1 and self.clkJKFF[ipos][iknd] == 0 and ip2 == 1)):
            if ij == 1 and ik == 0:
                self.qJKFF[ipos][iknd] = 1
            elif ij == 0 and ik == 1:
                self.qJKFF[ipos][iknd] = 0
            elif ij == 1 and ik == 1:
                self.qJKFF[ipos][iknd] = int(not self.qJKFF[ipos][iknd])

        self.clkJKFF[ipos][iknd] = ip2
        return self.qJKFF[ipos][iknd]

    def srff(self, ipos, iknd, ip2, isInput, ir):
        """
        SR flip-flop simulation.

        Parameters:
            ipos (int): Edge type (1 for positive edge, 0 for negative edge).
            iknd (int): Type of FF (range: 0 to maxFF).
            ip2 (int): New clock state to transition to.
            isInput (int): S input signal (Set).
            ir (int): R input signal (Reset).

        Returns:
            int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
        """
        if iknd >= self.maxFF:
            print(f"*** ERR: kind of SR-FF({iknd}) must be >=0 and <{self.maxFF}. ***")
            return -1

        if ((ipos == 0 and self.clkSRFF[ipos][iknd] == 1 and ip2 == 0) or 
            (ipos == 1 and self.clkSRFF[ipos][iknd] == 0 and ip2 == 1)):
            if ir == 1 and isInput == 0:
                self.qSRFF[ipos][iknd] = 0
            elif ir == 0 and isInput == 1:
                self.qSRFF[ipos][iknd] = 1
            elif ir == 1 and isInput == 1:
                print(f"*** ERR: S={isInput} and R={ir} is not permitted. ***")
                return -1

        self.clkSRFF[ipos][iknd] = ip2
        return self.qSRFF[ipos][iknd]

    def rsff(self, ipos, iknd, ip2, ir, isInput):
        """
        RS flip-flop simulation.

        Parameters:
            ipos (int): Edge type (1 for positive edge, 0 for negative edge).
            iknd (int): Type of FF (range: 0 to maxFF).
            ip2 (int): New clock state to transition to.
            ir (int): R input signal (Reset).
            isInput (int): S input signal (Set).

        Returns:
            int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
        """
        if iknd >= self.maxFF:
            print(f"*** ERR: kind of RS-FF({iknd}) must be >=0 and <{self.maxFF}. ***")
            return -1

        if ((ipos == 0 and self.clkRSFF[ipos][iknd] == 1 and ip2 == 0) or 
            (ipos == 1 and self.clkRSFF[ipos][iknd] == 0 and ip2 == 1)):
            if ir == 1 and isInput == 0:
                self.qRSFF[ipos][iknd] = 0
            elif ir == 0 and isInput == 1:
                self.qRSFF[ipos][iknd] = 1
            elif ir == 1 and isInput == 1:
                print(f"*** ERR: R={ir} and S={isInput} is not permitted. ***")
                return -1

        self.clkRSFF[ipos][iknd] = ip2
        return self.qRSFF[ipos][iknd]

    def dff(self, ipos, iknd, ip2, idInput, idummy=0):
        """
        D flip-flop simulation.

        Parameters:
            ipos (int): Edge type (1 for positive edge, 0 for negative edge).
            iknd (int): Type of D-FF (range: 0 to maxFF).
            ip2 (int): New clock state to transition to.
            idInput (int): D input signal (Data).
            idummy (int, optional): Placeholder parameter; default is 0.

        Returns:
            int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
        """
        if iknd >= self.maxFF:
            print(f"*** ERR: kind of D-FF({iknd}) must be >=0 and <{self.maxFF}. ***")
            return -1

        if ((ipos == 0 and self.clkDFF[ipos][iknd] == 1 and ip2 == 0) or 
            (ipos == 1 and self.clkDFF[ipos][iknd] == 0 and ip2 == 1)):
            self.qDFF[ipos][iknd] = int(idInput)

        self.clkDFF[ipos][iknd] = ip2
        return self.qDFF[ipos][iknd]

    def tff(self, ipos, iknd, ip2, it, idummy=0):
        """
        T flip-flop simulation.

        Parameters:
            ipos (int): Edge type (1 for positive edge, 0 for negative edge).
            iknd (int): Type of T-FF (range: 0 to maxFF).
            ip2 (int): New clock state to transition to.
            it (int): T input signal (Toggle).
            idummy (int, optional): Placeholder parameter; default is 0.

        Returns:
            int: The new Q (output) state of the flip-flop, or -1 if an error occurs.
        """
        if iknd >= self.maxFF:
            print(f"*** ERR: kind of T-FF({iknd}) must be >=0 and <{self.maxFF}. ***")
            return -1

        if ((ipos == 0 and self.clkTFF[ipos][iknd] == 1 and ip2 == 0) or 
            (ipos == 1 and self.clkTFF[ipos][iknd] == 0 and ip2 == 1)):
            if it == 1:
                self.qTFF[ipos][iknd] = int(not self.qTFF[ipos][iknd])

        self.clkTFF[ipos][iknd] = ip2
        return self.qTFF[ipos][iknd]

    def ffN(self, numFF, flagPositive, clock, ffConfigs):
        """
        Generic function to handle multiple flip-flops.

        Parameters:
            numFF (int): Number of flip-flops (1-16).
            flagPositive (int): Edge type (1 for positive, 0 for negative).
            clock (int): Clock signal.
            ffConfigs (list): List of tuples (ffFunction, input1, input2) for each FF.

        Returns:
            tuple: Clock value and outputs of all flip-flops.
        """
        if numFF < 1 or numFF > 16:
            print(f"*** ERROR: number of FF ({numFF}) should be between 1 and 16 ***")
            return None

        results = []
        for i in range(numFF):
            if i < len(ffConfigs):
                ffFunc, input1, input2 = ffConfigs[i]
                result = ffFunc(flagPositive, i, clock, input1, input2)
            else:
                # Default to DFF with 0 inputs
                result = self.dff(flagPositive, i, clock, 0, 0)
            results.append(result)

        return tuple([clock] + results)

    def resetFF(self, flagPositive, ffName_str, numFF):
        """
        Resets a specified number of flip-flops to their initial state.

        Parameters:
            flagPositive (int): Specifies the clock edge type. 
                               Use 1 for a positive edge and 0 for a negative edge.
            ffName_str (str): String representing the flip-flop type. 
                             Acceptable values: 'JKFF', 'RSFF', 'SRFF', 'DFF', 'TFF'.
            numFF (int): The number of flip-flops to reset.

        Returns:
            tuple: The clock value and Q states of the flip-flops.
        """
        if numFF < 1 or numFF > 16:
            print(f"*** ERROR: number of FF ({numFF}) should be between 1 and 16 ***")
            return None

        clk = flagPositive

        # Determine input values based on FF type
        if ffName_str == 'RSFF':
            i1 = 1
        else:
            i1 = 0

        # Special handling for TFF reset
        if ffName_str == 'TFF':
            for ii in range(2):
                for jj in range(self.maxFF):
                    self.qTFF[ii][jj] = 0

        # Get the appropriate FF method
        ff_method = getattr(self, ffName_str.lower())

        # Create configuration for all FFs
        ffConfigs = [(ff_method, i1, 1-i1) for _ in range(numFF)]

        # Reset phase 1
        self.ffN(numFF, flagPositive, 1-clk, ffConfigs)
        # Reset phase 2
        result = self.ffN(numFF, flagPositive, clk, ffConfigs)

        return result

    @staticmethod
    def separator(inum, nth):
        """
        Returns the value of the nth bit of the input number `inum`, using little-endian order.

        Parameters:
            inum (int): Input number (unsigned integer).
            nth (int): Bit position to extract (0, 1, ...), counted from right to left.

        Returns:
            int: The value of the specified bit (0 or 1).
        """
        ione = 1
        inum = inum >> nth
        ival = inum & ione
        return ival


# Convenience functions for backward compatibility
def createFFController(maxFF=100):
    """Create a new FlipFlopController instance."""
    return FlipFlopController(maxFF)
