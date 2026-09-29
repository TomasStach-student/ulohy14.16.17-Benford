import csv

cisla={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,}
pocet=0

with open("data.csv",mode="r",encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["country"]=="China":
            cislo = str(row["weekly_count"])
            if cislo[0]!="0" and cislo[0]!="N":
                cislo=str(row["weekly_count"])
                index=cislo[0]
                cisla[index]+=1
                pocet+=1
for i in range(1,10):
    cisla[str(i)]=round(cisla[str(i)]/pocet*100,2)


print(cisla)