class Mahasiswa:
    def __init__(self, nama, usia, nilai):
        self.nama = nama
        self.usia = usia
        self.nilai = nilai
        
class Tampilan:
    @staticmethod
    def tampilkan_mahasiswa(mahasiswa_list):
        print("daftar mahasiswa")
        print(f"{'Nama':<25} {'Usia':<5} {'Nilai':<10}")
        print("=" * 40)
        for mahasiswa in mahasiswa_list:
            print(f"{mahasiswa.nama:<25} {mahasiswa.usia:<5} {mahasiswa.nilai:<10.2f}")
        print("=" * 40)
        
        
class Proses:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, nama, usia, nilai):
        if not nama or not isinstance(nama, str):
            raise ValueError("Nama harus berupa string yang tidak kosong.")
        if not isinstance(usia, int) or usia <= 0:
            raise ValueError("Usia harus berupa bilangan bulat positif.")
        if not isinstance(nilai, float) or not (0 <= nilai <= 100):
            raise ValueError("Nilai harus berupa float antara 0 dan 100.")

        mahasiswa = Mahasiswa(nama, usia, nilai)
        self.mahasiswa_list.append(mahasiswa)

    def ambil_mahasiswa(self):
        return self.mahasiswa_list
    
    
def main():
    proses = Proses()

    while True:
        try:
            nama = input("Masukkan nama mahasiswa: ")
            usia = int(input("Masukkan usia mahasiswa: "))
            nilai = float(input("Masukkan nilai mahasiswa (0-100): "))

            proses.tambah_mahasiswa(nama, usia, nilai)

            lebih = input("Apakah Anda ingin menambahkan mahasiswa lain? (y/n): ")
            if lebih.lower() != 'y':
                break
        except ValueError as e:
            print(f"Kesalahan input: {e}")

    # Tampilkan data mahasiswa
    mahasiswa_list = proses.ambil_mahasiswa()
    Tampilan.tampilkan_mahasiswa(mahasiswa_list)

if __name__ == "__main__":
    main()
