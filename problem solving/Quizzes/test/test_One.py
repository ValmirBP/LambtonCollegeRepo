class color:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightGrey = '\033[37m'
    darkGrey = '\033[90m'
    lightRed = '\033[91m'
    lightGreen = '\033[92m'
    yellow = '\033[93m'
    lightBlue = '\033[94m'
    pink = '\033[95m'
    lightCyan = '\033[96m'
    reset = '\033[0m'

# -------------------------------------------------------------------------------------------
# Write a python program to find the sum of all even numbers from 0 to 10


def test_one_1():
    total = 0
    for i in range(0, 11):
        print(color.green, f"{i}", color.reset, end=" ")
        total = total + i

    print(color.cyan,
          f"\nThe Sum of Even Numbers from 1 to 10 = {total}", color.reset)


test_one_1()
# -------------------------------------------------------------------------------------------
# Write down a python code that prints out the following pattern:


def test_one_2():
    # number of rows
    rows = int(input("Enter the number of rows: "))

    # Outer loop will print the number of rows
    for i in range(0, rows):
        # This inner loop will print the stars
        for j in range(0, i + 1):
            print("*", end=' ')
        # Change line after each iteration
        print(" ")
    # For second pattern
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")


test_one_2()
# -------------------------------------------------------------------------------------------
# Write a python program that print out the complete list of couples of prime
# numbers that are less than 50, but their sum is bigger than 40. For instance:
# (29,13) or (37,17), etc. Your program should print all couples.


def test_one_3(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


primes = []
for i in range(2, 51):
    if test_one_3(i):
        primes.append(i)

couples = []

n = len(primes)
for i in range(n):
    for j in range(i+1, n):
        if ((primes[i]+primes[j]) > 40):
            couples.append((primes[i], primes[j]))
print(couples)

test_one_3()
# -------------------------------------------------------------------------------------------

# Write a python code to reverse the order of the elements in an array. For
# example, if A = [1, 2, 3, 4], the reverse of it would be [4, 3, 2, 1].


def test_one_4():
    myArr = [1, 2, 3, 4, 5]
    print(f"The Original Array is : {myArr}")

    res = myArr[::-1]  # reversing using list slicing
    print(f"New Array is: {res}")


test_one_4()
# -------------------------------------------------------------------------------------------
# Write a python code to find the first duplicate of an integer in an array. For
# example, if A= [1, 2, 3, 4, 5, 2, 1, 4], then the result would be 2, because 2 is
# the first duplicated integer.


def test_one_5(nums):
    setting = set()
    noDuplicate = -1

    for i in range(len(nums)):
        if nums[i] in setting:
            return nums[i]
        else:
            setting.add(nums[i])

    return noDuplicate


print(test_one_5([0, 2, 3, 4, 5, 1, 4]))
print(test_one_5([1, 2, 3, 4]))
print(test_one_5([2, 3, 3, 2, 2]))

# --------------------------------------------------------------

# Write a python program to sum the prime numbers existing in an array. For
# instance, if A = [4, 7, 12, 3, 9], the output should be 10.


def test_one_6(arr):
    lenghArray = len(arr)
    ValueMax = max(arr)
    prime = [True for i in range(ValueMax + 1)]  # creating the array

    prime[0] = False
    prime[1] = False

    for p in range(2, ValueMax + 1):
        if (p * p > ValueMax):
            break
        if (prime[p] == True):
            for i in range(p * 2, ValueMax+1, p):
                prime[i] = False

    sum = 0
    for i in range(lenghArray):
        if (prime[arr[i]]):
            sum += arr[i]
    return sum


arr = [4, 7, 12, 3, 9]
print("The summ  is", test_one_6(arr))


# --------------------------------------------------------------

# Write a python program to multiply the elements of two arrays in reverse
# order and then sum them up. Assume that two arrays have the same size.
# For example, if A = [2, 1, 8, 9] and B = [4, 2, 7, 12], then the result would be:
# (2*12) + (1*7) + (8*2) + (9*4) = 24 + 7 + 16 + 36 = 83

def test_one_7():
    a = list(map(int, input('Type here the Array A: ').split()))
    print("array A is ", a)
    b = list(map(int, input('Type here the Array B: ').split()))
    print("array B is ", b)
    s = 0
    for i in range(len(a)):
        s = s + (a[i]*b[-i-1])

    print(s)


test_one_7()

# --------------------------------------------------------------

# Write the python code that takes in an array and prints out all pairs of
# integers from the array whose sum is a prime number. For instance, if A = [2,
# 9, 1, 8], the outcome would be (2, 1) , (2,9) and (9, 8).


def test_one_8(m):
    if ((m) % 2 == 0):
        return 0
    else:
        for k in range(3, m):
            if (m % k == 0):
                return 0
        return 1


n = int(input("How is the lengh of the array?  "))
i = 0
arr = []
while (i < n):
    num = int(input("Enter number : "))
    arr.append(num)
    i = i+1
print(arr)
for i in range(n-1):
    for j in range(i+1, n):

        res = test_one_8(arr[i]+arr[j])

        if (res == 1):
            print("(", arr[i], ",", arr[j], ')')
