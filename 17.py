vstup="AKO SA MAS"
vystup=""
policka={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
max_hodnota=0
max_cislo=""

for symbol in vstup:
    if symbol==" ":
        vystup+="0"
    else:
        skupina=(ord(symbol)-65)//3+1
        poradie=(ord(symbol)-65)%3+1
        vystup+=(str(skupina)*int(poradie))

for i in vystup:
    policka[str(i)]+=1
for k in policka:
    if policka[k]>max_hodnota:
        max_hodnota=policka[k]
        max_cislo=k

print(max_cislo,":",max_hodnota)
print(vystup)
