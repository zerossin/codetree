m1, d1, m2, d2 = map(int, input().split())

yoil = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

months_day = [0, 31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]

m = 0
chai = 0
yoilindex = 0

if m1*30+d1 < m2*30+d2:
    for i in range(m1, m2):
        m += months_day[i]

    chai = m + (d2-d1)
    yoilindex = chai % 7
else:
    for i in range(m2, m1):
        m += months_day[i]
    
    chai = m + (d1-d2)
    yoilindex = -(chai % 7)

print(yoil[yoilindex])
# Please write your code here.