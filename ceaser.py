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
		key=key%26
		enc=""
		for i in range(len(string)):
			val = ord(string[i])
			if(val >=ord('a') and val <=ord('z')):
				val-=ord('a')
				val+=key;
				val = val%26;
				val+=ord('a')
			elif(val >=ord('A') and val <=ord('Z')):
				val-=ord('A')
				val+=key;
				val = val%26;
				val+=ord('A')
			enc=enc+chr(val)
		print (enc)
	