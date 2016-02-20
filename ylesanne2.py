# Seda koodi ma ei viitsinud kommenteerida
andmed = [{'a':3, 'b':47, 'c':6},{'c':21, 'd':3},{'b':7, 'd':3,'x':12},{'y':23,'a':2}]
#tahed = ['a','b','c','d','x','y'] # Tähestiku järgi
tahed = ['b','c','a','d','x','y'] # Siia tuleks teha, et saab need tähed ise kätte stringis andmed

kogustring = "["+str(tahed)+",\n["

jrk = 0
jrklimit = len(andmed)
jrktaht = 0
jrktahtlimit = len(tahed)
taht = ""

while jrk < jrklimit:
  
    taht = tahed[jrktaht]

    onkoma = ","
    if jrktaht == jrktahtlimit-1: onkoma = ""

    addspace = "" #NULL
    
    try:
        if int(andmed[jrk][taht]) < 10:
            addspace = "   " #KOLM
        elif int(andmed[jrk][taht]) < 100:
            addspace = "  " #KAKS
        
        kogustring = str(kogustring) + addspace + str(andmed[jrk][taht]) + onkoma
    except:
        addspace = "   " #KOLM
        kogustring = kogustring + addspace + "0" + onkoma


    jrktaht = jrktaht + 1

    if jrktaht == jrktahtlimit:
        jrktaht = 0
        jrk = jrk + 1
        if jrk == jrklimit:
            kogustring = kogustring + "]]"
        else:
            kogustring = kogustring + "],\n["





print(kogustring)




