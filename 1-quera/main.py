def game(number):
    both = [int(a) for a in str(number)]
    if both[0] > both[1]:
        print(both[0] - both[1])
    elif both[0] < both[1]:
        print(both[1] - both[0])
    else:
        print(both[0] - both[1])


game(int(input("Enter Number : ")))
