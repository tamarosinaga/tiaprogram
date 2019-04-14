def kalkulator ():

        #fungsi pengurangan
        def add(x,y) :
                return x + y
        
        def subtract(x, y):
                return x - y
        # fungsi perkalian
        def multiply(x,y) :
                return x * y
        #fungsi pembagian
        def divide(x,y):
                return x / y

        #menu operasi
        print("pilih Operasi.")
        print("1.jumlah")
        print("2.kurang")
        print("3.kali")
        print("4.bagi")

        #meminta input dari user
        choice = input("Masukan pilihan(1/2/3/4): ")

        num1 = int(input("Masukan bilangan pertama: "))
        num2 = int(input("Masukan bilangan kedua:: "))

        if choice == '1':
                print(num1,"+",num2,"=",
        add(num1,num2))

        elif choice == '2':
                print(num1,"-",num2,"=",subtract(num1,num2))

        elif choice == '3':
                print(num1,"*",num2,"=",multiply(num1,num2))

        elif choice == '4':
                print(num1,"/",num2,"=",divide(num1,num2))
        else :
                print("input salah")
        tambah()


        
def tambah() :
    
    tambah = input ("\nKembali KeAwal(y/t)? ")
    if tambah == 'y' :
        kalkulator()

    else :
        exit



