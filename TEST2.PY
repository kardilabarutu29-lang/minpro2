# LIST DATA PEKERJA
data_pekerja = [
    {"nama": "Asep", "nik": 670108050007, "jabatan": "Askep"},
    {"nama": "Hakim", "nik": 6472061123812, "jabatan": "Pemanen"},
    {"nama": "Attar", "nik": 6472061903070005, "jabatan": "Manajer"}
]

# Menampilkan semua data pekerja
def tampilkan_data():
    if not data_pekerja:
        print("Data pekerja kosong.")
    else:
        print("Daftar Pekerja:")
        for i, pekerja in enumerate(data_pekerja, start=1):
            print(f"{i}. Nama: {pekerja['nama']}, NIK: {pekerja['nik']}, Jabatan: {pekerja['jabatan']}")

# Menambahkan pekerja baru
def tambah_data():
    try:
        nama = input("Masukkan nama: ")
        nik = int(input("Masukkan NIK: "))
        jabatan = input("Masukkan jabatan: ")
        data_pekerja.append({"nama": nama, "nik": nik, "jabatan": jabatan})
        print(f"Data {nama} berhasil ditambahkan.")
    except ValueError:
        print("eeettt tidak valid dong. NIK nya harus angka")
    except KeyboardInterrupt :
        print("Tidak bisa ctrl c")


# Menghapus pekerja berdasarkan NIK
def hapus_data():
    try:
        nik = int(input("Masukkan NIK pekerja yang ingin dihapus: "))
        for pekerja in data_pekerja:
            if pekerja["nik"] == nik:
                data_pekerja.remove(pekerja)
                print(f"Data {pekerja['nama']} berhasil dihapus.")
                return
        print("Data tidak ditemukan.")
    except ValueError:
        print("eeettt tidak valid dong. NIK nya harus angka")
    except KeyboardInterrupt :
        print("Tidak bisa ctrl c")


# Mengupdate data pekerja berdasarkan NIK
def update_data():
    try:
        nik = int(input("Masukkan NIK pekerja yang ingin diperbarui: "))
        for pekerja in data_pekerja:
            if pekerja["nik"] == nik:
                print("Data lama:", pekerja)
                pekerja["nama"] = input("Masukkan nama baru: ")
                pekerja["jabatan"] = input("Masukkan jabatan baru: ")
                print("Data berhasil diperbarui.")
                return
        print("Data tidak ditemukan.")
    except ValueError:
        print("eeettt tidak valid dong. NIK nya harus angka")
    except KeyboardInterrupt :
        print("Tidak bisa ctrl c")

# login role
print ("silakan login dulu")
role = input("Masukkan role (ADMIN atau mau masuk USER gankkk):")
if role == "ADMIN":
    while True:
        print("\n Menu Admin:")
        print("1. Tambah Data Pekerja")
        print("2. Tampilkan Data Pekerja")
        print("3. Update Data Pekerja")
        print("4. Hapus Data Pekerja")
        print("5. Keluar")

        try:
            pilihan = int(input("Pilih menu (1-5): "))
            if pilihan == 1:
                tambah_data()
            elif pilihan == 2:
                tampilkan_data()
            elif pilihan == 3:
                update_data()
            elif pilihan == 4:
                hapus_data()
            elif pilihan == 5:
                print("Program selesai. Terima kasih yaaa i love you!")
                break
            else:
                print("Pilihan tidak tersedia gantenggg.")
        except ValueError:
            print("aku bilang Input harus berupa angka.")
        except KeyboardInterrupt :
            print("Tidak bisa ctrl c")

elif role == "USER":
    while True:
        print("\n Menu User:")
        print("1. Tampilkan Data Pekerja")
        print("2. Keluar")

        try:
            pilihan = int(input("Pilih menu (1-2): "))
            if pilihan == 1:
                tampilkan_data()
            elif pilihan == 2:
                print("Program selesai. Terima kasih yaaa i love you!")
                break
            else:
                print("Pilihan tidak tersedia.")
        except ValueError:
            print("Input harus berupa angka.")
        except KeyboardInterrupt :
            print("Tidak bisa ctrl c")
else:
    print("hayuuu Role tidak dikenali. coba jalankan ulang program.")
