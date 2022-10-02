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

print("==================")

Points_team_A = 90
Points_team_B = 80
Points_team_C = 90

if(Points_team_A > Points_team_B and Points_team_C):
    print("Team A menang atas tim B dan tim C")

print("How To Use Elif Keyword")

if (Points_team_A == 80):
    print("Tim B tidak memenangkan Laga")
elif(Points_team_B == 99):
    print("Tim A memenangkan Laga")
else:
    print("Tim C memenangkan Laga")

print("Nested IF in Python")
"""
if (condition):
    if(condition):
        if(condition):
            Indented block of decision to make
"""

teamAPoints = 99
teamBPoints = 89
teamCPoints = 88

if (teamAPoints > teamBPoints):
    if (teamAPoints >= teamBPoints):
        if (teamAPoints >= teamCPoints):
            print("Team A won the league")