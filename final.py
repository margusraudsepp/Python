### ------------------------------------------- ### SISUKORD ### ------------------------------------------- ###
### LINE ~1      SISUKORD
### LINE ~13     UPDATES
### lINE ~20     IMPORT
### lINE ~24     FROM
### lINE ~29     GAME CONFIG
### lINE ~36     RAAM
### lINE ~38     FIRST RUN
### lINE ~54     RESULTS
### lINE ~59     GAME VASTAMINE
### lINE ~74     GAME
### lINE ~139   + TOP

### ------------------------------------------- ### UPDATE'S ### ------------------------------------------- ###
### 1. TOP 10 parimat tulemust suuremast väikemani
### 2. Lisab Tulemuse TOP'i
### 3. Nime lisamine
### 4. Õigeid ja valesi vastuseid

### -------------------------------------------- ### IMPORT ### -------------------------------------------- ###
import random


### --------------------------------------------- ### FROM ### --------------------------------------------- ###
from tkinter import *
from tkinter import ttk
from functools import partial

### ------------------------------------------ ### GAME CONFIG ### ----------------------------------------- ###
'''
skoor = 0
oiged = 0
valesid = 0
'''

### ------------------------------------------- ### FIRST RUN ### ------------------------------------------ ###

### --------------------------------------------- ### RAAM ### --------------------------------------------- ###

gameraam = Tk()
gameraam.title("Viktoriin - ")
gameraam.geometry("500x300")
#gameraam.eval('Ttk::PlaceWindow %s center' % gameraam.winfo_pathname(gameraam.winfo_id()))

silt = ttk.Label(gameraam, text="Nimi:")
silt.place(x=30, y=5)
 
nimi = ttk.Entry(gameraam)
nimi.place(x=70, y=5, width=150)
 
nupp = ttk.Button(gameraam, text="Alusta", command=lambda: startgame(0,0,8))
nupp.place(x=70, y=30, width=150)

### -------------------------------------------- ### RESULTS ### ------------------------------------------- ###
def results():
    print("ENDEX")
    nuppa.destroy()
    
### ---------------------------------------- ### GAME VASTAMINE ### ---------------------------------------- ###

def vastab(vastatav,vastus,oiged,valesid,mitmeskysimus):
    
    if vastatav == vastus:
        #print("oige")
        oiged = oiged + 1
    else:
        #print("vale")
        valesid = valesid + 1

    #mitmeskysimus = mitmeskysimus + 1 # Liidame siin juba juurde
    startgame(oiged,valesid,mitmeskysimus)

    
### --------------------------------------------- ### GAME ### --------------------------------------------- ###

def startgame(oiged,valesid,mitmeskysimus):

    maxkysimusi = 10 # Palju kysimusi esitab
   
    mitmeskysimus = mitmeskysimus + 1

    kysi = ttk.Label(gameraam, text="Küsimus "+str(mitmeskysimus)+"/"+str(maxkysimusi),font=('Helvetica', 20))
    kysi.place(x=10, y=60)
        
    kysimusid = random.randrange(1, maxkysimusi) # Default 1 - 10(maxkysimusi)
    
    def gennewkysimusid(): #Generate New Kysimus ID(line)
        kysimusid = random.randrange(1, maxkysimusi)

    # Vahel toimib, vahel mitte, üritab skipida küsimuse mis juba oli :D
    used = [1,3,6]
    if used.count(kysimusid) == 1:
        gennewkysimusid()
        #print("ReRoll "+str(kysimusid))
                       
    with open("kysi.txt") as fp:
        for i, line in enumerate(fp):         
            if i == kysimusid:                
                break
    
    
    gamesilt = ttk.Label(gameraam, text="Küsimus:")
    gamesilt.place(x=10, y=100)
        
    gamesilkysimus = ttk.Label(gameraam, text=line)
    gamesilkysimus.place(x=60, y=100)


    with open("vastus.txt") as fpv:
        for x, linev in enumerate(fpv):
            if x == kysimusid:
                break
    

    kysivastused = linev.split()

    nuppa = ttk.Button(gameraam, text=kysivastused[0], command=lambda: vastab(kysivastused[0],kysivastused[4],oiged,valesid,mitmeskysimus))
    nuppa.place(x=10, y=120, width=150)
    
    nuppb = ttk.Button(gameraam, text=kysivastused[1], command=lambda: vastab(kysivastused[1],kysivastused[4],oiged,valesid,mitmeskysimus))
    nuppb.place(x=160, y=120, width=150)

    nuppc = ttk.Button(gameraam, text=kysivastused[2], command=lambda: vastab(kysivastused[2],kysivastused[4],oiged,valesid,mitmeskysimus))
    nuppc.place(x=10, y=150, width=150)

    nuppd = ttk.Button(gameraam, text=kysivastused[3], command=lambda: vastab(kysivastused[3],kysivastused[4],oiged,valesid,mitmeskysimus))
    nuppd.place(x=160, y=150, width=150)

    def results():
        print("ENDEX")
        nuppa.destroy()

    if (mitmeskysimus >= maxkysimusi):
        gameraam.nuppa.pack_forget()
        results()

### ---------------------------------------------- ### TOP ### --------------------------------------------- ###

top10 = ttk.Label(gameraam, text="TOP 10")
top10.place(x=350, y=5)

topjrk = ttk.Label(gameraam, text="NR")
topjrk.place(x=350, y=20)

topname = ttk.Label(gameraam, text="Nimi")
topname.place(x=370, y=20)

topscore = ttk.Label(gameraam, text="Skoor")
topscore.place(x=420, y=20)

jooksevY = 40


#l = [6, 0, 2, 3, 1, 5, 4]
#print(sorted(l, reverse=True))

topnames = ""
topscores= ""

top10limit = 10

'''
from operator import itemgetter, attrgetter
data = [('kysivastused', 1123), ('blue', 321), ('red', 12), ('Emi', 222)]
juhan = sorted(data, key=itemgetter(1))
print (juhan)
print(juhan[0][0])
print(juhan[0][1])
'''

with open("top.txt") as top:
    for topx, topdataname in enumerate(top):

        
        if top10limit > topx:
            nameANDscore = topdataname.split()
            topnames = topnames + nameANDscore[0]
            topscores= topscores + nameANDscore[1]
        

        #topnames = topnames + nameANDscore[topx]
        #topscores= topnames + nameANDscore[topx+1]
        
            topjrk = ttk.Label(gameraam, text=topx+1)
            topjrk.place(x=350, y=jooksevY)
            
            topname = ttk.Label(gameraam, text=nameANDscore[0])
            topname.place(x=370, y=jooksevY)
            
            topscore = ttk.Label(gameraam, text=nameANDscore[1])
            topscore.place(x=420, y=jooksevY)
        

            jooksevY = jooksevY +20




