
def tester(ls, targ1, targ2):
    for i in range(len(ls)-1):
        if ls[i] == targ1 and ls[i+1] == targ2 or ls[i] == targ2 and ls[i+1] == targ1:
            return True
    return False
        
print("should be False: ", tester([3,1,0,19,4], 19, 5))
print("should be True: ", tester([3,1,0,19], 19, 0))

def tester2(lis, tar1, tar2):
    if tar1 in lis and tar2 in lis:
        if lis.index(tar1) - lis.index(tar2) == 1 or lis.index(tar1) - lis.index(tar2) == -1:
            return True
    return False

print("should be False: ", tester2([3,1,0,19,4], 19, 5))
print("should be True: ", tester2([3,1,0,19], 19, 0))