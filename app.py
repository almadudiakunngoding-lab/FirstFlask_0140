import sqlite3
from datetime import datetime
from pathlib import Path
from flask import Flask, request, render_template

app = Flask(__name__)

DB_PATH = Path(__file__).resolve().parent / "submissions.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS pengguna_post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                waktu_input TEXT NOT NULL
            )
            """
        )
        conn.commit()


init_db()


# --- Tugas: Parsing Parameter POST + Simpan ke SQLite ---
@app.route("/form-post", methods=["GET", "POST"])
def form_post():
    hasil = None
    pesan_error = None

    if request.method == "POST":
        nama = request.form.get("nama_pengguna", "").strip()
        if not nama:
            pesan_error = "Input tidak boleh kosong!"
        else:
            waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with get_db_connection() as conn:
                conn.execute(
                    "INSERT INTO pengguna_post (nama, waktu_input) VALUES (?, ?)",
                    (nama, waktu_sekarang),
                )
                conn.commit()
            hasil = f"Halo, {nama}! Data berhasil disimpan ke SQLite."

    with get_db_connection() as conn:
        daftar_data = conn.execute(
            "SELECT id, nama, waktu_input FROM pengguna_post ORDER BY id DESC"
        ).fetchall()

    return render_template(
        "index.html",
        hasil=hasil,
        pesan_error=pesan_error,
        daftar_data=daftar_data,
    )


# --- Slide 5 & 6: Basic & Static Routes ---
@app.route("/")
def home():
    return "login ke http://127.0.0.1:5000/form-post"


@app.route("/about")
def about():
    return "About us"


# --- Slide 6: Dynamic Routes ---
@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"


@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"


# --- Slide 7: Quick Check & Challenge ---
@app.route("/hi/<name>")
def hi(name):
    return f"Hi, {name}!"


@app.route("/double/<int:n>")
def double(n):
    return f"{n * 2}"


@app.route("/age/<int:age>")
def check_age(age):
    return f"You are {age}"


# --- Slide 8: GET and POST Request ---
@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return """
    <form method="post">
      <input name="name" placeholder="Masukkan nama">
      <button>Send</button>
    </form>
    """


# --- Slide 9: Render HTML Template ---
@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)