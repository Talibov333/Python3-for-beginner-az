



# while dongusu ile input dan alan deyerini herflerde girdikse sehv olmasi ucun
# except ValueError ist edirk.eger reqm girerse else bloku isleyecek

counter = 1 # dongunun nece defe donmesini bilmek ucun 1 deyr veririk
while True:
    try:
        age = int(input("enter your age: "))
    except ValueError:
        print("Please use numbers")
    else:
        print(f'you have got {age}')
        break
    finally:
        print(f'proqram {counter} defe isledi')
        counter += 1
        if counter > 5:
            print('siz 5 sansdan ist etdiniz')
            break
# sonucu if bize 5defe icaze verecek inputa sehv kod girmeye

# finally bir programda sehv ve duz olmasindam asli olmyrq isleyeck kodlari gost
# burda biz dongunun nece defe donmesi gostrmk ucun finnallyden ist edirik

"""   Pythonda programda istifadecinin etdityi sehvleri ona bildirmek
ucun try ve except den ist edilir
finally: kodu bir seyin programin veziyetinden asili olmayaraq isletmek istdiymz
kodlar ucn ist edilir daha cox
Umumiyetce programin duzgun islediyini
terminalda exit code 0 olanda duzgun islediyin gosterir
0 dan basqa deyer aldiqda demeli sehv var  mes:1,2,3
bir nece sehvle qarsilasma ehtimali ValueError
1) ValueError -- herfin yerine reqem reqemin yerine herf girende gorsedir
2) TypeError --  koddari duzgun yazmiyanda
3) ZeroDivisionError -- 0 bolmek olmaz erroru,
4) except:exception as exceptionObject:
     print('something',exceptionObject)
4cu sehv gosterme kodumuz butun sehvleri gostermek ucun ist edilir yeni
eger biz sehvin hardan olacagini gostermeden (gozlenilmez sehvleri)
 bu kod vasitesi ile py onu ozu
tapacag ve bir object kimi sehvi print vasitesi ile gosterecek

# ValueError: inputda alinan dyr eger herf yazlarsa excptdeki print isleyck
try:
     age = int(input('Yasinizi girin '))
     print(f' {age} yasiniz var ')
except ValueError:
    print('siz herflerden ist etmisiz')


# TypeError: bu misalda input alinan deyer rqmlerden ist olunsa bele onnan soraki
gelen print funksiyasinda age + yasiniz var sehvdir eslinde ya age,'yasiniz var'
yada f stringden ist edilmeli burda onun yazilis sehvi oldgunu gosterir


try:
     age = int(input('Yasinizi girin '))
     print(' age + yasiniz var ')
except ValueError:
    print('siz herflerden ist etmisiz')
except TypeError:
    print('kodlariniz sehvdi')

# ZeroDivisionError:  burda biz inputa 0 yazsaq maas/age  olduguna gora
0 bolmel xetasi alriq onuda except sonucu exceptde gosterik
try:
     age = int(input('Yasinizi girin '))
     print(age,'yasiniz var')
     maas = 1300
     pensiya = maas/age
     print('size dusen pensiya',pensiya)
except ValueError:
    print('siz herflerden ist etmisiz')
except TypeError:
    print('kodlariniz sehvdi')
except ZeroDivisionError:
    print('siz 0 girdiniz 0 a bolmek olmaz')


 """
