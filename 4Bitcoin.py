from bitcoinaddress import Wallet
import urllib.request
import smtplib, random, codecs, time, sys, atexit
from rich.console import Console
gmail_user = 'youremail@gmail.com'
gmail_password = 'yourpassword'
console = Console()
console.clear()

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

my_colours = [W, R, G, O, B, P]

icons= ['⏳', 'ℹ️', '✅', '⛔️', '🔁', '🔑', '💸', '😔', '🌍', '✍️', '🚌', '👇', '📋', '📣', '🤩','😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾', '👋', '🤚', '🖐', '✋', '🖖', '👌', '🤌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉', '👆', '🖕', '👇', '☝️', '👍', '👎', '✊', '👊', '🤛', '🤜', '👏', '🙌', '👐', '🤲', '🤝', '🙏', '✍️', '💅', '🤳', '💪', '🦾', '🦵', '🦿', '🦶', '👣', '👂', '🦻', '👃', '🫀', '🫁', '🧠', '🦷', '🦴', '👀', '👁', '👅', '👄', '💋', '🩸', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🪱', '🐛', '🦋', '🐌', '🐞', '🐜', '🪰', '🪲', '🪳', '🦟', '🦗', '🕷', '🕸', '🦂', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🦧', '🦣', '🐘', '🦛', '🦏', '🐪', '🐫', '🦒', '🦘', '🦬', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', '🦌', '🐕', '🐩', '🦮', '🐕‍🦺', '🐈', '🐈‍⬛', '🪶', '🐓', '🦃', '🦤', '🦚', '🦜', '🦢', '🦩', '🕊', '🐇', '🦝', '🦨', '🦡', '🦫', '🦦', '🦥', '🐁', '🐀', '🐿', '🦔', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🪵', '🌱', '🌿', '☘️', '🍀', '🎍', '🪴', '🎋', '🍃', '🍂', '🍁', '🍄', '🐚', '🪨', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '🪐', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥', '🌪', '🌈', '☀️', '🌤', '⛅️', '🌥', '☁️', '🌦', '🌧', '⛈', '🌩', '🌨', '❄️', '☃️', '⛄️', '🌬', '💨', '💧', '💦', '☔️', '☂️', '🌊', '🌫', '⏰', '💰', '🎅🏻', '🎄', '🎁', '🎶']

animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]", "[■■■■□□□□□□□□□□□□□□□□]", "[■■■■■□□□□□□□□□□□□□□□]", "[■■■■■■□□□□□□□□□□□□□□]", "[■■■■■■■□□□□□□□□□□□□□]", "[■■■■■■■■□□□□□□□□□□□□]", "[■■■■■■■■■□□□□□□□□□□□]", "[■■■■■■■■■■□□□□□□□□□□]", "[■■■■■■■■■■■□□□□□□□□□]", "[■■■■■■■■■■■■□□□□□□□□]", "[■■■■■■■■■■■■■□□□□□□□]", "[■■■■■■■■■■■■■■□□□□□□]", "[■■■■■■■■■■■■■■■□□□□□]", "[■■■■■■■■■■■■■■■■□□□□]", "[■■■■■■■■■■■■■■■■■■□□]", "[■■■■■■■■■■■■■■■■■■■□]", "[■■■■■■■■■■■■■■■■■■■■]"]

console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow]                 Starting search...[/yellow]")
console.print("[yellow]                Using Block Chain API...[/yellow]")
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
a = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
b = 2**y
console.print("[purple]⏳Starting search... Please Wait ⏳[/purple]")
console.print("==========================================================")

    

counter = 0
total = 0
while True:
    lol= random.choice(icons)
    lol1= random.choice(icons)
    lol2= random.choice(icons)
    lol3= random.choice(icons)
    colour = random.choice(my_colours)
    counter+=1
    total+=5
    ran=random.randrange(a,b)
    HEX = "%064x" % ran
    wallet = Wallet(HEX)
    uaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr3'] #3 segwit_address
    bcaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH']  #bc1 P2WPKH address
    bc1addr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] #bc1 P2WSH address
    wif = wallet.key.__dict__['mainnet'].__dict__['wif']
    wifc = wallet.key.__dict__['mainnet'].__dict__['wifc']


    contents = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + uaddr).read()
    contents2 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + caddr).read()
    contents3 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + saddr).read()
    contents4 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + bcaddr).read()
    contents5 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + bc1addr).read()
    
    if int (contents) != 0 or int (contents2) != 0 or int (contents3) != 0 or int (contents4) != 0 or int (contents5) != 0:
        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('🤩Address Uncompressed🤩: ', uaddr, ' [bold green]                            💸Total Received💸: ' + str(contents.decode('UTF8')))
        console.print('🤩Address Compressed  🤩: ', caddr, ' [bold green]                            💸Total Received💸: ' + str(contents2.decode('UTF8')))
        console.print('🤩Address 3 Segwit    🤩: ', saddr, ' [bold green]                            💸Total Received💸: ' + str(contents3.decode('UTF8')))
        console.print('🤩Address bc1 P2WPKH  🤩: ', bcaddr, ' [bold green]                    💸Total Received💸: ' + str(contents4.decode('UTF8')))
        console.print('🤩Address bc1 P2WSH   🤩: ', bc1addr, ' [bold green]💸Total Received💸: ' + str(contents5.decode('UTF8')))
        print('🔑 PrivateKey (WIF) Compressed   : ' + wifc)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wif)
        print('🔑 Private Key (HEX) : ' + HEX)
        print('🔑 Private Key (DEC) : ' + str(ran))
        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran))
        f.write('\nPrivatekey (hex): ' + HEX)
        f.write('\nPrivatekey Uncompressed: ' + wif)
        f.write('\nPrivatekey compressed: ' + wifc)
        f.write('\nAddress 1 Compressed: ' + caddr + ' Total Received : ' + str(contents2.decode('UTF8')))
        f.write('\nAddress 1 Uncompressed: ' + uaddr + ' Total Received : ' + str(contents.decode('UTF8')))
        f.write('\nAddress 3 Segwit: ' + saddr + ' Total Received : ' + str(contents3.decode('UTF8')))
        f.write('\nAddress bc1 P2WPKH: ' + bcaddr + ' Total Received : ' + str(contents4.decode('UTF8')))
        f.write('\nAddress bc1 P2WSH: ' + bc1addr + ' Total Received : ' + str(contents5.decode('UTF8')))
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        sent_from = gmail_user
        to = ['youremail@gmail.com']
        subject = ['OMG Super Important Message']
        body = '\nPrivatekey (dec): ' + str(ran) + '\nPrivatekey (hex): ' + HEX + '\nPrivatekey Uncompressed: ' + wif + '\nPrivatekey compressed: ' + wifc + '\nPublic Address 1 Uncompressed: ' + uaddr + ' Total Received : ' + str(contents.decode('UTF8')) + '\nPublic Address 1 Compressed: ' + caddr + ' Total Received : ' + str(contents2.decode('UTF8')) + '\nPublic Address 3 Segwit: ' + saddr + ' Total Received : ' + str(contents3.decode('UTF8')) + '\nPublic Address bc1 P2WPKH: ' + bcaddr + ' Total Received : ' + str(contents4.decode('UTF8')) + '\nPublic Address bc1 P2WSH: ' + bc1addr + ' Total Received : ' + str(contents5.decode('UTF8')) +'\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====\n'
        
        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        
            print ('Email sent!')
        except:
            print('Something went wrong...')
            break
               
    else: 
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('😔 Address Uncompressed: ', uaddr, ' [red]                            😔Total Received😔 : ' + str(contents.decode('UTF8')))
        console.print('😔 Address Compressed  : ', caddr, ' [red]                            😔Total Received😔 : ' + str(contents2.decode('UTF8')))
        console.print('😔 Address 3 Segwit    : ', saddr, ' [red]                            😔Total Received😔 : ' + str(contents3.decode('UTF8')))
        console.print('😔 Address bc1 P2WPKH  : ', bcaddr, ' [red]                    😔Total Received😔 : ' + str(contents4.decode('UTF8')))
        console.print('😔 Address bc1 P2WSH   : ', bc1addr, ' [red]😔Total Received😔 : ' + str(contents5.decode('UTF8')))
        print('🔑 PrivateKey (WIF) Compressed : ' + wifc)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wif)
        print('🔑 Private Key (HEX) : ' + HEX)
        print('🔑 Private Key (DEC) : ' + str(ran))
        console.print(lol, lol1, lol2, lol3, "[purple]⏳ Sleeping for 0.2 seconds... Please Wait ⏳[/purple]", lol3, lol2, lol1, lol)
        for i in range(len(animation)):
            time.sleep(0.01)
            sys.stdout.write("\r" + colour + lol + "Loading:" + animation[i % len(animation)])
            sys.stdout.flush()
