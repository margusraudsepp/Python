### ------------------------------------------- ### SISUKORD ### ------------------------------------------- ###
### LINE ~1      SISUKORD
### lINE ~5      IMPORT
### lINE ~9      FROM
### lINE ~14     GAME CONFIG
### lINE ~21     FIRST RUN
### lINE ~25     GAME VASTAMINE
### lINE ~40     GAME
### lINE ~91     RAAM
### lINE ~108    TOP

### -------------------------------------------- ### IMPORT ### -------------------------------------------- ###
import random

### --------------------------------------------- ### FROM ### --------------------------------------------- ###
from tkinter import *
from tkinter import ttk

### ------------------------------------------ ### GAME CONFIG ### ----------------------------------------- ###
skoor = 0
oiged = 0
valesid = 0


### ------------------------------------------- ### FIRST RUN ### ------------------------------------------ ###


### ---------------------------------------- ### GAME VASTAMINE ### ---------------------------------------- ###

def vastab(vastatav,vastus):
    if vastatav == vastus:
        print("oige")
        #skoor = skoor + 1
        #oiged = oigeid = + 1
    else:
        print("vale")
        #valesid = valesid + 1

    startgame()

    
### --------------------------------------------- ### GAME ### --------------------------------------------- ###
def startgame():
    
    
    kysimusid = random.randrange(1, 6) # Default
    
    def gennewkysimusid(): #Generate New Kysimus ID(line)
        kysimusid = random.randrange(1, 6)

    # Vahel toimib, vahel mitte
    used = [1,3,6]
    if used.count(kysimusid) == 1:
        gennewkysimusid()
        print("Reroll"+str(kysimusid))
                       
    with open("kysi.txt") as fp:
        for i, line in enumerate(fp):         
            if i == kysimusid:                
                break
    
    
    gamesilt = ttk.Label(gameraam, text="Küsimus:")
    gamesilt.place(x=10, y=80)
        
    gamesilkysimus = ttk.Label(gameraam, text=line)
    gamesilkysimus.place(x=60, y=80)


    with open("vastus.txt") as fpv:
        for x, linev in enumerate(fpv):
            if x == kysimusid:
                break
    

    kysivastused = linev.split()

    nuppa = ttk.Button(gameraam, text=kysivastused[0], command=lambda: vastab(kysivastused[0],kysivastused[4]))
    nuppa.place(x=10, y=100, width=150)
    
    nuppb = ttk.Button(gameraam, text=kysivastused[1], command=lambda: vastab(kysivastused[1],kysivastused[4]))
    nuppb.place(x=160, y=100, width=150)

    nuppc = ttk.Button(gameraam, text=kysivastused[2], command=lambda: vastab(kysivastused[2],kysivastused[4]))
    nuppc.place(x=10, y=130, width=150)

    nuppd = ttk.Button(gameraam, text=kysivastused[3], command=lambda: vastab(kysivastused[3],kysivastused[4]))
    nuppd.place(x=160, y=130, width=150)
    


### --------------------------------------------- ### RAAM ### --------------------------------------------- ###

gameraam = Tk()
gameraam.title("Viktoriin - ")
gameraam.geometry("500x300")
#gameraam.eval('Ttk::PlaceWindow %s center' % gameraam.winfo_pathname(gameraam.winfo_id()))

silt = ttk.Label(gameraam, text="Nimi:")
silt.place(x=30, y=5)
 
nimi = ttk.Entry(gameraam)
nimi.place(x=70, y=5, width=150)
 
nupp = ttk.Button(gameraam, text="Alusta", command=startgame)
nupp.place(x=70, y=30, width=150)

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

'''
#l = [6, 0, 2, 3, 1, 5, 4]
#print(sorted(l, reverse=True))

topnames = ""
topscores= ""

top10limit = 10


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



