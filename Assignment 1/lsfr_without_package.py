class GeneralLFSR:
    def __init__(self, size=4, taps=[0, 3], initial_state="0110"):
        self.size = size
        self.taps = taps  # position for XOR feedback
        self.state = [int(bit) for bit in initial_state]
        self.initial_state = self.state.copy()

    def get_state(self):
        return ''.join(map(str, self.state))

    def set_state(self, new_state):
        self.state = [int(bit) for bit in new_state]

    def reset(self):
        self.state = self.initial_state.copy()

    def set_taps(self, new_taps):
        self.taps = new_taps

    def next_bit(self):
        # XOR all positions on taps
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        output_bit = self.state[-1]
        self.state = [feedback] + self.state[:-1]
        return output_bit

# Similar test to the with library file (size 4, taps [0, 3], init state 0110)
lfsr = GeneralLFSR(size=4, taps=[0, 3], initial_state="0110")
print("General LFSR (without library):")
for i in range(20):
    print(f"{i+1:02d}. State: {lfsr.get_state()} -> Next bit: {lfsr.next_bit()}")
