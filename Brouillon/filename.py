vaccination = "vacsi-tot-reg-2022-06-15-19h00.csv"
ligneCount= 0
cours={}
with open (vaccination) as f:
    for ligne in f:
        if (ligneCount >=1):
            x=ligne.replace('"', '').split(";")
            if not '-' in x:
               
                    print(x[1])
        ligneCount += 1
