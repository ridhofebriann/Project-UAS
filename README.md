Nama        : M.Ridho Febrian <p>

Kelas       : TI.24.A.5 <p>

Nim         : 312410500 <p>

Mata kuliah : Bahasa Pemrograman <p>


# Project-UAS BAHASA PEMROGRAMAN

![tugas](https://github.com/ridhofebriann/Project-UAS/blob/main/tugas%20uas.png?raw=true)

# 1. class mahasiswa (class data)
```python
class Mahasiswa:
    def __init__(self, nama, usia, nilai):
        self.nama = nama
        self.usia = usia
        self.nilai = nilai
```
penjelasan :

 class ini berfungsi sebagai model data untuk mahasiswa. Ini menyimpan informasi tentang nama, usia, dan nilai mahasiswa.
Kelas `Mahasiswa`: Kelas ini digunakan untuk merepresentasikan seorang mahasiswa.

Metode `__init__`: Ini adalah metode inisialisasi yang dipanggil saat kita membuat objek baru dari kelas ini.

Parameter:

`nama`: Nama mahasiswa.

`usia`: Usia mahasiswa.

`nilai`: Nilai mahasiswa.

Atribut:

self.nama, self.usia, dan self.nilai adalah atribut yang menyimpan informasi tentang mahasiswa. self merujuk pada objek saat ini.

# 2. class tampilan (class view)
```python
class Tampilan:
    @staticmethod
    def tampilkan_mahasiswa(mahasiswa_list):
        print("daftar mahasiswa")
        print(f"{'Nama':<25} {'Usia':<5} {'Nilai':<10}")
        print("=" * 40)
        for mahasiswa in mahasiswa_list:
            print(f"{mahasiswa.nama:<25} {mahasiswa.usia:<5} {mahasiswa.nilai:<10.2f}")
        print("=" * 40)
```

penjelasan:

class ini bertanggung jawab untuk menampilkan data mahasiswa. Metode tampilkan_mahasiswa mencetak daftar mahasiswa dengan format yang rapi.

Kelas `Tampilan`: Kelas ini bertanggung jawab untuk menampilkan data mahasiswa.

Metode Statis `tampilkan_mahasiswa`:

Metode ini tidak memerlukan objek untuk dipanggil (ditandai dengan `@staticmethod`).

Parameter: `mahasiswa_list` adalah daftar objek mahasiswa yang akan ditampilkan.

Format Tabel:

Menggunakan `print` untuk mencetak header tabel dan garis pemisah.
Menggunakan format string untuk memastikan kolom-kolom data teratur. Misalnya, `{'Nama':<25}` berarti kolom "Nama" akan memiliki lebar 25 karakter.

# 3. class prosess (class Process)
```python
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
```

penjelasan:

Kelas Proses: Kelas ini mengelola logika untuk menambah dan mengambil data mahasiswa.

Atribut `mahasiswa_list`: Ini adalah daftar yang menyimpan semua objek mahasiswa.

Metode `tambah_mahasiswa`:

Memeriksa validitas input:

-Nama harus berupa string yang tidak kosong.

-Usia harus berupa bilangan bulat positif.

-Nilai harus berupa float antara 0 dan 100.

Jika input valid, objek Mahasiswa baru dibuat dan ditambahkan ke `mahasiswa_list`.

Metode `ambil_mahasiswa`: Mengembalikan daftar mahasiswa yang telah ditambahkan

Fungsi: Kelas ini mengelola logika bisnis untuk menambah mahasiswa dan mengambil daftar mahasiswa. Metode tambah_mahasiswa juga melakukan validasi input.

OOP: Kelas ini berfungsi sebagai penghubung antara data (kelas Mahasiswa) dan tampilan (kelas Tampilan).

# 4. Fungsi main (Fungsi utama program)
```python
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
```

penjelasan:

Fungsi main: Ini adalah titik masuk program.

Instansiasi Proses: Membuat objek Proses untuk mengelola data mahasiswa.

`Loop Input`:

Program meminta pengguna untuk memasukkan nama, usia, dan nilai mahasiswa.

Jika input tidak valid, program akan menangkap ValueError dan menampilkan pesan kesalahan.

Setelah memasukkan data, pengguna ditanya apakah ingin menambahkan mahasiswa lain. Jika tidak, loop akan berhenti.

Menampilkan Data: Setelah semua data dimasukkan, program memanggil metode tampilkan_mahasiswa dari kelas Tampilan untuk menampilkan daftar mahasiswa.

# Hasil Program Saya:
![foto](https://github.com/ridhofebriann/Project-UAS/blob/main/hasil.png?raw=true)
