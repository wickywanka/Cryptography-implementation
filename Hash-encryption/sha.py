# Python 3 code to demonstrate 
# SHA hash algorithms. 
# all SHA combined
import hashlib 

# initializing string 
#str = "9996695225"
f=open('phno.txt',"r")
str=f.read()
f.close()

# encoding GeeksforGeeks using encode() 
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "GeeksforGeeks"

# encoding GeeksforGeeks using encode() 
# then sending to SHA384() 
result = hashlib.sha384(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA384 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "GeeksforGeeks"

# encoding GeeksforGeeks using encode() 
# then sending to SHA224() 
result = hashlib.sha224(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA224 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "GeeksforGeeks"

# encoding GeeksforGeeks using encode() 
# then sending to SHA512() 
result = hashlib.sha512(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA512 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "GeeksforGeeks"

# encoding GeeksforGeeks using encode() 
# then sending to SHA1() 
result = hashlib.sha1(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 is : ") 
print(result.hexdigest()) 
