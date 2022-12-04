from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
import webbrowser
typkonsoli=['NES','Genesis','SNES','Saturn','PS1','N64','Dreamcast','PS2','Xbox','GameCube','Xbox360','PS3','Wii','WiiWare','GB','GBC','GBA','DS','PSP']
print('1: NES')
print('2: Sega Genesis/Mega Drive')
print('3: SNES')
print('4: Sega Saturn')
print('5: PS1')
print('6: Nintendo 64')
print('7: DreamCast')
print('8: PS2')
print('9: Xbox')
print('10: GameCube')
print('11: Xbox360')
print('12: PS3')
print('13: Wii')
print('14: WiiWare')
print('15: GameBoy')
print('16: GameBoy Color')
print('17: GameBoy Advance')
print('18: DS')
print('19: PSP')
while True:
    nazwakonsoli = int(input("Type number of console: "))
    nazwakonsoli=nazwakonsoli-1
    if nazwakonsoli<0 or nazwakonsoli>18:
        print("Wrong ID, try again")
    else:
        break


gra = str(input("Type game title (at least 3 characters): "))

if len(gra)<3:
    print("Too short")
    input("Press ENTER/RETURN to quit")
    quit();
if gra[0]==" " or gra[0]=="0" or gra[0]=="1" or gra[0]=="2" or gra[0]=="3" or gra[0]=="4" or gra[0]=="5" or gra[0]=="6" or gra[0]=="7" or gra[0]=="8" or gra[0]=="9":
    print("Error")
    input("Press ENTER/RETURN to quit")
    quit();

if gra[0].isalpha()==True:
    req = Request(
        url='https://vimm.net/vault/'+typkonsoli[nazwakonsoli]+'/'+gra[0].upper(), 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
else:
    print("Error")
    input("Press ENTER/RETURN to quit")
    quit()
webpage = urlopen(req).read()
webpagee = webpage
soup = BeautifulSoup(webpagee, 'html.parser')
n=0
linki = []
tytulygier = []
try:
    while True:
        result = soup.find_all(class_="even")[n].get_text()
        realwynik = str(result).lower()
        if gra.lower() in realwynik.lower():
            stronawynik = str(soup.find_all(class_="even")[n])
            stronawynik = stronawynik[stronawynik.find("href="):]
            stronawynik = stronawynik[0:stronawynik.find(">")]
            if "onmouseover" in stronawynik:
                stronawynik = stronawynik[0:stronawynik.find(" ")]
            #print(stronawynik)
            stronawynik = stronawynik[6:]
            stronawynik = stronawynik[:-1]
            linki.extend(['https://vimm.net'+stronawynik])
            tytulygier.extend([result])
            #sys.quit();
            
        n=n+1
        
except:
    n=0
    try:
        while True:
            result = soup.find_all(class_="odd")[n].get_text()
            realwynik = str(result).lower()
            if gra.lower() in realwynik.lower():
                stronawynik = str(soup.find_all(class_="odd")[n])
                stronawynik = stronawynik[stronawynik.find("href="):]
                stronawynik = stronawynik[0:stronawynik.find(">")]
                if "onmouseover" in stronawynik:
                    stronawynik = stronawynik[0:stronawynik.find(" ")]
                #print(stronawynik)
                stronawynik = stronawynik[6:]
                stronawynik = stronawynik[:-1]
                linki.extend(['https://vimm.net'+stronawynik])
                tytulygier.extend([result])
                
                
            n=n+1
    except:
            print("Done searching")

if len(linki)==0:
    print("No games found. Press ENTER/RETURN to quit")
    input()
    quit()
elif len(linki)>1:
    n=0
    dlugosctabeli = len(linki)
    while n<dlugosctabeli:
        print(str(n+1)+": "+tytulygier[n])
        n=n+1
    wybranagra=int(input("Type number to open the game: "))
    wybranagra=wybranagra-1
    if wybranagra<0 or wybranagra>len(linki):
        print("Wrong number")
        quit()
    webbrowser.open(str(linki[wybranagra]))
    
    
else:
    print("Only 1 game found")
    webbrowser.open(str(linki[0]))
    
    


