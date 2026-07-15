# ==============================================
# APLIKASI siLATIH - BJKW VI MAKASSAR (VERSI 2.0)
# Balai Jasa Konstruksi Wilayah VI Makassar - PUPR
# Fitur: Pengelolaan Status Pelatihan & Hak Akses Terbatas
# ==============================================

# 1. MUAT PUSTAKA & GAYA KUSTOM PUPR
# ==============================================
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime, date
import re

# === GAYA WARNA & LATAR IDENTITAS PUPR ===
st.markdown("""
<style>
:root {
    --pu-biru-utama: #004B87;
    --pu-biru-terang: #0071BC;
    --pu-biru-muda: #E8F3FC;
    --pu-merah: #DC2626;
    --pu-hijau: #059669;
    --pu-kuning: #F59E0B;
    --pu-abu: #F5F7FA;
    --pu-teks: #2C3E50;
}
.stApp {
    background-color: var(--pu-biru-muda);
    background-image: radial-gradient(circle at 20% 50%, rgba(0,75,135,0.03) 0%, transparent 50%),
                      radial-gradient(circle at 80% 20%, rgba(0,113,188,0.03) 0%, transparent 50%);
    background-attachment: fixed;
}
h1, h2, h3, h4 { color: var(--pu-biru-utama); font-weight: 700; }
.stButton>button, .stDownloadButton>button {
    background-color: var(--pu-biru-utama); color: white; border-radius: 6px;
    border: 2px solid var(--pu-biru-utama); padding: 0.5rem 1.2rem;
    font-weight: 500; transition: all 0.3s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: var(--pu-biru-terang); border-color: var(--pu-biru-terang); transform: translateY(-1px);
}
.pu-info { background: white; border-left: 6px solid var(--pu-biru-utama); padding: 1.2rem; border-radius: 8px; margin-bottom: 1rem; }
.pu-sukses { background: #F0FDF4; border-left: 6px solid var(--pu-hijau); padding: 1.2rem; border-radius: 8px; margin-bottom: 1rem; }
.pu-tolak { background: #FEF2F2; border-left: 6px solid var(--pu-merah); padding: 1.2rem; border-radius: 8px; margin-bottom: 1rem; }
.pu-kuning { background: #FFFBEB; border-left: 6px solid var(--pu-kuning); padding: 1.2rem; border-radius: 8px; margin-bottom: 1rem; }
section[data-testid="stSidebar"] { background-color: white; border-right: 3px solid var(--pu-biru-muda); }
.stDataFrame { border-radius: 8px; border: 1px solid var(--pu-biru-muda); }
div[data-testid="stForm"] {background: white; padding: 1.5rem; border-radius: 10px;}
.status-akan {color: var(--pu-biru-terang); font-weight: 600;}
.status-langsung {color: var(--pu-hijau); font-weight: 600;}
.status-selesai {color: #6B7280; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

# ==============================================
# 2. KONFIGURASI & DATA REFERENSI
# ==============================================
st.set_page_config(page_title="siLATIH - BJKW VI Makassar", page_icon="🏗️", layout="wide", initial_sidebar_state="expanded")

# === TABEL PERSYARATAN PENGALAMAN KERJA ===
persyaratan = {
    "Ahli Utama Teknik Sumber Daya Air": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Sumber Daya Air": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Sumber Daya Air": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Rekayasa Jalan Raya": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Pengawas Pelaksanaan Gedung": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Tukang Beton Terampil": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Operator Bulldozer": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Ekskavator": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Teknisi Mekanik Alat Berat": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Instalasi Listrik Terampil": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Pemasangan Panel Surya": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Ahli Utama Keselamatan dan Kesehatan Kerja": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Manajer Proyek Utama": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    }
}

daftar_jabatan = [
    {"no": 1, "kode_jabatan": "SI-SDA-001", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 2, "kode_jabatan": "SI-SDA-002", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 3, "kode_jabatan": "SI-SDA-003", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 4, "kode_jabatan": "SI-JLN-001", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan & Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Rekayasa Jalan Raya", "acuan_skkni": "SKKNI 137-2022"},
    {"no": 5, "kode_jabatan": "SI-GED-001", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Gedung", "kualifikasi": "Pengawas", "jenjang": 6, "nama_jabatan": "Pengawas Pelaksanaan Gedung", "acuan_skkni": "SKKNI 141-2021"},
    {"no": 6, "kode_jabatan": "SI-BET-001", "klasifikasi": "SIPIL", "subklasifikasi": "Pekerjaan Beton", "kualifikasi": "Tukang", "jenjang": 4, "nama_jabatan": "Tukang Beton Terampil", "acuan_skkni": "SKKNI 135-2022"},
    {"no": 7, "kode_jabatan": "ME-ABT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022"},
    {"no": 8, "kode_jabatan": "ME-ABG-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Ekskavator", "acuan_skkni": "SKKNI 91-2010"},
    {"no": 9, "kode_jabatan": "ME-MNT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Pemeliharaan Alat Berat", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Mekanik Alat Berat", "acuan_skkni": "SKKNI 190-2024"},
    {"no": 10, "kode_jabatan": "EL-ILG-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Instalasi Listrik", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Instalasi Listrik Terampil", "acuan_skkni": "SKKNI 130-2021"},
    {"no": 11, "kode_jabatan": "EL-SRY-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Energi Terbarukan", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Pemasangan Panel Surya", "acuan_skkni": "SKKNI 241-2024"},
    {"no": 12, "kode_jabatan": "K3-SMK-001", "klasifikasi": "KESELAMATAN KERJA", "subklasifikasi": "Sistem Manajemen K3", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan dan Kesehatan Kerja", "acuan_skkni": "SKKNI 119-2020"},
    {"no": 13, "kode_jabatan": "MN-MPR-001", "klasifikasi": "MANAJEMEN PROYEK", "subklasifikasi": "Manajemen Proyek", "kualifikasi": "Manajer", "jenjang": 9, "nama_jabatan": "Manajer Proyek Utama", "acuan_skkni": "SKKNI 145-2021"}
]

# Data Akun Admin
akun_admin = {"username": "admin_silatih", "password": "pupr_bjkw6_2026"}

# Inisialisasi State
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "sedang_login" not in st.session_state:
    st.session_state.sedang_login = False

# ==============================================
# 3. FUNGSI BANTUAN & VALIDASI
# ==============================================

def tentukan_status(tgl_mulai, tgl_selesai):
    """Menentukan status pelatihan berdasarkan tanggal hari ini"""
    hari_ini = date.today()
    if hari_ini < tgl_mulai:
        return "🟢 Akan Datang"
    elif tgl_mulai <= hari_ini <= tgl_selesai:
        return "🔴 Sedang Berlangsung"
    else:
        return "⚪ Sudah Selesai"

def validasi_nik(nik):
    return bool(re.fullmatch(r"\d{16}", nik.strip()))

def validasi_no_hp(kontak):
    return bool(re.fullmatch(r"^(0|\+62)\d{9,13}$", kontak.strip()))

def validasi_email(email):
    if not email: return True
    return bool(re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email.strip()))

def validasi_link_pddikti(link):
    return bool(re.match(r"^https?://pddikti\.kemdikbud\.go\.id/", link.strip()))

def ekstrak_tahun_pengalaman(berkas_list):
    total_tahun = 0
    try:
        for berkas in berkas_list:
            nama_berkas = berkas.name.lower()
            pola_tanggal = r'(\d{4})'
            tahun = re.findall(pola_tanggal, nama_berkas)
            if len(tahun) >= 2:
                mulai = int(tahun[0])
                selesai = int(tahun[1]) if int(tahun[1]) <= datetime.now().year else datetime.now().year
                total_tahun += max(0, selesai - mulai)
            elif len(tahun) == 1:
                total_tahun += max(0, datetime.now().year - int(tahun[0]))
        return round(total_tahun, 1) if total_tahun > 0 else 0
    except:
        return 0

def cek_kesesuaian_ktp_ijazah(nama_ktp, nik_ktp, nama_ijazah, nik_ijazah=""):
    if not nama_ktp or not nama_ijazah:
        return False, "Nama lengkap wajib diisi pada kedua berkas"
    nama_sama = nama_ktp.lower().strip() == nama_ijazah.lower().strip()
    nik_sama = True
    if nik_ijazah:
        nik_sama = nik_ktp.strip() == nik_ijazah.strip()
    if nama_sama and nik_sama:
        return True, "Data KTP dan Ijazah sesuai"
    elif not nama_sama:
        return False, "Nama lengkap pada KTP tidak sama dengan Ijazah"
    else:
        return False, "Nomor identitas pada KTP tidak sesuai dengan Ijazah"

def verifikasi_syarat(jabatan_pilihan, jenjang_pendidikan, total_pengalaman):
    if jabatan_pilihan not in persyaratan:
        return True, "Syarat belum tercantum, diterima sementara"
    syarat = persyaratan[jabatan_pilihan]
    min_tahun = syarat["min_tahun"]
    jenjang_terdekat = next((k for k in min_tahun.keys() if jenjang_pendidikan.lower() in k.lower()), None)
    if not jenjang_terdekat:
        return False, f"Jenjang pendidikan {jenjang_pendidikan} tidak sesuai untuk jabatan ini"
    butuh = min_tahun[jenjang_terdekat]
    if total_pengalaman >= butuh:
        return True, f"Pengalaman kerja {total_pengalaman} tahun memenuhi syarat minimal {butuh} tahun"
    else:
        return False, f"Pengalaman kerja {total_pengalaman} tahun belum memenuhi syarat minimal {butuh} tahun"

# ==============================================
# 4. TAMPILAN UTAMA
# ==============================================
st.markdown("<hr style='border: 3px solid #004B87; border-radius: 2px; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)
st.title("🏛️ Aplikasi Pelatihan & Sertifikasi UJI Kompetensi")
st.subheader("Balai Jasa Konstruksi Wilayah VI Makassar")
st.markdown("<h3 style='color:#004B87;'>siLATIH - Sistem Informasi Pelatihan Terintegrasi</h3>", unsafe_allow_html=True)

st.markdown("""
<div class="pu-info">
📢 <strong>Selamat Datang!</strong><br>
Aplikasi resmi untuk informasi jabatan SKKNI, pengelolaan pelatihan, serta pendaftaran uji kompetensi.
</div>
""", unsafe_allow_html=True)

# --- DAFTAR JABATAN ---
st.header("📋 Daftar Jabatan Berdasarkan SKKNI")
df = pd.DataFrame(daftar_jabatan)
st.sidebar.markdown("---")
st.sidebar.header("🔎 Saring Data")
pilih_klasifikasi = st.sidebar.multiselect("Bidang Klasifikasi", options=sorted(df["klasifikasi"].unique()))
if pilih_klasifikasi: df = df[df["klasifikasi"].isin(pilih_klasifikasi)]
pilih_kualifikasi = st.sidebar.multiselect("Tingkat Kualifikasi", options=sorted(df["kualifikasi"].unique()))
if pilih_kualifikasi: df = df[df["kualifikasi"].isin(pilih_kualifikasi)]
kata_kunci = st.text_input("🔍 Cari Jabatan atau Kode Jabatan:")
if kata_kunci: df = df[df["nama_jabatan"].str.contains(kata_kunci, case=False) | df["kode_jabatan"].str.contains(kata_kunci, case=False)]
st.info(f"✅ Menampilkan **{len(df)}** jabatan yang sesuai kriteria Anda")
st.dataframe(df, use_container_width=True, hide_index=True)

# --- UNDUH DATA ---
st.subheader("📥 Unduh Daftar Jabatan")
buffer = BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer: df.to_excel(writer, index=False, sheet_name="Daftar Jabatan SKKNI")
st.download_button(label="📂 Unduh File Excel (.xlsx)", data=buffer.getvalue(), file_name="Daftar_Jabatan_SKKNI_BJKW6_PUPR.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# --- SISTEM LOGIN ADMIN ---
st.sidebar.markdown("---")
st.sidebar.header("🔐 Akses Pengelola")

if not st.session_state.sedang_login:
    with st.sidebar.expander("🔑 Masuk Pengelola"):
        user = st.text_input("Nama Pengguna")
        sandi = st.text_input("Kata Sandi", type="password")
        if st.button("Masuk Akun"):
            if user == akun_admin["username"] and sandi == akun_admin["password"]:
                st.session_state.sedang_login = True
                st.rerun()
            else:
                st.error("❌ Nama pengguna atau kata sandi salah!")
else:
    st.sidebar.success("✅ Sedang masuk sebagai Pengelola")
    if st.sidebar.button("🚪 Keluar Akun"):
        st.session_state.sedang_login = False
        st.rerun()

    # === MENU PENGELOLA: TAMBAH & UBAH PELATIHAN ===
    st.markdown("---")
    st.header("⚙️ Pengelolaan Pelatihan (Hanya untuk Pengelola)")
    
    # Form Tambah Pelatihan Baru
    with st.form("form_pelatihan_baru", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nama_pelatihan = st.text_input("Nama Pelatihan *")
            jabatan_terkait = st.selectbox("Jabatan Terkait *", df["nama_jabatan"].unique())
            lokasi = st.text_input("Lokasi Pelatihan", value="Balai Jasa Konstruksi VI Makassar")
            kuota = st.number_input("Kuota Peserta", min_value=1, value=25)
        with col2:
            tgl_buka_daftar = st.date_input("Tanggal Buka Pendaftaran")
            tgl_tutup_daftar = st.date_input("Tanggal Tutup Pendaftaran")
            tgl_mulai = st.date_input("Tanggal Mulai Pelatihan *")
            tgl_selesai = st.date_input("Tanggal Selesai Pelatihan *")
        
        simpan = st.form_submit_button("➕ Tambahkan Pelatihan Baru")
        if simpan:
            if tgl_mulai > tgl_selesai:
                st.error("❌ Tanggal mulai tidak boleh lebih lambat dari tanggal selesai!")
            else:
                st.session_state.daftar_pelatihan.append({
                    "nama": nama_pelatihan, "jabatan": jabatan_terkait, "lokasi": lokasi,
                    "kuota": kuota, "buka_daftar": tgl_buka_daftar, "tutup_daftar": tgl_tutup_daftar,
                    "mulai": tgl_mulai, "selesai": tgl_selesai
                })
                st.success("✅ Pelatihan berhasil ditambahkan!")
                st.rerun()

    # Daftar Semua Pelatihan untuk Diedit
    st.subheader("📋 Daftar Semua Pelatihan (Bisa Diedit/Dihapus)")
    if not st.session_state.daftar_pelatihan:
        st.info("ℹ️ Belum ada pelatihan yang dibuat.")
    else:
        for idx, latih in enumerate(st.session_state.daftar_pelatihan, 1):
            status = tentukan_status(latih["mulai"], latih["selesai"])
            warna_status = "status-akan" if "Akan Datang" in status else ("status-langsung" if "Sedang Berlangsung" in status else "status-selesai")
            
            with st.expander(f"📌 {idx}. {latih['nama']} — <span class='{warna_status}'>{status}</span>", unsafe_allow_html=True):
                with st.form(f"ubah_pelatihan_{idx}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        ubah_nama = st.text_input("Nama Pelatihan *", value=latih["nama"])
                        ubah_jabatan = st.selectbox("Jabatan Terkait *", df["nama_jabatan"].unique(), index=df["nama_jabatan"].tolist().index(latih["jabatan"]))
                        ubah_lokasi = st.text_input("Lokasi", value=latih["lokasi"])
                        ubah_kuota = st.number_input("Kuota", min_value=1, value=latih["kuota"])
                    with col2:
                        ubah_buka = st.date_input("Buka Pendaftaran", value=latih["buka_daftar"])
                        ubah_tutup = st.date_input("Tutup Pendaftaran", value=latih["tutup_daftar"])
                        ubah_mulai = st.date_input("Mulai Pelatihan *", value=latih["mulai"])
                        ubah_selesai = st.date_input("Selesai Pelatihan *", value=latih["selesai"])
                    
                    ubah = st.form_submit_button("💾 Simpan Perubahan")
                    hapus = st.form_submit_button("🗑️ Hapus Pelatihan", type="secondary")
                    
                    if ubah:
                        if ubah_mulai > ubah_selesai:
                            st.error("❌ Tanggal mulai tidak boleh lebih lambat dari selesai!")
                        else:
                            st.session_state.daftar_pelatihan[idx-1] = {
                                "nama": ubah_nama, "jabatan": ubah_jabatan, "lokasi": ubah_lokasi,
                                "kuota": ubah_kuota, "buka_daftar": ubah_buka, "tutup_daftar": ubah_tutup,
                                "mulai": ubah_mulai, "selesai": ubah_selesai
                            }
                            st.success("✅ Data pelatihan diperbarui!")
                            st.rerun()
                    if hapus:
                        st.session_state.daftar_pelatihan.pop(idx-1)
                        st.success("🗑️ Pelatihan dihapus!")
                        st.rerun()

# --- HALAMAN UTAMA PESERTA: DAFTAR PELATIHAN BERDASARKAN STATUS ---
st.markdown("---")
st.header("📚 Informasi Pelatihan")

# Kelompokkan pelatihan
pelatihan_akan = []
pelatihan_langsung = []
pelatihan_selesai = []

for latih in st.session_state.daftar_pelatihan:
    status = tentukan_status(latih["mulai"], latih["selesai"])
    if "Akan Datang" in status:
        pelatihan_akan.append((latih, status))
    elif "Sedang Berlangsung" in status:
        pelatihan_langsung.append((latih, status))
    else:
        pelatihan_selesai.append((latih, status))

# Tampilkan Pelatihan Akan Datang
st.subheader("🟢 Pelatihan Akan Datang")
if pelatihan_akan:
    for latih, status in pelatihan_akan:
        st.markdown(f"""
        <div class="pu-info">
        <h4>{latih['nama']}</h4>
        <p>Jabatan: <strong>{latih['jabatan']}</strong><br>
        Pendaftaran dibuka: {latih['buka_daftar']} s.d {latih['tutup_daftar']}<br>
        Pelatihan: {latih['mulai']} s.d {latih['selesai']}<br>
        Kuota: {latih['kuota']} peserta | Lokasi: {latih['lokasi']}</p>
        </div>""", unsafe_allow_html=True)
else:
    st.info("ℹ️ Belum ada pelatihan yang dijadwalkan.")

# Tampilkan Pelatihan Sedang Berlangsung
st.subheader("🔴 Pelatihan Sedang Berlangsung")
if pelatihan_langsung:
    for latih, status in pelatihan_langsung:
        st.markdown(f"""
        <div class="pu-kuning">
        <h4>{latih['nama']}</h4>
        <p>Jabatan: <strong>{latih['jabatan']}</strong><br>
        Pelatihan berlangsung: {latih['mulai']} s.d {latih['selesai']}<br>
        Lokasi: {latih['lokasi']}</p>
        <p><em>Pendaftaran sudah ditutup.</em></p>
        </div>""", unsafe_allow_html=True)
else:
    st.info("ℹ️ Tidak ada pelatihan yang sedang berlangsung saat ini.")

# Tampilkan Pelatihan Sudah Selesai
st.subheader("⚪ Pelatihan Telah Selesai")
if pelatihan_selesai:
    for latih, status in pelatihan_selesai:
        st.markdown(f"""
        <div style="background: #F9FAFB; border-left: 6px solid #9CA3AF; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
        <h4 style="color: #6B7280;">{latih['nama']}</h4>
        <p>Jabatan: {latih['jabatan']}<br>
        Pelatihan dilaksanakan: {latih['mulai']} s.d {latih['selesai']}<br>
        Lokasi: {latih['lokasi']}</p>
        <p><em>Periode pendaftaran telah berakhir.</em></p>
        </div>""", unsafe_allow_html=True)
else:
    st.info("ℹ️ Belum ada riwayat pelatihan selesai.")

# --- FORM PENDAFTARAN (HANYA UNTUK PELATIHAN YANG BISA DIDAFTAR) ---
st.markdown("---")
st.header("📝 Formulir Pendaftaran")

# Ambil daftar pelatihan yang bisa didaftar
pilihan_pendaftaran = []
for latih, status in pelatihan_akan + pelatihan_langsung:
    if "Akan Datang" in status:
        pilihan_pendaftaran.append(f"{latih['nama']} — {latih['jabatan']}")

if not pilihan_pendaftaran:
    st.warning("⏳ Saat ini tidak ada pelatihan yang menerima pendaftaran. Silakan cek kembali nanti.")
else:
    with st.form("pendaftaran_pelatihan"):
        st.subheader("👤 Data Diri Peserta")
        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("Nama Lengkap Sesuai KTP *")
            nik = st.text_input("Nomor NIK / KTP *", max_chars=16)
        with col2:
            kontak = st.text_input("Nomor HP / WhatsApp *", placeholder="Contoh: 08123456789")
            email = st.text_input("Alamat Email")
        alamat = st.text_area("Alamat Lengkap Tempat Tinggal")

        st.subheader("🎓 Data Pendidikan & Ijazah")
        jenjang_pendidikan = st.selectbox("Jenjang Pendidikan Terakhir *", ["Pilih...", "Pendidikan Dasar", "SMA", "SMK", "SMK Plus/D1", "D2", "D3", "D4/S1", "Profesi", "S2", "Spesialis_1", "Doktor/Spesialis_2"])
        nama_ijazah = st.text_input("Nama Lengkap Sesuai Ijazah *", placeholder="Harus sama persis dengan KTP")
        nik_ijazah = st.text_input("Nomor Identitas di Ijazah (jika ada)")
        berkas_ijazah = st.file_uploader("Unggah Scan Ijazah Terakhir *", type=["pdf", "jpg", "jpeg", "png", "doc", "docx"])

        st.subheader("📎 Bukti Pendukung Lainnya")
        bukti_ig = st.file_uploader("Bukti Mengikuti Instagram @bjkw6_makassar *", type=["pdf", "jpg", "jpeg", "png", "doc", "docx"])
        link_pddikti = st.text_input("Link Bukti Kelulusan PDDIKTI *", placeholder="Harus dimulai dengan https://pddikti.kemdikbud.go.id/")
        
        st.subheader("💼 Bukti Pengalaman Kerja")
        st.markdown("""
        <div style="background:#FFF8E1;padding:1rem;border-radius:8px;border-left:5px solid #FF9800;">
        ⚠️ <strong>Petunjuk:</strong> Sistem akan menghitung masa kerja otomatis berdasarkan tahun yang tertulis pada nama berkas (Contoh: SK_2020_2024.pdf).<br>
        Format berkas yang diterima: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX, RAR, ZIP
        </div>""", unsafe_allow_html=True)
        bukti_pengalaman = st.file_uploader("Unggah Bukti Pengalaman Kerja *", type=["pdf", "jpg", "jpeg", "png", "doc", "docx", "xls", "xlsx", "rar", "zip"], accept_multiple_files=True)

        st.subheader("📄 Berkas Utama")
        berkas_ktp = st.file_uploader("Unggah Scan KTP *", type=["pdf", "jpg", "jpeg", "png", "doc", "docx"])

        st.subheader("🎓 Pilihan Pelatihan")
        pilihan = st.selectbox("Pilih Pelatihan yang Diikuti *", pilihan_pendaftaran)
        jabatan_pilihan = pilihan.split(" — ")[1] if " — " in pilihan else pilihan

        kirim = st.form_submit_button("✅ Kirim & Verifikasi Pendaftaran")

        if kirim:
            valid = True
            pesan_error = []

            if not nama or not nik or not kontak or not nama_ijazah or not berkas_ijazah or not bukti_ig or not link_pddikti or not bukti_pengalaman or not berkas_ktp or jenjang_pendidikan == "Pilih...":
                pesan_error.append("Lengkapi semua kolom bertanda * terlebih dahulu!")
                valid = False
            
            if not validasi_nik(nik):
                pesan_error.append("Format NIK salah! Harus berisi 16 digit angka.")
                valid = False

            if not validasi_no_hp(kontak):
                pesan_error.append("Format nomor HP salah! Contoh yang benar: 08123456789 atau +628123456789.")
                valid = False

            if not validasi_email(email):
                pesan_error.append("Format email tidak valid.")
                valid = False

            if not validasi_link_pddikti(link_pddikti):
                pesan_error.append("Link PDDIKTI harus berasal dari situs resmi: https://pddikti.kemdikbud.go.id/")
                valid = False

            if not valid:
                for err in pesan_error: st.error(f"⚠️ {err}")
                st.stop()
            
            # Cek kesesuaian data
            sesuai_ktp, pesan_ktp = cek_kesesuaian_ktp_ijazah(nama, nik, nama_ijazah, nik_ijazah)
            if not sesuai_ktp:
                st.markdown(f"""
                <div class="pu-tolak"><h4>❌ Pendaftaran Ditolak</h4><p>{pesan_ktp}</p>
                <p>Silakan perbaiki data dan unggah ulang berkas yang sesuai.</p></div>""", unsafe_allow_html=True)
                st.stop()
            
            total_pengalaman = ekstrak_tahun_pengalaman(bukti_pengalaman)
            st.info(f"🔍 Hasil perhitungan otomatis: Akumulasi pengalaman kerja Anda adalah **{total_pengalaman} tahun**")
            
            lulus_syarat, pesan_syarat = verifikasi_syarat(jabatan_pilihan, jenjang_pendidikan, total_pengalaman)
            if not lulus_syarat:
                st.markdown(f"""
                <div class="pu-tolak"><h4>❌ Pendaftaran Ditolak</h4><p>{pesan_syarat}</p>
                <p>Silakan tambahkan bukti pengalaman kerja atau pilih jabatan yang sesuai dengan kualifikasi Anda.</p></div>""", unsafe_allow_html=True)
                st.stop()
            
            st.balloons()
            st.markdown(f"""
            <div class="pu-sukses"><h4>🎉 Pendaftaran Diterima!</h4>
            <p>Terima kasih <strong>{nama}</strong> telah mendaftar untuk pelatihan <strong>{pilihan}</strong>.</p>
            <p>✅ {pesan_ktp}<br>✅ {pesan_syarat}</p>
            <p>Kami akan menghubungi Anda lewat nomor {kontak} paling lambat 3 hari kerja.</p></div>""", unsafe_allow_html=True)

# Kaki halaman
st.markdown("<hr style='border: 2px solid #004B87; margin-top: 2rem;'>", unsafe_allow_html=True)
st.caption("© 2026 Balai Jasa Konstruksi Wilayah VI Makassar — Kementerian Pekerjaan Umum | siLATIH v2.0")
