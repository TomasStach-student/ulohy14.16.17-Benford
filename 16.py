file=open("mena_zamestnancov.txt","r")
vysledok=open("mena_zamestnancov_zorad.txt","w")
zoznam=[]
mena=[]
priezviska=[]
pocitadlo=0
najdlsie_meno=0
najdlsie_priezvisko=0

for riadok in file:
    riadok=riadok.strip()
    zoznam.append(riadok)

for meno in zoznam:
    if pocitadlo<len(zoznam)//2:
        mena.append(meno)
        pocitadlo+=1
        if najdlsie_meno<len(meno):
            najdlsie_meno=len(meno)
    else:
        priezviska.append(meno)
        if najdlsie_priezvisko<len(meno):
            najdlsie_priezvisko=len(meno)

for i in range(len(mena)):
    medzera = " "*(najdlsie_meno-len(mena[i])+1)
    vysledok.write(f"{mena[i]}{medzera}{priezviska[i]}\n")
vysledok.write(f"\nNajdlsie meno: {najdlsie_meno} \nNajdlhsie priezvisko: {najdlsie_priezvisko}")
