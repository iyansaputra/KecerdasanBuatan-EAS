x_jumlahChar = input ('Masukan Jumlah Charakter B5 Anda (Limited B5) = ')
y_jumlahWep = input ('Masukan Jumlah Weapon B5 Anda (Limited B5) = ')

jumlahChar = int (x_jumlahChar)
jumlahWep = int (y_jumlahWep)

# Fuzzifikasi
# Jumlah Charakter 
if jumlahChar <= 9 :
    value_f2p = 1
    value_p2p = 0
    value_sultan = 0

if jumlahChar > 9 and jumlahChar < 18 :
    value_f2p = (18-jumlahChar) / (18-9)
    value_p2p = (jumlahChar-9) / (18-9)
    value_sultan = 0

if jumlahChar == 18 :
    value_f2p = 0
    value_p2p = 1
    value_sultan = 0

if jumlahChar > 18 and jumlahChar < 27 :
    value_f2p = 0
    value_p2p = (27-jumlahChar) / (27-18)
    value_sultan = (jumlahChar-18) / (27-18)

if jumlahChar == 27 :
    value_f2p = 0
    value_p2p = 0
    value_sultan = 1

# Jumlah Weapon
if jumlahWep <= 9 :
    value_Wf2p = 1
    value_Wp2p = 0
    value_Wsultan = 0

if jumlahWep > 9 and jumlahWep < 18 :
    value_Wf2p = (18-jumlahWep) / (18-9)
    value_Wp2p = (jumlahWep-9) / (18-9)
    value_Wsultan = 0

if jumlahWep == 18 :
    value_Wf2p = 0
    value_Wp2p = 1
    value_Wsultan = 0

if jumlahWep > 18 and jumlahWep < 27 :
    value_Wf2p = 0
    value_Wp2p = (27-jumlahWep) / (27-18)
    value_Wsultan = (jumlahWep-18) / (27-18)

if jumlahWep == 27 :
    value_Wf2p = 0
    value_Wp2p = 0
    value_Wsultan = 1

print ('Hasil Drajat Keanggotaaan Charakter')
print ('Nilai Free Player = ', value_f2p)
print ('Nilai Top-Up Player = ', value_p2p)
print ('Nilai Player Sultan = ', value_sultan)
print ('')

print ('Hasil Drajat Keanggotaaan Weapon')
print ('Nilai Free Player = ', value_Wf2p)
print ('Nilai Top-Up Player = ', value_Wp2p)
print ('Nilai Player Sultan = ', value_Wsultan)
print ('')

# Sistem Inferensi
