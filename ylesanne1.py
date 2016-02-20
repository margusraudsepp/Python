# Impordime decimal sest seda läheb summa arvutamisel vaja.
import decimal

# Määrame ja avame faili, paneme tulemuse stringi ja sulgeme faili.
f = open("arvud.txt")
arvud = f.readlines()
f.close()

# Teeme nüüd 100 tühja faili
jrk = 1         # Mis numbrist algab while, jrk on järjekorranumber.
jrklimit = 100  # Hetkel limit 10 kuna result liiga pikk poleks.

while jrk <= jrklimit:
    filename = 'ristsumma'+str(jrk)+'.txt'
    with open (filename, 'a') as f: f.write ("")

# Et while igavesti ringi ei käiks siis liidame juurde ühe.
    jrk = jrk + 1

# Sama asi nagu jrk aga teises while's
arve = 0 

# Loeb stringi arvud, et mitu erinevat tulemust seal on.
arvelimit = len(arvud) 

# Käime niikaua ringi kui tulemus on olemas
while arve < arvelimit:
    
# Teeme numbrid korda ehk eemaldame \n või muu sõna ehk see käsklus otsib reast kõik numbrid välja.
# Kui see string(arvud[0]) ei sisaldab numbrit siis jookseb see kokku.
    ilmaenita = int(''.join(ele for ele in arvud[arve] if ele.isdigit() or ele == '.'))

# Lisab saaduda arvud listi.
    listenita = list(str(ilmaenita))

# Liidab listis olevad arvud.
# NB! Kui listis on asi mis pole arv siis jookseb see kokku.
    failinumber = int(sum(decimal.Decimal(x) for x in listenita))

# Lisame faili infot.
    filename = 'ristsumma'+str(failinumber)+'.txt'
    with open (filename, 'a') as f: f.write (arvud[arve])

# Et while igavesti ringi ei käiks siis liidame juurde ühe.
    arve = arve + 1;

# Siin lihtsalt väljastame mingi lause.
print("Tehti " + str(jrk-1) + " faili ja lisati " + str(arvelimit) + " tulemust.")
