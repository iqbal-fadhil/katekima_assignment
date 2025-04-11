from pylfsr import LFSR

# Konfigurasi sama: size = 4, feedback polynomial (tap) di posisi 4 dan 1
lfsr = LFSR(fpoly=[4, 1], initstate=[0, 1, 1, 0])
print("General LFSR menggunakan pylfsr:")

# Reset ke state awal jika mau diulang
lfsr.set(fpoly=[4, 1], initstate=[0, 1, 1, 0])

for i in range(20):
    state = ''.join(map(str, lfsr.state))
    next_bit = lfsr.next()
    print(f"{i+1:02d}. State: {state} -> Next bit: {next_bit}")
