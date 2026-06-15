m1, d1, m2, d2 = map(int, input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m = 0

for i in range(m1, m2):
    m += num_of_days[i]

print(m+(d2 - d1)+1)

# Please write your code here.
