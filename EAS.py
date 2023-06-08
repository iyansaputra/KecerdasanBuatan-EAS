print('--------->Implementasi Logika Fuzzy<------------')
print('')
x_temp  = input('Masukkan Nilai Temperature Saat ini (F) = ' )
y_cloud = input ('Masukkan Nilai Cloud Cover (%) = ')

temp  = int(x_temp)
cloud = int(y_cloud)

#Fuzzifikasi
#Temperature
if  temp<= 30:
    value_freezing = 1
    value_cool = 0
    value_warm = 0
    value_hot  = 0

if temp>30 and temp<50 :
    value_freezing = (50-temp)/(50-30)
    value_cool = (temp-30)/(50-30)
    value_warm = 0
    value_hot  = 0
   
if temp ==50:
   value_freezing = 0
   value_cool = 1
   value_warm = 0
   value_hot  = 0
    
if temp>50 and temp<70:
   value_freezing = 0
   value_cool = (70-temp)/(70-50)
   value_warm = (temp - 50)/(70-50)
   value_hot  = 0
   
if temp ==70:
   value_freezing = 0
   value_cool = 0
   value_warm = 1
   value_hot  = 0   
   
if temp>70 and temp<90:
   value_freezing = 0
   value_cool = 0
   value_warm = (90-temp)/(90-70)
   value_hot  = (temp-70)/(90-70)
   
if temp>=90:
   value_freezing = 0
   value_cool = 0
   value_warm = 0
   value_hot  = 1

#Cloud Cover
if cloud<=20:
   value_sunny = 1
   value_partlycloudy = 0
   value_overcast = 0
   
if cloud>20 and cloud <40:
    value_sunny = (40-cloud)/(40-20)
    value_overcast = 0
    
if cloud>20 and cloud <50:
    value_partlycloudy = (cloud - 20)/(50-20)
    value_overcast = 0

if cloud >= 40:
   value_sunny = 0
    
if cloud == 50:
   value_sunny = 0
   value_partlycloudy = 1
   value_overcast = 0
   
if cloud>50 and cloud<80:
   value_partlycloudy = (80 - cloud)/(80-50)
   
if cloud <=60:
    value_overcast=0

if cloud>60 and cloud<80:
    value_overcast = (cloud-60)/(80-60)
   
if cloud>=80:
   value_partlycloudy=0
   value_overcast=1
print('')
print('Hasil Proses Fuzzifikasi') 
print('Hasil derajat keanggotaan pada setiap variabel Linguistik "Temperature"')
print('Nilai Freezing =', value_freezing)
print('Nilai Cool =', value_cool)
print('Nilai Warm =', value_warm)
print('Nilai Hot =', value_hot)
print('')
print('Hasil derajat keanggotaan pada setiap variabel Linguistik "Cloud Cover"' )
print('Nilai Sunny =', value_sunny)
print('Nilai Partly Cloudy =', value_partlycloudy)
print('Nilai Overcast =', value_overcast)

#Sistem Inferensi
print('Sistem Inferensi / Menyesuaikan sesuai aturan yang dibuat')
speed=[]
speed.clear()
# diisi titik slow adalah 25, dan fast adalah 75
def fungsiinferensislow(value_temp, value_cloud):
    if value_temp!=0 :
       if value_cloud!=0:
           hasil_fungsi = min(value_temp, value_cloud)
           speed.append([hasil_fungsi,25])
           

def fungsiinferensifast(value_temp, value_cloud):
    if value_temp!=0 :
       if value_cloud!=0:
           hasil_fungsi = min(value_temp, value_cloud)
           speed.append([hasil_fungsi,75])


fungsiinferensislow(value_freezing,value_sunny)
fungsiinferensislow(value_freezing,value_partlycloudy)
fungsiinferensislow(value_freezing,value_overcast)
fungsiinferensislow(value_cool,value_sunny)
fungsiinferensislow(value_cool,value_partlycloudy)
fungsiinferensislow(value_cool,value_overcast)
fungsiinferensifast(value_warm,value_sunny)
fungsiinferensifast(value_warm,value_partlycloudy)
fungsiinferensifast(value_warm,value_overcast)
fungsiinferensifast(value_hot,value_sunny)
fungsiinferensifast(value_hot,value_partlycloudy)
fungsiinferensifast(value_hot,value_overcast)


print('Hasil Keputusan Kecepatan Adalah = ', speed )
# Defuzzifikasi (Contructing the output)
perkalian_new = 0
pembagian_new = 0
for j in range(0,len(speed)):
    perkalian = speed[j][0]*speed[j][1]
    pembagian = speed[j][0]
    perkalian_new= perkalian_new +perkalian
    pembagian_new=pembagian_new+pembagian
    print(perkalian_new, pembagian_new)

weighted_mean=(perkalian_new/pembagian_new)
print('Maka Kecepatan Mobil Adalah = ', weighted_mean, '(mph)')