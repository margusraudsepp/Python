### ------------------------------------------- ### SISUKORD ### ------------------------------------------- ###
### LINE ~1      SISUKORD
### LINE ~13     UPDATES
### lINE ~20     IMPORT
### lINE ~24     FROM
### lINE ~30     FIRST RUN
### lINE ~57     RAAM
### lINE ~74     BEFORE GAME
### lINE ~108    GAME VASTAMINE
### lINE ~118    GAME
### lINE ~187    RESULT
### lINE ~222    TOP

### ------------------------------------------- ### UPDATE'S ### ------------------------------------------- ###
### 1. Mängu lõpetamine kui 10 küsimust täis ning suunab tagasi algusesse
### 2. 
### 3. 
### 4. 

### -------------------------------------------- ### IMPORT ### -------------------------------------------- ###
import random
import easygui

### --------------------------------------------- ### FROM ### --------------------------------------------- ###
from tkinter import *
from tkinter import ttk
from functools import partial
from operator import itemgetter, attrgetter #TOP'is aksutab seda

### ------------------------------------------- ### FIRST RUN ### ------------------------------------------ ###
# Checkime kas on olemas top,kysi ja vastus TXT
# Kysimused
try:
    with open('kysi.txt') as file:
        print("")    
except IOError as e:
        with open ("kysi.txt", 'a') as f:
            f.write ("Kysi1\nKysi2\nKysi3\nKysi4\nKysi5\nKysi6\nKysi7\nKysi8\nKysi9\nKysi10\nKysi11\nKysi12")
# Vastused
try:
    with open('vastus.txt') as file:
        print("")    
except IOError as e:
        with open ("avastus.txt", 'a') as f:
            f.write ("Vastus1 Vastus Vastus3 Vastus4 Vastus\nVastus1 Vastus2 Vastus Vastus4 Vastus\nVastus1 Vastus2 Vastus Vastus4 Vastus\nVastus1 Vastus2 Vastus3 Vastus Vastus\nVastus Vastus2 Vastus3 Vastus4 Vastus\nVastus1 Vastus2 Vastus3 Vastus Vastus\nVastus1 Vastus Vastus3 Vastus4 Vastus\nVastus1 Vastus2 Vastus Vastus4 Vastus\nVastus1 Vastus2 Vastus Vastus4 Vastus\nVastus1 Vastus2 Vastus3 Vastus Vastus\nVastus Vastus2 Vastus3 Vastus4 Vastus\nVastus1 Vastus2 Vastus3 Vastus Vastus")

# TOP
try:
    with open('top.txt') as file:
        print("")    
except IOError as e:
        with open ("top.txt", 'a') as f:
                     f.write ("Kala 12\nPehnmo 2\nEminem 12\nD12 3\nSnoop 7\nMianmi 2\nKusti 5\nTola 2\nSepo 3\nSavikas 7\nKakaka 10\nPaks 5\nNotsu 6\nKrooks 6\nLy 8\nMurka 4\nMadis 5\nHiie 9")

### --------------------------------------------- ### RAAM ### --------------------------------------------- ###

gameraam = Tk()
gameraam.title("Viktoriin ")
gameraam.geometry("700x400")

#def raam():
alustaLabel = ttk.Label(gameraam, text="Nimi:",font=('Helvetica', 16))
alustaLabel.place(x=55, y=10) 
#alustaKysiLabel = ttk.Label(gameraam, text="Kysimusi:",font=('Helvetica', 16))
#alustaKysiLabel.place(x=10, y=40)

alustaName = ttk.Entry(gameraam, text="Kolja", font=('Helvetica', 16))
alustaName.place(x=110, y=10, width=150)
#alustaKysiName = ttk.Entry(gameraam, text="10", font=('Helvetica', 16))
#alustaKysiName.place(x=110, y=40, width=150)
 
alustaButton = ttk.Button(gameraam, text="Alusta", command=lambda: beforegame())
alustaButton.place(x=110, y=70, width=150, height=30)

### ------------------------------------------ ### BEFORE GAME ### ----------------------------------------- ###
def beforegame():

    name = alustaName.get()
    #kysimusi = alustaKysiName.get()
    kysimusi = 10
    
    # Kontrollime, et nime topis poleks
    namestop = []
    with open("top.txt") as top:
        for topx, topdataname in enumerate(top):
            GetName = topdataname.split()
            namestop.append(GetName[0])
        
    # Palju kysimusi on
    totalkysimus = sum(1 for line in open('kysi.txt'))      
    
    if (kysimusi == ""):
        easygui.msgbox("Palun sisestage küsimuse number ", title="Viktoriin - Veateade")
    elif namestop.count(name) == 1:
        easygui.msgbox("Nimi " + name + " on juba kasutuses ", title="Viktoriin - Veateade")
    elif (int(kysimusi) <= 0):
        easygui.msgbox("Küsimusi number peab olemas suurem kui 0 ", title="Viktoriin - Veateade")
    elif (int(kysimusi) > int(totalkysimus)):
        easygui.msgbox("Küsimusi number ei sa suurem olla, kui " + str(totalkysimus), title="Viktoriin - Veateade")
    elif (name.isalpha() == False):
        easygui.msgbox("Nimi peab olema ÜKS sõna mis ei sisalda numbreid, tühkuid ega erilisi sümboleid", title="Viktoriin - Veateade")
    elif (len(name) > 10):
        easygui.msgbox("Nimi ei tohi olla pikem kui 10 tähte ", title="Viktoriin - Veateade")
    else:
        gameraam.title("Viktoriin - " + name)
        startgame(0,0,0)

### ---------------------------------------- ### GAME VASTAMINE ### ---------------------------------------- ###
def vastab(vastatav,vastus,oiged,valesid,mitmeskysimus):
    
    if vastatav == vastus:
        oiged = oiged + 1
    else:
        valesid = valesid + 1

    gameraam.gamesiltkysimus.place_forget() 
    startgame(oiged,valesid,mitmeskysimus)
    
### --------------------------------------------- ### GAME ### --------------------------------------------- ###

def startgame(oiged,valesid,mitmeskysimus):

    used = []

    # Varjame selle ära
    alustaLabel.place_forget()
    alustaName.place_forget()
    #alustaKysiLabel.place_forget()
    #alustaKysiName.place_forget()
    alustaButton.place_forget()
    #newgamebu.place_forget()

    maxkysimusi = 10 # Palju kysimusi esitab
    #maxkysimusi = alustaKysiName.get()

    totalkysimus = sum(1 for line in open('kysi.txt'))
   
    mitmeskysimus = mitmeskysimus + 1  
    
    gamekysi = ttk.Label(gameraam, text="Küsimus "+str(mitmeskysimus)+"/"+str(maxkysimusi),font=('Helvetica', 20))
    gamekysi.place(x=10, y=10)
        
    kysimusid = random.randrange(0, totalkysimus ) # Default 1 - 10(maxkysimusi)
    
    def gennewkysimusid(): #Generate New Kysimus ID(line)
        kysimusid = random.randrange(0, totalkysimus )

    # Vahel toimib, vahel mitte, üritab skipida küsimuse mis juba oli :D
    if used.count(kysimusid) == 1:
        gennewkysimusid()
        #print("ReRoll "+str(kysimusid))

    used.append(int(kysimusid))
    #print(used)

    
    with open("kysi.txt") as fp:
        for i, line in enumerate(fp):         
            if i == kysimusid:                
                break
    # Splitime siin küsimust          
    Jupitame = line.split("\\n")
    JupitameKysi = ""
    JupitameNR = 0
    try:
        while (Jupitame[JupitameNR]):
            JupitameKysi = JupitameKysi + "\n" + Jupitame[JupitameNR]
            JupitameNR = JupitameNR +1
    except:
        print("")
    
    gameraam.gamesiltkysimus = ttk.Label(gameraam, text=JupitameKysi,font=('Helvetica', 16),width=25)
    gameraam.gamesiltkysimus.place(x=10, y=50)

    with open("vastus.txt") as fpv:
        for x, linev in enumerate(fpv):
            if x == kysimusid:
                break
    
    kysivastused = linev.split()

    gameraam.nuppa = ttk.Button(gameraam, text=kysivastused[0], command=lambda: vastab(kysivastused[0],kysivastused[4],oiged,valesid,mitmeskysimus))
    gameraam.nuppa.place(x=10, y=247.5, width=150, height=40)
       
    gameraam.nuppb = ttk.Button(gameraam, text=kysivastused[1], command=lambda: vastab(kysivastused[1],kysivastused[4],oiged,valesid,mitmeskysimus))
    gameraam.nuppb.place(x=160, y=247.5, width=150, height=40)

    gameraam.nuppc = ttk.Button(gameraam, text=kysivastused[2], command=lambda: vastab(kysivastused[2],kysivastused[4],oiged,valesid,mitmeskysimus))
    gameraam.nuppc.place(x=10, y=287.5, width=150, height=40)

    gameraam.nuppd = ttk.Button(gameraam, text=kysivastused[3], command=lambda: vastab(kysivastused[3],kysivastused[4],oiged,valesid,mitmeskysimus))
    gameraam.nuppd.place(x=160, y=287.5, width=150, height=40)

    if (mitmeskysimus > maxkysimusi):
        gameraam.newgame = ttk.Button(gameraam, text="Mäng läbi")
        gameraam.newgame.place(x=10, y=10, width=300,height=180)
        result(oiged,valesid)

### -------------------------------------------- ### RESULT ### -------------------------------------------- ###
def result(oiged,valesid):

    WhatName = alustaName.get()
    CalcScore = oiged - valesid

    # Lisame tulemuse topi
    with open ("top.txt", 'a') as f: f.write ("\n" + WhatName + " " + str(CalcScore))

    tulemus = ttk.Label(gameraam, text="Teie tulemus on " + str(CalcScore),font=('Helvetica', 16))
    tulemus.place(x=75, y=250)

    CheckSpot = []
    with open("top.txt") as place:
        for spotx, NamesDataPlace in enumerate(place):
            PlaceData = NamesDataPlace.split()
            CheckSpot.append([PlaceData[0], int(PlaceData[1])])
    
    PlacList = sorted(CheckSpot, key=itemgetter(1), reverse=True) #itemgetter(0) nime järgi

    # Koha saamine
    KohtiTopis = sum(1 for line in open('top.txt'))
    WhatPlace = 0

    while (WhatPlace <= KohtiTopis):
        #print(PlacList[WhatPlace][0])
        if (WhatName == PlacList[WhatPlace][0]):
            koht = ttk.Label(gameraam, text="Teie koht on " + str(WhatPlace+1),font=('Helvetica', 16))
            koht.place(x=75, y=280)
            break        
        WhatPlace = WhatPlace + 1

    maketop() #Kuna see mingi skoor võib tulla TOP10 sisse siis reloadime nagu topi

    
### ---------------------------------------------- ### TOP ### --------------------------------------------- ###
# OSA 1 #Esialgne kujundus

def maketop():

    top10 = ttk.Label(gameraam, text="TOP 10",font=('Helvetica', 20))
    top10.place(x=350, y=10)

    topjrk = ttk.Label(gameraam, text="NR",font=('Helvetica', 16))
    topjrk.place(x=350, y=50)

    topname = ttk.Label(gameraam, text="Nimi",font=('Helvetica', 16))
    topname.place(x=380, y=50)

    topscore = ttk.Label(gameraam, text="Skoor",font=('Helvetica', 16))
    topscore.place(x=480, y=50)

    #OSA 2 #Sebime andmed array'sse
    topdata = []

    with open("top.txt") as top:
        for topx, topdataname in enumerate(top):
            nameANDscore = topdataname.split()
            topdata.append([nameANDscore[0], int(nameANDscore[1])]) 


    ## OSA 3 #Printime tulemuse suuremast väiksemani, limit 10
    toplimit = 10
    count = 0
    jooksevY = 75

    topdatadesc = sorted(topdata, key=itemgetter(1), reverse=True) #itemgetter(0) nime järgi

    while (count < toplimit):

        topjrk = ttk.Label(gameraam, text=count+1,font=('Helvetica', 16))
        topjrk.place(x=350, y=jooksevY)
        
        topname = ttk.Label(gameraam, text=topdatadesc[count][0],font=('Helvetica', 16))
        topname.place(x=380, y=jooksevY)

        topscore = ttk.Label(gameraam, text=topdatadesc[count][1],font=('Helvetica', 16))
        topscore.place(x=480, y=jooksevY)
        
        count = count + 1
        jooksevY = jooksevY + 25

maketop() # Prindime topi välja
