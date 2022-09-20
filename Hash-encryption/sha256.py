# Python 3 code to demonstrate 
# SHA hash algorithms. 

import hashlib 

# initializing string phone number
f=open('phno.txt',"r")
str=f.read()
f.close()
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 
# storing the equivalent hexadecimal value. 
g=open('phnoe.txt',"w")
g.write(result.hexdigest())
g.close()

# initializing string phone number
f=open('card.txt',"r")
str=f.read()
f.close()
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 
# storing the equivalent hexadecimal value. 
g=open('carde.txt',"w")
g.write(result.hexdigest())
g.close()


