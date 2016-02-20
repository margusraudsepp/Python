# Esimene osa ehk  määrame faili
f = open('arvud.txt')

# Teine osa üritame saada kõik numbrid eraldi ja liidame
for word in f.read().split(" ",1):
    esimene = int(word[0])+int(word[1])
    teine = int(word[3])
    kolmas = int(word[5])+int(word[6])

#Kolmas osa käime 100 korda ringi, teeme faili ja lisame sisu kui vaja
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

print("Kood sai läbi by: KylaPoiss")
f.close()


