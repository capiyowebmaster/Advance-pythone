#

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hello capiyo the genious")  # Press Ctrl+F8 to toggle the breakpoint.


def summingLists():
    print("please Enter number to be searched")
    num = int(input())
    list = [20, 40, 56, 34, 28,89]
    for x in list:
        if x == num:
            print("Numbers was found at: ", list.index(x))
            return


def looper(n):
    for x in range(0, n):
        for y in range(0, x + 1):
            print("Oscar", end="  ")
        print("\r")


def backWard(n):
    for x in range(0, n - 4):
        for y in range(x + 1, 10):
            print("Oscar", end="  ")
        print("\r")


def addTwo():
    for count in [1, 2, 3]:
        print(count)
    print('Yes')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # addTwo()
    looper(5)
    summingLists()
