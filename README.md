
# ZIP to Text

ZIP to Text adalah aplikasi berbasis Flask yang memungkinkan Anda untuk mengunggah file ZIP, memilih file tertentu dari dalamnya, dan menghasilkan output berisi isi file tersebut dengan format yang terorganisir.

## **Fitur**
- Unggah file ZIP dan pilih file yang ingin diproses.
- Struktur folder ditampilkan dengan opsi Select All / Unselect All.
- Hasil dapat disalin ke clipboard atau diunduh sebagai file teks.

---

## **Langkah-Langkah untuk Memulai**

### **1. Clone Repository**
Clone repository ini ke komputer Anda menggunakan perintah berikut:
```bash
git clone https://github.com/NickDabizaz/zip-to-text.git
```

### **2. Masuk ke Direktori Proyek**
Pindah ke folder proyek:
```bash
cd zip-to-text
```

### **3. Jalankan Aplikasi**
Jalankan aplikasi dengan perintah berikut:
```bash
python app.py
```

### **4. Akses Aplikasi**
Buka browser dan akses aplikasi di:
```
http://127.0.0.1:5000
```

---

## **Penggunaan**
1. Unggah file ZIP menggunakan form yang tersedia.
2. Pilih file yang ingin diproses menggunakan checkbox.
3. Klik tombol **Generate Output** untuk menampilkan isi file.
4. Salin hasil ke clipboard menggunakan tombol **Copy to Clipboard** atau unduh hasil menggunakan tombol **Download as File**.

---

## **Struktur Folder**
```
zip-to-text/
├── app.py
├── templates/
│   └── index.html
└── README.md
```

- **app.py**: File utama aplikasi Flask.
- **templates/index.html**: Antarmuka pengguna.
- **requirements.txt**: Daftar dependensi Python (Flask).

---

## **Lisensi**
Aplikasi ini dirilis di bawah lisensi [MIT](LICENSE).
