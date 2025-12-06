
def reverse(x):

    rev = 0
    if x > 0:
        while (x>0):

            rem = x % 10

            rev = rev*10 + rem

            x= x//10
        return rev
    else:
        temp = x * (-1)
        print(temp)
        rev = 0
        while (temp>0):

            rem = temp % 10

            rev = rev*10 + rem

            temp= temp//10
        return (temp)

if __name__ == "__main__":
    x = -123
    print(reverse(x))