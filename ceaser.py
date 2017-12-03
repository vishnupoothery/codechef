print ("Welcome to Ceaser's Cipher\n")

cmd = ""

while cmd !="0":
    print ("Enter your choice")
    print ("1. Encrypt")
    print ("2. Decrypt")
    print ("0. Exit")

    cmd = input(" : ")

    if cmd == "1":
        string = input("Enter string to Encrypt :\n")
        key = int(input("Enter encryption key : "))