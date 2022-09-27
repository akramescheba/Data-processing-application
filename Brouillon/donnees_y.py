import pandas as pd
import numpy as np
import statistics


vaccination = "vacsi-s-a-reg-2022-06-22-19h00.csv"

ligneCount= 0

with open (vaccination) as f:
    for ligne in f:
        if (ligneCount >=1):
        
            x= (ligne).replace('"', '').split(";")
            if not '-' in x:
                ligneCount += 1
                print(x[2])
          


