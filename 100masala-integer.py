# 1-masala
# l=int(input("metrni kiriting"))
# metr=l*100
# print("to`liq metrlar= ", metr)

# 2-masala
# m=int(input("kilogramni kiriting"))
# tonna=m//1000
# print("to`liq tonnalar= " , tonna)

# 3-masala
# a=int(input("baytni kiriting"))
# Kb=a//1024
# print("to`liq Kb=" , Kb)

#4-masala
# a=int(input("a sonini kiriting"))
# b=int(input("b sonini kiriting"))
# a>b
# a,b>0
# print("necha marta joylashtirish mumkin: ", a//b)

# 5-masala
# a=int(input("a sonini kiriting"))
# b=int(input("b sonini kiriting"))
# a>b
# a,b>0
# print("joylashmagan qismi=",a%b)

#6-masala
# a = int(input("2 xonali son kiriting"))
# print(a//10, a%10)

# 7-masala
# a=int(input("2 xonali son kiriting"))
# b=a//10
# c=a%10
# a= b,c
# print(b+c)

# 8-masala
# a=int(input("2 xonali son kiriting"))
# b=a//10
# c=a%10
# a= b,c
# print(c,b)

# 9-masala
# a=int(input("3 xonali son kiriting"))
# print(a//100)

# 10-masala
# a=int(input("3 xonali sonni kiriting"))
# b=a//100
# c=a//10%10
# d=a%100%10
# a=b,c,d
# print(d)
# print(c)

# 11-masala
# a=int(input("3 xonali sonni kiriting"))
# b=a//100
# c=a//10%10
# d=a%100%10
# a=b,c,d
# print(b+c+d)

# 12-masala
# a=int(input("3 xonali sonni kiriting"))
# b=a//100
# c=a//10%10
# d=a%100%10
# a=b,c,d
# print(d, c, b)

# 13-masala
# a=int(input("3 xonali sonni kiriting"))
# b=a//100
# c=a//10%10
# d=a%100%10
# a=b,c,d
# print(c, d, b)

# 14-masala
# a=int(input("3 xonali sonni kiriting"))
# b=a//100
# c=a//10%10
# d=a%100%10
# a=b,c,d
# print(d,b,c)

# 15-masala
# a=int(input("3 xonali sonni kiriting"))
# b=a//100
# c=a//10%10
# d=a%100%10
# a=b,c,d
# print(c,b,d)

# 16-masala
# a=int(input("3 xonali sonni kiriting"))
# b=a//100
# c=a//10%10
# d=a%100%10
# a=b,c,d
# print(b,d,c)

# 17-masala

# a=input("4 xonali son kiriting")
# if len(a)==4:
#     print(int(a)%1000//100)
# else:
#     print("faqat 4 xonali son kiriting")

#18-masala
# a=input("4 xonali son kiriting")
# if len(a)==4:
#     print(int(a)//1000)
# else:
#     print("faqat 4 xonali son kiriting")

# 19-masala
# n=int(input("n-sekundni kiriting"))
# a=n/60
# print("kun boshidan", a, "minut")

# 20-masala
# n=int(input("sekundni kiriting"))
# a=n/3600
# print("kun boshidan", a, "soat")

# 21-masala
# n=int(input("sekundni kiriting"))
# a=n//60
# b=n%60
# print("kun boshidan", a, "minut", "va",b, "sekund vaqt o`tgan" )

# 22-masala
# n=int(input("sekundni kiriting"))
# a=n//3600
# b=n%60
# print("kun boshidan boshlab", a, "soat", b, "sekund o`tgan")

# 23-masala
# n=int(input("sekundni kiriting"))
# a=n//3600
# b=n//60
# c=n%60
# print("kun boshidan boshlab", a, "soat", b, "minut va", c, "sekund o`tgan")

# 24-masala
# kun=int(input("kunni kiriting"))
# hafta=["yakshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]
# boshlanish=1
# topish=(kun+boshlanish-1)%7
# print(f"{kun} -raqam  haftaning {hafta[topish]} kuniga teng")

# 25-masala
# kun=int(input("kunni kiriting"))
# hafta=["yakshanba", "dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba"]
# boshlanish=4
# topish=(kun+boshlanish-1)%7
# print(f"{kun}-sana haftaning {hafta[topish]}  kuniga to`g`ri keladi")

# 26-masala
# kun=int(input("sanani kiriting"))
# hafta=["dushanba", "seshanba", "chorshanba", "payshanba", "juma", "shanba", "yakshanba"]
# boshlanish=2
# topish=(kun+boshlanish-1)%7
# print(f"{kun}-sanasi haftaning {hafta[topish]} kuniga to`g`ri keladi")