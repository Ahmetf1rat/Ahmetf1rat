#1'den 100 kadar 5'in katları dışındakiler yazdıran program..



a=1

while a<=100:
    print("Güncel sayi :",a)
    a =a+1
    if a%5==0:
        a=a+1
        continue
print("İşlem başarıyla tamamlanddı..")
