#100BITS.py Check for 500 bitcoin address per scan=====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====
from bitcoinaddress import Wallet

print('Bitcoin Addresses Loading Please Wait: ')
filename ='puzzle.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read(1024*1024).split()
add = set(add)
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
x=int(input("'Start range in BITs 0 or Higher(Puzzle StartNumber) -> "))
a = 2**x
y=int(input("Stop range Max in BITs 256 Max (Puzzle StopNumber) -> "))
b = 2**y
m=int(input("Magnitude Jump Stride -> "))
print("Starting search... Please Wait min range: " + str(a))
print("Max range: " + str(b))
print("==========================================================")
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))

total=0
count=0
remainingtotal=b-a
div= round(remainingtotal / 100)
finish = div + a
remaining = finish
F = []
P = a
while P<finish:
    count+=1
    remainingtotal-=m
    remaining-=m
    P+=m
    div= round(remainingtotal / 100)
    total+=495
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
    
    percent = div * 2
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
    
    percent1 = div * 3
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
    
    percent2 = div * 4
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
    
    percent3 = div * 5
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
    
    percent4 = div * 6
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
    
    percent5 = div * 7
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
    
    percent6 = div * 8
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
    
    percent7 = div * 9
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
    
    percent8 = div * 10
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
    
    percent9 = div * 11
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
    
    percent10 = div * 12
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
    
    percent11 = div * 13
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
    
    percent12 = div * 14
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
    
    percent13 = div * 15
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
    
    percent14 = div * 16
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
    
    percent15 = div * 17
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
    
    percent16 = div * 18
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
    
    percent17 = div * 19
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
    
    percent18 = div * 20
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
    
    percent19 = div * 21
    ran20= P+percent19
    HEX20 = "%064x" % ran20
    wallet20 = Wallet(HEX20)
    uaddr20 = wallet20.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr20 = wallet20.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr20 = wallet20.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr20 = wallet20.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr20 = wallet20.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif20 = wallet20.key.__dict__['mainnet'].__dict__['wif']
    wifc20 = wallet20.key.__dict__['mainnet'].__dict__['wifc']
    
    percent20 = div * 22
    ran21= P+percent20
    HEX21 = "%064x" % ran21
    wallet21 = Wallet(HEX21)
    uaddr21 = wallet21.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr21 = wallet21.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr21 = wallet21.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr21 = wallet21.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr21 = wallet21.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif21 = wallet21.key.__dict__['mainnet'].__dict__['wif']
    wifc21 = wallet21.key.__dict__['mainnet'].__dict__['wifc']
    
    percent21 = div * 23
    ran22= P+percent21
    HEX22 = "%064x" % ran22
    wallet22 = Wallet(HEX22)
    uaddr22 = wallet22.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr22 = wallet22.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr22 = wallet22.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr22 = wallet22.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr22 = wallet22.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif22 = wallet22.key.__dict__['mainnet'].__dict__['wif']
    wifc22 = wallet22.key.__dict__['mainnet'].__dict__['wifc']
    
    percent22 = div * 24
    ran23= P+percent22
    HEX23 = "%064x" % ran23
    wallet23 = Wallet(HEX23)
    uaddr23 = wallet23.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr23 = wallet23.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr23 = wallet23.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr23 = wallet23.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr23 = wallet23.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif23 = wallet23.key.__dict__['mainnet'].__dict__['wif']
    wifc23 = wallet23.key.__dict__['mainnet'].__dict__['wifc']
    
    percent23 = div * 25
    ran24= P+percent23
    HEX24 = "%064x" % ran24
    wallet24 = Wallet(HEX24)
    uaddr24 = wallet24.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr24 = wallet24.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr24 = wallet24.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr24 = wallet24.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr24 = wallet24.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif24 = wallet24.key.__dict__['mainnet'].__dict__['wif']
    wifc24 = wallet24.key.__dict__['mainnet'].__dict__['wifc']
    
    percent24 = div * 26
    ran25= P+percent24
    HEX25 = "%064x" % ran25
    wallet25 = Wallet(HEX25)
    uaddr25 = wallet25.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr25 = wallet25.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr25 = wallet25.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr25 = wallet25.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr25 = wallet25.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif25 = wallet25.key.__dict__['mainnet'].__dict__['wif']
    wifc25 = wallet25.key.__dict__['mainnet'].__dict__['wifc']
    
    percent25 = div * 27
    ran26= P+percent25
    HEX26 = "%064x" % ran26
    wallet26 = Wallet(HEX26)
    uaddr26 = wallet26.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr26 = wallet26.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr26 = wallet26.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr26 = wallet26.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr26 = wallet26.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif26 = wallet26.key.__dict__['mainnet'].__dict__['wif']
    wifc26 = wallet26.key.__dict__['mainnet'].__dict__['wifc']
    
    percent26 = div * 28
    ran27= P+percent26
    HEX27 = "%064x" % ran27
    wallet27 = Wallet(HEX27)
    uaddr27 = wallet27.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr27 = wallet27.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr27 = wallet27.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr27 = wallet27.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr27 = wallet27.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif27 = wallet27.key.__dict__['mainnet'].__dict__['wif']
    wifc27 = wallet27.key.__dict__['mainnet'].__dict__['wifc']
    
    percent27 = div * 29
    ran28= P+percent27
    HEX28 = "%064x" % ran28
    wallet28 = Wallet(HEX28)
    uaddr28 = wallet28.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr28 = wallet28.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr28 = wallet28.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr28 = wallet28.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr28 = wallet28.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif28 = wallet28.key.__dict__['mainnet'].__dict__['wif']
    wifc28 = wallet28.key.__dict__['mainnet'].__dict__['wifc']
    
    percent28 = div * 30
    ran29= P+percent28
    HEX29 = "%064x" % ran29
    wallet29 = Wallet(HEX29)
    uaddr29 = wallet29.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr29 = wallet29.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr29 = wallet29.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr29 = wallet29.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr29 = wallet29.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif29 = wallet29.key.__dict__['mainnet'].__dict__['wif']
    wifc29 = wallet29.key.__dict__['mainnet'].__dict__['wifc']
    
    percent29 = div * 31
    ran30= P+percent29
    HEX30 = "%064x" % ran30
    wallet30 = Wallet(HEX30)
    uaddr30 = wallet30.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr30 = wallet30.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr30 = wallet30.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr30 = wallet30.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr30 = wallet30.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif30 = wallet30.key.__dict__['mainnet'].__dict__['wif']
    wifc30 = wallet30.key.__dict__['mainnet'].__dict__['wifc']
    
    percent30 = div * 32
    ran31= P+percent30
    HEX31 = "%064x" % ran31
    wallet31 = Wallet(HEX31)
    uaddr31 = wallet31.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr31 = wallet31.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr31 = wallet31.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr31 = wallet31.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr31 = wallet31.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif31 = wallet31.key.__dict__['mainnet'].__dict__['wif']
    wifc31 = wallet31.key.__dict__['mainnet'].__dict__['wifc']
    
    percent31 = div * 33
    ran32= P+percent31
    HEX32 = "%064x" % ran32
    wallet32 = Wallet(HEX32)
    uaddr32 = wallet32.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr32 = wallet32.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr32 = wallet32.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr32 = wallet32.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr32 = wallet32.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif32 = wallet32.key.__dict__['mainnet'].__dict__['wif']
    wifc32 = wallet32.key.__dict__['mainnet'].__dict__['wifc']
    
    percent32 = div * 34
    ran33= P+percent32
    HEX33 = "%064x" % ran33
    wallet33 = Wallet(HEX33)
    uaddr33 = wallet33.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr33 = wallet33.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr33 = wallet33.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr33 = wallet33.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr33 = wallet33.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif33 = wallet33.key.__dict__['mainnet'].__dict__['wif']
    wifc33 = wallet33.key.__dict__['mainnet'].__dict__['wifc']
    
    percent33 = div * 35
    ran34= P+percent33
    HEX34 = "%064x" % ran34
    wallet34 = Wallet(HEX34)
    uaddr34 = wallet34.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr34 = wallet34.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr34 = wallet34.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr34 = wallet34.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr34 = wallet34.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif34 = wallet34.key.__dict__['mainnet'].__dict__['wif']
    wifc34 = wallet34.key.__dict__['mainnet'].__dict__['wifc']
    
    percent34 = div * 36
    ran35= P+percent34
    HEX35 = "%064x" % ran35
    wallet35 = Wallet(HEX35)
    uaddr35 = wallet35.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr35 = wallet35.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr35 = wallet35.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr35 = wallet35.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr35 = wallet35.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif35 = wallet35.key.__dict__['mainnet'].__dict__['wif']
    wifc35 = wallet35.key.__dict__['mainnet'].__dict__['wifc']
    
    percent35 = div * 37
    ran36= P+percent35
    HEX36 = "%064x" % ran36
    wallet36 = Wallet(HEX36)
    uaddr36 = wallet36.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr36 = wallet36.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr36 = wallet36.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr36 = wallet36.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr36 = wallet36.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif36 = wallet36.key.__dict__['mainnet'].__dict__['wif']
    wifc36 = wallet36.key.__dict__['mainnet'].__dict__['wifc']
    
    percent36 = div * 38
    ran37= P+percent36
    HEX37 = "%064x" % ran37
    wallet37 = Wallet(HEX37)
    uaddr37 = wallet37.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr37 = wallet37.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr37 = wallet37.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr37 = wallet37.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr37 = wallet37.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif37 = wallet37.key.__dict__['mainnet'].__dict__['wif']
    wifc37 = wallet37.key.__dict__['mainnet'].__dict__['wifc']
    
    percent37 = div * 39
    ran38= P+percent37
    HEX38 = "%064x" % ran38
    wallet38 = Wallet(HEX38)
    uaddr38 = wallet38.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr38 = wallet38.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr38 = wallet38.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr38 = wallet38.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr38 = wallet38.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif38 = wallet38.key.__dict__['mainnet'].__dict__['wif']
    wifc38 = wallet38.key.__dict__['mainnet'].__dict__['wifc']
    
    percent38 = div * 40
    ran39= P+percent38
    HEX39 = "%064x" % ran39
    wallet39 = Wallet(HEX39)
    uaddr39 = wallet39.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr39 = wallet39.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr39 = wallet39.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr39 = wallet39.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr39 = wallet39.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif39 = wallet39.key.__dict__['mainnet'].__dict__['wif']
    wifc39 = wallet39.key.__dict__['mainnet'].__dict__['wifc']
    
    percent39 = div * 41
    ran40= P+percent39
    HEX40 = "%064x" % ran40
    wallet40 = Wallet(HEX40)
    uaddr40 = wallet40.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr40 = wallet40.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr40 = wallet40.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr40 = wallet40.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr40 = wallet40.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif40 = wallet40.key.__dict__['mainnet'].__dict__['wif']
    wifc40 = wallet40.key.__dict__['mainnet'].__dict__['wifc']
    
    percent40 = div * 42
    ran41= P+percent40
    HEX41 = "%064x" % ran41
    wallet41 = Wallet(HEX41)
    uaddr41 = wallet41.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr41 = wallet41.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr41 = wallet41.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr41 = wallet41.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr41 = wallet41.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif41 = wallet41.key.__dict__['mainnet'].__dict__['wif']
    wifc41 = wallet41.key.__dict__['mainnet'].__dict__['wifc']
    
    percent41 = div * 43
    ran42= P+percent41
    HEX42 = "%064x" % ran42
    wallet42 = Wallet(HEX42)
    uaddr42 = wallet42.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr42 = wallet42.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr42 = wallet42.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr42 = wallet42.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr42 = wallet42.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif42 = wallet42.key.__dict__['mainnet'].__dict__['wif']
    wifc42 = wallet42.key.__dict__['mainnet'].__dict__['wifc']
    
    percent42 = div * 44
    ran43= P+percent42
    HEX43 = "%064x" % ran43
    wallet43 = Wallet(HEX43)
    uaddr43 = wallet43.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr43 = wallet43.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr43 = wallet43.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr43 = wallet43.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr43 = wallet43.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif43 = wallet43.key.__dict__['mainnet'].__dict__['wif']
    wifc43 = wallet43.key.__dict__['mainnet'].__dict__['wifc']
    
    percent43 = div * 45
    ran44= P+percent43
    HEX44 = "%064x" % ran44
    wallet44 = Wallet(HEX44)
    uaddr44 = wallet44.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr44 = wallet44.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr44 = wallet44.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr44 = wallet44.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr44 = wallet44.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif44 = wallet44.key.__dict__['mainnet'].__dict__['wif']
    wifc44 = wallet44.key.__dict__['mainnet'].__dict__['wifc']
    
    percent44 = div * 46
    ran45= P+percent44
    HEX45 = "%064x" % ran45
    wallet45 = Wallet(HEX45)
    uaddr45 = wallet45.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr45 = wallet45.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr45 = wallet45.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr45 = wallet45.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr45 = wallet45.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif45 = wallet45.key.__dict__['mainnet'].__dict__['wif']
    wifc45 = wallet45.key.__dict__['mainnet'].__dict__['wifc']
    
    percent45 = div * 47
    ran46= P+percent45
    HEX46 = "%064x" % ran46
    wallet46 = Wallet(HEX46)
    uaddr46 = wallet46.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr46 = wallet46.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr46 = wallet46.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr46 = wallet46.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr46 = wallet46.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif46 = wallet46.key.__dict__['mainnet'].__dict__['wif']
    wifc46 = wallet46.key.__dict__['mainnet'].__dict__['wifc']
    
    percent46 = div * 48
    ran47= P+percent46
    HEX47 = "%064x" % ran47
    wallet47 = Wallet(HEX47)
    uaddr47 = wallet47.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr47 = wallet47.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr47 = wallet47.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr47 = wallet47.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr47 = wallet47.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif47 = wallet47.key.__dict__['mainnet'].__dict__['wif']
    wifc47 = wallet47.key.__dict__['mainnet'].__dict__['wifc']
    
    percent47 = div * 49
    ran48= P+percent47
    HEX48 = "%064x" % ran48
    wallet48 = Wallet(HEX48)
    uaddr48 = wallet48.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr48 = wallet48.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr48 = wallet48.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr48 = wallet48.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr48 = wallet48.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif48 = wallet48.key.__dict__['mainnet'].__dict__['wif']
    wifc48 = wallet48.key.__dict__['mainnet'].__dict__['wifc']
    
    percent48 = div * 50
    ran49= P+percent48
    HEX49 = "%064x" % ran49
    wallet49 = Wallet(HEX49)
    uaddr49 = wallet49.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr49 = wallet49.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr49 = wallet49.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr49 = wallet49.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr49 = wallet49.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif49 = wallet49.key.__dict__['mainnet'].__dict__['wif']
    wifc49 = wallet49.key.__dict__['mainnet'].__dict__['wifc']
    
    percent49 = div * 51
    ran50= P+percent49
    HEX50 = "%064x" % ran50
    wallet50 = Wallet(HEX50)
    uaddr50 = wallet50.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr50 = wallet50.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr50 = wallet50.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr50 = wallet50.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr50 = wallet50.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif50 = wallet50.key.__dict__['mainnet'].__dict__['wif']
    wifc50 = wallet50.key.__dict__['mainnet'].__dict__['wifc']
    
    percent50 = div * 52
    ran51= P+percent50
    HEX51 = "%064x" % ran51
    wallet51 = Wallet(HEX51)
    uaddr51 = wallet51.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr51 = wallet51.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr51 = wallet51.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr51 = wallet51.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr51 = wallet51.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif51 = wallet51.key.__dict__['mainnet'].__dict__['wif']
    wifc51 = wallet51.key.__dict__['mainnet'].__dict__['wifc']
    
    percent51 = div * 53
    ran52= P+percent51
    HEX52 = "%064x" % ran52
    wallet52 = Wallet(HEX52)
    uaddr52 = wallet52.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr52 = wallet52.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr52 = wallet52.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr52 = wallet52.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr52 = wallet52.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif52 = wallet52.key.__dict__['mainnet'].__dict__['wif']
    wifc52 = wallet52.key.__dict__['mainnet'].__dict__['wifc']
    
    percent52 = div * 54
    ran53= P+percent52
    HEX53 = "%064x" % ran53
    wallet53 = Wallet(HEX53)
    uaddr53 = wallet53.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr53 = wallet53.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr53 = wallet53.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr53 = wallet53.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr53 = wallet53.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif53 = wallet53.key.__dict__['mainnet'].__dict__['wif']
    wifc53 = wallet53.key.__dict__['mainnet'].__dict__['wifc']
    
    percent53 = div * 55
    ran54= P+percent53
    HEX54 = "%064x" % ran54
    wallet54 = Wallet(HEX54)
    uaddr54 = wallet54.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr54 = wallet54.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr54 = wallet54.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr54 = wallet54.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr54 = wallet54.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif54 = wallet54.key.__dict__['mainnet'].__dict__['wif']
    wifc54 = wallet54.key.__dict__['mainnet'].__dict__['wifc']
    
    percent54 = div * 56
    ran55= P+percent54
    HEX55 = "%064x" % ran55
    wallet55 = Wallet(HEX55)
    uaddr55 = wallet55.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr55 = wallet55.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr55 = wallet55.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr55 = wallet55.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr55 = wallet55.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif55 = wallet55.key.__dict__['mainnet'].__dict__['wif']
    wifc55 = wallet55.key.__dict__['mainnet'].__dict__['wifc']
    
    percent55 = div * 57
    ran56= P+percent55
    HEX56 = "%064x" % ran56
    wallet56 = Wallet(HEX56)
    uaddr56 = wallet56.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr56 = wallet56.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr56 = wallet56.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr56 = wallet56.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr56 = wallet56.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif56 = wallet56.key.__dict__['mainnet'].__dict__['wif']
    wifc56 = wallet56.key.__dict__['mainnet'].__dict__['wifc']
    
    percent56 = div * 58
    ran57= P+percent56
    HEX57 = "%064x" % ran57
    wallet57 = Wallet(HEX57)
    uaddr57 = wallet57.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr57 = wallet57.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr57 = wallet57.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr57 = wallet57.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr57 = wallet57.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif57 = wallet57.key.__dict__['mainnet'].__dict__['wif']
    wifc57 = wallet57.key.__dict__['mainnet'].__dict__['wifc']
    
    percent57 = div * 59
    ran58= P+percent57
    HEX58 = "%064x" % ran58
    wallet58 = Wallet(HEX58)
    uaddr58 = wallet58.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr58 = wallet58.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr58 = wallet58.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr58 = wallet58.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr58 = wallet58.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif58 = wallet58.key.__dict__['mainnet'].__dict__['wif']
    wifc58 = wallet58.key.__dict__['mainnet'].__dict__['wifc']
    
    percent58 = div * 60
    ran59= P+percent58
    HEX59 = "%064x" % ran59
    wallet59 = Wallet(HEX9)
    uaddr59 = wallet59.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr59 = wallet59.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr59 = wallet59.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr59 = wallet59.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr59 = wallet59.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif59 = wallet59.key.__dict__['mainnet'].__dict__['wif']
    wifc59 = wallet59.key.__dict__['mainnet'].__dict__['wifc']
    
    percent59 = div * 61
    ran60 = P+percent59
    HEX60 = "%064x" % ran60
    wallet60 = Wallet(HEX60)
    uaddr60 = wallet60.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr60 = wallet60.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr60 = wallet60.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr60 = wallet60.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr60 = wallet60.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif60 = wallet60.key.__dict__['mainnet'].__dict__['wif']
    wifc60 = wallet60.key.__dict__['mainnet'].__dict__['wifc']
    
    percent60 = div * 62
    ran61= P+percent60
    HEX61 = "%064x" % ran61
    wallet61 = Wallet(HEX61)
    uaddr61 = wallet61.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr61 = wallet61.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr61 = wallet61.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr61 = wallet61.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr61 = wallet61.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif61 = wallet61.key.__dict__['mainnet'].__dict__['wif']
    wifc61 = wallet61.key.__dict__['mainnet'].__dict__['wifc']
    
    percent61 = div * 63
    ran62= P+percent61
    HEX62 = "%064x" % ran62
    wallet62 = Wallet(HEX62)
    uaddr62 = wallet62.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr62 = wallet62.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr62 = wallet62.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr62 = wallet62.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr62 = wallet62.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif62 = wallet62.key.__dict__['mainnet'].__dict__['wif']
    wifc62 = wallet62.key.__dict__['mainnet'].__dict__['wifc']
    
    percent62 = div * 64
    ran63= P+percent62
    HEX63 = "%064x" % ran63
    wallet63 = Wallet(HEX63)
    uaddr63 = wallet63.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr63 = wallet63.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr63 = wallet63.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr63 = wallet63.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr63 = wallet63.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif63 = wallet63.key.__dict__['mainnet'].__dict__['wif']
    wifc63 = wallet63.key.__dict__['mainnet'].__dict__['wifc']
    
    percent63 = div * 65
    ran64= P+percent63
    HEX64 = "%064x" % ran64
    wallet64 = Wallet(HEX64)
    uaddr64 = wallet64.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr64 = wallet64.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr64 = wallet64.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr64 = wallet64.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr64 = wallet64.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif64 = wallet64.key.__dict__['mainnet'].__dict__['wif']
    wifc64 = wallet64.key.__dict__['mainnet'].__dict__['wifc']
    
    percent64 = div * 66
    ran65= P+percent64
    HEX65 = "%064x" % ran65
    wallet65 = Wallet(HEX65)
    uaddr65 = wallet65.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr65 = wallet65.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr65 = wallet65.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr65 = wallet65.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr65 = wallet65.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif65 = wallet65.key.__dict__['mainnet'].__dict__['wif']
    wifc65 = wallet65.key.__dict__['mainnet'].__dict__['wifc']
    
    percent65 = div * 67
    ran66 = P+percent65
    HEX66 = "%064x" % ran66
    wallet66 = Wallet(HEX66)
    uaddr66 = wallet66.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr66 = wallet66.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr66 = wallet66.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr66 = wallet66.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr66 = wallet66.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif66 = wallet66.key.__dict__['mainnet'].__dict__['wif']
    wifc66 = wallet66.key.__dict__['mainnet'].__dict__['wifc']
    
    percent66 = div * 68
    ran67 = P+percent66
    HEX67 = "%064x" % ran67
    wallet67 = Wallet(HEX67)
    uaddr67 = wallet67.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr67 = wallet67.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr67 = wallet67.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr67 = wallet67.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr67 = wallet67.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif67 = wallet67.key.__dict__['mainnet'].__dict__['wif']
    wifc67 = wallet67.key.__dict__['mainnet'].__dict__['wifc']
    
    percent67 = div * 69
    ran68 = P+percent67
    HEX68 = "%064x" % ran68
    wallet68 = Wallet(HEX68)
    uaddr68 = wallet68.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr68 = wallet68.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr68 = wallet68.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr68 = wallet68.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr68 = wallet68.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif68 = wallet68.key.__dict__['mainnet'].__dict__['wif']
    wifc68 = wallet68.key.__dict__['mainnet'].__dict__['wifc']
    
    percent68 = div * 70
    ran69= P+percent68
    HEX69 = "%064x" % ran69
    wallet69 = Wallet(HEX69)
    uaddr69 = wallet69.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr69 = wallet69.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr69 = wallet69.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr69 = wallet69.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr69 = wallet69.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif69 = wallet69.key.__dict__['mainnet'].__dict__['wif']
    wifc69 = wallet69.key.__dict__['mainnet'].__dict__['wifc']
    
    percent69 = div * 71
    ran70 = P+percent69
    HEX70 = "%064x" % ran70
    wallet70 = Wallet(HEX70)
    uaddr70 = wallet70.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr70 = wallet70.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr70 = wallet70.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr70 = wallet70.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr70 = wallet70.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif70 = wallet70.key.__dict__['mainnet'].__dict__['wif']
    wifc70 = wallet70.key.__dict__['mainnet'].__dict__['wifc']
    
    percent70 = div * 72
    ran71= P+percent70
    HEX71 = "%064x" % ran71
    wallet71 = Wallet(HEX71)
    uaddr71 = wallet71.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr71 = wallet71.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr71 = wallet71.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr71 = wallet71.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr71 = wallet71.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif71 = wallet71.key.__dict__['mainnet'].__dict__['wif']
    wifc71 = wallet71.key.__dict__['mainnet'].__dict__['wifc']
    
    percent71 = div * 73
    ran72= P+percent71
    HEX72 = "%064x" % ran72
    wallet72 = Wallet(HEX72)
    uaddr72 = wallet72.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr72 = wallet72.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr72 = wallet72.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr72 = wallet72.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr72 = wallet72.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif72 = wallet72.key.__dict__['mainnet'].__dict__['wif']
    wifc72 = wallet72.key.__dict__['mainnet'].__dict__['wifc']
    
    percent72 = div * 74
    ran73= P+percent72
    HEX73 = "%064x" % ran73
    wallet73 = Wallet(HEX73)
    uaddr73 = wallet73.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr73 = wallet73.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr73 = wallet73.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr73 = wallet73.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr73 = wallet73.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif73 = wallet73.key.__dict__['mainnet'].__dict__['wif']
    wifc73 = wallet73.key.__dict__['mainnet'].__dict__['wifc']
    
    percent73 = div * 75
    ran74= P+percent73
    HEX74 = "%064x" % ran74
    wallet74 = Wallet(HEX74)
    uaddr74 = wallet74.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr74 = wallet74.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr74 = wallet74.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr74 = wallet74.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr74 = wallet74.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif74 = wallet74.key.__dict__['mainnet'].__dict__['wif']
    wifc74 = wallet74.key.__dict__['mainnet'].__dict__['wifc']
    
    percent74 = div * 76
    ran75= P+percent74
    HEX75 = "%064x" % ran75
    wallet75 = Wallet(HEX75)
    uaddr75 = wallet75.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr75 = wallet75.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr75 = wallet75.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr75 = wallet75.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr75 = wallet75.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif75 = wallet75.key.__dict__['mainnet'].__dict__['wif']
    wifc75 = wallet75.key.__dict__['mainnet'].__dict__['wifc']
    
    percent75 = div * 77
    ran76= P+percent75
    HEX76 = "%064x" % ran76
    wallet76 = Wallet(HEX76)
    uaddr76 = wallet76.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr76 = wallet76.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr76 = wallet76.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr76 = wallet76.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr76 = wallet76.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif76 = wallet76.key.__dict__['mainnet'].__dict__['wif']
    wifc76 = wallet76.key.__dict__['mainnet'].__dict__['wifc']
    
    percent76 = div * 78
    ran77= P+percent76
    HEX77 = "%064x" % ran77
    wallet77 = Wallet(HEX77)
    uaddr77 = wallet77.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr77 = wallet77.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr77 = wallet77.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr77 = wallet77.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr77 = wallet77.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif77 = wallet77.key.__dict__['mainnet'].__dict__['wif']
    wifc77 = wallet77.key.__dict__['mainnet'].__dict__['wifc']
    
    percent77 = div * 79
    ran78= P+percent77
    HEX78 = "%064x" % ran78
    wallet78 = Wallet(HEX78)
    uaddr78 = wallet78.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr78 = wallet78.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr78 = wallet78.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr78 = wallet78.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr78 = wallet78.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif78 = wallet78.key.__dict__['mainnet'].__dict__['wif']
    wifc78 = wallet78.key.__dict__['mainnet'].__dict__['wifc']
    
    percent78 = div * 80
    ran79= P+percent78
    HEX79 = "%064x" % ran79
    wallet79 = Wallet(HEX79)
    uaddr79 = wallet79.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr79 = wallet79.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr79 = wallet79.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr79 = wallet79.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr79 = wallet79.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif79 = wallet79.key.__dict__['mainnet'].__dict__['wif']
    wifc79 = wallet79.key.__dict__['mainnet'].__dict__['wifc']
    
    percent79 = div * 81
    ran80 = P+percent79
    HEX80 = "%064x" % ran80
    wallet80 = Wallet(HEX80)
    uaddr80 = wallet80.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr80 = wallet80.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr80 = wallet80.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr80 = wallet80.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr80 = wallet80.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif80 = wallet80.key.__dict__['mainnet'].__dict__['wif']
    wifc80 = wallet80.key.__dict__['mainnet'].__dict__['wifc']
    
    percent80 = div * 82
    ran81= P+percent80
    HEX81 = "%064x" % ran81
    wallet81 = Wallet(HEX81)
    uaddr81 = wallet81.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr81 = wallet81.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr81 = wallet81.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr81 = wallet81.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr81 = wallet81.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif81 = wallet81.key.__dict__['mainnet'].__dict__['wif']
    wifc81 = wallet81.key.__dict__['mainnet'].__dict__['wifc']
    
    percent81 = div * 83
    ran82= P+percent81
    HEX82 = "%064x" % ran82
    wallet82 = Wallet(HEX82)
    uaddr82 = wallet82.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr82 = wallet82.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr82 = wallet82.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr82 = wallet82.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr82 = wallet82.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif82 = wallet82.key.__dict__['mainnet'].__dict__['wif']
    wifc82 = wallet82.key.__dict__['mainnet'].__dict__['wifc']
    
    percent82 = div * 84
    ran83= P+percent82
    HEX83 = "%064x" % ran83
    wallet83 = Wallet(HEX83)
    uaddr83 = wallet83.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr83 = wallet83.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr83 = wallet83.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr83 = wallet83.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr83 = wallet83.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif83 = wallet83.key.__dict__['mainnet'].__dict__['wif']
    wifc83 = wallet83.key.__dict__['mainnet'].__dict__['wifc']
    
    percent83 = div * 85
    ran84= P+percent83
    HEX84 = "%064x" % ran84
    wallet84 = Wallet(HEX84)
    uaddr84 = wallet84.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr84 = wallet84.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr84 = wallet84.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr84 = wallet84.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr84 = wallet84.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif84 = wallet84.key.__dict__['mainnet'].__dict__['wif']
    wifc84 = wallet84.key.__dict__['mainnet'].__dict__['wifc']
    
    percent84 = div * 86
    ran85= P+percent84
    HEX85 = "%064x" % ran85
    wallet85 = Wallet(HEX85)
    uaddr85 = wallet85.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr85 = wallet85.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr85 = wallet85.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr85 = wallet85.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr85 = wallet85.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif85 = wallet85.key.__dict__['mainnet'].__dict__['wif']
    wifc85 = wallet85.key.__dict__['mainnet'].__dict__['wifc']
    
    percent85 = div * 87
    ran86= P+percent85
    HEX86 = "%064x" % ran86
    wallet86 = Wallet(HEX86)
    uaddr86 = wallet86.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr86 = wallet86.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr86 = wallet86.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr86 = wallet86.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr86 = wallet86.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif86 = wallet86.key.__dict__['mainnet'].__dict__['wif']
    wifc86 = wallet86.key.__dict__['mainnet'].__dict__['wifc']
    
    percent86 = div * 88
    ran87= P+percent86
    HEX87 = "%064x" % ran87
    wallet87 = Wallet(HEX87)
    uaddr87 = wallet87.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr87 = wallet87.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr87 = wallet87.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr87 = wallet87.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr87 = wallet87.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif87 = wallet87.key.__dict__['mainnet'].__dict__['wif']
    wifc87 = wallet87.key.__dict__['mainnet'].__dict__['wifc']
    
    percent87 = div * 89
    ran88= P+percent87
    HEX88 = "%064x" % ran88
    wallet88 = Wallet(HEX88)
    uaddr88 = wallet88.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr88 = wallet88.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr88 = wallet88.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr88 = wallet88.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr88 = wallet88.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif88 = wallet88.key.__dict__['mainnet'].__dict__['wif']
    wifc88 = wallet88.key.__dict__['mainnet'].__dict__['wifc']
    
    percent88 = div * 90
    ran89= P+percent88
    HEX89 = "%064x" % ran89
    wallet89 = Wallet(HEX89)
    uaddr89 = wallet89.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr89 = wallet89.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr89 = wallet89.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr89 = wallet89.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr89 = wallet89.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif89 = wallet89.key.__dict__['mainnet'].__dict__['wif']
    wifc89 = wallet89.key.__dict__['mainnet'].__dict__['wifc']
    
    percent89 = div * 91
    ran90 = P+percent89
    HEX90 = "%064x" % ran90
    wallet90 = Wallet(HEX90)
    uaddr90 = wallet90.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr90 = wallet90.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr90 = wallet90.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr90 = wallet90.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr90 = wallet90.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif90 = wallet90.key.__dict__['mainnet'].__dict__['wif']
    wifc90 = wallet90.key.__dict__['mainnet'].__dict__['wifc']
    
    percent90 = div * 92
    ran91= P+percent90
    HEX91 = "%064x" % ran91
    wallet91 = Wallet(HEX91)
    uaddr91 = wallet91.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr91 = wallet91.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr91 = wallet91.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr91 = wallet91.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr91 = wallet91.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif91 = wallet91.key.__dict__['mainnet'].__dict__['wif']
    wifc91 = wallet91.key.__dict__['mainnet'].__dict__['wifc']
    
    percent91 = div * 93
    ran92= P+percent91
    HEX92 = "%064x" % ran92
    wallet92 = Wallet(HEX92)
    uaddr92 = wallet92.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr92 = wallet92.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr92 = wallet92.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr92 = wallet92.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr92 = wallet92.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif92 = wallet92.key.__dict__['mainnet'].__dict__['wif']
    wifc92 = wallet92.key.__dict__['mainnet'].__dict__['wifc']
    
    percent92 = div * 94
    ran93= P+percent92
    HEX93 = "%064x" % ran93
    wallet93 = Wallet(HEX93)
    uaddr93 = wallet93.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr93 = wallet93.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr93 = wallet93.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr93 = wallet93.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr93 = wallet93.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif93 = wallet93.key.__dict__['mainnet'].__dict__['wif']
    wifc93 = wallet93.key.__dict__['mainnet'].__dict__['wifc']
    
    percent93 = div * 95
    ran94= P+percent93
    HEX94 = "%064x" % ran94
    wallet94 = Wallet(HEX94)
    uaddr94 = wallet94.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr94 = wallet94.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr94 = wallet94.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr94 = wallet94.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr94 = wallet94.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif94 = wallet94.key.__dict__['mainnet'].__dict__['wif']
    wifc94 = wallet94.key.__dict__['mainnet'].__dict__['wifc']
    
    percent94 = div * 96
    ran95= P+percent94
    HEX95 = "%064x" % ran95
    wallet95 = Wallet(HEX95)
    uaddr95 = wallet95.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr95 = wallet95.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr95 = wallet95.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr95 = wallet95.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr95 = wallet95.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif95 = wallet95.key.__dict__['mainnet'].__dict__['wif']
    wifc95 = wallet95.key.__dict__['mainnet'].__dict__['wifc']
    
    percent95 = div * 97
    ran96= P+percent95
    HEX96 = "%064x" % ran96
    wallet96 = Wallet(HEX96)
    uaddr96 = wallet96.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr96 = wallet96.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr96 = wallet96.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr96 = wallet96.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr96 = wallet96.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif96 = wallet96.key.__dict__['mainnet'].__dict__['wif']
    wifc96 = wallet96.key.__dict__['mainnet'].__dict__['wifc']
    
    percent96 = div * 98
    ran97= P+percent96
    HEX97 = "%064x" % ran97
    wallet97 = Wallet(HEX97)
    uaddr97 = wallet97.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr97 = wallet97.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr97 = wallet97.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr97 = wallet97.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr97 = wallet97.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif97 = wallet97.key.__dict__['mainnet'].__dict__['wif']
    wifc97 = wallet97.key.__dict__['mainnet'].__dict__['wifc']
    
    percent97 = div * 99
    ran98= P+percent97
    HEX98 = "%064x" % ran98
    wallet98 = Wallet(HEX98)
    uaddr98 = wallet98.address.__dict__['mainnet'].__dict__['pubaddr1'] #Legacy uncompressed address
    caddr98 = wallet98.address.__dict__['mainnet'].__dict__['pubaddr1c'] #Legacy compressed address
    saddr98 = wallet98.address.__dict__['mainnet'].__dict__['pubaddr3'] #segwit_address
    bcaddr98 = wallet98.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WPKH'] 
    bc1addr98 = wallet98.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH'] 
    wif98 = wallet98.key.__dict__['mainnet'].__dict__['wif']
    wifc98 = wallet98.key.__dict__['mainnet'].__dict__['wifc']
    
    
    print('Scan: ', count , ' :Remaining: ', str(remaining), ' :Total: ', str(total), end='\r')
    #print('\n :HEX    : ', HEX, '\n :HEX 5%: ', HEX4, '\n :HEX 10%: ', HEX9, '\n :HEX 15%: ', HEX14, '\n :HEX 20%: ', HEX19, '\n :HEX 25%: ', HEX24, '\n :HEX 30%: ', HEX29, '\n :HEX 35%: ', HEX34, '\n :HEX 40%: ', HEX39, '\n :HEX 45%: ', HEX44, '\n :HEX 50%: ', HEX49, '\n :HEX 55%: ', HEX54, '\n :HEX 60%: ', HEX59, '\n :HEX 65%: ', HEX64, '\n :HEX 70%: ', HEX69, '\n :HEX 75%: ', HEX74, '\n :HEX 80%: ', HEX79, '\n :HEX 85%: ', HEX84, '\n :HEX 90%: ', HEX89, '\n :HEX 95%: ', HEX94)

    if caddr in add or uaddr in add or saddr in add or bcaddr in add or bc1addr in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran,'\nPrivatekey (hex): ', HEX, '\nPrivatekey Uncompressed: ', wif, '\nPrivatekey compressed: ', wifc, '\nPublic Address 1 Uncompressed: ', uaddr, '\nPublic Address 1 Compressed: ', caddr, '\nPublic Address 3 Segwit: ', saddr, '\nPublic Address bc1 P2WPKH: ', bcaddr, '\nPublic Address bc1 P2WSH: ', bc1addr)
        
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
        f.close()
        
    if caddr1 in add or uaddr1 in add or saddr1 in add or bcaddr1 in add or bc1addr1 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran1,'\nPrivatekey (hex): ', HEX1, '\nPrivatekey Uncompressed: ', wif1, '\nPrivatekey compressed: ', wifc1, '\nPublic Address 1 Uncompressed: ', uaddr1, '\nPublic Address 1 Compressed: ', caddr1, '\nPublic Address 3 Segwit: ', saddr1, '\nPublic Address bc1 P2WPKH: ', bcaddr1, '\nPublic Address bc1 P2WSH: ', bc1addr1)
        
        f=open("winner.txt","a")
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
        f.close()
        
    if caddr2 in add or uaddr2 in add or saddr2 in add or bcaddr2 in add or bc1addr2 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran2,'\nPrivatekey (hex): ', HEX2, '\nPrivatekey Uncompressed: ', wif2, '\nPrivatekey compressed: ', wifc2, '\nPublic Address 1 Uncompressed: ', uaddr2, '\nPublic Address 1 Compressed: ', caddr2, '\nPublic Address 3 Segwit: ', saddr2, '\nPublic Address bc1 P2WPKH: ', bcaddr2, '\nPublic Address bc1 P2WSH: ', bc1addr2)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr3 in add or uaddr3 in add or saddr3 in add or bcaddr3 in add or bc1addr3 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran3,'\nPrivatekey (hex): ', HEX3, '\nPrivatekey Uncompressed: ', wif3, '\nPrivatekey compressed: ', wifc3, '\nPublic Address 1 Uncompressed: ', uaddr3, '\nPublic Address 1 Compressed: ', caddr3, '\nPublic Address 3 Segwit: ', saddr3, '\nPublic Address bc1 P2WPKH: ', bcaddr3, '\nPublic Address bc1 P2WSH: ', bc1addr3)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr4 in add or uaddr4 in add or saddr4 in add or bcaddr4 in add or bc1addr4 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran4,'\nPrivatekey (hex): ', HEX4, '\nPrivatekey Uncompressed: ', wif4, '\nPrivatekey compressed: ', wifc4, '\nPublic Address 1 Uncompressed: ', uaddr4, '\nPublic Address 1 Compressed: ', caddr4, '\nPublic Address 3 Segwit: ', saddr4, '\nPublic Address bc1 P2WPKH: ', bcaddr4, '\nPublic Address bc1 P2WSH: ', bc1addr4)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr5 in add or uaddr5 in add or saddr5 in add or bcaddr5 in add or bc1addr5 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran5,'\nPrivatekey (hex): ', HEX5, '\nPrivatekey Uncompressed: ', wif5, '\nPrivatekey compressed: ', wifc5, '\nPublic Address 1 Uncompressed: ', uaddr5, '\nPublic Address 1 Compressed: ', caddr5, '\nPublic Address 3 Segwit: ', saddr5, '\nPublic Address bc1 P2WPKH: ', bcaddr5, '\nPublic Address bc1 P2WSH: ', bc1addr5)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr6 in add or uaddr6 in add or saddr6 in add or bcaddr6 in add or bc1addr6 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran6,'\nPrivatekey (hex): ', HEX6, '\nPrivatekey Uncompressed: ', wif6, '\nPrivatekey compressed: ', wifc6, '\nPublic Address 1 Uncompressed: ', uaddr6, '\nPublic Address 1 Compressed: ', caddr6, '\nPublic Address 3 Segwit: ', saddr6, '\nPublic Address bc1 P2WPKH: ', bcaddr6, '\nPublic Address bc1 P2WSH: ', bc1addr6)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr7 in add or uaddr7 in add or saddr7 in add or bcaddr7 in add or bc1addr7 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran7,'\nPrivatekey (hex): ', HEX7, '\nPrivatekey Uncompressed: ', wif7, '\nPrivatekey compressed: ', wifc7, '\nPublic Address 1 Uncompressed: ', uaddr7, '\nPublic Address 1 Compressed: ', caddr7, '\nPublic Address 3 Segwit: ', saddr7, '\nPublic Address bc1 P2WPKH: ', bcaddr7, '\nPublic Address bc1 P2WSH: ', bc1addr7)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr8 in add or uaddr8 in add or saddr8 in add or bcaddr8 in add or bc1addr8 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran8,'\nPrivatekey (hex): ', HEX8, '\nPrivatekey Uncompressed: ', wif8, '\nPrivatekey compressed: ', wifc8, '\nPublic Address 1 Uncompressed: ', uaddr8, '\nPublic Address 1 Compressed: ', caddr8, '\nPublic Address 3 Segwit: ', saddr8, '\nPublic Address bc1 P2WPKH: ', bcaddr8, '\nPublic Address bc1 P2WSH: ', bc1addr8)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr9 in add or uaddr9 in add or saddr9 in add or bcaddr9 in add or bc1addr9 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran9,'\nPrivatekey (hex): ', HEX9, '\nPrivatekey Uncompressed: ', wif9, '\nPrivatekey compressed: ', wifc9, '\nPublic Address 1 Uncompressed: ', uaddr9, '\nPublic Address 1 Compressed: ', caddr9, '\nPublic Address 3 Segwit: ', saddr9, '\nPublic Address bc1 P2WPKH: ', bcaddr9, '\nPublic Address bc1 P2WSH: ', bc1addr9)
        
        f=open("winner.txt","a")
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
        f.close()
        
    if caddr10 in add or uaddr10 in add or saddr10 in add or bcaddr10 in add or bc1addr10 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran10,'\nPrivatekey (hex): ', HEX10, '\nPrivatekey Uncompressed: ', wif10, '\nPrivatekey compressed: ', wifc10, '\nPublic Address 1 Uncompressed: ', uaddr10, '\nPublic Address 1 Compressed: ', caddr10, '\nPublic Address 3 Segwit: ', saddr10, '\nPublic Address bc1 P2WPKH: ', bcaddr10, '\nPublic Address bc1 P2WSH: ', bc1addr10)
        
        f=open("winner.txt","a")
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
        f.close()
        
    if caddr11 in add or uaddr11 in add or saddr11 in add or bcaddr11 in add or bc1addr11 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran11,'\nPrivatekey (hex): ', HEX11, '\nPrivatekey Uncompressed: ', wif11, '\nPrivatekey compressed: ', wifc11, '\nPublic Address 1 Uncompressed: ', uaddr11, '\nPublic Address 1 Compressed: ', caddr11, '\nPublic Address 3 Segwit: ', saddr11, '\nPublic Address bc1 P2WPKH: ', bcaddr11, '\nPublic Address bc1 P2WSH: ', bc1addr11)
        
        f=open("winner.txt","a")
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
        f.close()
        
    if caddr12 in add or uaddr12 in add or saddr12 in add or bcaddr12 in add or bc1addr12 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran12,'\nPrivatekey (hex): ', HEX12, '\nPrivatekey Uncompressed: ', wif12, '\nPrivatekey compressed: ', wifc12, '\nPublic Address 1 Uncompressed: ', uaddr12, '\nPublic Address 1 Compressed: ', caddr12, '\nPublic Address 3 Segwit: ', saddr12, '\nPublic Address bc1 P2WPKH: ', bcaddr12, '\nPublic Address bc1 P2WSH: ', bc1addr12)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr13 in add or uaddr13 in add or saddr13 in add or bcaddr13 in add or bc1addr13 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran13,'\nPrivatekey (hex): ', HEX13, '\nPrivatekey Uncompressed: ', wif13, '\nPrivatekey compressed: ', wifc13, '\nPublic Address 1 Uncompressed: ', uaddr13, '\nPublic Address 1 Compressed: ', caddr13, '\nPublic Address 3 Segwit: ', saddr13, '\nPublic Address bc1 P2WPKH: ', bcaddr13, '\nPublic Address bc1 P2WSH: ', bc1addr13)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr14 in add or uaddr14 in add or saddr14 in add or bcaddr14 in add or bc1addr14 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran14,'\nPrivatekey (hex): ', HEX14, '\nPrivatekey Uncompressed: ', wif14, '\nPrivatekey compressed: ', wifc14, '\nPublic Address 1 Uncompressed: ', uaddr14, '\nPublic Address 1 Compressed: ', caddr14, '\nPublic Address 3 Segwit: ', saddr14, '\nPublic Address bc1 P2WPKH: ', bcaddr14, '\nPublic Address bc1 P2WSH: ', bc1addr14)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr15 in add or uaddr15 in add or saddr15 in add or bcaddr15 in add or bc1addr15 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran15,'\nPrivatekey (hex): ', HEX15, '\nPrivatekey Uncompressed: ', wif15, '\nPrivatekey compressed: ', wifc15, '\nPublic Address 1 Uncompressed: ', uaddr15, '\nPublic Address 1 Compressed: ', caddr15, '\nPublic Address 3 Segwit: ', saddr15, '\nPublic Address bc1 P2WPKH: ', bcaddr15, '\nPublic Address bc1 P2WSH: ', bc1addr15)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr16 in add or uaddr16 in add or saddr16 in add or bcaddr16 in add or bc1addr16 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran16,'\nPrivatekey (hex): ', HEX16, '\nPrivatekey Uncompressed: ', wif16, '\nPrivatekey compressed: ', wifc16, '\nPublic Address 1 Uncompressed: ', uaddr16, '\nPublic Address 1 Compressed: ', caddr16, '\nPublic Address 3 Segwit: ', saddr16, '\nPublic Address bc1 P2WPKH: ', bcaddr16, '\nPublic Address bc1 P2WSH: ', bc1addr16)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr17 in add or uaddr17 in add or saddr17 in add or bcaddr17 in add or bc1addr17 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran17,'\nPrivatekey (hex): ', HEX17, '\nPrivatekey Uncompressed: ', wif17, '\nPrivatekey compressed: ', wifc17, '\nPublic Address 1 Uncompressed: ', uaddr17, '\nPublic Address 1 Compressed: ', caddr17, '\nPublic Address 3 Segwit: ', saddr17, '\nPublic Address bc1 P2WPKH: ', bcaddr17, '\nPublic Address bc1 P2WSH: ', bc1addr17)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr18 in add or uaddr18 in add or saddr18 in add or bcaddr18 in add or bc1addr18 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran18,'\nPrivatekey (hex): ', HEX18, '\nPrivatekey Uncompressed: ', wif18, '\nPrivatekey compressed: ', wifc18, '\nPublic Address 1 Uncompressed: ', uaddr18, '\nPublic Address 1 Compressed: ', caddr18, '\nPublic Address 3 Segwit: ', saddr18, '\nPublic Address bc1 P2WPKH: ', bcaddr18, '\nPublic Address bc1 P2WSH: ', bc1addr18)
        
        f=open("winner.txt","a")
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
        f.close()

    if caddr19 in add or uaddr19 in add or saddr19 in add or bcaddr19 in add or bc1addr19 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran19,'\nPrivatekey (hex): ', HEX19, '\nPrivatekey Uncompressed: ', wif19, '\nPrivatekey compressed: ', wifc19, '\nPublic Address 1 Uncompressed: ', uaddr19, '\nPublic Address 1 Compressed: ', caddr19, '\nPublic Address 3 Segwit: ', saddr19, '\nPublic Address bc1 P2WPKH: ', bcaddr19, '\nPublic Address bc1 P2WSH: ', bc1addr19)
        
        f=open("winner.txt","a")
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
        
    if caddr20 in add or uaddr20 in add or saddr20 in add or bcaddr20 in add or bc1addr20 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran20,'\nPrivatekey (hex): ', HEX20, '\nPrivatekey Uncompressed: ', wif20, '\nPrivatekey compressed: ', wifc20, '\nPublic Address 1 Uncompressed: ', uaddr20, '\nPublic Address 1 Compressed: ', caddr20, '\nPublic Address 3 Segwit: ', saddr20, '\nPublic Address bc1 P2WPKH: ', bcaddr20, '\nPublic Address bc1 P2WSH: ', bc1addr20)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran20))
        f.write('\nPrivatekey (hex): ' + HEX20)
        f.write('\nPrivatekey Uncompressed: ' + wif20)
        f.write('\nPrivatekey compressed: ' + wifc20)
        f.write('\nPublic Address 1 Compressed: ' + caddr20)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr20)
        f.write('\nPublic Address 3 Segwit: ' + saddr20)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr20)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr20)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr21 in add or uaddr21 in add or saddr21 in add or bcaddr21 in add or bc1addr21 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran21,'\nPrivatekey (hex): ', HEX21, '\nPrivatekey Uncompressed: ', wif21, '\nPrivatekey compressed: ', wifc21, '\nPublic Address 1 Uncompressed: ', uaddr21, '\nPublic Address 1 Compressed: ', caddr21, '\nPublic Address 3 Segwit: ', saddr21, '\nPublic Address bc1 P2WPKH: ', bcaddr21, '\nPublic Address bc1 P2WSH: ', bc1addr21)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran21))
        f.write('\nPrivatekey (hex): ' + HEX21)
        f.write('\nPrivatekey Uncompressed: ' + wif21)
        f.write('\nPrivatekey compressed: ' + wifc21)
        f.write('\nPublic Address 1 Compressed: ' + caddr21)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr21)
        f.write('\nPublic Address 3 Segwit: ' + saddr21)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr21)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr21)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr22 in add or uaddr22 in add or saddr22 in add or bcaddr22 in add or bc1addr22 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran22,'\nPrivatekey (hex): ', HEX22, '\nPrivatekey Uncompressed: ', wif22, '\nPrivatekey compressed: ', wifc22, '\nPublic Address 1 Uncompressed: ', uaddr22, '\nPublic Address 1 Compressed: ', caddr22, '\nPublic Address 3 Segwit: ', saddr22, '\nPublic Address bc1 P2WPKH: ', bcaddr22, '\nPublic Address bc1 P2WSH: ', bc1addr22)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran22))
        f.write('\nPrivatekey (hex): ' + HEX22)
        f.write('\nPrivatekey Uncompressed: ' + wif22)
        f.write('\nPrivatekey compressed: ' + wifc22)
        f.write('\nPublic Address 1 Compressed: ' + caddr22)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr22)
        f.write('\nPublic Address 3 Segwit: ' + saddr22)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr22)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr22)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr23 in add or uaddr23 in add or saddr23 in add or bcaddr23 in add or bc1addr23 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran23,'\nPrivatekey (hex): ', HEX23, '\nPrivatekey Uncompressed: ', wif23, '\nPrivatekey compressed: ', wifc23, '\nPublic Address 1 Uncompressed: ', uaddr23, '\nPublic Address 1 Compressed: ', caddr23, '\nPublic Address 3 Segwit: ', saddr23, '\nPublic Address bc1 P2WPKH: ', bcaddr23, '\nPublic Address bc1 P2WSH: ', bc1addr23)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran23))
        f.write('\nPrivatekey (hex): ' + HEX23)
        f.write('\nPrivatekey Uncompressed: ' + wif23)
        f.write('\nPrivatekey compressed: ' + wifc23)
        f.write('\nPublic Address 1 Compressed: ' + caddr23)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr23)
        f.write('\nPublic Address 3 Segwit: ' + saddr23)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr23)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr23)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr24 in add or uaddr24 in add or saddr24 in add or bcaddr24 in add or bc1addr24 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran24,'\nPrivatekey (hex): ', HEX24, '\nPrivatekey Uncompressed: ', wif24, '\nPrivatekey compressed: ', wifc24, '\nPublic Address 1 Uncompressed: ', uaddr24, '\nPublic Address 1 Compressed: ', caddr24, '\nPublic Address 3 Segwit: ', saddr24, '\nPublic Address bc1 P2WPKH: ', bcaddr24, '\nPublic Address bc1 P2WSH: ', bc1addr24)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran24))
        f.write('\nPrivatekey (hex): ' + HEX24)
        f.write('\nPrivatekey Uncompressed: ' + wif24)
        f.write('\nPrivatekey compressed: ' + wifc24)
        f.write('\nPublic Address 1 Compressed: ' + caddr24)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr24)
        f.write('\nPublic Address 3 Segwit: ' + saddr24)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr24)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr24)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr25 in add or uaddr25 in add or saddr25 in add or bcaddr25 in add or bc1addr25 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran25,'\nPrivatekey (hex): ', HEX25, '\nPrivatekey Uncompressed: ', wif25, '\nPrivatekey compressed: ', wifc25, '\nPublic Address 1 Uncompressed: ', uaddr25, '\nPublic Address 1 Compressed: ', caddr25, '\nPublic Address 3 Segwit: ', saddr25, '\nPublic Address bc1 P2WPKH: ', bcaddr25, '\nPublic Address bc1 P2WSH: ', bc1addr25)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran25))
        f.write('\nPrivatekey (hex): ' + HEX25)
        f.write('\nPrivatekey Uncompressed: ' + wif25)
        f.write('\nPrivatekey compressed: ' + wifc25)
        f.write('\nPublic Address 1 Compressed: ' + caddr25)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr25)
        f.write('\nPublic Address 3 Segwit: ' + saddr25)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr25)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr25)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr26 in add or uaddr26 in add or saddr26 in add or bcaddr26 in add or bc1addr26 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran26,'\nPrivatekey (hex): ', HEX26, '\nPrivatekey Uncompressed: ', wif26, '\nPrivatekey compressed: ', wifc26, '\nPublic Address 1 Uncompressed: ', uaddr26, '\nPublic Address 1 Compressed: ', caddr26, '\nPublic Address 3 Segwit: ', saddr26, '\nPublic Address bc1 P2WPKH: ', bcaddr26, '\nPublic Address bc1 P2WSH: ', bc1addr26)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran26))
        f.write('\nPrivatekey (hex): ' + HEX26)
        f.write('\nPrivatekey Uncompressed: ' + wif26)
        f.write('\nPrivatekey compressed: ' + wifc26)
        f.write('\nPublic Address 1 Compressed: ' + caddr26)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr26)
        f.write('\nPublic Address 3 Segwit: ' + saddr26)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr26)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr26)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr27 in add or uaddr27 in add or saddr27 in add or bcaddr27 in add or bc1addr27 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran27,'\nPrivatekey (hex): ', HEX27, '\nPrivatekey Uncompressed: ', wif27, '\nPrivatekey compressed: ', wifc27, '\nPublic Address 1 Uncompressed: ', uaddr27, '\nPublic Address 1 Compressed: ', caddr27, '\nPublic Address 3 Segwit: ', saddr27, '\nPublic Address bc1 P2WPKH: ', bcaddr27, '\nPublic Address bc1 P2WSH: ', bc1addr27)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran27))
        f.write('\nPrivatekey (hex): ' + HEX27)
        f.write('\nPrivatekey Uncompressed: ' + wif27)
        f.write('\nPrivatekey compressed: ' + wifc27)
        f.write('\nPublic Address 1 Compressed: ' + caddr27)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr27)
        f.write('\nPublic Address 3 Segwit: ' + saddr27)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr27)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr27)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr28 in add or uaddr28 in add or saddr28 in add or bcaddr28 in add or bc1addr28 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran28,'\nPrivatekey (hex): ', HEX28, '\nPrivatekey Uncompressed: ', wif28, '\nPrivatekey compressed: ', wifc28, '\nPublic Address 1 Uncompressed: ', uaddr28, '\nPublic Address 1 Compressed: ', caddr28, '\nPublic Address 3 Segwit: ', saddr28, '\nPublic Address bc1 P2WPKH: ', bcaddr28, '\nPublic Address bc1 P2WSH: ', bc1addr28)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran28))
        f.write('\nPrivatekey (hex): ' + HEX28)
        f.write('\nPrivatekey Uncompressed: ' + wif28)
        f.write('\nPrivatekey compressed: ' + wifc28)
        f.write('\nPublic Address 1 Compressed: ' + caddr28)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr28)
        f.write('\nPublic Address 3 Segwit: ' + saddr28)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr28)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr28)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr29 in add or uaddr29 in add or saddr29 in add or bcaddr29 in add or bc1addr29 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran29,'\nPrivatekey (hex): ', HEX29, '\nPrivatekey Uncompressed: ', wif29, '\nPrivatekey compressed: ', wifc29, '\nPublic Address 1 Uncompressed: ', uaddr29, '\nPublic Address 1 Compressed: ', caddr29, '\nPublic Address 3 Segwit: ', saddr29, '\nPublic Address bc1 P2WPKH: ', bcaddr29, '\nPublic Address bc1 P2WSH: ', bc1addr29)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran29))
        f.write('\nPrivatekey (hex): ' + HEX29)
        f.write('\nPrivatekey Uncompressed: ' + wif29)
        f.write('\nPrivatekey compressed: ' + wifc29)
        f.write('\nPublic Address 1 Compressed: ' + caddr29)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr29)
        f.write('\nPublic Address 3 Segwit: ' + saddr29)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr29)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr29)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr30 in add or uaddr30 in add or saddr30 in add or bcaddr30 in add or bc1addr30 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran30,'\nPrivatekey (hex): ', HEX30, '\nPrivatekey Uncompressed: ', wif30, '\nPrivatekey compressed: ', wifc30, '\nPublic Address 1 Uncompressed: ', uaddr30, '\nPublic Address 1 Compressed: ', caddr30, '\nPublic Address 3 Segwit: ', saddr30, '\nPublic Address bc1 P2WPKH: ', bcaddr30, '\nPublic Address bc1 P2WSH: ', bc1addr30)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran30))
        f.write('\nPrivatekey (hex): ' + HEX30)
        f.write('\nPrivatekey Uncompressed: ' + wif30)
        f.write('\nPrivatekey compressed: ' + wifc30)
        f.write('\nPublic Address 1 Compressed: ' + caddr30)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr30)
        f.write('\nPublic Address 3 Segwit: ' + saddr30)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr30)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr30)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr31 in add or uaddr31 in add or saddr31 in add or bcaddr31 in add or bc1addr31 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran31,'\nPrivatekey (hex): ', HEX31, '\nPrivatekey Uncompressed: ', wif31, '\nPrivatekey compressed: ', wifc31, '\nPublic Address 1 Uncompressed: ', uaddr31, '\nPublic Address 1 Compressed: ', caddr31, '\nPublic Address 3 Segwit: ', saddr31, '\nPublic Address bc1 P2WPKH: ', bcaddr31, '\nPublic Address bc1 P2WSH: ', bc1addr31)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran31))
        f.write('\nPrivatekey (hex): ' + HEX31)
        f.write('\nPrivatekey Uncompressed: ' + wif31)
        f.write('\nPrivatekey compressed: ' + wifc31)
        f.write('\nPublic Address 1 Compressed: ' + caddr31)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr31)
        f.write('\nPublic Address 3 Segwit: ' + saddr31)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr31)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr31)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr32 in add or uaddr32 in add or saddr32 in add or bcaddr32 in add or bc1addr32 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran32,'\nPrivatekey (hex): ', HEX32, '\nPrivatekey Uncompressed: ', wif32, '\nPrivatekey compressed: ', wifc32, '\nPublic Address 1 Uncompressed: ', uaddr32, '\nPublic Address 1 Compressed: ', caddr32, '\nPublic Address 3 Segwit: ', saddr32, '\nPublic Address bc1 P2WPKH: ', bcaddr32, '\nPublic Address bc1 P2WSH: ', bc1addr32)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran32))
        f.write('\nPrivatekey (hex): ' + HEX32)
        f.write('\nPrivatekey Uncompressed: ' + wif32)
        f.write('\nPrivatekey compressed: ' + wifc32)
        f.write('\nPublic Address 1 Compressed: ' + caddr32)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr32)
        f.write('\nPublic Address 3 Segwit: ' + saddr32)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr32)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr32)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr33 in add or uaddr33 in add or saddr33 in add or bcaddr33 in add or bc1addr33 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran33,'\nPrivatekey (hex): ', HEX33, '\nPrivatekey Uncompressed: ', wif33, '\nPrivatekey compressed: ', wifc33, '\nPublic Address 1 Uncompressed: ', uaddr33, '\nPublic Address 1 Compressed: ', caddr33, '\nPublic Address 3 Segwit: ', saddr33, '\nPublic Address bc1 P2WPKH: ', bcaddr33, '\nPublic Address bc1 P2WSH: ', bc1addr33)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran33))
        f.write('\nPrivatekey (hex): ' + HEX33)
        f.write('\nPrivatekey Uncompressed: ' + wif33)
        f.write('\nPrivatekey compressed: ' + wifc33)
        f.write('\nPublic Address 1 Compressed: ' + caddr33)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr33)
        f.write('\nPublic Address 3 Segwit: ' + saddr33)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr33)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr33)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr34 in add or uaddr34 in add or saddr34 in add or bcaddr34 in add or bc1addr34 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran34,'\nPrivatekey (hex): ', HEX34, '\nPrivatekey Uncompressed: ', wif34, '\nPrivatekey compressed: ', wifc34, '\nPublic Address 1 Uncompressed: ', uaddr34, '\nPublic Address 1 Compressed: ', caddr34, '\nPublic Address 3 Segwit: ', saddr34, '\nPublic Address bc1 P2WPKH: ', bcaddr34, '\nPublic Address bc1 P2WSH: ', bc1addr34)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran34))
        f.write('\nPrivatekey (hex): ' + HEX34)
        f.write('\nPrivatekey Uncompressed: ' + wif34)
        f.write('\nPrivatekey compressed: ' + wifc34)
        f.write('\nPublic Address 1 Compressed: ' + caddr34)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr34)
        f.write('\nPublic Address 3 Segwit: ' + saddr34)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr34)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr34)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr35 in add or uaddr35 in add or saddr35 in add or bcaddr35 in add or bc1addr35 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran35,'\nPrivatekey (hex): ', HEX35, '\nPrivatekey Uncompressed: ', wif35, '\nPrivatekey compressed: ', wifc35, '\nPublic Address 1 Uncompressed: ', uaddr35, '\nPublic Address 1 Compressed: ', caddr35, '\nPublic Address 3 Segwit: ', saddr35, '\nPublic Address bc1 P2WPKH: ', bcaddr35, '\nPublic Address bc1 P2WSH: ', bc1addr35)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran35))
        f.write('\nPrivatekey (hex): ' + HEX35)
        f.write('\nPrivatekey Uncompressed: ' + wif35)
        f.write('\nPrivatekey compressed: ' + wifc35)
        f.write('\nPublic Address 1 Compressed: ' + caddr35)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr35)
        f.write('\nPublic Address 3 Segwit: ' + saddr35)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr35)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr35)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr36 in add or uaddr36 in add or saddr36 in add or bcaddr36 in add or bc1addr36 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran36,'\nPrivatekey (hex): ', HEX36, '\nPrivatekey Uncompressed: ', wif36, '\nPrivatekey compressed: ', wifc36, '\nPublic Address 1 Uncompressed: ', uaddr36, '\nPublic Address 1 Compressed: ', caddr36, '\nPublic Address 3 Segwit: ', saddr36, '\nPublic Address bc1 P2WPKH: ', bcaddr36, '\nPublic Address bc1 P2WSH: ', bc1addr36)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran36))
        f.write('\nPrivatekey (hex): ' + HEX36)
        f.write('\nPrivatekey Uncompressed: ' + wif36)
        f.write('\nPrivatekey compressed: ' + wifc36)
        f.write('\nPublic Address 1 Compressed: ' + caddr36)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr36)
        f.write('\nPublic Address 3 Segwit: ' + saddr36)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr36)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr36)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr37 in add or uaddr37 in add or saddr37 in add or bcaddr37 in add or bc1addr37 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran37,'\nPrivatekey (hex): ', HEX37, '\nPrivatekey Uncompressed: ', wif37, '\nPrivatekey compressed: ', wifc37, '\nPublic Address 1 Uncompressed: ', uaddr37, '\nPublic Address 1 Compressed: ', caddr37, '\nPublic Address 3 Segwit: ', saddr37, '\nPublic Address bc1 P2WPKH: ', bcaddr37, '\nPublic Address bc1 P2WSH: ', bc1addr37)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran37))
        f.write('\nPrivatekey (hex): ' + HEX37)
        f.write('\nPrivatekey Uncompressed: ' + wif37)
        f.write('\nPrivatekey compressed: ' + wifc37)
        f.write('\nPublic Address 1 Compressed: ' + caddr37)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr37)
        f.write('\nPublic Address 3 Segwit: ' + saddr37)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr37)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr37)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr38 in add or uaddr38 in add or saddr38 in add or bcaddr38 in add or bc1addr38 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran38,'\nPrivatekey (hex): ', HEX38, '\nPrivatekey Uncompressed: ', wif38, '\nPrivatekey compressed: ', wifc38, '\nPublic Address 1 Uncompressed: ', uaddr38, '\nPublic Address 1 Compressed: ', caddr38, '\nPublic Address 3 Segwit: ', saddr38, '\nPublic Address bc1 P2WPKH: ', bcaddr38, '\nPublic Address bc1 P2WSH: ', bc1addr38)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran38))
        f.write('\nPrivatekey (hex): ' + HEX38)
        f.write('\nPrivatekey Uncompressed: ' + wif38)
        f.write('\nPrivatekey compressed: ' + wifc38)
        f.write('\nPublic Address 1 Compressed: ' + caddr38)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr38)
        f.write('\nPublic Address 3 Segwit: ' + saddr38)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr38)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr38)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr39 in add or uaddr39 in add or saddr39 in add or bcaddr39 in add or bc1addr39 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran39,'\nPrivatekey (hex): ', HEX39, '\nPrivatekey Uncompressed: ', wif39, '\nPrivatekey compressed: ', wifc39, '\nPublic Address 1 Uncompressed: ', uaddr39, '\nPublic Address 1 Compressed: ', caddr39, '\nPublic Address 3 Segwit: ', saddr39, '\nPublic Address bc1 P2WPKH: ', bcaddr39, '\nPublic Address bc1 P2WSH: ', bc1addr39)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran39))
        f.write('\nPrivatekey (hex): ' + HEX39)
        f.write('\nPrivatekey Uncompressed: ' + wif39)
        f.write('\nPrivatekey compressed: ' + wifc39)
        f.write('\nPublic Address 1 Compressed: ' + caddr39)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr39)
        f.write('\nPublic Address 3 Segwit: ' + saddr39)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr39)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr39)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr40 in add or uaddr40 in add or saddr40 in add or bcaddr40 in add or bc1addr40 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran40,'\nPrivatekey (hex): ', HEX40, '\nPrivatekey Uncompressed: ', wif40, '\nPrivatekey compressed: ', wifc40, '\nPublic Address 1 Uncompressed: ', uaddr40, '\nPublic Address 1 Compressed: ', caddr40, '\nPublic Address 3 Segwit: ', saddr40, '\nPublic Address bc1 P2WPKH: ', bcaddr40, '\nPublic Address bc1 P2WSH: ', bc1addr40)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran40))
        f.write('\nPrivatekey (hex): ' + HEX40)
        f.write('\nPrivatekey Uncompressed: ' + wif40)
        f.write('\nPrivatekey compressed: ' + wifc40)
        f.write('\nPublic Address 1 Compressed: ' + caddr40)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr40)
        f.write('\nPublic Address 3 Segwit: ' + saddr40)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr40)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr40)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr41 in add or uaddr41 in add or saddr41 in add or bcaddr41 in add or bc1addr41 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran41,'\nPrivatekey (hex): ', HEX41, '\nPrivatekey Uncompressed: ', wif41, '\nPrivatekey compressed: ', wifc41, '\nPublic Address 1 Uncompressed: ', uaddr41, '\nPublic Address 1 Compressed: ', caddr41, '\nPublic Address 3 Segwit: ', saddr41, '\nPublic Address bc1 P2WPKH: ', bcaddr41, '\nPublic Address bc1 P2WSH: ', bc1addr41)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran41))
        f.write('\nPrivatekey (hex): ' + HEX41)
        f.write('\nPrivatekey Uncompressed: ' + wif41)
        f.write('\nPrivatekey compressed: ' + wifc41)
        f.write('\nPublic Address 1 Compressed: ' + caddr41)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr41)
        f.write('\nPublic Address 3 Segwit: ' + saddr41)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr41)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr41)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr42 in add or uaddr42 in add or saddr42 in add or bcaddr42 in add or bc1addr42 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran42,'\nPrivatekey (hex): ', HEX42, '\nPrivatekey Uncompressed: ', wif42, '\nPrivatekey compressed: ', wifc42, '\nPublic Address 1 Uncompressed: ', uaddr42, '\nPublic Address 1 Compressed: ', caddr42, '\nPublic Address 3 Segwit: ', saddr42, '\nPublic Address bc1 P2WPKH: ', bcaddr42, '\nPublic Address bc1 P2WSH: ', bc1addr42)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran42))
        f.write('\nPrivatekey (hex): ' + HEX42)
        f.write('\nPrivatekey Uncompressed: ' + wif42)
        f.write('\nPrivatekey compressed: ' + wifc42)
        f.write('\nPublic Address 1 Compressed: ' + caddr42)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr42)
        f.write('\nPublic Address 3 Segwit: ' + saddr42)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr42)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr42)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr43 in add or uaddr43 in add or saddr43 in add or bcaddr43 in add or bc1addr43 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran43,'\nPrivatekey (hex): ', HEX43, '\nPrivatekey Uncompressed: ', wif43, '\nPrivatekey compressed: ', wifc43, '\nPublic Address 1 Uncompressed: ', uaddr43, '\nPublic Address 1 Compressed: ', caddr43, '\nPublic Address 3 Segwit: ', saddr43, '\nPublic Address bc1 P2WPKH: ', bcaddr43, '\nPublic Address bc1 P2WSH: ', bc1addr43)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran43))
        f.write('\nPrivatekey (hex): ' + HEX43)
        f.write('\nPrivatekey Uncompressed: ' + wif43)
        f.write('\nPrivatekey compressed: ' + wifc43)
        f.write('\nPublic Address 1 Compressed: ' + caddr43)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr43)
        f.write('\nPublic Address 3 Segwit: ' + saddr43)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr43)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr43)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr44 in add or uaddr44 in add or saddr44 in add or bcaddr44 in add or bc1addr44 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran44,'\nPrivatekey (hex): ', HEX44, '\nPrivatekey Uncompressed: ', wif44, '\nPrivatekey compressed: ', wifc44, '\nPublic Address 1 Uncompressed: ', uaddr44, '\nPublic Address 1 Compressed: ', caddr44, '\nPublic Address 3 Segwit: ', saddr44, '\nPublic Address bc1 P2WPKH: ', bcaddr44, '\nPublic Address bc1 P2WSH: ', bc1addr44)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran44))
        f.write('\nPrivatekey (hex): ' + HEX44)
        f.write('\nPrivatekey Uncompressed: ' + wif44)
        f.write('\nPrivatekey compressed: ' + wifc44)
        f.write('\nPublic Address 1 Compressed: ' + caddr44)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr44)
        f.write('\nPublic Address 3 Segwit: ' + saddr44)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr44)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr44)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr45 in add or uaddr45 in add or saddr45 in add or bcaddr45 in add or bc1addr45 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran45,'\nPrivatekey (hex): ', HEX45, '\nPrivatekey Uncompressed: ', wif45, '\nPrivatekey compressed: ', wifc45, '\nPublic Address 1 Uncompressed: ', uaddr45, '\nPublic Address 1 Compressed: ', caddr45, '\nPublic Address 3 Segwit: ', saddr45, '\nPublic Address bc1 P2WPKH: ', bcaddr45, '\nPublic Address bc1 P2WSH: ', bc1addr45)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran45))
        f.write('\nPrivatekey (hex): ' + HEX45)
        f.write('\nPrivatekey Uncompressed: ' + wif45)
        f.write('\nPrivatekey compressed: ' + wifc45)
        f.write('\nPublic Address 1 Compressed: ' + caddr45)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr45)
        f.write('\nPublic Address 3 Segwit: ' + saddr45)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr45)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr45)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr46 in add or uaddr46 in add or saddr46 in add or bcaddr46 in add or bc1addr46 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran46,'\nPrivatekey (hex): ', HEX46, '\nPrivatekey Uncompressed: ', wif46, '\nPrivatekey compressed: ', wifc46, '\nPublic Address 1 Uncompressed: ', uaddr46, '\nPublic Address 1 Compressed: ', caddr46, '\nPublic Address 3 Segwit: ', saddr46, '\nPublic Address bc1 P2WPKH: ', bcaddr46, '\nPublic Address bc1 P2WSH: ', bc1addr46)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran46))
        f.write('\nPrivatekey (hex): ' + HEX46)
        f.write('\nPrivatekey Uncompressed: ' + wif46)
        f.write('\nPrivatekey compressed: ' + wifc46)
        f.write('\nPublic Address 1 Compressed: ' + caddr46)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr46)
        f.write('\nPublic Address 3 Segwit: ' + saddr46)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr46)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr46)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr47 in add or uaddr47 in add or saddr47 in add or bcaddr47 in add or bc1addr47 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran47,'\nPrivatekey (hex): ', HEX47, '\nPrivatekey Uncompressed: ', wif47, '\nPrivatekey compressed: ', wifc47, '\nPublic Address 1 Uncompressed: ', uaddr47, '\nPublic Address 1 Compressed: ', caddr47, '\nPublic Address 3 Segwit: ', saddr47, '\nPublic Address bc1 P2WPKH: ', bcaddr47, '\nPublic Address bc1 P2WSH: ', bc1addr47)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran47))
        f.write('\nPrivatekey (hex): ' + HEX47)
        f.write('\nPrivatekey Uncompressed: ' + wif47)
        f.write('\nPrivatekey compressed: ' + wifc47)
        f.write('\nPublic Address 1 Compressed: ' + caddr47)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr47)
        f.write('\nPublic Address 3 Segwit: ' + saddr47)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr47)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr47)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr48 in add or uaddr48 in add or saddr48 in add or bcaddr48 in add or bc1addr48 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran48,'\nPrivatekey (hex): ', HEX48, '\nPrivatekey Uncompressed: ', wif48, '\nPrivatekey compressed: ', wifc48, '\nPublic Address 1 Uncompressed: ', uaddr48, '\nPublic Address 1 Compressed: ', caddr48, '\nPublic Address 3 Segwit: ', saddr48, '\nPublic Address bc1 P2WPKH: ', bcaddr48, '\nPublic Address bc1 P2WSH: ', bc1addr48)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran48))
        f.write('\nPrivatekey (hex): ' + HEX48)
        f.write('\nPrivatekey Uncompressed: ' + wif48)
        f.write('\nPrivatekey compressed: ' + wifc48)
        f.write('\nPublic Address 1 Compressed: ' + caddr48)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr48)
        f.write('\nPublic Address 3 Segwit: ' + saddr48)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr48)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr48)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr49 in add or uaddr49 in add or saddr49 in add or bcaddr49 in add or bc1addr49 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran49,'\nPrivatekey (hex): ', HEX49, '\nPrivatekey Uncompressed: ', wif49, '\nPrivatekey compressed: ', wifc49, '\nPublic Address 1 Uncompressed: ', uaddr49, '\nPublic Address 1 Compressed: ', caddr49, '\nPublic Address 3 Segwit: ', saddr49, '\nPublic Address bc1 P2WPKH: ', bcaddr49, '\nPublic Address bc1 P2WSH: ', bc1addr49)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran49))
        f.write('\nPrivatekey (hex): ' + HEX49)
        f.write('\nPrivatekey Uncompressed: ' + wif49)
        f.write('\nPrivatekey compressed: ' + wifc49)
        f.write('\nPublic Address 1 Compressed: ' + caddr49)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr49)
        f.write('\nPublic Address 3 Segwit: ' + saddr49)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr49)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr49)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr50 in add or uaddr50 in add or saddr50 in add or bcaddr50 in add or bc1addr50 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran50,'\nPrivatekey (hex): ', HEX50, '\nPrivatekey Uncompressed: ', wif50, '\nPrivatekey compressed: ', wifc50, '\nPublic Address 1 Uncompressed: ', uaddr50, '\nPublic Address 1 Compressed: ', caddr50, '\nPublic Address 3 Segwit: ', saddr50, '\nPublic Address bc1 P2WPKH: ', bcaddr50, '\nPublic Address bc1 P2WSH: ', bc1addr50)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran50))
        f.write('\nPrivatekey (hex): ' + HEX50)
        f.write('\nPrivatekey Uncompressed: ' + wif50)
        f.write('\nPrivatekey compressed: ' + wifc50)
        f.write('\nPublic Address 1 Compressed: ' + caddr50)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr50)
        f.write('\nPublic Address 3 Segwit: ' + saddr50)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr50)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr50)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr51 in add or uaddr51 in add or saddr51 in add or bcaddr51 in add or bc1addr51 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran51,'\nPrivatekey (hex): ', HEX51, '\nPrivatekey Uncompressed: ', wif51, '\nPrivatekey compressed: ', wifc51, '\nPublic Address 1 Uncompressed: ', uaddr51, '\nPublic Address 1 Compressed: ', caddr51, '\nPublic Address 3 Segwit: ', saddr51, '\nPublic Address bc1 P2WPKH: ', bcaddr51, '\nPublic Address bc1 P2WSH: ', bc1addr51)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran51))
        f.write('\nPrivatekey (hex): ' + HEX51)
        f.write('\nPrivatekey Uncompressed: ' + wif51)
        f.write('\nPrivatekey compressed: ' + wifc51)
        f.write('\nPublic Address 1 Compressed: ' + caddr51)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr51)
        f.write('\nPublic Address 3 Segwit: ' + saddr51)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr51)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr51)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr52 in add or uaddr52 in add or saddr52 in add or bcaddr52 in add or bc1addr52 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran52,'\nPrivatekey (hex): ', HEX52, '\nPrivatekey Uncompressed: ', wif52, '\nPrivatekey compressed: ', wifc52, '\nPublic Address 1 Uncompressed: ', uaddr52, '\nPublic Address 1 Compressed: ', caddr52, '\nPublic Address 3 Segwit: ', saddr52, '\nPublic Address bc1 P2WPKH: ', bcaddr52, '\nPublic Address bc1 P2WSH: ', bc1addr52)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran52))
        f.write('\nPrivatekey (hex): ' + HEX52)
        f.write('\nPrivatekey Uncompressed: ' + wif52)
        f.write('\nPrivatekey compressed: ' + wifc52)
        f.write('\nPublic Address 1 Compressed: ' + caddr52)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr52)
        f.write('\nPublic Address 3 Segwit: ' + saddr52)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr52)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr52)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr53 in add or uaddr53 in add or saddr53 in add or bcaddr53 in add or bc1addr53 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran53,'\nPrivatekey (hex): ', HEX53, '\nPrivatekey Uncompressed: ', wif53, '\nPrivatekey compressed: ', wifc53, '\nPublic Address 1 Uncompressed: ', uaddr53, '\nPublic Address 1 Compressed: ', caddr53, '\nPublic Address 3 Segwit: ', saddr53, '\nPublic Address bc1 P2WPKH: ', bcaddr53, '\nPublic Address bc1 P2WSH: ', bc1addr53)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran53))
        f.write('\nPrivatekey (hex): ' + HEX53)
        f.write('\nPrivatekey Uncompressed: ' + wif53)
        f.write('\nPrivatekey compressed: ' + wifc53)
        f.write('\nPublic Address 1 Compressed: ' + caddr53)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr53)
        f.write('\nPublic Address 3 Segwit: ' + saddr53)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr53)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr53)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr54 in add or uaddr54 in add or saddr54 in add or bcaddr54 in add or bc1addr54 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran54,'\nPrivatekey (hex): ', HEX54, '\nPrivatekey Uncompressed: ', wif54, '\nPrivatekey compressed: ', wifc54, '\nPublic Address 1 Uncompressed: ', uaddr54, '\nPublic Address 1 Compressed: ', caddr54, '\nPublic Address 3 Segwit: ', saddr54, '\nPublic Address bc1 P2WPKH: ', bcaddr54, '\nPublic Address bc1 P2WSH: ', bc1addr54)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran54))
        f.write('\nPrivatekey (hex): ' + HEX54)
        f.write('\nPrivatekey Uncompressed: ' + wif54)
        f.write('\nPrivatekey compressed: ' + wifc54)
        f.write('\nPublic Address 1 Compressed: ' + caddr54)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr54)
        f.write('\nPublic Address 3 Segwit: ' + saddr54)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr54)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr54)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr55 in add or uaddr55 in add or saddr55 in add or bcaddr55 in add or bc1addr55 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran55,'\nPrivatekey (hex): ', HEX55, '\nPrivatekey Uncompressed: ', wif55, '\nPrivatekey compressed: ', wifc55, '\nPublic Address 1 Uncompressed: ', uaddr55, '\nPublic Address 1 Compressed: ', caddr55, '\nPublic Address 3 Segwit: ', saddr55, '\nPublic Address bc1 P2WPKH: ', bcaddr55, '\nPublic Address bc1 P2WSH: ', bc1addr55)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran55))
        f.write('\nPrivatekey (hex): ' + HEX55)
        f.write('\nPrivatekey Uncompressed: ' + wif55)
        f.write('\nPrivatekey compressed: ' + wifc55)
        f.write('\nPublic Address 1 Compressed: ' + caddr55)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr55)
        f.write('\nPublic Address 3 Segwit: ' + saddr55)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr55)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr55)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr56 in add or uaddr56 in add or saddr56 in add or bcaddr56 in add or bc1addr56 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran56,'\nPrivatekey (hex): ', HEX56, '\nPrivatekey Uncompressed: ', wif56, '\nPrivatekey compressed: ', wifc56, '\nPublic Address 1 Uncompressed: ', uaddr56, '\nPublic Address 1 Compressed: ', caddr56, '\nPublic Address 3 Segwit: ', saddr56, '\nPublic Address bc1 P2WPKH: ', bcaddr56, '\nPublic Address bc1 P2WSH: ', bc1addr56)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran56))
        f.write('\nPrivatekey (hex): ' + HEX56)
        f.write('\nPrivatekey Uncompressed: ' + wif56)
        f.write('\nPrivatekey compressed: ' + wifc56)
        f.write('\nPublic Address 1 Compressed: ' + caddr56)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr56)
        f.write('\nPublic Address 3 Segwit: ' + saddr56)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr56)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr56)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr57 in add or uaddr57 in add or saddr57 in add or bcaddr57 in add or bc1addr57 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran57,'\nPrivatekey (hex): ', HEX57, '\nPrivatekey Uncompressed: ', wif57, '\nPrivatekey compressed: ', wifc57, '\nPublic Address 1 Uncompressed: ', uaddr57, '\nPublic Address 1 Compressed: ', caddr57, '\nPublic Address 3 Segwit: ', saddr57, '\nPublic Address bc1 P2WPKH: ', bcaddr57, '\nPublic Address bc1 P2WSH: ', bc1addr57)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran57))
        f.write('\nPrivatekey (hex): ' + HEX57)
        f.write('\nPrivatekey Uncompressed: ' + wif57)
        f.write('\nPrivatekey compressed: ' + wifc57)
        f.write('\nPublic Address 1 Compressed: ' + caddr57)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr57)
        f.write('\nPublic Address 3 Segwit: ' + saddr57)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr57)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr57)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr58 in add or uaddr58 in add or saddr58 in add or bcaddr58 in add or bc1addr58 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran58,'\nPrivatekey (hex): ', HEX58, '\nPrivatekey Uncompressed: ', wif58, '\nPrivatekey compressed: ', wifc58, '\nPublic Address 1 Uncompressed: ', uaddr58, '\nPublic Address 1 Compressed: ', caddr58, '\nPublic Address 3 Segwit: ', saddr58, '\nPublic Address bc1 P2WPKH: ', bcaddr58, '\nPublic Address bc1 P2WSH: ', bc1addr58)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran58))
        f.write('\nPrivatekey (hex): ' + HEX58)
        f.write('\nPrivatekey Uncompressed: ' + wif58)
        f.write('\nPrivatekey compressed: ' + wifc58)
        f.write('\nPublic Address 1 Compressed: ' + caddr58)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr58)
        f.write('\nPublic Address 3 Segwit: ' + saddr58)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr58)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr58)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr59 in add or uaddr59 in add or saddr59 in add or bcaddr59 in add or bc1addr59 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran59,'\nPrivatekey (hex): ', HEX59, '\nPrivatekey Uncompressed: ', wif59, '\nPrivatekey compressed: ', wifc59, '\nPublic Address 1 Uncompressed: ', uaddr59, '\nPublic Address 1 Compressed: ', caddr59, '\nPublic Address 3 Segwit: ', saddr59, '\nPublic Address bc1 P2WPKH: ', bcaddr59, '\nPublic Address bc1 P2WSH: ', bc1addr59)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran59))
        f.write('\nPrivatekey (hex): ' + HEX59)
        f.write('\nPrivatekey Uncompressed: ' + wif59)
        f.write('\nPrivatekey compressed: ' + wifc59)
        f.write('\nPublic Address 1 Compressed: ' + caddr59)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr59)
        f.write('\nPublic Address 3 Segwit: ' + saddr59)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr59)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr59)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr60 in add or uaddr60 in add or saddr60 in add or bcaddr60 in add or bc1addr60 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran60,'\nPrivatekey (hex): ', HEX60, '\nPrivatekey Uncompressed: ', wif60, '\nPrivatekey compressed: ', wifc60, '\nPublic Address 1 Uncompressed: ', uaddr60, '\nPublic Address 1 Compressed: ', caddr60, '\nPublic Address 3 Segwit: ', saddr60, '\nPublic Address bc1 P2WPKH: ', bcaddr60, '\nPublic Address bc1 P2WSH: ', bc1addr60)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran60))
        f.write('\nPrivatekey (hex): ' + HEX60)
        f.write('\nPrivatekey Uncompressed: ' + wif60)
        f.write('\nPrivatekey compressed: ' + wifc60)
        f.write('\nPublic Address 1 Compressed: ' + caddr60)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr60)
        f.write('\nPublic Address 3 Segwit: ' + saddr60)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr60)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr60)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr61 in add or uaddr61 in add or saddr61 in add or bcaddr61 in add or bc1addr61 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran61,'\nPrivatekey (hex): ', HEX61, '\nPrivatekey Uncompressed: ', wif61, '\nPrivatekey compressed: ', wifc61, '\nPublic Address 1 Uncompressed: ', uaddr61, '\nPublic Address 1 Compressed: ', caddr61, '\nPublic Address 3 Segwit: ', saddr61, '\nPublic Address bc1 P2WPKH: ', bcaddr61, '\nPublic Address bc1 P2WSH: ', bc1addr61)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran61))
        f.write('\nPrivatekey (hex): ' + HEX61)
        f.write('\nPrivatekey Uncompressed: ' + wif61)
        f.write('\nPrivatekey compressed: ' + wifc61)
        f.write('\nPublic Address 1 Compressed: ' + caddr61)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr61)
        f.write('\nPublic Address 3 Segwit: ' + saddr61)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr61)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr61)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr62 in add or uaddr62 in add or saddr62 in add or bcaddr62 in add or bc1addr62 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran62,'\nPrivatekey (hex): ', HEX62, '\nPrivatekey Uncompressed: ', wif62, '\nPrivatekey compressed: ', wifc62, '\nPublic Address 1 Uncompressed: ', uaddr62, '\nPublic Address 1 Compressed: ', caddr62, '\nPublic Address 3 Segwit: ', saddr62, '\nPublic Address bc1 P2WPKH: ', bcaddr62, '\nPublic Address bc1 P2WSH: ', bc1addr62)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran62))
        f.write('\nPrivatekey (hex): ' + HEX62)
        f.write('\nPrivatekey Uncompressed: ' + wif62)
        f.write('\nPrivatekey compressed: ' + wifc62)
        f.write('\nPublic Address 1 Compressed: ' + caddr62)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr62)
        f.write('\nPublic Address 3 Segwit: ' + saddr62)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr62)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr62)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr63 in add or uaddr63 in add or saddr63 in add or bcaddr63 in add or bc1addr63 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran63,'\nPrivatekey (hex): ', HEX63, '\nPrivatekey Uncompressed: ', wif63, '\nPrivatekey compressed: ', wifc63, '\nPublic Address 1 Uncompressed: ', uaddr63, '\nPublic Address 1 Compressed: ', caddr63, '\nPublic Address 3 Segwit: ', saddr63, '\nPublic Address bc1 P2WPKH: ', bcaddr63, '\nPublic Address bc1 P2WSH: ', bc1addr63)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran63))
        f.write('\nPrivatekey (hex): ' + HEX63)
        f.write('\nPrivatekey Uncompressed: ' + wif63)
        f.write('\nPrivatekey compressed: ' + wifc63)
        f.write('\nPublic Address 1 Compressed: ' + caddr63)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr63)
        f.write('\nPublic Address 3 Segwit: ' + saddr63)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr63)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr63)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr64 in add or uaddr64 in add or saddr64 in add or bcaddr64 in add or bc1addr64 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran64,'\nPrivatekey (hex): ', HEX64, '\nPrivatekey Uncompressed: ', wif64, '\nPrivatekey compressed: ', wifc64, '\nPublic Address 1 Uncompressed: ', uaddr64, '\nPublic Address 1 Compressed: ', caddr64, '\nPublic Address 3 Segwit: ', saddr64, '\nPublic Address bc1 P2WPKH: ', bcaddr64, '\nPublic Address bc1 P2WSH: ', bc1addr64)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran64))
        f.write('\nPrivatekey (hex): ' + HEX64)
        f.write('\nPrivatekey Uncompressed: ' + wif64)
        f.write('\nPrivatekey compressed: ' + wifc64)
        f.write('\nPublic Address 1 Compressed: ' + caddr64)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr64)
        f.write('\nPublic Address 3 Segwit: ' + saddr64)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr64)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr64)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr65 in add or uaddr65 in add or saddr65 in add or bcaddr65 in add or bc1addr65 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran65,'\nPrivatekey (hex): ', HEX65, '\nPrivatekey Uncompressed: ', wif65, '\nPrivatekey compressed: ', wifc65, '\nPublic Address 1 Uncompressed: ', uaddr65, '\nPublic Address 1 Compressed: ', caddr65, '\nPublic Address 3 Segwit: ', saddr65, '\nPublic Address bc1 P2WPKH: ', bcaddr65, '\nPublic Address bc1 P2WSH: ', bc1addr65)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran65))
        f.write('\nPrivatekey (hex): ' + HEX65)
        f.write('\nPrivatekey Uncompressed: ' + wif65)
        f.write('\nPrivatekey compressed: ' + wifc65)
        f.write('\nPublic Address 1 Compressed: ' + caddr65)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr65)
        f.write('\nPublic Address 3 Segwit: ' + saddr65)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr65)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr65)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr66 in add or uaddr66 in add or saddr66 in add or bcaddr66 in add or bc1addr66 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran66,'\nPrivatekey (hex): ', HEX66, '\nPrivatekey Uncompressed: ', wif66, '\nPrivatekey compressed: ', wifc66, '\nPublic Address 1 Uncompressed: ', uaddr66, '\nPublic Address 1 Compressed: ', caddr66, '\nPublic Address 3 Segwit: ', saddr66, '\nPublic Address bc1 P2WPKH: ', bcaddr66, '\nPublic Address bc1 P2WSH: ', bc1addr66)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran66))
        f.write('\nPrivatekey (hex): ' + HEX66)
        f.write('\nPrivatekey Uncompressed: ' + wif66)
        f.write('\nPrivatekey compressed: ' + wifc66)
        f.write('\nPublic Address 1 Compressed: ' + caddr66)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr66)
        f.write('\nPublic Address 3 Segwit: ' + saddr66)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr66)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr66)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr67 in add or uaddr67 in add or saddr67 in add or bcaddr67 in add or bc1addr67 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran67,'\nPrivatekey (hex): ', HEX67, '\nPrivatekey Uncompressed: ', wif67, '\nPrivatekey compressed: ', wifc67, '\nPublic Address 1 Uncompressed: ', uaddr67, '\nPublic Address 1 Compressed: ', caddr67, '\nPublic Address 3 Segwit: ', saddr67, '\nPublic Address bc1 P2WPKH: ', bcaddr67, '\nPublic Address bc1 P2WSH: ', bc1addr67)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran67))
        f.write('\nPrivatekey (hex): ' + HEX67)
        f.write('\nPrivatekey Uncompressed: ' + wif67)
        f.write('\nPrivatekey compressed: ' + wifc67)
        f.write('\nPublic Address 1 Compressed: ' + caddr67)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr67)
        f.write('\nPublic Address 3 Segwit: ' + saddr67)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr67)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr67)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr68 in add or uaddr68 in add or saddr68 in add or bcaddr68 in add or bc1addr68 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran68,'\nPrivatekey (hex): ', HEX68, '\nPrivatekey Uncompressed: ', wif68, '\nPrivatekey compressed: ', wifc68, '\nPublic Address 1 Uncompressed: ', uaddr68, '\nPublic Address 1 Compressed: ', caddr68, '\nPublic Address 3 Segwit: ', saddr68, '\nPublic Address bc1 P2WPKH: ', bcaddr68, '\nPublic Address bc1 P2WSH: ', bc1addr68)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran68))
        f.write('\nPrivatekey (hex): ' + HEX68)
        f.write('\nPrivatekey Uncompressed: ' + wif68)
        f.write('\nPrivatekey compressed: ' + wifc68)
        f.write('\nPublic Address 1 Compressed: ' + caddr68)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr68)
        f.write('\nPublic Address 3 Segwit: ' + saddr68)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr68)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr68)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr69 in add or uaddr69 in add or saddr69 in add or bcaddr69 in add or bc1addr69 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran69,'\nPrivatekey (hex): ', HEX69, '\nPrivatekey Uncompressed: ', wif69, '\nPrivatekey compressed: ', wifc69, '\nPublic Address 1 Uncompressed: ', uaddr69, '\nPublic Address 1 Compressed: ', caddr69, '\nPublic Address 3 Segwit: ', saddr69, '\nPublic Address bc1 P2WPKH: ', bcaddr69, '\nPublic Address bc1 P2WSH: ', bc1addr69)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran69))
        f.write('\nPrivatekey (hex): ' + HEX69)
        f.write('\nPrivatekey Uncompressed: ' + wif69)
        f.write('\nPrivatekey compressed: ' + wifc69)
        f.write('\nPublic Address 1 Compressed: ' + caddr69)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr69)
        f.write('\nPublic Address 3 Segwit: ' + saddr69)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr69)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr69)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr70 in add or uaddr70 in add or saddr70 in add or bcaddr70 in add or bc1addr70 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran70,'\nPrivatekey (hex): ', HEX70, '\nPrivatekey Uncompressed: ', wif70, '\nPrivatekey compressed: ', wifc70, '\nPublic Address 1 Uncompressed: ', uaddr70, '\nPublic Address 1 Compressed: ', caddr70, '\nPublic Address 3 Segwit: ', saddr70, '\nPublic Address bc1 P2WPKH: ', bcaddr70, '\nPublic Address bc1 P2WSH: ', bc1addr70)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran70))
        f.write('\nPrivatekey (hex): ' + HEX70)
        f.write('\nPrivatekey Uncompressed: ' + wif70)
        f.write('\nPrivatekey compressed: ' + wifc70)
        f.write('\nPublic Address 1 Compressed: ' + caddr70)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr70)
        f.write('\nPublic Address 3 Segwit: ' + saddr70)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr70)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr70)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr71 in add or uaddr71 in add or saddr71 in add or bcaddr71 in add or bc1addr71 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran71,'\nPrivatekey (hex): ', HEX71, '\nPrivatekey Uncompressed: ', wif71, '\nPrivatekey compressed: ', wifc71, '\nPublic Address 1 Uncompressed: ', uaddr71, '\nPublic Address 1 Compressed: ', caddr71, '\nPublic Address 3 Segwit: ', saddr71, '\nPublic Address bc1 P2WPKH: ', bcaddr71, '\nPublic Address bc1 P2WSH: ', bc1addr71)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran71))
        f.write('\nPrivatekey (hex): ' + HEX71)
        f.write('\nPrivatekey Uncompressed: ' + wif71)
        f.write('\nPrivatekey compressed: ' + wifc71)
        f.write('\nPublic Address 1 Compressed: ' + caddr71)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr71)
        f.write('\nPublic Address 3 Segwit: ' + saddr71)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr71)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr71)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr72 in add or uaddr72 in add or saddr72 in add or bcaddr72 in add or bc1addr72 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran72,'\nPrivatekey (hex): ', HEX72, '\nPrivatekey Uncompressed: ', wif72, '\nPrivatekey compressed: ', wifc72, '\nPublic Address 1 Uncompressed: ', uaddr72, '\nPublic Address 1 Compressed: ', caddr72, '\nPublic Address 3 Segwit: ', saddr72, '\nPublic Address bc1 P2WPKH: ', bcaddr72, '\nPublic Address bc1 P2WSH: ', bc1addr72)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran72))
        f.write('\nPrivatekey (hex): ' + HEX72)
        f.write('\nPrivatekey Uncompressed: ' + wif72)
        f.write('\nPrivatekey compressed: ' + wifc72)
        f.write('\nPublic Address 1 Compressed: ' + caddr72)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr72)
        f.write('\nPublic Address 3 Segwit: ' + saddr72)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr72)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr72)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr73 in add or uaddr73 in add or saddr73 in add or bcaddr73 in add or bc1addr73 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran73,'\nPrivatekey (hex): ', HEX73, '\nPrivatekey Uncompressed: ', wif73, '\nPrivatekey compressed: ', wifc73, '\nPublic Address 1 Uncompressed: ', uaddr73, '\nPublic Address 1 Compressed: ', caddr73, '\nPublic Address 3 Segwit: ', saddr73, '\nPublic Address bc1 P2WPKH: ', bcaddr73, '\nPublic Address bc1 P2WSH: ', bc1addr73)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran73))
        f.write('\nPrivatekey (hex): ' + HEX73)
        f.write('\nPrivatekey Uncompressed: ' + wif73)
        f.write('\nPrivatekey compressed: ' + wifc73)
        f.write('\nPublic Address 1 Compressed: ' + caddr73)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr73)
        f.write('\nPublic Address 3 Segwit: ' + saddr73)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr73)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr73)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr74 in add or uaddr74 in add or saddr74 in add or bcaddr74 in add or bc1addr74 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran74,'\nPrivatekey (hex): ', HEX74, '\nPrivatekey Uncompressed: ', wif74, '\nPrivatekey compressed: ', wifc74, '\nPublic Address 1 Uncompressed: ', uaddr74, '\nPublic Address 1 Compressed: ', caddr74, '\nPublic Address 3 Segwit: ', saddr74, '\nPublic Address bc1 P2WPKH: ', bcaddr74, '\nPublic Address bc1 P2WSH: ', bc1addr74)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran74))
        f.write('\nPrivatekey (hex): ' + HEX74)
        f.write('\nPrivatekey Uncompressed: ' + wif74)
        f.write('\nPrivatekey compressed: ' + wifc74)
        f.write('\nPublic Address 1 Compressed: ' + caddr74)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr74)
        f.write('\nPublic Address 3 Segwit: ' + saddr74)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr74)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr74)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr75 in add or uaddr75 in add or saddr75 in add or bcaddr75 in add or bc1addr75 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran75,'\nPrivatekey (hex): ', HEX75, '\nPrivatekey Uncompressed: ', wif75, '\nPrivatekey compressed: ', wifc75, '\nPublic Address 1 Uncompressed: ', uaddr75, '\nPublic Address 1 Compressed: ', caddr75, '\nPublic Address 3 Segwit: ', saddr75, '\nPublic Address bc1 P2WPKH: ', bcaddr75, '\nPublic Address bc1 P2WSH: ', bc1addr75)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran75))
        f.write('\nPrivatekey (hex): ' + HEX75)
        f.write('\nPrivatekey Uncompressed: ' + wif75)
        f.write('\nPrivatekey compressed: ' + wifc75)
        f.write('\nPublic Address 1 Compressed: ' + caddr75)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr75)
        f.write('\nPublic Address 3 Segwit: ' + saddr75)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr75)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr75)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr76 in add or uaddr76 in add or saddr76 in add or bcaddr76 in add or bc1addr76 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran76,'\nPrivatekey (hex): ', HEX76, '\nPrivatekey Uncompressed: ', wif76, '\nPrivatekey compressed: ', wifc76, '\nPublic Address 1 Uncompressed: ', uaddr76, '\nPublic Address 1 Compressed: ', caddr76, '\nPublic Address 3 Segwit: ', saddr76, '\nPublic Address bc1 P2WPKH: ', bcaddr76, '\nPublic Address bc1 P2WSH: ', bc1addr76)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran76))
        f.write('\nPrivatekey (hex): ' + HEX76)
        f.write('\nPrivatekey Uncompressed: ' + wif76)
        f.write('\nPrivatekey compressed: ' + wifc76)
        f.write('\nPublic Address 1 Compressed: ' + caddr76)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr76)
        f.write('\nPublic Address 3 Segwit: ' + saddr76)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr76)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr76)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr77 in add or uaddr77 in add or saddr77 in add or bcaddr77 in add or bc1addr77 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran77,'\nPrivatekey (hex): ', HEX77, '\nPrivatekey Uncompressed: ', wif77, '\nPrivatekey compressed: ', wifc77, '\nPublic Address 1 Uncompressed: ', uaddr77, '\nPublic Address 1 Compressed: ', caddr77, '\nPublic Address 3 Segwit: ', saddr77, '\nPublic Address bc1 P2WPKH: ', bcaddr77, '\nPublic Address bc1 P2WSH: ', bc1addr77)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran77))
        f.write('\nPrivatekey (hex): ' + HEX77)
        f.write('\nPrivatekey Uncompressed: ' + wif77)
        f.write('\nPrivatekey compressed: ' + wifc77)
        f.write('\nPublic Address 1 Compressed: ' + caddr77)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr77)
        f.write('\nPublic Address 3 Segwit: ' + saddr77)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr77)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr77)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr78 in add or uaddr78 in add or saddr78 in add or bcaddr78 in add or bc1addr78 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran78,'\nPrivatekey (hex): ', HEX78, '\nPrivatekey Uncompressed: ', wif78, '\nPrivatekey compressed: ', wifc78, '\nPublic Address 1 Uncompressed: ', uaddr78, '\nPublic Address 1 Compressed: ', caddr78, '\nPublic Address 3 Segwit: ', saddr78, '\nPublic Address bc1 P2WPKH: ', bcaddr78, '\nPublic Address bc1 P2WSH: ', bc1addr78)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran78))
        f.write('\nPrivatekey (hex): ' + HEX78)
        f.write('\nPrivatekey Uncompressed: ' + wif78)
        f.write('\nPrivatekey compressed: ' + wifc78)
        f.write('\nPublic Address 1 Compressed: ' + caddr78)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr78)
        f.write('\nPublic Address 3 Segwit: ' + saddr78)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr78)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr78)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr79 in add or uaddr79 in add or saddr79 in add or bcaddr79 in add or bc1addr79 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran79,'\nPrivatekey (hex): ', HEX79, '\nPrivatekey Uncompressed: ', wif79, '\nPrivatekey compressed: ', wifc79, '\nPublic Address 1 Uncompressed: ', uaddr79, '\nPublic Address 1 Compressed: ', caddr79, '\nPublic Address 3 Segwit: ', saddr79, '\nPublic Address bc1 P2WPKH: ', bcaddr79, '\nPublic Address bc1 P2WSH: ', bc1addr79)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran79))
        f.write('\nPrivatekey (hex): ' + HEX79)
        f.write('\nPrivatekey Uncompressed: ' + wif79)
        f.write('\nPrivatekey compressed: ' + wifc79)
        f.write('\nPublic Address 1 Compressed: ' + caddr79)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr79)
        f.write('\nPublic Address 3 Segwit: ' + saddr79)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr79)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr79)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr80 in add or uaddr80 in add or saddr80 in add or bcaddr80 in add or bc1addr80 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran80,'\nPrivatekey (hex): ', HEX80, '\nPrivatekey Uncompressed: ', wif80, '\nPrivatekey compressed: ', wifc80, '\nPublic Address 1 Uncompressed: ', uaddr80, '\nPublic Address 1 Compressed: ', caddr80, '\nPublic Address 3 Segwit: ', saddr80, '\nPublic Address bc1 P2WPKH: ', bcaddr80, '\nPublic Address bc1 P2WSH: ', bc1addr80)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran80))
        f.write('\nPrivatekey (hex): ' + HEX80)
        f.write('\nPrivatekey Uncompressed: ' + wif80)
        f.write('\nPrivatekey compressed: ' + wifc80)
        f.write('\nPublic Address 1 Compressed: ' + caddr80)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr80)
        f.write('\nPublic Address 3 Segwit: ' + saddr80)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr80)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr80)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr81 in add or uaddr81 in add or saddr81 in add or bcaddr81 in add or bc1addr81 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran81,'\nPrivatekey (hex): ', HEX81, '\nPrivatekey Uncompressed: ', wif81, '\nPrivatekey compressed: ', wifc81, '\nPublic Address 1 Uncompressed: ', uaddr81, '\nPublic Address 1 Compressed: ', caddr81, '\nPublic Address 3 Segwit: ', saddr81, '\nPublic Address bc1 P2WPKH: ', bcaddr81, '\nPublic Address bc1 P2WSH: ', bc1addr81)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran81))
        f.write('\nPrivatekey (hex): ' + HEX81)
        f.write('\nPrivatekey Uncompressed: ' + wif81)
        f.write('\nPrivatekey compressed: ' + wifc81)
        f.write('\nPublic Address 1 Compressed: ' + caddr81)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr81)
        f.write('\nPublic Address 3 Segwit: ' + saddr81)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr81)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr81)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr82 in add or uaddr82 in add or saddr82 in add or bcaddr82 in add or bc1addr82 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran82,'\nPrivatekey (hex): ', HEX82, '\nPrivatekey Uncompressed: ', wif82, '\nPrivatekey compressed: ', wifc82, '\nPublic Address 1 Uncompressed: ', uaddr82, '\nPublic Address 1 Compressed: ', caddr82, '\nPublic Address 3 Segwit: ', saddr82, '\nPublic Address bc1 P2WPKH: ', bcaddr82, '\nPublic Address bc1 P2WSH: ', bc1addr82)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran82))
        f.write('\nPrivatekey (hex): ' + HEX82)
        f.write('\nPrivatekey Uncompressed: ' + wif82)
        f.write('\nPrivatekey compressed: ' + wifc82)
        f.write('\nPublic Address 1 Compressed: ' + caddr82)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr82)
        f.write('\nPublic Address 3 Segwit: ' + saddr82)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr82)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr82)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr83 in add or uaddr83 in add or saddr83 in add or bcaddr83 in add or bc1addr83 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran83,'\nPrivatekey (hex): ', HEX83, '\nPrivatekey Uncompressed: ', wif83, '\nPrivatekey compressed: ', wifc83, '\nPublic Address 1 Uncompressed: ', uaddr83, '\nPublic Address 1 Compressed: ', caddr83, '\nPublic Address 3 Segwit: ', saddr83, '\nPublic Address bc1 P2WPKH: ', bcaddr83, '\nPublic Address bc1 P2WSH: ', bc1addr83)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran83))
        f.write('\nPrivatekey (hex): ' + HEX83)
        f.write('\nPrivatekey Uncompressed: ' + wif83)
        f.write('\nPrivatekey compressed: ' + wifc83)
        f.write('\nPublic Address 1 Compressed: ' + caddr83)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr83)
        f.write('\nPublic Address 3 Segwit: ' + saddr83)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr83)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr83)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr84 in add or uaddr84 in add or saddr84 in add or bcaddr84 in add or bc1addr84 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran84,'\nPrivatekey (hex): ', HEX84, '\nPrivatekey Uncompressed: ', wif84, '\nPrivatekey compressed: ', wifc84, '\nPublic Address 1 Uncompressed: ', uaddr84, '\nPublic Address 1 Compressed: ', caddr84, '\nPublic Address 3 Segwit: ', saddr84, '\nPublic Address bc1 P2WPKH: ', bcaddr84, '\nPublic Address bc1 P2WSH: ', bc1addr84)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran84))
        f.write('\nPrivatekey (hex): ' + HEX84)
        f.write('\nPrivatekey Uncompressed: ' + wif84)
        f.write('\nPrivatekey compressed: ' + wifc84)
        f.write('\nPublic Address 1 Compressed: ' + caddr84)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr84)
        f.write('\nPublic Address 3 Segwit: ' + saddr84)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr84)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr84)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr85 in add or uaddr85 in add or saddr85 in add or bcaddr85 in add or bc1addr85 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran85,'\nPrivatekey (hex): ', HEX85, '\nPrivatekey Uncompressed: ', wif85, '\nPrivatekey compressed: ', wifc85, '\nPublic Address 1 Uncompressed: ', uaddr85, '\nPublic Address 1 Compressed: ', caddr85, '\nPublic Address 3 Segwit: ', saddr85, '\nPublic Address bc1 P2WPKH: ', bcaddr85, '\nPublic Address bc1 P2WSH: ', bc1addr85)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran85))
        f.write('\nPrivatekey (hex): ' + HEX85)
        f.write('\nPrivatekey Uncompressed: ' + wif85)
        f.write('\nPrivatekey compressed: ' + wifc85)
        f.write('\nPublic Address 1 Compressed: ' + caddr85)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr85)
        f.write('\nPublic Address 3 Segwit: ' + saddr85)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr85)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr85)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr86 in add or uaddr86 in add or saddr86 in add or bcaddr86 in add or bc1addr86 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran86,'\nPrivatekey (hex): ', HEX86, '\nPrivatekey Uncompressed: ', wif86, '\nPrivatekey compressed: ', wifc86, '\nPublic Address 1 Uncompressed: ', uaddr86, '\nPublic Address 1 Compressed: ', caddr86, '\nPublic Address 3 Segwit: ', saddr86, '\nPublic Address bc1 P2WPKH: ', bcaddr86, '\nPublic Address bc1 P2WSH: ', bc1addr86)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran86))
        f.write('\nPrivatekey (hex): ' + HEX86)
        f.write('\nPrivatekey Uncompressed: ' + wif86)
        f.write('\nPrivatekey compressed: ' + wifc86)
        f.write('\nPublic Address 1 Compressed: ' + caddr86)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr86)
        f.write('\nPublic Address 3 Segwit: ' + saddr86)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr86)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr86)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr87 in add or uaddr87 in add or saddr87 in add or bcaddr87 in add or bc1addr87 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran87,'\nPrivatekey (hex): ', HEX87, '\nPrivatekey Uncompressed: ', wif87, '\nPrivatekey compressed: ', wifc87, '\nPublic Address 1 Uncompressed: ', uaddr87, '\nPublic Address 1 Compressed: ', caddr87, '\nPublic Address 3 Segwit: ', saddr87, '\nPublic Address bc1 P2WPKH: ', bcaddr87, '\nPublic Address bc1 P2WSH: ', bc1addr87)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran87))
        f.write('\nPrivatekey (hex): ' + HEX87)
        f.write('\nPrivatekey Uncompressed: ' + wif87)
        f.write('\nPrivatekey compressed: ' + wifc87)
        f.write('\nPublic Address 1 Compressed: ' + caddr87)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr87)
        f.write('\nPublic Address 3 Segwit: ' + saddr87)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr87)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr87)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr88 in add or uaddr88 in add or saddr88 in add or bcaddr88 in add or bc1addr88 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran88,'\nPrivatekey (hex): ', HEX88, '\nPrivatekey Uncompressed: ', wif88, '\nPrivatekey compressed: ', wifc88, '\nPublic Address 1 Uncompressed: ', uaddr88, '\nPublic Address 1 Compressed: ', caddr88, '\nPublic Address 3 Segwit: ', saddr88, '\nPublic Address bc1 P2WPKH: ', bcaddr88, '\nPublic Address bc1 P2WSH: ', bc1addr88)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran88))
        f.write('\nPrivatekey (hex): ' + HEX88)
        f.write('\nPrivatekey Uncompressed: ' + wif88)
        f.write('\nPrivatekey compressed: ' + wifc88)
        f.write('\nPublic Address 1 Compressed: ' + caddr88)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr88)
        f.write('\nPublic Address 3 Segwit: ' + saddr88)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr88)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr88)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr89 in add or uaddr89 in add or saddr89 in add or bcaddr89 in add or bc1addr89 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran89,'\nPrivatekey (hex): ', HEX89, '\nPrivatekey Uncompressed: ', wif89, '\nPrivatekey compressed: ', wifc89, '\nPublic Address 1 Uncompressed: ', uaddr89, '\nPublic Address 1 Compressed: ', caddr89, '\nPublic Address 3 Segwit: ', saddr89, '\nPublic Address bc1 P2WPKH: ', bcaddr89, '\nPublic Address bc1 P2WSH: ', bc1addr89)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran89))
        f.write('\nPrivatekey (hex): ' + HEX89)
        f.write('\nPrivatekey Uncompressed: ' + wif89)
        f.write('\nPrivatekey compressed: ' + wifc89)
        f.write('\nPublic Address 1 Compressed: ' + caddr89)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr89)
        f.write('\nPublic Address 3 Segwit: ' + saddr89)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr89)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr89)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr90 in add or uaddr90 in add or saddr90 in add or bcaddr90 in add or bc1addr90 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran90,'\nPrivatekey (hex): ', HEX90, '\nPrivatekey Uncompressed: ', wif90, '\nPrivatekey compressed: ', wifc90, '\nPublic Address 1 Uncompressed: ', uaddr90, '\nPublic Address 1 Compressed: ', caddr90, '\nPublic Address 3 Segwit: ', saddr90, '\nPublic Address bc1 P2WPKH: ', bcaddr90, '\nPublic Address bc1 P2WSH: ', bc1addr90)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran90))
        f.write('\nPrivatekey (hex): ' + HEX90)
        f.write('\nPrivatekey Uncompressed: ' + wif90)
        f.write('\nPrivatekey compressed: ' + wifc90)
        f.write('\nPublic Address 1 Compressed: ' + caddr90)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr90)
        f.write('\nPublic Address 3 Segwit: ' + saddr90)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr90)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr90)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr91 in add or uaddr91 in add or saddr91 in add or bcaddr91 in add or bc1addr91 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran91,'\nPrivatekey (hex): ', HEX91, '\nPrivatekey Uncompressed: ', wif91, '\nPrivatekey compressed: ', wifc91, '\nPublic Address 1 Uncompressed: ', uaddr91, '\nPublic Address 1 Compressed: ', caddr91, '\nPublic Address 3 Segwit: ', saddr91, '\nPublic Address bc1 P2WPKH: ', bcaddr91, '\nPublic Address bc1 P2WSH: ', bc1addr91)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran91))
        f.write('\nPrivatekey (hex): ' + HEX91)
        f.write('\nPrivatekey Uncompressed: ' + wif91)
        f.write('\nPrivatekey compressed: ' + wifc91)
        f.write('\nPublic Address 1 Compressed: ' + caddr91)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr91)
        f.write('\nPublic Address 3 Segwit: ' + saddr91)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr91)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr91)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        
    if caddr92 in add or uaddr92 in add or saddr92 in add or bcaddr92 in add or bc1addr92 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran92,'\nPrivatekey (hex): ', HEX92, '\nPrivatekey Uncompressed: ', wif92, '\nPrivatekey compressed: ', wifc92, '\nPublic Address 1 Uncompressed: ', uaddr92, '\nPublic Address 1 Compressed: ', caddr92, '\nPublic Address 3 Segwit: ', saddr92, '\nPublic Address bc1 P2WPKH: ', bcaddr92, '\nPublic Address bc1 P2WSH: ', bc1addr92)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran92))
        f.write('\nPrivatekey (hex): ' + HEX92)
        f.write('\nPrivatekey Uncompressed: ' + wif92)
        f.write('\nPrivatekey compressed: ' + wifc92)
        f.write('\nPublic Address 1 Compressed: ' + caddr92)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr92)
        f.write('\nPublic Address 3 Segwit: ' + saddr92)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr92)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr92)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr93 in add or uaddr93 in add or saddr93 in add or bcaddr93 in add or bc1addr93 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran93,'\nPrivatekey (hex): ', HEX93, '\nPrivatekey Uncompressed: ', wif93, '\nPrivatekey compressed: ', wifc93, '\nPublic Address 1 Uncompressed: ', uaddr93, '\nPublic Address 1 Compressed: ', caddr93, '\nPublic Address 3 Segwit: ', saddr93, '\nPublic Address bc1 P2WPKH: ', bcaddr93, '\nPublic Address bc1 P2WSH: ', bc1addr93)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran93))
        f.write('\nPrivatekey (hex): ' + HEX93)
        f.write('\nPrivatekey Uncompressed: ' + wif93)
        f.write('\nPrivatekey compressed: ' + wifc93)
        f.write('\nPublic Address 1 Compressed: ' + caddr93)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr93)
        f.write('\nPublic Address 3 Segwit: ' + saddr93)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr93)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr93)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr94 in add or uaddr94 in add or saddr94 in add or bcaddr94 in add or bc1addr94 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran94,'\nPrivatekey (hex): ', HEX94, '\nPrivatekey Uncompressed: ', wif94, '\nPrivatekey compressed: ', wifc94, '\nPublic Address 1 Uncompressed: ', uaddr94, '\nPublic Address 1 Compressed: ', caddr94, '\nPublic Address 3 Segwit: ', saddr94, '\nPublic Address bc1 P2WPKH: ', bcaddr94, '\nPublic Address bc1 P2WSH: ', bc1addr94)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran94))
        f.write('\nPrivatekey (hex): ' + HEX94)
        f.write('\nPrivatekey Uncompressed: ' + wif94)
        f.write('\nPrivatekey compressed: ' + wifc94)
        f.write('\nPublic Address 1 Compressed: ' + caddr94)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr94)
        f.write('\nPublic Address 3 Segwit: ' + saddr94)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr94)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr94)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr95 in add or uaddr95 in add or saddr95 in add or bcaddr95 in add or bc1addr95 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran95,'\nPrivatekey (hex): ', HEX95, '\nPrivatekey Uncompressed: ', wif95, '\nPrivatekey compressed: ', wifc95, '\nPublic Address 1 Uncompressed: ', uaddr95, '\nPublic Address 1 Compressed: ', caddr95, '\nPublic Address 3 Segwit: ', saddr95, '\nPublic Address bc1 P2WPKH: ', bcaddr95, '\nPublic Address bc1 P2WSH: ', bc1addr95)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran95))
        f.write('\nPrivatekey (hex): ' + HEX95)
        f.write('\nPrivatekey Uncompressed: ' + wif95)
        f.write('\nPrivatekey compressed: ' + wifc95)
        f.write('\nPublic Address 1 Compressed: ' + caddr95)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr95)
        f.write('\nPublic Address 3 Segwit: ' + saddr95)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr95)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr95)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr96 in add or uaddr96 in add or saddr96 in add or bcaddr96 in add or bc1addr96 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran96,'\nPrivatekey (hex): ', HEX96, '\nPrivatekey Uncompressed: ', wif96, '\nPrivatekey compressed: ', wifc96, '\nPublic Address 1 Uncompressed: ', uaddr96, '\nPublic Address 1 Compressed: ', caddr96, '\nPublic Address 3 Segwit: ', saddr96, '\nPublic Address bc1 P2WPKH: ', bcaddr96, '\nPublic Address bc1 P2WSH: ', bc1addr96)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran96))
        f.write('\nPrivatekey (hex): ' + HEX96)
        f.write('\nPrivatekey Uncompressed: ' + wif96)
        f.write('\nPrivatekey compressed: ' + wifc96)
        f.write('\nPublic Address 1 Compressed: ' + caddr96)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr96)
        f.write('\nPublic Address 3 Segwit: ' + saddr96)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr96)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr96)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr97 in add or uaddr97 in add or saddr97 in add or bcaddr97 in add or bc1addr97 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran97,'\nPrivatekey (hex): ', HEX97, '\nPrivatekey Uncompressed: ', wif97, '\nPrivatekey compressed: ', wifc97, '\nPublic Address 1 Uncompressed: ', uaddr97, '\nPublic Address 1 Compressed: ', caddr97, '\nPublic Address 3 Segwit: ', saddr97, '\nPublic Address bc1 P2WPKH: ', bcaddr97, '\nPublic Address bc1 P2WSH: ', bc1addr97)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran97))
        f.write('\nPrivatekey (hex): ' + HEX97)
        f.write('\nPrivatekey Uncompressed: ' + wif97)
        f.write('\nPrivatekey compressed: ' + wifc97)
        f.write('\nPublic Address 1 Compressed: ' + caddr97)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr97)
        f.write('\nPublic Address 3 Segwit: ' + saddr97)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr97)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr97)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()

    if caddr98 in add or uaddr98 in add or saddr98 in add or bcaddr98 in add or bc1addr98 in add:
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', ran98,'\nPrivatekey (hex): ', HEX98, '\nPrivatekey Uncompressed: ', wif98, '\nPrivatekey compressed: ', wifc98, '\nPublic Address 1 Uncompressed: ', uaddr98, '\nPublic Address 1 Compressed: ', caddr98, '\nPublic Address 3 Segwit: ', saddr98, '\nPublic Address bc1 P2WPKH: ', bcaddr98, '\nPublic Address bc1 P2WSH: ', bc1addr98)
        
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(ran98))
        f.write('\nPrivatekey (hex): ' + HEX98)
        f.write('\nPrivatekey Uncompressed: ' + wif98)
        f.write('\nPrivatekey compressed: ' + wifc98)
        f.write('\nPublic Address 1 Compressed: ' + caddr98)
        f.write('\nPublic Address 1 Uncompressed: ' + uaddr98)
        f.write('\nPublic Address 3 Segwit: ' + saddr98)
        f.write('\nPublic Address bc1 P2WPKH: ' + bcaddr98)
        f.write('\nPublic Address bc1 P2WSH: ' + bc1addr98)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()