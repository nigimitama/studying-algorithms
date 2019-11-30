N = int(input())
addresses = [input().split(".") for x in range(N)]

for address in addresses:
    if len(address) == 4:
        try:
            address = list(map(int, address))
            values_in_valid_range = [x for x in address if 0 <= x <= 255]
            if len(values_in_valid_range) == 4:
                print("True")
            else:
                print("False")
        except:
            print("False")
    else:
        print("False")
