#!/usr/bin/python


def print_array(arr):
    beginning = ''.join('{0}'.format(element) for element in arr) + flag
    end = flag+ ''.join('{0}'.format(element) for element in arr)
    if choice == 1:
        file.write(beginning + "\n")
    elif choice == 2:
        file.write(end + "\n")



def inc_cell(arr, position, minimum, maximum):
    for i in range(minimum, maximum):
        arr[position] = i
        print_array(arr)

def inc_array(arr, current_position, minimum, maximum):

    if current_position == array_max_position:
        inc_cell(arr, current_position, minimum, maximum)

    else:
        for i in range(minimum, maximum):
            arr[current_position] = i
            inc_array(arr, (current_position + 1), minimum, maximum)

if __name__ == '__main__':
    file = open("data.txt", "w+")



    print("----------------------------------")
    print"Enter the flag you would like to generate? \n"
    print("----------------------------------\n")
    flag = raw_input()

    print("----------------------------------")
    print"How many character are you trying to generate? \nExample: flag_ _ _ _"
    print("----------------------------------\n")
    array_size = int(raw_input())

    print("----------------------------------")
    print "Where would you like to place these characters? \n1. Beginning \n2. End \nExample: 9999flag or flag9999"
    print("----------------------------------\n")    
    choice = int(raw_input())

    array_max_position = array_size - 1
    min_range = 0
    max_range = 10
    array = bytearray(array_size)
    inc_array(array, 0, min_range, max_range)
    
    file.close()
    print"bruteforce.py Finished"
print"exiting..."
file.close()

