print ('\t================================================================')
print ('\t\tProgram Menghitung Harga Akun Genshin Impact')
print ('\t\tBerdasarkan Charakter dan Weapon Player')
print ('\t================================================================\n')

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

print ('\t================================================================\n')
print ('Hasil Drajat Keanggotaaan Charakter')
print ('Nilai Free Player = ', value_f2p)
print ('Nilai Top-Up Player = ', value_p2p)
print ('Nilai Player Sultan = ', value_sultan)
print ('')

print ('\t================================================================\n')
print ('Hasil Drajat Keanggotaaan Weapon')
print ('Nilai Free Player = ', value_Wf2p)
print ('Nilai Top-Up Player = ', value_Wp2p)
print ('Nilai Player Sultan = ', value_Wsultan)
print ('')

# Sistem Inferensi
harga = []
harga.clear

def harga1 (value_jumlahChar, value_jumlahWep) :
    if value_jumlahChar != 0 :
        if value_jumlahWep != 0 :
            hasil_harga = min (value_jumlahChar, value_jumlahWep)
            harga.append ([hasil_harga, 1080])

def harga2 (value_jumlahChar, value_jumlahWep) :
    if value_jumlahChar != 0 :
        if value_jumlahWep != 0 :
            hasil_harga = min (value_jumlahChar, value_jumlahWep)
            harga.append ([hasil_harga, 2160])

def harga3 (value_jumlahChar, value_jumlahWep) :
    if value_jumlahChar != 0 :
        if value_jumlahWep != 0 :
            hasil_harga = min (value_jumlahChar, value_jumlahWep)
            harga.append ([hasil_harga, 3240])

harga1 (value_f2p, value_Wf2p)
harga1 (value_f2p, value_Wp2p)
harga1 (value_f2p, value_Wsultan)
harga2 (value_p2p, value_Wf2p)
harga2 (value_p2p, value_Wp2p)
harga2 (value_p2p, value_Wsultan)
harga3 (value_sultan, value_Wf2p)
harga3 (value_sultan, value_Wp2p)
harga3 (value_sultan, value_Wsultan)

print ('\t================================================================\n')
print ('Hasil Keputusan Harga Adalah : ', harga)

# Contructing the Output
perkalian_b = 0
pembagian_b = 0

for n in range (0, len(harga)):
    perkalian = harga[n][0] * harga[n][1]
    pembagian = harga[n][0]
    perkalian_b = perkalian_b + perkalian
    pembagian_b = pembagian_b + pembagian
    print (perkalian_b, pembagian_b)

print ('\t================================================================\n')
mean = (perkalian_b / pembagian_b)
print ('Maka Perkiraan Harga Akun Adalah = ', int(mean), 'Rupiah')