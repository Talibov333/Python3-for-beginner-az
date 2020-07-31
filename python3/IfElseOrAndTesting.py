# import random
# 
# default = random.randint(1, 100)
# print(default)
# for numb in range(5):
#     choose = int(input('enter a number: '))
#     if default > choose:
#         print('write big number')
#     elif default < choose:
#          print('write less number')
#     else:
#         print('conguralitions')
#         break
# if default != choose:
#     print('Sorry you didnt find!!! number is: ', default)
        
menu = """
Girdiyiniz ededler arasindaki reqemlerin toplanmasi
"""
print(menu)
numb1 = int(input('bir reqem girin: '))
numb2 = int(input('basqa reqem girin '))
topla = 0

for num in range(numb1,numb2+1):
    topla += num
    print('ededler arasindaki reqemlerin cemi',topla)
    
# bu misalda ilk once ne edecyimizi menu deyiskeni ile print etdik
# istifadeciden iki integer deyisken girmeyini istedik
# topla deyiskenine default olaraq 0 deyerini verdik
# for dongusu ile bu girilecek deyerlere gore dongu yaratdiq
# range ile dongu arasi donecek deyerleri verdik bu ist-den al-nan deyr
# ikinci girilen deyiskenide aid etmek ucun +1 yazdiq
# topla+=num for ucun metodumuzu bildirdik
# bunun basqa yazilisi topla = topla + num
# yuxarida topla deyiskenine 0 verdiyimiz ucun
# for dongusu oz deyiskenine(yeni num) gore alinan reqemleri toplayacaq
# ve sonda print for dongusunun altinda yazmadiq cunku
# ele yazsaq nece hesablandiqini yazacaq yeni ededler arasinda olan 
# reqemleri topladiqca deyerlerini gosterecek.