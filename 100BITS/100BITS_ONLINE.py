#100BITS_ONLINE.py Check for 100 bitcoin address per scan and Check Balance=====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====
from bitcoinaddress import Wallet
import codecs, sys, atexit, time, requests, random
from rich.console import Console
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

animation = ["□□□□□□□□□□□□□□□□□□□□  0%","■□□□□□□□□□□□□□□□□□□□  5%","■■□□□□□□□□□□□□□□□□□□ 10%","■■■□□□□□□□□□□□□□□□□□ 15%","■■■■□□□□□□□□□□□□□□□□ 20%","■■■■■□□□□□□□□□□□□□□□ 25%","■■■■■■□□□□□□□□□□□□□□ 30%","■■■■■■■□□□□□□□□□□□□□ 35%","■■■■■■■■□□□□□□□□□□□□ 40%","■■■■■■■■■□□□□□□□□□□□ 45%","■■■■■■■■■■□□□□□□□□□□ 50%","■■■■■■■■■■■□□□□□□□□□ 55%","■■■■■■■■■■■■□□□□□□□□ 60%","■■■■■■■■■■■■■□□□□□□□ 65%","■■■■■■■■■■■■■■□□□□□□ 70%","■■■■■■■■■■■■■■■□□□□□ 75%","■■■■■■■■■■■■■■■■□□□□ 80%","■■■■■■■■■■■■■■■■■□□□ 85%","■■■■■■■■■■■■■■■■■■□□ 90%","■■■■■■■■■■■■■■■■■■■□ 95%","■■■■■■■■■■■■■■■■■■■■100%"]

#animation = ["□□□□□□□□□□□□□□□□□□□□  0%","🔑□□□□□□□□□□□□□□□□□□□  5%","🔑🔑□□□□□□□□□□□□□□□□□□ 10%","🔑🔑🔑□□□□□□□□□□□□□□□□□ 15%","🔑🔑🔑🔑□□□□□□□□□□□□□□□□ 20%","🔑🔑🔑🔑🔑□□□□□□□□□□□□□□□ 25%","🔑🔑🔑🔑🔑🔑□□□□□□□□□□□□□□ 30%","🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□□□□ 35%","🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□□□ 40%","🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□□ 45%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□□ 50%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□□ 55%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□□ 60%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□□ 65%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□□ 70%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□□ 75%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□□ 80%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□□ 85%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□□ 90%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑□ 95%","🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑🔑100%"]
   
console.print(" [yellow]-----------------💰HUNT4BITCOIN - 100BITS_ONLINE.py💰----------------------[/yellow]")
console.print("[yellow]                    🤖🤖🤖    Made by Mizogg    🤖🤖🤖[/yellow]")
console.print("[yellow]                       🤩   Starting search...   🤩 [/yellow]")
console.print("[yellow]                        Using Block Chain API...[/yellow]")
console.print(" [yellow]-----------------💰HUNT4BITCOIN - 100BITS_ONLINE.py💰----------------------[/yellow]")
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
a = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
b = 2**y
m=int(input("Magnitude Jump Stride -> "))
console.print("[purple] ✅Starting search... Please Wait min range: [/purple]" + str(a))
console.print("[purple] ⛔️Max range: [/purple]" + str(b))
print(" 🔁==========================================================🔁")

query = []
total=0
counter=0
remainingtotal=b-a
div= round(remainingtotal / 100)
finish = div + a
remaining = finish
F = []
P = a
while P<finish:
    lol= random.choice(icons)
    colour = random.choice(my_colours)
    counter+=1
    remainingtotal-=m
    remaining-=m
    P+=m
    div= round(remainingtotal / 100)
    total+=100
    ran= P
    HEX = "%064x" % ran
    wallet = Wallet(HEX)
    uaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr = wallet.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif = wallet.key.__dict__['mainnet'].__dict__['wif']
    wifc = wallet.key.__dict__['mainnet'].__dict__['wifc']
    
    percent = div * 5
    ran1= P+percent
    HEX1 = "%064x" % ran1
    wallet1 = Wallet(HEX1)
    uaddr1 = wallet1.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr1 = wallet1.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr1 = wallet1.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr1 = wallet1.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr1 = wallet1.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif1 = wallet1.key.__dict__['mainnet'].__dict__['wif']
    wifc1 = wallet1.key.__dict__['mainnet'].__dict__['wifc']
    
    percent1 = div * 10
    ran2= P+percent1
    HEX2 = "%064x" % ran2
    wallet2 = Wallet(HEX2)
    uaddr2 = wallet2.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr2 = wallet2.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr2 = wallet2.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr2 = wallet2.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr2 = wallet2.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif2 = wallet2.key.__dict__['mainnet'].__dict__['wif']
    wifc2 = wallet2.key.__dict__['mainnet'].__dict__['wifc']
    
    percent2 = div * 15
    ran3= P+percent2
    HEX3 = "%064x" % ran3
    wallet3 = Wallet(HEX3)
    uaddr3 = wallet3.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr3 = wallet3.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr3 = wallet3.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr3 = wallet3.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr3 = wallet3.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif3 = wallet3.key.__dict__['mainnet'].__dict__['wif']
    wifc3 = wallet3.key.__dict__['mainnet'].__dict__['wifc']
    
    percent3 = div * 20
    ran4= P+percent3
    HEX4 = "%064x" % ran4
    wallet4 = Wallet(HEX4)
    uaddr4 = wallet4.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr4 = wallet4.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr4 = wallet4.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr4 = wallet4.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr4 = wallet4.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif4 = wallet4.key.__dict__['mainnet'].__dict__['wif']
    wifc4 = wallet4.key.__dict__['mainnet'].__dict__['wifc']
    
    percent4 = div * 25
    ran5= P+percent4
    HEX5 = "%064x" % ran5
    wallet5 = Wallet(HEX5)
    uaddr5 = wallet5.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr5 = wallet5.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr5 = wallet5.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr5 = wallet5.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr5 = wallet5.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif5 = wallet5.key.__dict__['mainnet'].__dict__['wif']
    wifc5 = wallet5.key.__dict__['mainnet'].__dict__['wifc']
    
    percent5 = div * 30
    ran6= P+percent5
    HEX6 = "%064x" % ran6
    wallet6 = Wallet(HEX6)
    uaddr6 = wallet6.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr6 = wallet6.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr6 = wallet6.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr6 = wallet6.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr6 = wallet6.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif6 = wallet6.key.__dict__['mainnet'].__dict__['wif']
    wifc6 = wallet6.key.__dict__['mainnet'].__dict__['wifc']
    
    percent6 = div * 35
    ran7= P+percent6
    HEX7 = "%064x" % ran7
    wallet7 = Wallet(HEX7)
    uaddr7 = wallet7.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr7 = wallet7.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr7 = wallet7.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr7 = wallet7.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr7 = wallet7.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif7 = wallet7.key.__dict__['mainnet'].__dict__['wif']
    wifc7 = wallet7.key.__dict__['mainnet'].__dict__['wifc']
    
    percent7 = div * 40
    ran8= P+percent7
    HEX8 = "%064x" % ran8
    wallet8 = Wallet(HEX8)
    uaddr8 = wallet8.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr8 = wallet8.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr8 = wallet8.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr8 = wallet8.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr8 = wallet8.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif8 = wallet8.key.__dict__['mainnet'].__dict__['wif']
    wifc8 = wallet8.key.__dict__['mainnet'].__dict__['wifc']
    
    percent8 = div * 45
    ran9= P+percent8
    HEX9 = "%064x" % ran9
    wallet9 = Wallet(HEX9)
    uaddr9 = wallet9.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr9 = wallet9.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr9 = wallet9.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr9 = wallet9.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr9 = wallet9.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif9 = wallet9.key.__dict__['mainnet'].__dict__['wif']
    wifc9 = wallet9.key.__dict__['mainnet'].__dict__['wifc']
    
    percent9 = div * 50
    ran10= P+percent9
    HEX10 = "%064x" % ran10
    wallet10 = Wallet(HEX10)
    uaddr10 = wallet10.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr10 = wallet10.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr10 = wallet10.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr10 = wallet10.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr10 = wallet10.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif10 = wallet10.key.__dict__['mainnet'].__dict__['wif']
    wifc10 = wallet10.key.__dict__['mainnet'].__dict__['wifc']
    
    percent10 = div * 55
    ran11= P+percent10
    HEX11 = "%064x" % ran11
    wallet11 = Wallet(HEX11)
    uaddr11 = wallet11.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr11 = wallet11.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr11 = wallet11.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr11 = wallet11.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr11 = wallet11.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif11 = wallet11.key.__dict__['mainnet'].__dict__['wif']
    wifc11 = wallet11.key.__dict__['mainnet'].__dict__['wifc']
    
    percent11 = div * 60
    ran12= P+percent11
    HEX12 = "%064x" % ran12
    wallet12 = Wallet(HEX12)
    uaddr12 = wallet12.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr12 = wallet12.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr12 = wallet12.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr12 = wallet12.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr12 = wallet12.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif12 = wallet12.key.__dict__['mainnet'].__dict__['wif']
    wifc12 = wallet12.key.__dict__['mainnet'].__dict__['wifc']
    
    percent12 = div * 65
    ran13= P+percent12
    HEX13 = "%064x" % ran13
    wallet13 = Wallet(HEX13)
    uaddr13 = wallet13.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr13 = wallet13.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr13 = wallet13.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr13 = wallet13.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr13 = wallet13.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif13 = wallet13.key.__dict__['mainnet'].__dict__['wif']
    wifc13 = wallet13.key.__dict__['mainnet'].__dict__['wifc']
    
    percent13 = div * 70
    ran14= P+percent13
    HEX14 = "%064x" % ran14
    wallet14 = Wallet(HEX14)
    uaddr14 = wallet14.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr14 = wallet14.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr14 = wallet14.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr14 = wallet14.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr14 = wallet14.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif14 = wallet14.key.__dict__['mainnet'].__dict__['wif']
    wifc14 = wallet14.key.__dict__['mainnet'].__dict__['wifc']
    
    percent14 = div * 75
    ran15= P+percent14
    HEX15 = "%064x" % ran15
    wallet15 = Wallet(HEX15)
    uaddr15 = wallet15.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr15 = wallet15.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr15 = wallet15.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr15 = wallet15.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr15 = wallet15.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif15 = wallet15.key.__dict__['mainnet'].__dict__['wif']
    wifc15 = wallet15.key.__dict__['mainnet'].__dict__['wifc']
    
    percent15 = div * 80
    ran16= P+percent15
    HEX16 = "%064x" % ran16
    wallet16 = Wallet(HEX16)
    uaddr16 = wallet16.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr16 = wallet16.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr16 = wallet16.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr16 = wallet16.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr16 = wallet16.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif16 = wallet16.key.__dict__['mainnet'].__dict__['wif']
    wifc16 = wallet16.key.__dict__['mainnet'].__dict__['wifc']
    
    percent16 = div * 85
    ran17= P+percent16
    HEX17 = "%064x" % ran17
    wallet17 = Wallet(HEX17)
    uaddr17 = wallet17.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr17 = wallet17.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr17 = wallet17.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr17 = wallet17.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr17 = wallet17.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif17 = wallet17.key.__dict__['mainnet'].__dict__['wif']
    wifc17 = wallet17.key.__dict__['mainnet'].__dict__['wifc']
    
    percent17 = div * 90
    ran18= P+percent17
    HEX18 = "%064x" % ran18
    wallet18 = Wallet(HEX18)
    uaddr18 = wallet18.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr18 = wallet18.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr18 = wallet18.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr18 = wallet18.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr18 = wallet18.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif18 = wallet18.key.__dict__['mainnet'].__dict__['wif']
    wifc18 = wallet18.key.__dict__['mainnet'].__dict__['wifc']
    
    percent18 = div * 95
    ran19= P+percent18
    HEX19 = "%064x" % ran19
    wallet19 = Wallet(HEX19)
    uaddr19 = wallet19.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr19 = wallet19.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr19 = wallet19.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr19 = wallet19.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr19 = wallet19.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif19 = wallet19.key.__dict__['mainnet'].__dict__['wif']
    wifc19 = wallet19.key.__dict__['mainnet'].__dict__['wifc']
    query=(uaddr,uaddr1,uaddr2,uaddr3,uaddr4,uaddr5,uaddr6,uaddr7,uaddr8,uaddr9,uaddr10,uaddr11,uaddr12,uaddr13,uaddr14,uaddr15,uaddr16,uaddr17,uaddr18,uaddr19,caddr,caddr1,caddr2,caddr3,caddr4,caddr5,caddr6,caddr7,caddr8,caddr9,caddr10,caddr11,caddr12,caddr13,caddr14,caddr15,caddr16,caddr17,caddr18,caddr19,saddr,saddr1,saddr2,saddr3,saddr4,saddr5,saddr6,saddr7,saddr8,saddr9,saddr10,saddr11,saddr12,saddr13,saddr14,saddr15,saddr16,saddr17,saddr18,saddr19,bcaddr,bcaddr1,bcaddr2,bcaddr3,bcaddr4,bcaddr5,bcaddr6,bcaddr7,bcaddr8,bcaddr9,bcaddr10,bcaddr11,bcaddr12,bcaddr13,bcaddr14,bcaddr15,bcaddr16,bcaddr17,bcaddr18,bcaddr19,bc1addr,bc1addr1,bc1addr2,bc1addr3,bc1addr4,bc1addr5,bc1addr6,bc1addr7,bc1addr8,bc1addr9,bc1addr10,bc1addr11,bc1addr12,bc1addr13,bc1addr14,bc1addr15,bc1addr16,bc1addr17,bc1addr18,bc1addr19)
    if len(query) == 100:
        
        try:
            request = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query), timeout=10)
            request = request.json()


            for row in request["addresses"]:
                print(row)
                if row["final_balance"] > 0:
                    print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
                    f=open("winner.txt","a")
                    f.write('\nPrivatekey (dec): ' + str(ran))
                    f.write('\nPrivatekey (hex): ' + HEX)
                    f.write('\nPrivatekey Uncompressed: ' + wif)
                    f.write('\nPrivatekey compressed: ' + wifc)
                    f.write('\nPublic Address 1 Compressed: ' + caddr)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr)
                    f.write('\nPublic Address 3 Segwit: ' + saddr)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran1))
                    f.write('\nPrivatekey (hex): ' + HEX1)
                    f.write('\nPrivatekey Uncompressed: ' + wif1)
                    f.write('\nPrivatekey compressed: ' + wifc1)
                    f.write('\nPublic Address 1 Compressed: ' + caddr1)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr1)
                    f.write('\nPublic Address 3 Segwit: ' + saddr1)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr1)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr1)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran2))
                    f.write('\nPrivatekey (hex): ' + HEX2)
                    f.write('\nPrivatekey Uncompressed: ' + wif2)
                    f.write('\nPrivatekey compressed: ' + wifc2)
                    f.write('\nPublic Address 1 Compressed: ' + caddr2)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr2)
                    f.write('\nPublic Address 3 Segwit: ' + saddr2)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr2)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr2)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran3))
                    f.write('\nPrivatekey (hex): ' + HEX3)
                    f.write('\nPrivatekey Uncompressed: ' + wif3)
                    f.write('\nPrivatekey compressed: ' + wifc3)
                    f.write('\nPublic Address 1 Compressed: ' + caddr3)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr3)
                    f.write('\nPublic Address 3 Segwit: ' + saddr3)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr3)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr3)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
                    f.write('\nPrivatekey (dec): ' + str(ran4))
                    f.write('\nPrivatekey (hex): ' + HEX4)
                    f.write('\nPrivatekey Uncompressed: ' + wif4)
                    f.write('\nPrivatekey compressed: ' + wifc4)
                    f.write('\nPublic Address 1 Compressed: ' + caddr4)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr4)
                    f.write('\nPublic Address 3 Segwit: ' + saddr4)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr4)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr4)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran5))
                    f.write('\nPrivatekey (hex): ' + HEX5)
                    f.write('\nPrivatekey Uncompressed: ' + wif5)
                    f.write('\nPrivatekey compressed: ' + wifc5)
                    f.write('\nPublic Address 1 Compressed: ' + caddr5)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr5)
                    f.write('\nPublic Address 3 Segwit: ' + saddr5)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr5)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr5)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
                    f.write('\nPrivatekey (dec): ' + str(ran6))
                    f.write('\nPrivatekey (hex): ' + HEX6)
                    f.write('\nPrivatekey Uncompressed: ' + wif6)
                    f.write('\nPrivatekey compressed: ' + wifc6)
                    f.write('\nPublic Address 1 Compressed: ' + caddr6)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr6)
                    f.write('\nPublic Address 3 Segwit: ' + saddr6)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr6)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr6)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran7))
                    f.write('\nPrivatekey (hex): ' + HEX7)
                    f.write('\nPrivatekey Uncompressed: ' + wif7)
                    f.write('\nPrivatekey compressed: ' + wifc7)
                    f.write('\nPublic Address 1 Compressed: ' + caddr7)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr7)
                    f.write('\nPublic Address 3 Segwit: ' + saddr7)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr7)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr7)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran8))
                    f.write('\nPrivatekey (hex): ' + HEX8)
                    f.write('\nPrivatekey Uncompressed: ' + wif8)
                    f.write('\nPrivatekey compressed: ' + wifc8)
                    f.write('\nPublic Address 1 Compressed: ' + caddr8)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr8)
                    f.write('\nPublic Address 3 Segwit: ' + saddr8)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr8)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr8)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran9))
                    f.write('\nPrivatekey (hex): ' + HEX9)
                    f.write('\nPrivatekey Uncompressed: ' + wif9)
                    f.write('\nPrivatekey compressed: ' + wifc9)
                    f.write('\nPublic Address 1 Compressed: ' + caddr9)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr9)
                    f.write('\nPublic Address 3 Segwit: ' + saddr9)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr9)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr9)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran10))
                    f.write('\nPrivatekey (hex): ' + HEX10)
                    f.write('\nPrivatekey Uncompressed: ' + wif10)
                    f.write('\nPrivatekey compressed: ' + wifc10)
                    f.write('\nPublic Address 1 Compressed: ' + caddr10)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr10)
                    f.write('\nPublic Address 3 Segwit: ' + saddr10)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr10)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr10)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran11))
                    f.write('\nPrivatekey (hex): ' + HEX11)
                    f.write('\nPrivatekey Uncompressed: ' + wif11)
                    f.write('\nPrivatekey compressed: ' + wifc11)
                    f.write('\nPublic Address 1 Compressed: ' + caddr11)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr11)
                    f.write('\nPublic Address 3 Segwit: ' + saddr11)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr11)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr11)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran12))
                    f.write('\nPrivatekey (hex): ' + HEX12)
                    f.write('\nPrivatekey Uncompressed: ' + wif12)
                    f.write('\nPrivatekey compressed: ' + wifc12)
                    f.write('\nPublic Address 1 Compressed: ' + caddr12)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr12)
                    f.write('\nPublic Address 3 Segwit: ' + saddr12)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr12)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr12)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran13))
                    f.write('\nPrivatekey (hex): ' + HEX13)
                    f.write('\nPrivatekey Uncompressed: ' + wif13)
                    f.write('\nPrivatekey compressed: ' + wifc13)
                    f.write('\nPublic Address 1 Compressed: ' + caddr13)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr13)
                    f.write('\nPublic Address 3 Segwit: ' + saddr13)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr13)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr13)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
                    f.write('\nPrivatekey (dec): ' + str(ran14))
                    f.write('\nPrivatekey (hex): ' + HEX14)
                    f.write('\nPrivatekey Uncompressed: ' + wif14)
                    f.write('\nPrivatekey compressed: ' + wifc14)
                    f.write('\nPublic Address 1 Compressed: ' + caddr14)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr14)
                    f.write('\nPublic Address 3 Segwit: ' + saddr14)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr14)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr14)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran15))
                    f.write('\nPrivatekey (hex): ' + HEX15)
                    f.write('\nPrivatekey Uncompressed: ' + wif15)
                    f.write('\nPrivatekey compressed: ' + wifc15)
                    f.write('\nPublic Address 1 Compressed: ' + caddr15)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr15)
                    f.write('\nPublic Address 3 Segwit: ' + saddr15)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr15)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr15)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
                    f.write('\nPrivatekey (dec): ' + str(ran16))
                    f.write('\nPrivatekey (hex): ' + HEX16)
                    f.write('\nPrivatekey Uncompressed: ' + wif16)
                    f.write('\nPrivatekey compressed: ' + wifc16)
                    f.write('\nPublic Address 1 Compressed: ' + caddr16)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr16)
                    f.write('\nPublic Address 3 Segwit: ' + saddr16)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr16)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr16)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran17))
                    f.write('\nPrivatekey (hex): ' + HEX17)
                    f.write('\nPrivatekey Uncompressed: ' + wif17)
                    f.write('\nPrivatekey compressed: ' + wifc17)
                    f.write('\nPublic Address 1 Compressed: ' + caddr17)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr17)
                    f.write('\nPublic Address 3 Segwit: ' + saddr17)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr17)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr17)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran18))
                    f.write('\nPrivatekey (hex): ' + HEX18)
                    f.write('\nPrivatekey Uncompressed: ' + wif18)
                    f.write('\nPrivatekey compressed: ' + wifc18)
                    f.write('\nPublic Address 1 Compressed: ' + caddr18)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr18)
                    f.write('\nPublic Address 3 Segwit: ' + saddr18)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr18)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr18)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )
                    f.write('\nPrivatekey (dec): ' + str(ran19))
                    f.write('\nPrivatekey (hex): ' + HEX19)
                    f.write('\nPrivatekey Uncompressed: ' + wif19)
                    f.write('\nPrivatekey compressed: ' + wifc19)
                    f.write('\nPublic Address 1 Compressed: ' + caddr19)
                    f.write('\nPublic Address 1 Uncompressed: ' + uaddr19)
                    f.write('\nPublic Address 3 Segwit: ' + saddr19)
                    f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr19)
                    f.write('\nPublic Address bc1 P2WSH: ' + bc1addr19)
                    f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' )                     
                    f.close()
        except:
            pass
        query = []
        print('\n :HEX    : ', HEX, '\n :HEX 5%: ', HEX1, '\n :HEX 10%: ', HEX2, '\n :HEX 15%: ', HEX3, '\n :HEX 20%: ', HEX4, '\n :HEX 25%: ', HEX5, '\n :HEX 30%: ', HEX6, '\n :HEX 35%: ', HEX7, '\n :HEX 40%: ', HEX8, '\n :HEX 45%: ', HEX9, '\n :HEX 50%: ', HEX10, '\n :HEX 55%: ', HEX11, '\n :HEX 60%: ', HEX12, '\n :HEX 65%: ', HEX13, '\n :HEX 70%: ', HEX14, '\n :HEX 75%: ', HEX15, '\n :HEX 80%: ', HEX16, '\n :HEX 85%: ', HEX17, '\n :HEX 90%: ', HEX18, '\n :HEX 95%: ', HEX19)
        console.print(lol + "[purple]   Magnitude Jump Stride -> [/purple]" + str(m))
        console.print('[purple]✅Starting search... Please Wait min range: [ ' + str(a) + ' ][/purple]')
        console.print('[purple]⛔️Max range: [ ' + str(b) + ' ][/purple]')
        console.print('[red]Scan:  [' + str(counter) + '] [/red]' + '[red] :Remaining:  [' + str(remaining) + '] [/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        for i in range(len(animation)):
            time.sleep(0.5)
            sys.stdout.write("\r" + colour + lol + "Loading 10 Seconds :" + animation[i % len(animation)])
            sys.stdout.flush()
