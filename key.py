#!/usr/bin/env/python
#Copyright©MrL00L

import os,sys
from time import sleep
if sys.platform == "linux2" or sys.platform == "linux":                     
		    R = ("\033[31m")                                                    
		    W = ("\033[0;1m")                                                   
		    P = ("\033[35m") 
		    B = ("\033[34m")                                                   
		    G = ("\033[32m")                                                    
		    glp = ("\033[2m")
		    C = ("\033[36m")                                                   
		    Y = ("\033[33m")                        
                 
else:                                                                       
        R = ""                                                              
        W = ""
        Y = ""
        B = ""
        G = ""
        glp = ""
        
        
os.system('clear')
input('\nLanjut ? [Y] ')
sleep(1)
os.system('clear')
print (G+"		################################")
print (G+"		#"+R+"  Author"+W+"     :"+C+ "   Mr.L00L"+G+"      #")
print (G+"		################################")                
print (G+"		#"+R+"  Code" +W+"       :"+C+"   Python" +G+"       #")              
print (G+"		################################")
print (G+"		#" +R+ "  Version" +W+"    :" +C+"   1.0" +G+"          #")
print (G+"		################################")
print (G+"		#"+R+"  Contact Me" +W+" :" +C+" +6285872792870"+G+" #")
print (G+"		################################")
print (G+"		#"+R+"  Thanks To" +W+"  :" +C+"  MicroClone"+G+"    #")                 
print (G+"		################################")
print ("")
print ("")
sleep(1)
print (P+'Loading...')
sleep(3)
print(R+'\n\n[!] Making Termux Properties Directory..')
sleep(2)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(G+'[!] Success !')
sleep(1)
print(R+'\n[!] Making Setup')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
seting = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
seting.write(key)
seting.close()
sleep(1)
print(G+'[!] Success !')
sleep(1)
print(R+'\n[!] Setting Up..')
sleep(2)
os.system('termux-reload-settings')
print(G+'[!] Successfully !!!')
sleep(2)
os.system("clear")
sleep(1)
print (G+'NB : Silahkan Buka Kembali Termux Anda')
print (C+'\n\n- Terima Kasih -\n\n')
print ('')