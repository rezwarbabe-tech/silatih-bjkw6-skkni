# ==============================================
# 1. MUAT PUSTAKA & GAYA KUSTOM PUPR
# ==============================================
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime, date

# === GAYA WARNA & LATAR IDENTITAS PUPR ===
st.markdown("""
<style>
/* Warna dasar Kementerian PUPR: Biru Resmi */
:root {
    --pu-biru-utama: #004B87;
    --pu-biru-terang: #0071BC;
    --pu-biru-muda: #E8F3FC;
    --pu-abu: #F5F7FA;
    --pu-teks: #2C3E50;
}

/* Latar belakang dengan motif batik ringan */
.stApp {
    background-color: var(--pu-biru-muda);
    background-image: radial-gradient(circle at 20% 50%, rgba(0,75,135,0.03) 0%, transparent 50%),
                      radial-gradient(circle at 80% 20%, rgba(0,113,188,0.03) 0%, transparent 50%);
    background-attachment: fixed;
}

/* Judul dan teks utama */
h1, h2, h3, h4 {
    color: var(--pu-biru-utama);
    font-weight: 700;
}
p, div, span {
    color: var(--pu-teks);
}

/* Tombol gaya PUPR */
.stButton>button, .stDownloadButton>button {
    background-color: var(--pu-biru-utama);
    color: white;
    border-radius: 6px;
    border: 2px solid var(--pu-biru-utama);
    padding: 0.5rem 1.2rem;
    font-weight: 500;
    transition: all 0.3s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: var(--pu-biru-terang);
    border-color: var(--pu-biru-terang);
    transform: translateY(-1px);
}

/* Kotak info dan pesan */
.pu-info {
    background: white;
    border-left: 6px solid var(--pu-biru-utama);
    padding: 1.2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,75,135,0.08);
    margin-bottom: 1rem;
}
.pu-sukses {
    background: #F0F9FF;
    border-left: 6px solid #059669;
    padding: 1.2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(5,150,105,0.08);
    margin-bottom: 1rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 3px solid var(--pu-biru-muda);
}
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {
    color: var(--pu-biru-utama);
}

/* Tabel */
.stDataFrame {
    border-radius: 8px;
    border: 1px solid var(--pu-biru-muda);
}
</style>
""", unsafe_allow_html=True)

# ==============================================
# 2. KONFIGURASI & JUDUL UTAMA
# ==============================================
st.set_page_config(
    page_title="siLATIH - BJKW VI Makassar",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Garis pemisah atas berwarna biru PU
st.markdown("<hr style='border: 3px solid #004B87; border-radius: 2px; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)

st.title("🏛️ Aplikasi Pelatihan & Sertifikasi UJI Kompetensi")
st.subheader("Balai Jasa Konstruksi Wilayah VI Makassar")
st.markdown("<h3 style='color:#004B87;'>siLATIH - Sistem Informasi Pelatihan Terintegrasi</h3>", unsafe_allow_html=True)

st.markdown("""
<div class="pu-info">
📢 <strong>Selamat Datang!</strong><br>
Aplikasi resmi untuk informasi jabatan sesuai Standar Kompetensi Kerja Nasional Indonesia (SKKNI), pengelolaan pelatihan, serta pendaftaran uji kompetensi di lingkungan Kementerian Pekerjaan Umum dan Perumahan Rakyat.
</div>
""", unsafe_allow_html=True)

# ----------------------
# 3. DATA LENGKAP JABATAN SKKNI
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
# 4. FILTER & TABEL DATA JABATAN
# ----------------------
st.header("📋 Daftar Jabatan Berdasarkan SKKNI")

df = pd.DataFrame(daftar_jabatan)

st.sidebar.markdown("---")
st.sidebar.header("🔎 Saring Data")

pilih_klasifikasi = st.sidebar.multiselect("Bidang Klasifikasi", options=sorted(df["klasifikasi"].unique()))
if pilih_klasifikasi:
    df = df[df["klasifikasi"].isin(pilih_klasifikasi)]

pilih_kualifikasi = st.sidebar.multiselect("Tingkat Kualifikasi", options=sorted(df["kualifikasi"].unique()))
if pilih_kualifikasi:
    df = df[df["kualifikasi"].isin(pilih_kualifikasi)]

kata_kunci = st.text_input("🔍 Cari Jabatan atau Kode Jabatan:")
if kata_kunci:
    df = df[
        df["nama_jabatan"].str.contains(kata_kunci, case=False) |
        df["kode_jabatan"].str.contains(kata_kunci, case=False)
    ]

st.info(f"✅ Menampilkan **{len(df)}** jabatan yang sesuai kriteria Anda")
st.dataframe(df, use_container_width=True, hide_index=True)

# Unduh Data
st.subheader("📥 Unduh Daftar Jabatan")
buffer = BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name="Daftar Jabatan SKKNI")

st.download_button(
    label="📂 Unduh File Excel (.xlsx)",
    data=buffer.getvalue(),
    file_name="Daftar_Jabatan_SKKNI_BJKW6_PUPR.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ==============================================
# 5. SISTEM LOGIN ADMIN & KELOLA PELATIHAN
# ==============================================
st.sidebar.markdown("---")
st.sidebar.header("🔐 Akses Pengguna")
hak_akses = st.sidebar.radio("Masuk Sebagai", ["Peserta Pelatihan", "Pengelola Aplikasi"])

akun_admin = {"username": "admin_silatih", "password": "pupr_bjkw6_2026"}

if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []

if hak_akses == "Pengelola Aplikasi":
    st.sidebar.success("✅ Mode Pengelola: Bisa mengatur pelatihan")
    
    with st.sidebar.expander("🔑 Masuk Admin"):
        user = st.text_input("Nama Pengguna")
        sandi = st.text_input("Kata Sandi", type="password")
        login_ok = st.button("Masuk Akun")
    
    if login_ok and user == akun_admin["username"] and sandi == akun_admin["password"]:
        st.markdown("---")
        st.header("⚙️ Pengaturan Pelatihan")
        st.caption("Buat pelatihan baru yang terhubung langsung dengan jabatan SKKNI")
        
        with st.form("tambah_pelatihan", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                nama_pelatihan = st.text_input("Nama Pelatihan *")
                jabatan_terkait = st.selectbox("Jabatan Terkait *", df["nama_jabatan"].unique())
                lokasi = st.text_input("Lokasi Pelatihan")
            with col2:
                tanggal_buka = st.date_input("Tanggal Buka Pendaftaran")
                tanggal_tutup = st.date_input("Tanggal Tutup Pendaftaran")
                kuota = st.number_input("Kuota Peserta", min_value=1, value=25)
            
            simpan = st.form_submit_button("➕ Simpan Pelatihan Baru")
            if simpan:
                st.session_state.daftar_pelatihan.append({
                    "nama": nama_pelatihan, "jabatan": jabatan_terkait,
                    "buka": tanggal_buka, "tutup": tanggal_tutup,
                    "kuota": kuota, "lokasi": lokasi
                })
                st.success("✅ Pelatihan berhasil ditambahkan!")
                st.rerun()
        
        st.markdown("---")
        st.subheader("📋 Daftar Pelatihan Aktif")
        if st.session_state.daftar_pelatihan:
            for idx, latih in enumerate(st.session_state.daftar_pelatihan, 1):
                with st.expander(f"📌 {idx}. {latih['nama']}"):
                    st.write(f"🔹 Jabatan: {latih['jabatan']}")
                    st.write(f"🔹 Periode Daftar: {latih['buka']} s.d {latih['tutup']}")
                    st.write(f"🔹 Kuota: {latih['kuota']} peserta")
                    st.write(f"🔹 Lokasi: {latih['lokasi']}")
                    if st.button(f"🗑️ Hapus Pelatihan", key=f"hapus_{idx}"):
                        st.session_state.daftar_pelatihan.pop(idx-1)
                        st.rerun()
        else:
            st.info("ℹ️ Belum ada pelatihan yang dibuat.")

    elif login_ok:
        st.error("❌ Nama pengguna atau kata sandi salah!")

# --- HALAMAN PESERTA ---
st.markdown("---")
st.header("📚 Pelatihan yang Sedang Dibuka")
if st.session_state.daftar_pelatihan:
    for latih in st.session_state.daftar_pelatihan:
        st.markdown(f"""
        <div class="pu-info">
        <h4>{latih['nama']}</h4>
        <p>Untuk Jabatan: <strong>{latih['jabatan']}</strong><br>
        Batas Pendaftaran: {latih['tutup']} | Kuota: {latih['kuota']} orang<br>
        Lokasi: {latih['lokasi']}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("ℹ️ Saat ini belum ada pelatihan yang dibuka.")

# --- FORMULIR PENDAFTARAN ---
st.markdown("---")
st.header("📝 Formulir Pendaftaran Pelatihan")

with st.form("pendaftaran_pelatihan"):
    st.subheader("👤 Data Diri Peserta")
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Nama Lengkap *", placeholder="Sesuai KTP")
        nik = st.text_input("Nomor NIK / KTP *", placeholder="16 digit angka")
    with col2:
        kontak = st.text_input("Nomor HP / WhatsApp *", placeholder="08xx-xxxx-xxxx")
        email = st.text_input("Alamat Email", placeholder="anda@email.com")
    
    alamat = st.text_area("Alamat Lengkap Tempat Tinggal")

    st.subheader("🎓 Pilihan Pelatihan")
    if st.session_state.daftar_pelatihan:
        pilihan = st.selectbox("Pilih Pelatihan yang Diikuti *", 
                             [p["nama"] + " — " + p["jabatan"] for p in st.session_state.daftar_pelatihan])
    else:
        pilihan = "Belum ada pelatihan tersedia"
        st.warning("Pendaftaran ditutup.")

    st.subheader("📎 Berkas Persyaratan")
    ktp_file = st.file_uploader("Unggah Scan KTP *", type=["pdf", "jpg", "jpeg", "png"])
    ijazah_file = st.file_uploader("Unggah Scan Ijazah Terakhir", type=["pdf", "jpg", "jpeg", "png"])

    kirim = st.form_submit_button("✅ Kirim Pendaftaran Sekarang")

    if kirim:
        if not nama or not nik or not kontak or not ktp_file or pilihan == "Belum ada pelatihan tersedia":
            st.error("⚠️ Lengkapi semua kolom bertanda *!")
        else:
            st.balloons()
            st.markdown(f"""
            <div class="pu-sukses">
            <h4>🎉 Pendaftaran Berhasil Diterima!</h4>
            <p>Terima kasih <strong>{nama}</strong> untuk pelatihan <strong>{pilihan}</strong>.<br>
            Kami hubungi lewat {kontak} paling lambat 3 hari kerja.</p>
            </div>
            """, unsafe_allow_html=True)

# Kaki halaman
st.markdown("<hr style='border: 2px solid #004B87; margin-top: 2rem;'>", unsafe_allow_html=True)
st.caption("© 2026 Balai Jasa Konstruksi Wilayah VI Makassar — Kementerian Pekerjaan Umum dan Perumahan Rakyat | siLATIH v1.0")
