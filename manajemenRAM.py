# Responsi - Sistem Operasi Praktik Kelompok V - Manajemen RAM
# 5200411168 - Yodhi Anugrah Damar Saputra

# tampilkan judul program
print("")
print("=" * 45)
print("\t\tMANAJEMEN RAM")
print("=" * 45)

# instruksi untuk melakukan proses
print(" * untuk memroses, masukkan angka 0 (nol) \n   pada input nama program")
print("-" * 45)

# sistem menerima input yang sesuai
RAMGB = int(input("Masukkan kapasitas total RAM! \n GB => "))

print("")

BlokPerUnit = int(input("Masukkan kapasitas blok per unit! \n MB => "))

print("")

OSGB = int(input("Masukkan kapasitas OS! \n GB => "))

# sistem memeriksa validitas input
if RAMGB < 0 or BlokPerUnit < 0 or OSGB < 0:
    print("")
    print("=" * 24)
    print("|" + ("!" * 5) + " PERINGATAN " + ("!" * 5) + "|")
    print("|" + ("-" * 22) + "|")
    print("|" + "  Input harus berupa  " + "|")
    print("|" + "  bilangan positif!   " + "|")
    print("=" * 24)
    print("")
    
    # apabila input tidak valid, keluar dari sistem
    exit()

# sistem melakukan perulangan untuk menghitung proses utama
print("-" * 45)
ProgramTotal = 0
Urutan = 1
while 1:

    # sistem memperoleh input program tereksekusi
    ProgramTereksekusi = int(input("Masukkan kapasitas RAM program ke-{}\n MB => ".format(Urutan)))
    print("")

    # jumlah kapasitas semua program tereksekusi
    ProgramTotal += ProgramTereksekusi

    # sistem melakukan pengondisian
    # jika kapasitas program tereksekusi bernilai 0 maka akan masuk proses utama 
    if ProgramTereksekusi == 0:

        # konversi data yang diperlukan
        RAMMB = RAMGB * 1024
        OSMB = OSGB * 1024
        PetaBit = RAMMB / BlokPerUnit

        # opearsi data sisa
        RAMMBTerpakai = OSMB + ProgramTotal
        BlokTerpakai = round(RAMMBTerpakai / BlokPerUnit)
        RAMGBTerpakai = RAMMBTerpakai / 1024

        # opearsi data terpakai
        RAMMBSisa = RAMMB - RAMMBTerpakai
        BlokSisa = round(PetaBit - BlokTerpakai)
        RAMGBSisa = RAMMBSisa / 1024

        # tampilkan info output yang diperlukan
        print("-" * 45)
        print(" => Kapasitas total RAM \t: ")
        print("    - {} GB \n    - {} MB \n".format(RAMGB, RAMMB))

        print(" => Kapasitas total peta bit \t: ")
        print("    - {} MB \n".format(PetaBit))

        print(" => Kapasitas per peta bit \t: ")
        print("    - {} MB \n".format(BlokPerUnit))

        print(" => Kapasitas RAM terpakai \t: ")
        print("    - {} GB \n    - {} MB \n".format(RAMGBTerpakai, RAMMBTerpakai))

        print(" => Kapasitas RAM tersisa \t: ")
        print("    - {} GB \n    - {} MB \n".format(RAMGBSisa, RAMMBSisa))

        print(" => Jumlah blok bernilai 1 \t: ")
        print("    - {} \n".format(BlokTerpakai))
        print(" => Jumlah blok bernilai 0 \t: ")
        print("    - {}".format(BlokSisa))

        # tampilkan footer
        print("=" * 45)
        print("5200411168 - Sistem Operasi Praktik - Kelas V")
        print("=" * 45)
        print("")

        # sistem memeriksa validitas sisa ram apabila bernilai negatif
        if RAMGBSisa < 0 or RAMMBSisa < 0:

            # tampilkan peringatan
            print("=" * 24)
            print("|" + ("!" * 5) + " PERINGATAN " + ("!" * 5) + "|")
            print("|" + ("-" * 22) + "|")
            print("|" + "  Kapasitas RAM tidak " + "|")
            print("|" + "  memungkinkan untuk  " + "|")
            print("|" + "  menjalankan program!" + "|")
            print("=" * 24)
            print("")
            break
        break

    # sistem memeriksa validitas kapasitas program tereksekusi
    elif ProgramTereksekusi < 0:

        # tampilkan peringatan
        print("")
        print("=" * 24)
        print("|" + ("!" * 5) + " PERINGATAN " + ("!" * 5) + "|")
        print("|" + ("-" * 22) + "|")
        print("|" + "  Input harus berupa  " + "|")
        print("|" + "  bilangan positif!   " + "|")
        print("=" * 24)
        print("")
        continue

    # sistem memeriksa validitas kapasitas program tereksekusi bernilai positif 
    elif ProgramTereksekusi > 0:

        # tambahkan nilai urutan
        Urutan += 1
        continue