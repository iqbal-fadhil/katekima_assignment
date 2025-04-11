class GeneralLFSR:
    def __init__(self, size=4, taps=[0, 3], initial_state="0110"):
        self.size = size
        self.taps = taps  # posisi yang digunakan untuk feedback XOR
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
        # XOR semua posisi yang ada di taps
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        output_bit = self.state[-1]
        self.state = [feedback] + self.state[:-1]
        return output_bit

# Tes: Konfigurasi sama seperti LFSR dasar (size 4, taps [0, 3], init state 0110)
lfsr = GeneralLFSR(size=4, taps=[0, 3], initial_state="0110")
print("General LFSR (tanpa pustaka):")
for i in range(20):
    print(f"{i+1:02d}. State: {lfsr.get_state()} -> Next bit: {lfsr.next_bit()}")
