#!/usr/bin/ python
import hashlib


def md5_hash(string):
    return hashlib.md5(string).hexdigest()

def sha1_hash(string):
    return hashlib.sha1(string).hexdigest()

def sha224_hash(string):
    return hashlib.sha224(string).hexdigest()

def sha256_hash(string):
    return hashlib.sha256(string).hexdigest()

def sha384_hash(string):
    return hashlib.sha384_hash(string).hexdigest()

def sha512_hash(string):
    return hashlib.sha512(string).hexdigest()

def print_array(arr):
    beginning = ''.join('{0}'.format(element) for element in arr) + flag1
    end = flag1 + ''.join('{0}'.format(element) for element in arr)


#MD5
    if hash == 1:
        if choice == 1:
            file.write(beginning + "\t" + md5_hash(beginning) + "\n")
        elif choice == 2:
            file.write(end + "\t" + md5_hash(end) + "\n")
#sha1
    elif hash == 2:
        if choice == 1:
            file.write(beginning + "\t" + sha1_hash(beginning) + "\n")
        elif choice == 2:
            file.write(end + "\t" + sha1_hash(end) + "\n")
#sha224
    elif hash == 3:
        if choice == 1:
            file.write(beginning + "\t" + sha224_hash(beginning) + "\n")
        elif choice == 2:
            file.write(end + "\t" + sha224_hash(end) + "\n")
#sha256
    elif hash == 4:
        if choice == 1:
            file.write(beginning + "\t" + sha256_hash(beginning) + "\n")
        elif choice == 2:
            file.write(end + "\t" + sha256_hash(end) + "\n")
#sha384
    elif hash == 5:
        if choice == 1:
            file.write(beginning + "\t" + sha384_hash(beginning) + "\n")
        elif choice == 2:
            file.write(end + "\t" + sha384_hash(end) + "\n")
#sha512
    elif hash == 6:
        if choice == 1:
            file.write(beginning + "\t" + sha512_hash(beginning) + "\n")
        elif choice == 2:
            file.write(end + "\t" + sha512_hash(end) + "\n")



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
    print"Enter the type of hash algorithm: \n1. MD5 \n2. SHA1\n3. SHA224\n4. SHA256 \n5. SHA384 \n6. SHA512"
    print("----------------------------------\n")
    hash = int(raw_input())


    print("----------------------------------")
    print"Enter the flag you would like to generate? \n"
    print("----------------------------------\n")
    flag1 = raw_input()

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
    print"Brute.py Finished"

    print("----------------------------------")
    print"How many hashes are you looking for? \n"
    input = int(raw_input())
    print("----------------------------------")

    for x in range(0,input):
        print("----------------------------------")
        print"Enter the hash:  \n\n"
        finder = raw_input()
        print("----------------------------------")

        for line in open("data.txt"):
            if finder in line:
             print "Found! \n" + line

     print"exiting..."
     file.close()

