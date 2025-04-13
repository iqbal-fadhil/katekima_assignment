from pylfsr import LFSR

# Initialization for LFSR 
lfsr = LFSR(fpoly=[4, 1], initstate=[0, 1, 1, 0])
print("General LFSR with pylfsr:")

# Reset 
lfsr.set_fpoly([4, 1])
lfsr.set_state([0, 1, 1, 0])

for i in range(20):
    state = ''.join(map(str, lfsr.state))
    next_bit = lfsr.next()
    print(f"{i+1:02d}. State: {state} -> Next bit: {next_bit}")
