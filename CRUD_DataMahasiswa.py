import os
class Mahasiswa:
    def __init__(self):
        self.data_Maha = [["Kim Wexler","Nebraska", "Hukum", 20, 3.9], 
                          ["James McGill","Cicero", "Hukum", 20, 3.9],
                          ["Walter White","Alberquerque", "Kimia", 22, 4.0]]

    @property
    def infoProgram(self):
        print("***************************")
        print("UAS PROLAN") 
        print("Stephanus Kevin Andika Rata")
        print("22/498676/SV/21236")
        print("***************************\n\n")

    @property
    def showData(self): #Menampilkan Tabel Data Mahasiswa
        print(" " * 28 + "Tabel Data Mahasiswa")
        print("-" * 74)
        print("| No | Nama                | Asal         | Jurusan         | Umur | IPK |")
        for i, row in enumerate(self.data_Maha, start=1):
            print(f"| {i:<3}| {row[0]:<20}| {row[1]:<13}| {row[2]:<15} | {row[3]:<4} | {row[4]:<3} |")
        print("-" * 74)
    
    @property
    def addData(self): #Menambahkan Data ke List (Tabel) Data Mahasiswa
        print("\nMasukan Data Mahasiswa")
        print("----------------------\n")
        nama = input("Masukan Nama : ")
        asal = input("Masukan Asal : ")
        jurusan = input("Masukan Jurusan :")
        umur = int(input("Masukan Umur: "))
        IPK = float(input("Masukan IPK: ")) 

        self.data_Maha.append([nama,asal,jurusan,umur,IPK])

        print("\nData Mahasiswa telah ditambahkan!")

    @property
    def editData(self):  #Mengedit data pada index tertentu
        print("\nEdit Data Mahasiswa")
        print("-------------------")
        index = int(input("\nMasukan Nomor Data yang ingin diubah: "))
        os.system("cls")
        self.showData
        for i, row in enumerate(self.data_Maha, start=1):
            if i==index:
                print("\n\nMasukan Data Baru")
                print("----------------------\n")
                nama = input("Masukan Nama : ")
                asal = input("Masukan Asal : ")
                jurusan = input("Masukan Jurusan :")
                umur = int(input("Masukan Umur: "))
                IPK = float(input("Masukan IPK: "))
                self.data_Maha[index - 1] = [nama, asal, jurusan, umur, IPK]
            else:
                print("Anda Salah Memasukan Nomor!!")

    @property
    def delData(self): #Menghapus data pada index tertentu
        print("\nHapus Data Mahasiswa")
        print("-------------------")
        index = int(input("\nMasukan Nomor Data yang ingin diubah: "))
        for i, row in enumerate(self.data_Maha, start=1):
            if i==index:
                del self.data_Maha[index-1]
            else:
                print("Anda Salah Memasukan Nomor!!")

    @property
    def main(self): #Method untuk menjalankan program utama
        while True:
            os.system("cls")
            self.infoProgram
            self.showData
            print("\nMenu Data Mahasiswa:")
            print("1. Tambahkan data")
            print("2. Edit data")
            print("3. Hapus data")
            print("4. Keluar")

            pil = int (input("Masukkan pilihan (1-4): "))

            if pil == 1:
                os.system("cls")
                self.showData
                self.addData
            elif pil == 2:
                os.system("cls")
                self.showData
                print()
                self.editData
            elif pil == 3:
                os.system("cls")
                self.showData
                self.delData
            elif pil == 4:
                print("\nTerima kasih!")
                break
            else:
                print("Anda Salah Memasukan Angka!! Ulangi!!")
          
ugm = Mahasiswa()
ugm.main


