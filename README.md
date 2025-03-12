
# Panduan Penggunaan Program

## Deskripsi
Program ini memiliki dua fungsi utama:
1. **Membuat Folder dan File**: Program akan membuat folder bertingkat di dalam direktori pengguna dengan nama `SystemFolderRoot`. Setiap folder akan memiliki nama berformat `System_X` (dengan `X` adalah angka) dan berisi 500 file teks (`infoX.txt`).
2. **Menjalankan Game**: Program akan mencoba menjalankan game `snake.py` yang berada dalam folder `data_game` di direktori yang sama dengan skrip.

---

## Persyaratan
- Python harus sudah terinstal di sistem.
- Pastikan ada ruang penyimpanan yang cukup untuk membuat banyak folder dan file teks.
- File `snake.py` harus tersedia dalam direktori `data_game` agar dapat dijalankan.

---

## Cara Menggunakan

### 1. Jalankan Program
   
   - Buka terminal atau command prompt.
   - Navigasi ke direktori tempat file skrip Python berada.
   - Jalankan perintah berikut:
     ```sh
     python nama_file.py
     ```
   - Program akan secara otomatis membuat folder dan file serta menjalankan game `snake.py` jika tersedia.

### 2. Cek Folder yang Dibuat
   - Buka `C:\Users\<NamaPengguna>\SystemFolderRoot` untuk melihat folder yang dibuat.
   - Setiap folder bernama `System_X` berisi 500 file teks `infoX.txt` dengan isi lorem ipsum.

### 3. Menjalankan Game
   - Jika `snake.py` tersedia di `data_game`, program akan mencoba menjalankannya.
   - Jika tidak tersedia, program akan menampilkan pesan error.

---

## Catatan Tambahan
- Jika program dijalankan kembali, folder baru akan dilanjutkan dari angka terakhir yang tersedia.
- Jika direktori `SystemFolderRoot` belum ada, program akan membuatnya secara otomatis.
- Jika penyimpanan penuh, program akan berhenti membuat folder dan file.

---

## Troubleshooting

| Masalah | Penyebab | Solusi |
|---------|---------|--------|
| Tidak ada folder yang dibuat | Direktori tidak memiliki izin tulis | Jalankan program sebagai administrator atau ubah izin direktori |
| Game tidak berjalan | `snake.py` tidak ditemukan | Pastikan file `snake.py` ada di folder `data_game` |
| Penyimpanan penuh | Terlalu banyak file yang dibuat | Hapus beberapa file atau gunakan drive dengan lebih banyak ruang |

---

## Lisensi
Program ini bebas digunakan dan dimodifikasi sesuai kebutuhan.

