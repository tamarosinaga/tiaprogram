from texttable import Texttable
def pembayaran():
    table= Texttable ()
    no=0
    name=[]
    nim=[]
    kelas=[]
    bulanan=[]
    uts=[]
    uas=[]
    seminar=[]
    jawab3 = "y"
    while(jawab3 == "y"):
        nama=(input("Masukan Nama  : "))
        nim=(input("Masukan NIM   : "))
        kelas=(input("Masukan Kelas: "))
        pilih = (input("Apakah anda ingin membayar semester (y/t) ? "))
        if pilih == 'y':
            bulanan =int(input("untuk berapa bulan ? "))
            d_bulanan = 'bulanan'
            bulanan=400000*bulanan
        else :
            bulanan_ = ''
            bulanan=0

        pilih = (input("Apakah anda ingin membayar uts (y/t) ? "))
        if pilih == 'y':
            uts = 50000
            
        else :
            uts = ''

            
        pilih = (input("Apakah anda ingin membayar uas (y/t) ? "))
        if pilih == 'y':
            uas = 50000
            
        else :
            uas = ''
            
            
        pilih = (input("ingin bayar SEMINAR (y/t) ? "))
        if  pilih == 'y':
            seminar  = 'SEMINAR'
            seminar=100000
        else :
            seminar = ''
            seminar=0

        table.add_rows([['BULANAN ','UTS','UAS','SEMINAR'],
                        [bulanan,uts,uas,seminar]])
        print("_"*30)
        print("Total Rincian")
        print("_"*30)
        print ("Nama :",nama)
        print ("Nim :",nim)
        print ("Kelas :",kelas)
        print (table.draw())
        jawab3 = input("\n  Tambahkan Data PEMBAYARAN (y/t)? ") ; print("")
