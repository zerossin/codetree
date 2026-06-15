m1, d1, m2, d2 = map(int, input().split())
A = input()

yoil = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

months_day = [0, 31, 29, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]

m = 0

for i in range(m1, m2):
    m += months_day[i]

chai = m + (d2-d1)
yoilsu = chai // 7
yoilsu_chuga = chai % 7
if yoilsu_chuga >= yoil.index(A):
    yoilsu += 1

print(yoilsu)
# Please write your code here.