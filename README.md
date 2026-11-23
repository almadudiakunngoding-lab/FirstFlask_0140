# Aplikasi Web Flask: Parsing Method POST & Penyimpanan SQLite

Dokumentasi ini menjelaskan sintaks, struktur file, dan alur kerja pada proyek **Flask** (`FirstFlask_0140`) yang menangani *routing*, menerima input form dengan **method POST**, menata tampilan antarmuka, dan menyimpan data ke database **SQLite** (`submissions.db`).

## Penjelasan Sintaks pada Tiap File

### 1. `app.py` (Flask, POST, dan SQLite)
- **Inisialisasi Aplikasi & Path Database:** Menggunakan `Flask(__name__)` untuk membuat instance aplikasi serta `Path(__file__).resolve().parent / "submissions.db"` untuk menentukan lokasi file database SQLite.
- **Koneksi & Pembuatan Tabel SQLite:** Menggunakan `sqlite3.connect(...)` untuk membuka koneksi ke `submissions.db` dan `CREATE TABLE IF NOT EXISTS pengguna_post (id INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT NOT NULL, waktu_input TEXT NOT NULL)` agar tabel siap dipakai tanpa menimpa data lama.
- **Penanganan Request `GET` & `POST` di `/form-post`:** Menggunakan `@app.route("/form-post", methods=["GET", "POST"])` dan mengecek `request.method == "POST"`.
- **Parsing & Validasi Input Form:** Mengambil nilai input lewat `request.form.get("nama_pengguna", "").strip()`. Jika kosong, diisi variabel pesan *error*; jika ada isinya, format waktu diambil menggunakan `datetime.now().strftime(...)`.
- **Penyimpanan & Pembacaan Data:** Menyimpan data dengan perintah `INSERT INTO pengguna_post (nama, waktu_input) VALUES (?, ?)` lalu `conn.commit()`, kemudian mengambil data tersimpan menggunakan `SELECT id, nama, waktu_input FROM pengguna_post ORDER BY id DESC` dan mengirimkannya ke HTML lewat `render_template("index.html", ...)`.
- **Route Tambahan:** Mengatur *route* lain di Flask seperti `/`, `/about`, `/user/<name>`, `/post/<int:post_id>`, `/hi/<name>`, `/double/<int:n>`, `/age/<int:age>`, `/greet`, dan `/hello/<name>`.

### 2. `templates/index.html` (HTML & Jinja2)
- **Pemanggilan CSS:** Memuat *stylesheet* menggunakan `<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">`.
- **Form Method POST:** Menggunakan `<form method="POST" action="/form-post">` dengan `<input type="text" name="nama_pengguna">` dan tombol submit agar data dikirim sebagai *request* `POST`.
- **Tampilan Hasil, Error & Data SQLite:** Menggunakan sintaks Jinja2 seperti `{% if error %}`, `{% if hasil %}`, dan perulangan `{% for row in daftar_data %}` untuk menampilkan pesan validasi, hasil kiriman, serta baris data dari database ke dalam tabel HTML.

### 3. `static/styles.css` (Styling CSS)
- **Pengaturan Tata Letak & Elemen:** Mengatur tampilan visual halaman melalui selector seperti `body`, `.container`, elemen form (`label`, `input`, `button`), kotak pesan (`.error`, `.hasil`), serta tabel (`table`, `th`, `td`) agar lebih rapi dan mudah dibaca.

### 4. `submissions.db`
- File basis data lokal SQLite yang menyimpan seluruh record pada tabel `pengguna_post` (`id`, `nama`, `waktu_input`).

## Struktur Folder
```text
FirstFlask_0140/
├── app.py
├── submissions.db
├── static/
│   └── styles.css
└── templates/
    └── index.html
