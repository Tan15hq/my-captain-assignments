n = int(input('give the value of n for number of terms \n'))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
    t = b
    b = a + b
    a = t
    print(b)
