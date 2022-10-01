"""
Write a Python program to find those numbers 
which are divisible by 7 and multiple of 5, 
between 1500 and 2700 (both included).
"""

nl = []
for x in range(1500,2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print(','.join(nl))

print("Simple IF Else")
# DEclaration Variable

Nilai_1 = 90
Nilai_2 = 80
Nilai_3 = 90

Total = Nilai_1 + Nilai_2 + Nilai_3

if (Total > 200):
    print("Selamat Anda Lulus Tes ini")

if (Nilai_2 < Nilai_1):
    print("Ayo Coba Lagi , Tingkatkan Nilainya")