file = open("db-inventory.txt","a")
while True:
    x = input("Masukan data inventory baru (ya/tidak)")
    print('**********************************************')
    if x == 'tidak':
        file = open("db-inventory.txt","r")
        for item in file:
            item=item.strip()
            print(item)
        file.close()
        break
        
    elif x == 'ya' or 'ya':
        perangkat = input("Nama Perangkat: ")
        lokasi = input("Lokasi: ") 
        file.write("Nama Perangkat: " + perangkat + ", Lokasi: " + lokasi + "\n")
        print('------------------------------------------')
        file.close()