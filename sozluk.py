sozluk = {'Ad':"Ahmet","Yas":"25","Okul":"Universite"}


print(sozluk['Ad'])
print(sozluk['Yas'])
print(sozluk['Okul'])

sozluk['Ad']="Ali"  #sözlük içinde tanımı değiştirebiliyoruz..
print(sozluk['Ad'])

del sozluk['Ad']   #sözlüğümüzü yaştan başlatarak yazdıracak..
sozluk.clear()  # sözlüğün içini temizliyor(içini boş gösteriyor..)..
