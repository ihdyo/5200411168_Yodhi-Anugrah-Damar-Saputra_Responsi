# Responsi - Sistem Operasi Praktik Kelompok V - Penjadwalan Round Robin
# 5200411168 - Yodhi Anugrah Damar Saputra

# tampilkan judul program
print("")
print("=" * 45)
print("\t    MANAJEMEN ROUND ROBIN")
print("=" * 45)

# list kosong sebagai tempat menyimpan nilai
RRNamaProgram = []
RRBurstTime = []

# instruksi untuk melakukan proses
print(" * untuk memroses, masukkan karakter '='\n   (sama dengan) pada input nama program")
print("-" * 45)

# masuk perulangan untuk melakukan input nama program dan burst time
Urutan = 1
while 1:

    # sistem mendapatkan input nama program
    print("")
    NamaProgram = str(input("Masukkan nama program ke-{}\n => ".format(Urutan)))

    # sistem masuk pada kondisi yang memeriksa nama program
    # jika nama program bernama '=' maka proses perhitungan akan berjalan
    if NamaProgram == "=":

        # sistem mendapatkan input quantum time
        QuantumTime = int(input("\nMasukkan quantum time \n msec => "))

        # sistem memeriksa validitas quantum time
        if QuantumTime <= 0:
            print("")
            print("=" * 24)
            print("|" + ("!" * 5) + " PERINGATAN " + ("!" * 5) + "|")
            print("|" + ("-" * 22) + "|")
            print("|" + "  Quantum time harus  " + "|")
            print("|" + "  bilangan bulat      " + "|")
            print("|" + "  positif!            " + "|")
            print("=" * 24)
            print("")
            continue

        # sistem menghitung banyaknya jumlah program yang berjalan
        JumlahProgram = 0
        for Index in range(len(RRNamaProgram)):
            JumlahProgram += 1
            Index =+ 1

        # sistem menghitung jumlah total burst time
        TotalBurstTime = 0
        for Index in range(len(RRBurstTime)):
            TotalBurstTime += int(RRBurstTime[Index])

        # informasi program
        print("")
        print("-" * 45)
        print(" => Daftar program \t: ")
        
        for Index in range(len(RRBurstTime)):
            print("    {}. {}\t: {} msec".format(Index + 1, RRNamaProgram[Index], RRBurstTime[Index]))

        print("\n => Total program \t: {}".format(JumlahProgram))
        print(" => Total burst time \t: {}".format(TotalBurstTime))
        print(" => Quantum time \t: {}".format(QuantumTime))
        print("-" * 45)
        print("")

        # sistem masuk pada pemrosesan utama round robin
        SisaBurstTime = TotalBurstTime
        UrutanHasil = 1
        CompletionTime = 0
        while 1:

            # sistem mendapatkan index dari tiap element dalam array burst time
            for Index in range(len(RRBurstTime)):

                # memperoleh nilai element array burst time dari index
                FetchData = RRBurstTime[Index]

                # sistem memeriksa perbandingan nilai element array
                # apabila nilai element array lebih besar dari quantum time, dan total burst time tidak nol
                if FetchData >= QuantumTime and SisaBurstTime != 0:

                    # kurangi total burst time dengan burst time yang telah terpakai
                    SisaBurstTime -= QuantumTime

                    # kurangi nilai element array berdasarkan indeks sesuai dengan burst time yang telah terpakai 
                    RRBurstTime[Index] = FetchData - QuantumTime

                    # cetak informasi program sesuai urutan serta sisa burst time
                    print(" => Proses ke-{}".format(UrutanHasil))
                    print(" -  {} dieksekusi selama {} msec".format(RRNamaProgram[Index], QuantumTime))
                    print(" -  Sisa burst time {} adalah {} msec".format(RRNamaProgram[Index], RRBurstTime[Index]))
                    print(" -  Total burst time tersisa {} \n".format(SisaBurstTime))

                    # menambahkan nomor urutan hasil
                    UrutanHasil += 1

                # lainnya apabila nilai element array lebih kecil dari quantum time namun bukan nol, dan total burst time tidak nol
                elif FetchData < QuantumTime and FetchData != 0 and SisaBurstTime != 0:

                    # kurangi total burst time dengan burst time yang telah terpakai
                    SisaBurstTime -= FetchData

                    # kurangi nilai element array berdasarkan indeks sesuai dengan burst time yang telah terpakai 
                    RRBurstTime[Index] = FetchData - FetchData

                    # cetak informasi program sesuai urutan serta sisa burst time
                    print(" => Proses ke-{}".format(UrutanHasil))
                    print(" -  {} dieksekusi selama {} msec".format(RRNamaProgram[Index], FetchData))
                    print(" -  Sisa burst time {} adalah {} msec".format(RRNamaProgram[Index], RRBurstTime[Index]))
                    print(" -  Total burst time tersisa {} \n".format(SisaBurstTime))

                    # menambahkan nomor urutan hasil
                    UrutanHasil += 1

                # sistem melakukan pengkondisian apabila sisa total burst time sama dengan nol
                if SisaBurstTime == 0:

                    # tampilkan footer
                    print("=" * 45)
                    print("5200411168 - Sistem Operasi Praktik - Kelas V")
                    print("=" * 45)
                    print("")

                    # sistem akan menghentikan proses dan keluar untuk menghindari perulangan tak terbatas
                    exit()

    # Jika nama program yang dimasukkan selain karakter '=', maka sistem akan meminta input burst time
    else:

        # sistem mendapatkan input burst time
        BurstTime = int(input("Masukkan burst time dari {}\n msec => ".format(NamaProgram)))

        # sistem memeriksa apabila quantum time bernilai positif
        if BurstTime <= 0:
            print("")
            print("=" * 24)
            print("|" + ("!" * 5) + " PERINGATAN " + ("!" * 5) + "|")
            print("|" + ("-" * 22) + "|")
            print("|" + "  Burst time harus    " + "|")
            print("|" + "  bilangan bulat      " + "|")
            print("|" + "  positif!            " + "|")
            print("=" * 24)
            print("")
            continue

        # inputan nama program dan burst time dimasukan ke masing masing array
        RRNamaProgram.append(NamaProgram)
        RRBurstTime.append(BurstTime)

        # menambah nomor urutan
        Urutan += 1