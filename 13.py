import deauther
import sqlmap
import phishing
import location
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.traceback import install
from rich.panel import Panel
from rich import print

install()
console = Console()

os.system('cls||clear')

print(Panel.fit("""
                                 __    _                                   
                            _wr""        "-q__              
                          _dP                 9m_     
                        _#P                     9#_      
                       d#@                       9#m     
                      d##                         ###     
                     J###                         ###L    
                     {###K                       J###K    
                     ]####K      ___aaa___      J####F      
                 __gmM######_  w#P""   ""9#m  _d#####Mmw__    
              _g##############mZ_         __g##############m_     
            _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_     
           a###""          ,Z"#####@" '######"\g          ""M##m  
          J#@"             0L  "*## 313 ##@"  J#              *#K  
          #"               `#    "_gmwgm_~    dF               `#_ 
         7F                 "#_   ]#####F   _dK                 JE  
         ]                    *m__ ##### __g@"                   F  
                                "PJ#####LP"                         
          `                       0######_                      '   
                                _0########_                         
              .               _d#####^#####m__              ,     
               "*w_________am#####P"   ~9#####mw_________w*"     
                   ""9@#####@M""           ""P@#####@M""        
         


\nSamuraiX13 ~""", style="#4800ff", title="programmer"))
console.rule("[bold red]13 - Menu", style="#4800ff", align="center")
print(Panel.fit("[#d000ff](1) - deauther\n[#d000ff](2) - sqlmap\n[#d000ff](3) - phishing\n[#d000ff](4) - location", style="#4800ff", title="Tools"))

ask = Prompt.ask("\n[#d000ff]Enter tool you want to choice:", choices=["1", "2","3","4"])
if ask == "1":
	deauther.deauth()
if ask == "2":
	sqlmap.sqlmap()
if ask == "3":
	phishing.phishing()
if ask == "4":
	location.location()
