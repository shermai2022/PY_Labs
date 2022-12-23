list = [1,3,2,0,4,2,7,8,9]
new = []
b = 0
def order(list):
    for i in range(len(list)):
        if list[i] > list[i-1]:
            b = list[i]
            new.append(b)
        else:
            continue
    return new
    
    
    
print(order(list))
