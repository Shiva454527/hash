
import hashlib
print("")
print(" ---------------Hash convert-------------v1.0")
print("")
print("")
print("<============================================>")
print("              Created by shiva")
print("<============================================>")
print("")
print("")
print("Available Options:\n1.MD5\n2.SHA512\n3.SHA256\n4.Select All\n5.Exit")

while True:
	choice = int(input('Select An Option: '))
	if choice == 5:
		
		
		exit()
	else:
		string = input('Enter String To Hash: ')

	def md5(string):
		hash_object = hashlib.md5(string.encode())
		print("MD5: " + hash_object.hexdigest() + "\n")

	def sha512(string):
        	hash_object = hashlib.sha512(string.encode())
        	print("SHA512: " + hash_object.hexdigest() + "\n")

	def sha256(string):
        	hash_object = hashlib.sha256(string.encode())
        	print("SHA256: " + hash_object.hexdigest() + "\n")


	if choice == 1:
		md5(string)
	elif choice == 2:
		sha512(string)
	elif choice == 3:
		sha256(string)
	elif choice == 4:
		md5(string)
		sha512(string)
		sha256(string)
	else:
		print("Invalid Option!")
		
		

		exit()
			
	
	
	print("")
	print("                 Thank you for downloading.")
		
