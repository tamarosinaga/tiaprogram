def penggajian() :
    from texttable import Texttable
    table = Texttable ()
    no = 0
    nama = []
    jabatan = []
    gaji = []
    jawab = "y"

    while (jawab == 'y'):
        nama.append(input("Masukan Nama: "))
        jab = input("Jabatan : ")
        jabatan.append(jab)
        if  (jab == 'Programer') :
            gaji.append('3000000')
            no+=1
        
            jawab = input("\nTambah Lagi? ")
        elif (jab == 'Kasir') :
            gaji.append('200000')
            no+=1
        
            jawab = input("\nTambah Lagi? ")
        elif (jab == 'Satpam') :
            gaji.append('500000')
            jawab = input("\n tambah lagi : ")
            no+=1
        else:
            break
        
    for i in range (no) :

        table.add_rows([['No','Nama','Jabatan','Gaji'],[i+1, nama[i],jabatan[i],gaji[i]]])                     
    print(table.draw())

