import math

C = "0123456789ABCDEF"
number = input("please give a number:")
M = int(input("(2-16)from "))
while (M<2 or M>16):
    M = int(input("please input the numbwe from 2 to 16!!!\nfrom "))
N = int(input("\b to "))
while (N<2 or N>16):
    N = int(input("please input the numbwe from 2 to 16!!!\nto "))
number0X = 0
for i in range(len(number)):
    number0X += int(C.find(number[-(i+1)])*math.pow(M, i))

conclusion = ""
while (number0X!=0):
    conclusion = C[number0X%N] + conclusion
    number0X //= N
print(number, "from", M, "to", N, ":", conclusion)