teststring = 'py is a wonderfull'
print(len(teststring))

# len funksiyasi stringin xarekter sayini gosterir
# len() funks ile hemcinin input meselelrinde ist edilir

teststring = 'py is a wonderfull'
print(teststring.upper())

# stringin xarexterlerini boyutmek ucun .upper() ist edlr
# stringi orijinalini deyisdirmir yalniz xarextrni deysdirir

teststring = 'Py is a wonderfull'
teststring = teststring.upper()
print(teststring)

# burda stringimiz orijinal sekilde deyisdirir yeni boyudur

teststring = 'py is A wondeRFull'
print(teststring.lower())

# strng xarekterini kiciltmek ucn

teststring = 'pY is A wondeRFull'
print(teststring.title())

# stringin yalniz ilk herfini boyudur


teststring = 'pY is a wonderfull'
print(teststring.find('w'))

# find() metodu ile biz w herfini necenci sirada oldugunu bilmek isteyirikse
# burda ilk gorduyu xarekterini gosterecek


teststring = 'pY is a wonderfull'
print(teststring.replace('wonderfull','high level programing'))

# replace xarekterleri deyisdirmek ucun ist edlr.
# neticesi wonderful yerine high level programing olacag

teststring = 'py is a wonderfull'
print('py' in teststring)
print('python' in teststring)

# bir xarekterin stringde olub olmasi ucun in  metodundan ist edilir
# 1-ci printde 'py' sozu oldugu ucun True donecek
# 2-cide ise 'python' sozunu tapmayacag ve False donecek

teststring = 'Py is a wonderfull Programing wonderfull'
print(teststring.count('P'))
print(teststring.count('wonderfull'))

# bir sozun (ve ya herfin,reqemin) strng ifadade nece defe ilendiyini bilmek
# ucun ist edilir netice 2 yeni 'wonderfull' sozu 2defe islenib