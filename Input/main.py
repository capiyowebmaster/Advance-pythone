def takeInput():
    my_lists = []
    print("Enter your lists")
    for x in range(0, 8):
        element = int(input())
        my_lists.append(element)
        if my_lists.__len__() == 8:
            my_lists.sort()

            print(my_lists[-1])


if __name__ == '__main__':
    takeInput()
