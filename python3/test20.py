"""
      listden alan int datanin kubunu tapib type ifade kimi print etmk
listtest adnda list yaradiriq
typla cevirmek ucn resultlist adnda deyskn yaradiriq ve icrsnde for dongusu ile
 listtestden datalari item kimi qbl edib pow() funksi ile item-in kubunu(item,3)
 ve itemin ozunu donguye salib daha sonra print edirk


[(2, 8), (3, 27), (4, 64), (6, 216), (7, 343), (8, 512)]
"""

listtest = [2,4,8,6,7,3]
listtest.sort()  # bu listimizde olan melumtlarin kicikden boyuye duzmek ucndu
resultlist = [(item, pow(item,3)) for item in listtest]
print(resultlist)
