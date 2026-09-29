vstup="AKO SA MAS"
vystup=""

for symbol in vstup:
    if symbol==" ":
        vystup+="0"
    else:
        skupina=(ord(symbol)-65)//3+1
        poradie=(ord(symbol)-65)%3+1
        vystup+=(str(skupina)*int(poradie))

print(vystup)