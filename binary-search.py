data = [2,4,5,6,8,9,11,12,14,16,18,19,22,23,26,27]
target = 2

#Linear search -> Loop check
def linear(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

lsearch = linear(data, target)
print("Linear Result = " + str(lsearch))

# Binary search -> check one half, remove the other ... repeat...
def binary(data, target):
    data.sort()
    top = len(data) - 1
    bottom = 0

    while(top > bottom):
        middle = (top + bottom) // 2
        if (target == data[middle]):
            return True
        elif (target < data[middle]):
            top = middle
        elif (target > data[middle]):
            bottom = middle
    return False

bsearch = binary(data, target)
print("Binary Result = " + str(bsearch))
