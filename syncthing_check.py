# Script checontrolla ricorsivamente tutti i file conflittuali
import os
import sys

# Funzioni di stampa colorata
global badprint
badprint = False #impostare su True per disabilitare la stampa colorata
def rprint(skk): print(" E "+skk) if badprint else print("\033[91m E\033[00m {}" .format(skk))
def gprint(skk): print(" * "+skk) if badprint else print("\033[92m *\033[00m {}" .format(skk))
def xprint(skk): print(" ! "+skk) if badprint else print("\033[92m !\033[00m {}" .format(skk))

# Funzione ricorsiva di scansione delle directory e subdirectory
global counter
global conflict_list
conflict_list = []
def scan(directory,fullpath):
    global conflict_list
    global counter
    for entry in os.scandir(directory):
        if entry.is_dir():
            #print(entry.name)
            scan(entry,fullpath+"/"+entry.name)
        elif entry.is_file():
            if "sync-conflict" in entry.name:
                #rprint(fullpath+"/"+entry.name)
                conflict_list.append(fullpath+"/"+entry.name)
                counter += 1


# MAIN
print()
path = sys.argv[1]
gprint("Syncthing check v1.1:\t"+path)
counter = 0
scan(path,path)
print(" | Found conflicts:\t"+str(counter))

for el in conflict_list:
    rprint(el)
print()

# Notifica OS
if (counter > 0):
    os.system("notify-send 'Syncthing-Check' 'Found "+str(counter)+" conflicts in "+path+"'")

