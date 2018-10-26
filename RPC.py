import random
c=[]
p=[]
sp=0
cp=0
a=["Rock","paper","Scissor"]
w=int(input("How many turns is the Game:"))
for i in range(0,w):
	m=random.choice(a)
	k=input("Your Choice:")
	if(m=="Rock" and k=="Scissor"):
		cp=cp+1
		print("ComputerChoice:",m)
	elif(m=="Rock" and k=="paper"):
		sp=sp+1
		print("ComputerChoice:",m)
	elif(m=="paper" and k=="Scissor"):
		sp=sp+1
		print("ComputerChoice:",m)
	elif(m=="paper" and k=="Rock"):
		cp=cp+1
		print("ComputerChoice:",m)
	elif(m=="Scissor" and k=="Rock"):
		sp=sp+1
		print("ComputerChoice:",m)
	elif(m=="Scissor" and k=="paper"):
		cp=cp+1
		print("ComputerChoice:",m)
	else:
		print("ComputerChoice:",m)
print("Computer:",cp)
print("player:",sp)
if(cp>sp):
	print("Computer Won")
elif(cp==sp):
	print("Draw")
else:
	print("You WON")