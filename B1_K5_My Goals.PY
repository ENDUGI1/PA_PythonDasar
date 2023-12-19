import os
import time
import pwinput

users = [
    {'username': 'fauzan', 'password': '123'},
    {'username': 'arin', 'password': '321'}
]


goals = [
    {
        'id_user': 0,
        'tujuan': 'HP BARU',
        'total_rupiah': 550000,
        'rentang_waktu(bulan)': 12
    },
    {
        'id_user': 0,
        'tujuan': 'SHOPEE',
        'total_rupiah': 1000000,
        'rentang_waktu(bulan)': 2
    },
    {
        'id_user': 1,
        'tujuan': 'SEPATU NIKE',
        'total_rupiah': 1500000,
        'rentang_waktu(bulan)': 6
    },
    {
        'id_user': 0,
        'tujuan': 'JAKET',
        'total_rupiah': 350000,
        'rentang_waktu(bulan)': 3
    },
]


datapenting = ("Ahmad Nur Fauzan", 2209106057, "Wildanah Sirad",
               2209106062, "Arindra Nurshadrina Ramadini", 2209106070)

# fungsi estetika


def delay(waktu):
    time.sleep(waktu)


def clear_screen():
    os.system('cls'if os.name == 'nt' else 'clear')


def credit():
    print("="*150)
    print("Created by: ", datapenting)
    print("="*150)
    delay(2.5)
    clear_screen()
    


def keluar_app():
    clear_screen()
    print("""==========================================================""")
    print("""|                                                        |""")
    print("""|                                                        |""")
    print("""|              TERIMA KASIH SUDAH MENABUNG               |""")
    print("""|          JANGAN LUPA UNTUK MENABUNG LAGI BRO !!        |""")
    print("""|                                                        |""")
    print("""|                                                        |""")
    print("""==========================================================""")
    delay(2.5)
    clear_screen()
    credit()
    exit()


def create(id_user):
    while True:
        try:
            goalsBaru = {}
            print("-"*35)
            print("| ISILAH DATA GOALS DI BAWAH INI! |")
            print("-"*35)
            goalsBaru['id_user'] = id_user
            goalsBaru['tujuan'] = input("Masukkan tujuan anda menabung : ")          
            if goalsBaru['tujuan'] == "" :                                           #ERROR HANDLING MASZEH START !!!                 
                clear_screen()
                print ("<<< Tujuan tidak boleh dikosongkan >>>")
            elif goalsBaru['tujuan'].isupper()==False:                               #WAJIB KAPITAL
                print("<<< Tujuan yang dimasukkan harus huruf kapital semua >>>")
            elif len(goalsBaru['tujuan']) > 15:                                      # MAKSIMAL 15 HURUF MASZEH
                print("<<< maksimal 15 karakter >>>")  
            else: 
                goalsBaru['total_rupiah'] = int(input("Masukkan nominal rupiah yang ingin dicapai : "))
                if goalsBaru['total_rupiah'] < 0:                                       #TIDAK BOLEH 0 RUPIAH
                    print("<<< Nominal harus lebih dari 0 >>>")
                elif goalsBaru['total_rupiah'] > 10000000000:                           #TIDAK BOLEH LEBIH DARI 10 MILIAR RUPIAH
                    print("<<< Nominal tidak lebih dari 11 digit >>>")
                elif goalsBaru['total_rupiah'] > 0:
                    goalsBaru['rentang_waktu(bulan)'] = int(input("Masukkan rentang waktu yang diinginkan(bulan) : "))
                    if goalsBaru['rentang_waktu(bulan)'] < 0 :                             
                        print("<<< Rentang waktu harus lebih dari 0 bulan >>>")                  #TIDAK BOLEH KURANG DARI 0 BULAN
                    elif goalsBaru['rentang_waktu(bulan)'] > 150 :                         #TIDAK BOLEH LEBIH  DARI 12.5 TAHUN
                        print("<<< Rentang waktu tidak boleh lebih dari 150 bulan >>>")
                    elif goalsBaru['rentang_waktu(bulan)'] > 0 :                     #ERROR HANDLING END 
                        goals.append(goalsBaru)
                        print()
                        print('[Data goal tersimpan!')
                        delay(2.5)
                        clear_screen()
                        break
        except ValueError:
            print ("<<< harap isi data dengan benar >>>")


def delete_goal(id_user):
    while True:
        try:
            data_id = []
            for index in range(len(goals)):
                if (goals[index]['id_user'] == id_user):
                    data_id.append(index)
                    print("ID Goals             : ", index)
                    print("Tujuan               : ", goals[index]['tujuan'])
                    print("Total Rupiah         : ", goals[index]['total_rupiah'])
                    print("Rentang Waktu(Bulan) : ",
                        goals[index]['rentang_waktu(bulan)'])
                    print("-"*25)

            id_hapus = int(input("Masukkan id goalS yang mau dihapus : "))
            if(id_hapus  not in data_id):
                clear_screen()                                      #ERROR HANDLING
                print("<<< id goalS tidak ditemukan >>>")            #jika id yang dimasukkan tidak ada maka akan back to menu user
                print("-"*25)
                delay(0.5)
                menu_user(id_user)
            elif(id_hapus in data_id):
                goals.pop(id_hapus)
                print("Delete goalS berhasil")
                delay(2.5)
                break
        except ValueError:
            print("<<< Masukkan id yang ingin dihapus dengan benar! >>>")
            

def setor_bulanan(id_user):
    while True:
        try:
            data_id = []
            for index in range(len(goals)):
                if (goals[index]['id_user'] == id_user):
                    data_id.append(index)
                    print("-"*40)
                    print("ID Goals             : ", index)
                    print("Tujuan               : ", goals[index]['tujuan'])
                    print("Total Rupiah         : ", goals[index]['total_rupiah'])
                    print("Rentang Waktu(Bulan) : ",
                        goals[index]['rentang_waktu(bulan)'])
                    print("-"*40)
                elif (goals[index]['id_user'] == ""):
                    print("Goals tidak ada, silahkan buat goals terlebih dahulu")
                    delay(1.5)
                    return
                         #ERROR HANDLING JIKA TIDAK ADA GOALS MAKA AKAN DI ALIHKAN KE MENU USER 
            id_setor = int(input("Masukkan id goals yang mau disetor : "))
            if (id_setor not in data_id):
                print("ID GOALS SALAH ATAU TIDAK ADA DI DATA GOAL !")
                delay(1.5)
                break
            elif (id_setor in data_id):
                while True:
                    nominal = 0
                    print("=============================================================")
                    print("||            M E N U    S E T O R    R U T I N            ||")
                    print("-------------------------------------------------------------")
                    print("||                                                         ||")
                    print("||      [1] Rp 50.000                                      ||")
                    print("||      [2] Rp 100.000                                     ||")
                    print("||      [3] Rp 500.000                                     ||")
                    print("||      [4] Masukkan nominal sendiri                       ||")
                    print("||      [5] BACK TO MENU USER                              ||")
                    print("||                                                         ||")
                    print("=============================================================")
                    menu = input("Masukkan Pilihan : ")
                    if(menu == "1"):
                        nominal = 50000
                    elif(menu == "2"):
                        nominal = 100000
                    elif(menu == "3"):
                        nominal = 500000
                    elif(menu == "4"):
                        nominal = int(input("Masukkan Nominal : "))
                    elif(menu == "5"):
                        return
                    else:
                        print("Masukkan pilihan dengan benar!")
                        break                                           #E.H.
                    if(goals[id_setor]['total_rupiah']-nominal < 0):
                        print("Goal sudah tercapai ! ")
                        print("-"*40)
                        print("Uang lebih anda : ",nominal - goals[id_setor]['total_rupiah'] )
                        goals[id_setor]['total_rupiah'] = 0
                        delay(2.5)
                    else:
                        goals[id_setor]['total_rupiah'] = goals[id_setor]['total_rupiah']-nominal
                        print("-"*40)
                        print("Jumlah yang harus dikumpulkan lagi : Rp.",
                                goals[id_setor]['total_rupiah'])
                        print()
                        delay(2.5)
                        break
        except ValueError:
            print("<<< Masukkan pilihan yang benar! >>>")

def before_start_nabung():
    clear_screen()
    print("""==========================================================""")
    print("""|                                                        |""")
    print("""|         SELAMAT DATANG DI PROGRAM NABUNG RUTIN         |""")
    print("""|                                                        |""")
    print("""|--------------------------------------------------------|""")
    print("""|                                                        |""")
    print("""|              A JOURNEY OF A THOUSAND MILES             |""")
    print("""|              BEGINS WITH A SINGLE STEP !!!             |""")
    print("""|                                                        |""")
    print("""==========================================================""")
    delay(2.5)
    clear_screen()


def register():
    while True:
        try:
            print("-"*28)
            print("| SILAHKAN BUAT AKUN BARU! |")
            print("-"*28)
            username = input("Masukkan Username : ")
            for data in users:
                if (data['username'] == username):      #Mengecek apakah Username sudah di gunakan atau belum
                    print("<<< Username sudah digunakan >>>" )
                    delay(1.5)
                    return   
            if username.isalnum()==False:         #Mengecek apakah username ad spasi, simbol/kosong aj
                    print("<<< Username tidak boleh ada spasi, simbol dan kosong >>>")
            else:         
                password = pwinput.pwinput("Masukkan Password : ")
                konfirmasiPassword = pwinput.pwinput("Konfirmasi Password : ")
                if (password == konfirmasiPassword):
                    akunBaru = {}
                    akunBaru['username'] = username
                    akunBaru['password'] = password
                    users.append(akunBaru)
                    print("-"*35)
                    print("<<< Registrasi Berhasil, silahkan masuk >>>")
                    delay(2.5)
                    break
                else:
                    print("<<< Password dan konfirmasi password berbeda >>>")
        except ValueError:
                print("<<< Data tidak boleh kosong >>>")


def display_goal(id_user):
    for data in goals:
        if (data['id_user'] == id_user):
            print("-"*40)
            print("Tujuan               : ", data['tujuan'])
            if(data['total_rupiah'] == 0):
                print("Total Rupiah         : Sudah tercapai")
            else:
                print("Total Rupiah         : ", data['total_rupiah'])
            print("Rentang Waktu(Bulan) : ", data['rentang_waktu(bulan)'])
            print("-"*40)
    input(">> Tekan ENTER untuk melanjutkan <<")


def menu_user(id_user):
    while True:
        clear_screen()
        print("==========================================================")
        print("||                  M E N U    U S E R                  ||")
        print("==========================================================")
        print("||                                                      ||")
        print("||       [1] START MENABUNG                             ||")
        print("||       [2] VIEW GOALS                                 ||")
        print("||       [3] SETOR BULANAN                              ||")
        print("||       [4] DELETE GOAL                                ||")
        print("||       [5] LOG OUT                                    ||")
        print("||                                                      ||")
        print("==========================================================")
        menu = input("Masukkan Pilihan : ")
        if menu == "1":
            create(id_user)
        elif menu == "2":
            display_goal(id_user)
        elif menu == "3":
            setor_bulanan(id_user)
        elif menu == "4":
            delete_goal(id_user)
        elif menu == "5":
            break


def menu_utama():
    while True:
        clear_screen()
        print("============================================================")
        print("||                  M E N U    U T A M A                  ||")
        print("============================================================")
        print("||                                                        ||")
        print("||       [1] REGISTER                                     ||")
        print("||       [2] LOGIN                                        ||")
        print("||       [3] EXIT                                         ||")
        print("||                                                        ||")
        print("============================================================")
        menu = input("Masukkan Pilihan : ")
        if menu == "1":
            register()
        elif menu == "2":
            login()
        elif menu == "3":
            keluar_app()
        else:
            print("Pilihan tidak ada")  #error handling maszeh
            delay(1.5)


def login():
    username = input("Masukkan Username : ")
    password = pwinput.pwinput("Masukkan Password : ")
    for index in range(len(users)):
        if username == users[index]['username'] and password == users[index]['password']:
            before_start_nabung()
            menu_user(index)
            return
    print("-"*25)
    print("<<< Username & Password yang Anda Masukkan Salah ! >>>")
    print("<<< Apakah anda sudah punya akun?, jika belum silahkan registrasi ! >>>")
    delay(3)


def heading():
    print("""==========================================================""")
    print("""|                                                        |""")
    print("""|                                                        |""")
    print("""|          SELAMAT DATANG DI PROGRAM MY GOALS            |""")
    print("""|                                                        |""")
    print("""|                                                        |""")
    print("""==========================================================""")
    delay(2.5)
    clear_screen()
    menu_utama()





heading()       #INI TRIGGER PROGRAMNYA
