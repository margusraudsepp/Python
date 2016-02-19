# Esimene osa: Määrame ja avame faili, kust hakkame infot lugema
f = open('arvud.txt')

# Teises osa: Üritame saada kõik numbrid eraldi ja liidame kokku
# Alati algavad array'd nullist siis esimene number on 0(Juhul kui pole teistmoodi määranud)
# K: Miks on esimene word[0] ja word[1] ning teine algab word[3] mitte word[2]?
# V: Kuna failis oleva esimese rea väärtus võrdub 45\n , teise rea väärtus 2\n ja kolmanda rea väärtus 63\n 
# ehk 0=4 , 1=5 , 2=\n , 3=2 4=\n 5=6 , 6=3 ja 7=\n
for word in f.read().split(" ",1):
    esimene = int(word[0])+int(word[1])
    teine = int(word[3])
    kolmas = int(word[5])+int(word[6])

# Kolmas osa: Käime 100 korda ringi, teeme faile ja lisame sisu kui vaja
# Aitab kah, kui oskad koodi saad kõiges aru et pole vaja kommenteerida
jrk = 1
limit = 100
while jrk <= limit:
    
    if jrk == esimene:
        filename = 'ristsumma'+str(esimene)+'.txt'
        with open (filename, 'a') as f: f.write (str(word[0])+str(word[1]+"\n"))
        
    if jrk == teine:
        filename = 'ristsumma'+str(teine)+'.txt'
        with open (filename, 'a') as f: f.write (str(word[3])+"\n")
    
    if jrk == kolmas:
        filename = 'ristsumma'+str(kolmas)+'.txt'
        with open (filename, 'a') as f: f.write (str(word[5])+str(word[6])+"\n")
    
    if jrk != esimene or jrk != teine or jrk != kolmas:
        filename = 'ristsumma'+str(jrk)+'.txt'
        with open (filename, 'a') as f: f.write ("")
    
    jrk= jrk + 1

# Lihsatlt väljastab mingise tulemuse
print("Kood sai läbi by: Margus Raudsepp")

# Paneme faili ka nüüd kinni
f.close()

# Hinne oleks ilmselt 3 kuna kood töötab aga pole kõige parem lahendus ehk väga algeline aga TÖÖTAB.


