#log-Liste erstellen mit Datum, Uhrzeit, IP, Anmeldeinformation, Ausschluss in  Tabelle
#Auswahlmöglichkeit von Zeitraum, erfolgreicher/fehlgeschlagener Anmeldung, Ausschluss
#Zuordnung von IP-Adresse nach Herkunft (Land) über whatismyip
#GUI mit Filterfunktion und Ausgabefeld

import datetime, argparse, random, pandas as pd, numpy as np

def random_dates(start, end, n):
    for i in range(n):
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        start_u = start.value//10**9
        end_u = end.value//10**9
        date = pd.to_datetime(np.random.randint(start_u, end_u), unit='s')
        log_in = random.randint(0,1)
        locked = random.randint(0, 10)
        with open("log_file.csv", "a") as log_file:
            if log_in == 1:
                log_file.write(f"{ip}, {date}, success, false, \n") 
            else:
                if locked == 1:
                    log_file.write(f"{ip}, {date}, failure, true, \n")
                else:
                    log_file.write(f"{ip}, {date}, failure, false, \n")
    print("Log file ready")
    
def table(start, end):
    with open("log_file.csv", "r") as f:
        df = pd.DataFrame(columns = ["ip", "Date", "Log-in", "Lock-out"])
        for row in f:
            df.append({"ip" : row.split(",")[0]},
                      {"date" : row.split(",")[1]},
                      {"log_in" : row.split(",")[2]},
                     # {"lock_out" : row.split(",")[3]}
                     ignore_index = True
                      )
            print(df)
            #print(ip, date, log_in) 
                   
        
        '''df = pd.DataFrame({"IP": log_data.readline,
                           "Date": log_data.readline})
        print(df)'''

start = pd.to_datetime('2024-01-01')
end = pd.to_datetime('2024-12-31')
n = 1000
#random_dates(start, end, n)
table(start, end)
