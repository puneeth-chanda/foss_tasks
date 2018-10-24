import random
cap=["A1b4Mk","N1an56G","V1aj7M"]
m=random.choice(cap)
total=0
print("Welcome to Stupid Stores")
name=input("Can i know your name plz?:")
print("hello",name,"What do you want to buy, we have all the necesssites u need :")
print("select anyone of the following:")
print("A:Sports")
print("1. Football:")
print("    (a)Nike:1400")
print("    (b)Adidas:1200")
print("    (c)puma:1500")
print("2. Rackets")
print("   (a)Yonex:500")
print("   (b)Hand:1000")
print("   (c)Shivalik:800")
print("B:Sanitary")
print("1. Soaps:")
print("    (a)Lux:40")
print("    (b)Dettol:120")
print("    (c)Fassak:50")
print("2. Shampoo")
print("   (a)patanjali:500")
print("   (b)panteen:100")
print("   (c)head and shoulder:80")
print("C:Stationary")
print("1. Pens:")
print("    (a)Nippo:10")
print("    (b)Reynolds:20")
print("    (c)Parker:100")
print("2. Pencils")
print("   (a)apsara:5")
print("   (b)natraj:10")
print("   (c)classmate:8")
print("D:Electronics")
print("1. Mobiles:")
print("    (a)Oppo:10000")
print("    (b)Viv0:20000")
print("    (c)Moto:10000")
print("2. Laptops")
print("   (a)Lg:500000")
print("   (b)Toshiba:100000")
print("   (c)Lenovo:80000")
print("if u want to leave type checkout")
while(True):
    k=input()
    if(k=="A1a"):
        total=total+1400
    elif(k=="A1b"):
        total=total+1200
    elif(k=="A1c"):
        total=total+1500
    elif(k=="A2a"):
        total=total+500
    elif(k=="A2b"):
        total=total+1000
    elif(k=="A2c"):
        total=total+800
    elif(k=="B1a"):
        total=total+40
    elif(k=="B1b"):
        total=total+120
    elif(k=="B1c"):
        total=total+50
    elif(k=="B2a"):
        total=total+500
    elif(k=="B2b"):
        total=total+100
    elif(k=="B2c"):
        total=total+80
    elif(k=="C1a"):
        total=total+10
    elif(k=="C1b"):
        total=total+20
    elif(k=="C1c"):
        total=total+100
    elif(k=="C2a"):
        total=total+5
    elif(k=="C2b"):
        total=total+10
    elif(k=="C2c"):
        total=total+8
    elif(k=="D1a"):
        total=total+10000
    elif(k=="D1b"):
        total=total+20000
    elif(k=="D1c"):
        total=total+10000
    elif(k=="D2a"):
        total=total+50000
    elif(k=="D2b"):
        total=total+100000
    elif(k=="D2c"):
        total=total+80000
    elif(k=="checkout"):
        print("Type the following Captcha:",m)
        while(True):
            us=input()
            if(us==m):
                print("your total is:",total)
                print("Thank you for shopping with us")
                print("do you have a coupun for discount sir???")
                cou=input()
                if(cou=="yes"):
                    print("your payable amount is:",(-(total)*4/100)+total)
                else:
                    print("your payable amount is:",total)
                break
            else:
                print("wrong Captcha")
    else:
        print("Please,Choose from above options")