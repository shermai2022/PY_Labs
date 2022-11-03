a = True
b = False

print(a and b)
print((a & b) | b)
print((a & b) ^ (a & b))
print (a & b ^ (a & b) | b)
print(b and b or not a and (a or b or a) or not (a or b))
print (1<<2)
print(1 & 1 | 101 >> 3)
print (1 & 0 | 1 << 1)
print( 0b101 & 0b111 ^ 0b111 | 0b010)




num_1 = input("число 1: ")
num_2 = input("число 2: ")

if num_1 > num_2:
    print(num_2)

else:
    print(num_1) # при сравнении некоторых чисел происходит
                 # ошибка, например, при вводе 19 и 6 выводит 19

num_1 = input("число 1: ")
num_2 = input("число 2: ")
num_3 = input("число 3: ")

if num_1 > num_2 > num_3:
    print(num_1)

elif num_3 > num_2 > num_1:
    print(num_3)

elif num_2 > num_1 > num_3:
    print (num_2)
else:
    print("числа равны")

    
num_1 = input("число 1: ")
num_2 = input("число 2: ")
num_3 = input("число 3: ")

number = [num_1, num_2, num_3]
sss = len(set(number))
print(sss)
