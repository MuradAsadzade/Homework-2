
# Task1
# a=int(input("Number:"))
# if a%3==0 and a%7==0 and a%8==0:
#     print("Yes")
# else:
#     print("No")

# Task2
# kod=input("Password:")
# if len(kod)==10 and kod[0:3].isupper and kod[3:].isdigit  :
#     print("Yes")
# else:
#     print("No")


# Task3
# pul=int(input("Alinan borc:"))
# borc=1
# if pul<2000 and pul>500000:
#     print("Borc verilmir")
# elif pul<10000:
#     borc=pul*1.05
#     print(borc)
# elif pul<50000:
#     borc=pul*1.04
#     print(borc)
# elif pul<200000:
#     borc=pul*1.03
#     print(borc)
# elif pul<500000:
#     borc=pul*1.02
#     print(borc)

# Task4
# a=input("Password:")
# say=0
# boyuk=0
# kicik=0
# herf=0
# reqem=0
# if 8<=len(a)<=40:
#     for i in range(0,len(a)):
#         if a[i].isalnum:
#             say+=1
#         if a[i].isupper:
#             boyuk+=1
#         if a[i].islower:
#             kicik+=1
#         if a[i].isdigit:
#             reqem+=1
#         if a[i].isalpha:
#             herf+=1
#     if say==len(a) and boyuk>=1 and kicik>=1 and herf>=1 and reqem>=1:
#         print("Mumkundur")
#     else:
#         print("Mumkun deyil")
# else:
#         print("Mumkun deyil")


# Task5

# Task6
# a=int(input("Eded:"))
# hasil=1
# for i in range(1,a+1):
#     hasil*=i
# print(hasil)

# Task7
# sentence=input("Cumle:")
# heca=0
# for i in range(0,len(sentence)):
#     if sentence[i]=='a' or sentence[i]=='e' or sentence[i]=='u' or sentence[i]=='i' or sentence[i]=='o':
#          heca+=1
# print(f'Hecalarin sayi:{heca}')

# Task8
# a=input("Number:")
# say=0
# if len(a)==13 and a[:4]=="+994":
#     for i in range(4,len(a)):
#         if  a[i].isalpha:
#             print("{} reqem deyil",format(a[i]))
#             break
#         else:
#             say+=1
# else:
#     print("Mumkun deyil")
# if say==9:
#     print("Nomrede problem yoxdu")
            
# Task9
# a='123456789'
# for i in range(len(a)-1,0,-1):
#     print(f'{a[i]} saniye')
# print("Vaxt bitdi!")

# Task10
# a=int(input("Eded:"))
# for i in range(2,a):
#     check=True
#     for j in range(2,i):
#         if i%j==0:
#             check=False
#     if a%i==0 and check==True:
#         print(i)

# Task11
a=0
b=1
c=int(input("Eded:"))
print(a,end=" ")
while b<=c:
    a,b=b,a+b
    if b<=c:
        print(b,end=" ")