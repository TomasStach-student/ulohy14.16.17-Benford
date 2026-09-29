file=open("skok_do_dialky.txt","r")
krajiny={"SVE":0,"RUS":0,"FIN":0,"HUN":0,"USA":0,"FRA":0}
zoz_kraj=[]
dlzka=[]
max_skok=0

for line in file:
    line=line.strip()
    Meno,kod_krajiny,vykon1,vykon2,vykon3,vykon4,vykon5=line.split()
    zoz_kraj.append(kod_krajiny)
    krajiny[kod_krajiny]+=1
    dlzka.append(vykon1)
    dlzka.append(vykon2)
    dlzka.append(vykon3)
    dlzka.append(vykon4)
    dlzka.append(vykon5)
    for skok in dlzka:
        if int(skok)>int(max_skok):
            max_skok=skok
            max_meno=Meno


print(f"Najviac doskocil {max_meno} a to {max_skok}cm")
print("Zoznam krajin:",zoz_kraj)
print(krajiny)


