# and , or 
# iki ve daha artiq ifadanin deyerlerinin eyni olmasi ve onu elave kod
# sekilinde yazmamaqdan otru and kodundan ist edilir 

hot = False
cold = True
sunny = False
snow = True

if hot and sunny:
    print('The wheather is hot')
    print('also very sunny day')
elif cold and snow:
    print('The wheather is very cold')
    print('It,s snowing|take warm clothes')
else:
    print('The wheather is normal.| not sunny and cold')


# and 





print()  # bosduq qoyur

hot = True
cold = False
sunny = True
snow = False


if hot and not sunny:
    print('The wheather is hot')
    print('also very sunny day')
elif cold and not snow:
    print('The wheather is very cold')
    print('It,s snowing|take warm clothes')
else:
    print('The wheather is normal.| not sunny and cold')
print('have a good day')

# and not birlesmesi iki deyerden biri false olsa bele onu qebul edecek
# burda 1ci ifadeni gosterecey
#  (sunny-nin deyeri False olmasina baxmayaraq ) 


print()  # bosduq qoyur

hot = True
cold = False
sunny = True
snow = False


if hot or sunny:
    print('The wheather is hot')
    print('also very sunny day')
elif cold or snow:
    print('The wheather is very cold')
    print('It,s snowing|take warm clothes')
else:
    print('The wheather is normal.| not sunny and cold')
print('have a good day')

# iki deyerden biri true olarsa neticeni gostercey


print()  # bosduq qoyur

hot = False
cold = False
temp = 5

if temp > 30:
    hot = True
elif temp < 10:
    cold = True
    if hot:
       print('The wheather is very hot')
    elif cold:
       print('the wheather is cold')
else:
    print('It is a warm day')

# temp hansi deyer olacagsa bizim verdiyimiz dereceden
# < ve > olacagsa ona gore  isleyecek.
# hemcinin verdiyimiz deyerin ona ve ondan boyuk ve ya kicik 
# olmasi ucun >= , <= olur
# yalniz verilen deyere beraber olacagi halda  ==

print()
# misal 1 girilen deyere gore havanin nece olamgini gosterek

