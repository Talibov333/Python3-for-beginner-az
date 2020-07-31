# sade bir hesablama kalkulyatoru 

desk = 'Mini Calculyator with Python3'
menu = """
1) Toplama
2) Cixma
3) Vurma
4) Bolme
5) Quvvet 
 """
print(desk)
print(menu)

print()

value = 1

while value == 1:
    choose = input('birini secin ve ya (q/Q)-ile cixis edin ')
    if choose == '1':
        print('toplama ucun ededleri daxil edin')
        print()
        numb1 = int(input('1ci reqem '))
        numb2 = int(input('2ci reqem '))
        print('Cavab =',numb1+numb2)
    elif choose == "2":
        print('cixma ucun ededleri daxil edin')
        print()
        numb1 = int(input('1ci reqem '))
        numb2 = int(input('2ci reqem '))
        print('Cavab =',numb1-numb2)
    elif choose == "3":
        print('vurma ucun ededleri daxil edin')
        print()
        numb1 = int(input('1ci reqem '))
        numb2 = int(input('2ci reqem '))
        print('Cavab =',numb1*numb2)
    elif choose == "4":
        print('bolme ucun ededleri daxil edin')
        print()
        numb1 = int(input('1ci reqem '))
        numb2 = int(input('2ci reqem '))
        print('Cavab =',numb1/numb2)
    elif choose == "5":
        print('quvvet ucun ededleri daxil edin')
        print()
        numb1 = int(input('1ci reqem '))
        numb2 = int(input('2ci reqem '))
        print('Cavab =',numb1**numb2)
    elif choose == "q" or choose == "Q":
        print("cixis etdiniz.tewekurler")
        value = 0
    else:
        print()
        print('seciminiz sehvdir!!')
        print('bu secimlerden birini edin', menu)
        
        
        

    
    
        
        
        
        
   
        
    
    
    
   
    
            
    
   
        

        
            
        
        
        
    
                 
    