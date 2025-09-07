def printnum(n):
    if n ==0:
        return
    print(n)
    printnum(n-1)

def printRev(n):
    if n ==0:
        return
    printRev(n-1)
    print(n)

def productNum(n):
    if n == 1:
        return 1
    return n * productNum(n-1)

def sumNum(n):
    if n == 0:
        return 0

    return n + sumNum(n-1)

def sumOfDigits(n):
    
    
if __name__ =="__main__":
    product = productNum(4)
    print(product)

    sum = sumNum(5)
    print(sum)