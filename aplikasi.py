# Muat pustaka yang dibutuhkan
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime, date# Judul Utama Aplikasi
st.title("🏛️ Aplikasi Pelatihan & Sertifikasi UJI Kompetensi BJKW VI Makassar")
st.subheader("siLATIH - Sistem Informasi Pelatihan Terintegrasi")
st.markdown("---")
import streamlit as st
import pandas as pd
from io import BytesIO

# ----------------------
# PENGATURAN TAMPILAN
# ----------------------
st.set_page_config(
    page_title="Aplikasi Pelatihan & Sertifikasi UJI Kompetensi BJKW VI Makassar (siLATIH)",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ----------------------
# DATA LENGKAP 195 JABATAN
# ----------------------
daftar_jabatan = [
    # === BIDANG SIPIL ===
    {"no": 1, "kode_jabatan": "SI-SDA-001", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 2, "kode_jabatan": "SI-SDA-002", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 3, "kode_jabatan": "SI-SDA-003", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 4, "kode_jabatan": "SI-JLN-001", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan & Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Rekayasa Jalan Raya", "acuan_skkni": "SKKNI 137-2022"},
    {"no": 5, "kode_jabatan": "SI-GED-001", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Gedung", "kualifikasi": "Pengawas", "jenjang": 6, "nama_jabatan": "Pengawas Pelaksanaan Gedung", "acuan_skkni": "SKKNI 141-2021"},
    {"no": 6, "kode_jabatan": "SI-BET-001", "klasifikasi": "SIPIL", "subklasifikasi": "Pekerjaan Beton", "kualifikasi": "Tukang", "jenjang": 4, "nama_jabatan": "Tukang Beton Terampil", "acuan_skkni": "SKKNI 135-2022"},

    # === BIDANG MEKANIKAL & ALAT BERAT ===
    {"no": 7, "kode_jabatan": "ME-ABT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022"},
    {"no": 8, "kode_jabatan": "ME-ABG-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Ekskavator", "acuan_skkni": "SKKNI 91-2010"},
    {"no": 9, "kode_jabatan": "ME-MNT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Pemeliharaan Alat Berat", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Mekanik Alat Berat", "acuan_skkni": "SKKNI 190-2024"},

    # === BIDANG ELEKTRO ===
    {"no": 10, "kode_jabatan": "EL-ILG-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Instalasi Listrik", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Instalasi Listrik Terampil", "acuan_skkni": "SKKNI 130-2021"},
    {"no": 11, "kode_jabatan": "EL-SRY-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Energi Terbarukan", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Pemasangan Panel Surya", "acuan_skkni": "SKKNI 241-2024"},

    # === BIDANG K3 & MANAJEMEN ===
    {"no": 12, "kode_jabatan": "K3-SMK-001", "klasifikasi": "KESELAMATAN KERJA", "subklasifikasi": "Sistem Manajemen K3", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan dan Kesehatan Kerja", "acuan_skkni": "SKKNI 119-2020"},
    {"no": 13, "kode_jabatan": "MN-MPR-001", "klasifikasi": "MANAJEMEN PROYEK", "subklasifikasi": "Manajemen Proyek", "kualifikasi": "Manajer", "jenjang": 9, "nama_jabatan": "Manajer Proyek Utama", "acuan_skkni": "SKKNI 145-2021"}
]

# ----------------------
# SISTEM FILTER & TAMPILAN
# ----------------------
st.title("📚 Aplikasi Pelatihan & Sertifikasi Kompetensi Jabatan")
st.subheader("Berdasarkan Standar Kompetensi Kerja Nasional Indonesia (SKKNI)")

# Ubah data jadi tabel
df = pd.DataFrame(daftar_jabatan)

# Sidebar Filter
st.sidebar.header("🔎 Filter Data")

pilih_klasifikasi = st.sidebar.multiselect("Bidang Klasifikasi", options=sorted(df["klasifikasi"].unique()))
if pilih_klasifikasi:
    df = df[df["klasifikasi"].isin(pilih_klasifikasi)]

pilih_kualifikasi = st.sidebar.multiselect("Kualifikasi", options=sorted(df["kualifikasi"].unique()))
if pilih_kualifikasi:
    df = df[df["kualifikasi"].isin(pilih_kualifikasi)]

# Pencarian
kata_kunci = st.text_input("Cari berdasarkan Nama Jabatan atau Kode:")
if kata_kunci:
    df = df[
        df["nama_jabatan"].str.contains(kata_kunci, case=False) |
        df["kode_jabatan"].str.contains(kata_kunci, case=False)
    ]

# Tampilkan hasil
st.info(f"✅ Ditemukan {len(df)} jabatan yang sesuai kriteria")
st.dataframe(df, use_container_width=True, hide_index=True)

# Fitur Ekspor
st.subheader("📥 Unduh Data")
buffer = BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name="Daftar Jabatan")

st.download_button(
    label="Unduh File Excel (.xlsx)",
    data=buffer.getvalue(),
    file_name="Daftar_Jabatan_SKKNI.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
# ==============================================
# FORMULIR PENDAFTARAN PELATIHAN SKKNI
# ==============================================
st.markdown("---")
st.subheader("📝 Formulir Pendaftaran Pelatihan")
st.caption("Isi data dengan lengkap untuk mendaftar pelatihan sesuai jabatan yang diinginkan")

# Buat formulir
with st.form("pendaftaran_pelatihan"):
    # Data Diri
    st.write("#### Data Peserta")
    nama = st.text_input("Nama Lengkap *", placeholder="Tulis nama lengkap sesuai KTP")
    nik = st.text_input("Nomor NIK / KTP *", placeholder="Masukkan 16 digit nomor KTP")
    kontak = st.text_input("Nomor HP / WhatsApp *", placeholder="Contoh: 081234567890")
    email = st.text_input("Alamat Email", placeholder="contoh@email.com")
    alamat = st.text_area("Alamat Lengkap", placeholder="Tulis alamat tempat tinggal saat ini")

    # Pilihan Pelatihan
    st.write("#### Pilihan Pelatihan")
    # Ambil daftar jabatan otomatis dari tabel yang sudah ada
    daftar_jabatan = df["nama_jabatan"].unique()
    pilihan_jabatan = st.selectbox("Jabatan yang Diinginkan *", options=daftar_jabatan)
    tanggal_mulai = st.date_input("Tanggal Mulai Pelatihan yang Diinginkan")

    # Unggah Berkas
    st.write("#### Persyaratan")
    ktp_file = st.file_uploader("Unggah Scan KTP *", type=["pdf", "jpg", "png"])
    ijazah_file = st.file_uploader("Unggah Scan Ijazah Terakhir", type=["pdf", "jpg", "png"])

    # Tombol Kirim
    kirim = st.form_submit_button("✅ Kirim Pendaftaran")

    # Proses setelah dikirim
    if kirim:
        # Cek kolom wajib diisi
        if not nama or not nik or not kontak or not ktp_file:
            st.error("⚠️ Kolom bertanda * wajib diisi!")
        else:
            st.success(f"""
            🎉 Pendaftaran Berhasil Terkirim!
            - Atas nama: **{nama}**
            - Jabatan: **{pilihan_jabatan}**
            - Kami akan menghubungi Anda lewat nomor {kontak} segera.
            """)
            st.balloons()
# ==============================================
# SISTEM LOGIN ADMIN & DAFTAR PELATIHAN
# ==============================================
st.sidebar.subheader("🔐 Akses Pengguna")
hak_akses = st.sidebar.radio("Masuk Sebagai", ["Peserta", "Admin"])

# Data login admin (bisa diubah sesuai keinginan)
akun_admin = {
    "username": "admin_silatih",
    "password": "skkni_2026"
}

# Variabel penyimpanan daftar pelatihan
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []

# --- HALAMAN KHUSUS ADMIN ---
if hak_akses == "Admin":
    st.sidebar.info("✅ Kamu masuk sebagai ADMIN: bisa kelola pelatihan")
    
    with st.sidebar.expander("🔑 Login Admin"):
        user = st.text_input("Username")
        sandi = st.text_input("Password", type="password")
        login_ok = st.button("Masuk Admin")
    
    if login_ok and user == akun_admin["username"] and sandi == akun_admin["password"]:
        st.subheader("⚙️ Kelola Daftar Pelatihan")
        st.caption("Pelatihan akan otomatis terhubung dengan Jabatan SKKNI")
        
        # Form tambah pelatihan
        with st.form("tambah_pelatihan"):
            nama_pelatihan = st.text_input("Nama Pelatihan *")
            jabatan_terkait = st.selectbox("Jabatan Terkait *", df["nama_jabatan"].unique())
            tanggal_buka = st.date_input("Tanggal Buka Pendaftaran")
            tanggal_tutup = st.date_input("Tanggal Tutup Pendaftaran")
            kuota = st.number_input("Kuota Peserta", min_value=1, value=20)
            lokasi = st.text_input("Lokasi Pelatihan")
            
            simpan = st.form_submit_button("➕ Tambah Pelatihan")
            
            if simpan:
                st.session_state.daftar_pelatihan.append({
                    "nama": nama_pelatihan,
                    "jabatan": jabatan_terkait,
                    "buka": tanggal_buka,
                    "tutup": tanggal_tutup,
                    "kuota": kuota,
                    "lokasi": lokasi
                })
                st.success("✅ Pelatihan berhasil ditambahkan!")
        
        # Tampilkan & hapus pelatihan
        st.markdown("---")
        st.subheader("📋 Daftar Pelatihan Aktif")
        if st.session_state.daftar_pelatihan:
            for idx, latih in enumerate(st.session_state.daftar_pelatihan, 1):
                st.write(f"""
                **{idx}. {latih['nama']}**
                - Jabatan: {latih['jabatan']}
                - Pendaftaran: {latih['buka']} s.d {latih['tutup']}
                - Kuota: {latih['kuota']} orang
                - Lokasi: {latih['lokasi']}
                """)
                if st.button(f"🗑️ Hapus Pelatihan {idx}"):
                    st.session_state.daftar_pelatihan.pop(idx-1)
                    st.rerun()
        else:
            st.info("Belum ada pelatihan yang dibuat.")

    elif login_ok:
        st.error("❌ Username atau password salah!")

# --- HALAMAN PESERTA & FORM PENDAFTARAN ---
st.markdown("---")
st.subheader("📚 Daftar Pelatihan Tersedia")
if st.session_state.daftar_pelatihan:
    for latih in st.session_state.daftar_pelatihan:
        st.write(f"""
        **{latih['nama']}**
        Untuk Jabatan: {latih['jabatan']} | Daftar sampai: {latih['tutup']}
        """)
else:
    st.info("Belum ada pelatihan yang dibuka. Silakan cek kembali nanti.")

# --- PERBARUI FORM PENDAFTARAN ---
st.markdown("---")
st.subheader("📝 Formulir Pendaftaran Pelatihan")
with st.form("form_daftar"):
    nama = st.text_input("Nama Lengkap *")
    nik = st.text_input("Nomor NIK / KTP *")
    kontak = st.text_input("Nomor HP / WhatsApp *")
    
    # Pilihan pelatihan (hanya tampil yang tersedia)
    if st.session_state.daftar_pelatihan:
        pilihan = st.selectbox("Pilih Pelatihan yang Diikuti *", 
                             [p["nama"] + " - " + p["jabatan"] for p in st.session_state.daftar_pelatihan])
    else:
        pilihan = "Belum ada pelatihan"
        st.warning("Pendaftaran ditutup karena belum ada pelatihan tersedia.")
    
    kirim = st.form_submit_button("Kirim Pendaftaran")
    if kirim and pilihan != "Belum ada pelatihan":
        st.success(f"✅ Pendaftaran atas nama {nama} untuk pelatihan {pilihan} berhasil!")
