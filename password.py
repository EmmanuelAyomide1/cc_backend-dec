import string
import random
Letters=string.ascii_letters
Numbers=string.digits
SpecialCharacter=string.punctuation
amount=int(input("How long should the password be\n"))
password=[]
Choices=[Letters,Numbers,SpecialCharacter,Letters]
i=0
while i<amount:
   choice=random.choice(Choices)
   password.append(random.choice(choice))
   i+=1
StrongPassword="".join(password)
print(StrongPassword)