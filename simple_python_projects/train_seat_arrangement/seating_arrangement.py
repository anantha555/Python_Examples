def user_input1(range_limt):
    while True:
        try:
            if range_limt == 105:
                input_value = int(input("Enter the number of test cases:\n"))
            elif range_limt == 108:
                input_value = int(input())

            if 0 < input_value < range_limt+1:
                return input_value
            else:
                raise ValueError
        except ValueError:
            print("Input only accepts value in range 1 to", range_limt, ".\n")

def check_seat_type(seatnum):
    seatnum = seatnum + 2 *(6-(seatnum-1)%12)-1

    if seatnum % 6 < 2:
        print(str(seatnum)+ " "+ "WS")
    elif (seatnum % 6 == 2 or seatnum % 6 == 5):
        print(str(seatnum)+" MS")
    else:
        print(str(seatnum)+" AS")


lst = []

N = user_input1(105)
print("Enter", N, "seat numbers of your choice:")

for i in range(0, N):
    ele = user_input1(108)
    lst.append(ele)

print("The facing seat-number and the seat-type of seats", str(lst)[1:-1], "are:")

for i in range(0, N):
    s = lst[i]
    check_seat_type(s)

