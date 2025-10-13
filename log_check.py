import datetime, argparse, random, pandas as pd, numpy as np

def new_log_file(start, end, n):
    n = int(n)
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

def log_in_check(start, end):
    with open("log_file.csv", "r") as f:
        d = {"ip" : [], "Date" : [], "Log-in" : [], "Lock-out" : []}
        df = pd.DataFrame(data=d, index=[])
        for row in f:
            ip = row.split(',')[0]
            date = row.split(',')[1].strip(" ")
            log_in = row.split(',')[2].strip(" ")
            lock_out = row.split(',')[3].strip(" ")
            if f"{start}" < date < f"{end}":
                if log_in == "success":
                    d_row = {"ip" : ip, "Date" : date, "Log-in" : log_in, "Lock-out" : lock_out}
                    df = df._append(d_row, ignore_index = True)
                else:
                    pass
        print(df)
        df.to_excel("result.xlsx", index=False)

def lock_out_check(start, end):
    with open("log_file.csv", "r") as f:
        d = {"ip" : [], "Date" : [], "Log-in" : [], "Lock-out" : []}
        df = pd.DataFrame(data=d, index=[])
        for row in f:
            ip = row.split(',')[0]
            date = row.split(',')[1].strip(" ")
            log_in = row.split(',')[2].strip(" ")
            lock_out = row.split(',')[3].strip(" ")
            if f"{start}" < date < f"{end}":
                if lock_out == "true":
                    d_row = {"ip" : ip, "Date" : date, "Log-in" : log_in, "Lock-out" : lock_out}
                    df = df._append(d_row, ignore_index = True)
                else:
                    pass
        print(df)
        df.to_excel("result.xlsx", index=False)

def date_check(start, end):
    with open("log_file.csv", "r") as f:
        d = {"ip" : [], "Date" : [], "Log-in" : [], "Lock-out" : []}
        df = pd.DataFrame(data=d, index=[])
        for row in f:
            ip = row.split(',')[0]
            date = row.split(',')[1].strip(" ")
            log_in = row.split(',')[2].strip(" ")
            lock_out = row.split(',')[3].strip(" ")           
            if f"{start}" < date < f"{end}":
                d_row = {"ip" : ip, "Date" : date, "Log-in" : log_in, "Lock-out" : lock_out}
                df = df._append(d_row, ignore_index = True)
            else:
                pass
        print(df)
        df.to_excel("result.xlsx", index=False)

def ip_check(start, end, searched_ip):
    with open("log_file.csv", "r") as f:
        d = {"ip" : [], "Date" : [], "Log-in" : [], "Lock-out" : []}
        df = pd.DataFrame(data=d, index=[])
        for row in f:
            ip = row.split(',')[0]
            date = row.split(',')[1].strip(" ")
            log_in = row.split(',')[2].strip(" ")
            lock_out = row.split(',')[3].strip(" ")
            if f"{start}" < date < f"{end}":
                if ip == searched_ip:
                    d_row = {"ip" : ip, "Date" : date, "Log-in" : log_in, "Lock-out" : lock_out}
                    df = df._append(d_row, ignore_index = True)
        print(df)
        df.to_excel("result.xlsx", index=False)

def main():
    parser = argparse.ArgumentParser(description="Create or Check Log-In data")
    parser.add_argument("-s", "--start", nargs="?", default="2020-01-01 00:00:00", help="Define start date (format: 'YYYY-MM-DD HH:MM:SS').")
    parser.add_argument("-e", "--end", nargs="?", default=datetime.datetime.now(), help="Define end date (format: 'YYYY-MM-DD HH:MM:SS')")
    parser.add_argument("-n", "--new", nargs="?", const=500, type=int, help="Create a new file with log-in data")
    parser.add_argument("-l", "--log_in", action="store_true", help="Check for successfull/unsuccsessfull log-in attempts.")
    parser.add_argument("-d", "--date", action="store_true", help="Check for log-in data between specified dates")
    parser.add_argument("-i", "--ip", help="Search for specified ip-address.")
    parser.add_argument("-o", "--lock_out", action="store_true", help="Check for locked out IPs")
    
    args = parser.parse_args()
    
    start = pd.to_datetime(args.start)
    end = pd.to_datetime(args.end)

    if args.new:
        print("Create new log-file")
        new_log_file(start, end, args.new)
    elif args.log_in == True:
        print("Log-in")
        log_in_check(start, end)
    elif args.date == True:
        print("Check by date")
        date_check(start, end)
    elif args.ip:
        print("IP-Check")
        ip_check(start, end, args.ip)
    elif args.lock_out:
        print("Check for locked out")
        lock_out_check(start, end)

if __name__ == "__main__":
    main()
    
# gui (in copy)
# input fields for dates and ip
# button for each function
# results in window with filter function etc.