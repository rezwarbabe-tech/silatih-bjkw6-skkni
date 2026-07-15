# ==============================================
# APLIKASI siLATIH - BJKW VI MAKASSAR (VERSI 2.3)
# Ditambahkan: Alat Hitung Capaian Output Manual + Unggah + Grafik Lengkap
# ==============================================

# 1. MUAT PUSTAKA & GAYA KUSTOM PUPR
# ==============================================
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime, date
import re
import plotly.express as px
import plotly.graph_objects as go

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
.card-hasil {background: white; padding: 1.2rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 1rem;}
</style>
""", unsafe_allow_html=True)

# ==============================================
# 2. KONFIGURASI & DATA REFERENSI
# ==============================================
st.set_page_config(page_title="siLATIH - BJKW VI Makassar", page_icon="🏗️", layout="wide", initial_sidebar_state="expanded")

# === DAFTAR PENGELOLA YANG DIPERBOLEHKAN ===
daftar_pengelola = [
    {
        "nama_lengkap": "Muhamad Reza Bugis",
        "nip": "197904142009111002"
    }
]

# === BOBOT INDIKATOR (STANDAR) ===
BOBOT_STANDAR = {
    "revisi_dipa": 10,
    "deviasi_hal3": 15,
    "penyerapan": 10,
    "belanja_kontrak": 10,
    "tagihan": 10,
    "up_tup": 10,
    "capaian_output": 25,
    "lainnya": 20
}

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

# Inisialisasi State
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "sedang_login" not in st.session_state:
    st.session_state.sedang_login = False
if "nama_pengelola" not in st.session_state:
    st.session_state.nama_pengelola = ""
if "data_capaian" not in st.session_state:
    st.session_state.data_capaian = pd.DataFrame()

# ==============================================
# 3. FUNGSI BANTUAN & VALIDASI
# ==============================================

def cek_akses_pengelola(nama, nip):
    nama_bersih = nama.strip().lower()
    nip_bersih = nip.strip()
    for pengelola in daftar_pengelola:
        if (pengelola["nama_lengkap"].lower() == nama_bersih and 
            pengelola["nip"] == nip_bersih):
            return True, pengelola["nama_lengkap"]
    return False, ""

def tentukan_status(tgl_mulai, tgl_selesai):
    hari_ini = date.today()
    if hari_ini < tgl_mulai:
        return "🟢 Akan Datang"
    elif tgl_mulai <= hari_ini <= tgl_selesai:
        return "🔴 Sedang Berlangsung"
    else:
        return "⚪ Sudah Selesai"

def validasi_nik(nik):
    return bool(re.fullmatch(r"\d{16}", nik.strip()))

def validasi_nip(nip):
    return bool(re.fullmatch(r"\d{18}", nip.strip()))

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

def hitung_nilai_capaian(data):
    """Menghitung nilai gabungan dari semua komponen"""
    # Nilai Aspek Perencanaan
    nilai_perencanaan = round(
        (data["revisi_dipa"] * BOBOT_STANDAR["revisi_dipa"] / 100) +
        (data["deviasi_hal3"] * BOBOT_STANDAR["deviasi_hal3"] / 100), 2
    )
    # Nilai Aspek Pelaksanaan
    nilai_pelaksanaan = round(
        (data["penyerapan"] * BOBOT_STANDAR["penyerapan"] / 100) +
        (data["belanja_kontrak"] * BOBOT_STANDAR["belanja_kontrak"] / 100) +
        (data["tagihan"] * BOBOT_STANDAR["tagihan"] / 100) +
        (data["up_tup"] * BOBOT_STANDAR["up_tup"] / 100), 2
    )
    # Nilai Aspek Hasil
    nilai_hasil = round(data["capaian_output"] * BOBOT_STANDAR["capaian_output"] / 100, 2)
    # Nilai Akhir
    nilai_total = round(nilai_perencanaan + nilai_pelaksanaan + nilai_hasil, 2)
    nilai_akhir = round(nilai_total / 1, 2)  # Konversi bobot total 100%
    
    return {
        "nilai_perencanaan": nilai_perencanaan,
        "nilai_pelaksanaan": nilai_pelaksanaan,
        "nilai_hasil": nilai_hasil,
        "nilai_total": nilai_total,
        "nilai_akhir": nilai_akhir
    }

def olah_data_capaian(file):
    """Mengolah file Excel capaian output sesuai format standar"""
    try:
        df = pd.read_excel(file)
        data_baru = {}
        periode = ""
        
        # Membaca data sesuai struktur tabel yang diberikan
        for idx, baris in df.iterrows():
            if str(baris.iloc[0]) == "1" and str(baris.iloc[1]).isdigit():
                bulan = int(baris.iloc[1])
                nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                             "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                periode = f"Bulan {nama_bulan[bulan-1]}" if 1 <= bulan <=12 else f"Bulan {bulan}"
                
                # Mengambil nilai komponen
                data_baru = {
                    "Periode": periode,
                    "Revisi DIPA": float(str(baris.iloc[7]).replace(',', '.')),
                    "Deviasi Halaman III": float(str(baris.iloc[8]).replace(',', '.')),
                    "Penyerapan Anggaran": float(str(baris.iloc[10]).replace(',', '.')),
                    "Belanja Kontraktual": float(str(baris.iloc[11]).replace(',', '.')),
                    "Penyelesaian Tagihan": float(str(baris.iloc[12]).replace(',', '.')),
                    "Pengelolaan UP & TUP": float(str(baris.iloc[13]).replace(',', '.')),
                    "Capaian Output": float(str(baris.iloc[15]).replace(',', '.')),
                    "Nilai Akhir": float(str(baris.iloc[21]).replace(',', '.'))
                }
                break
        
        if data_baru:
            return pd.DataFrame([data_baru])
        else:
            st.error("❌ Tidak ditemukan data nilai pada file! Pastikan format tabel sesuai.")
            return None
            
    except Exception as e:
        st.error(f"❌ Gagal membaca file: {str(e)}")
        return None

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
Aplikasi resmi untuk informasi jabatan SKKNI, pengelolaan pelatihan, serta pendaftaran uji kompetensi dan capaian kinerja anggaran.
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

# --- SISTEM LOGIN PENGELOLA ---
st.sidebar.markdown("---")
st.sidebar.header("🔐 Akses Pengelola")

if not st.session_state.sedang_login:
    with st.sidebar.expander("🔑 Masuk Sebagai Pengelola"):
        nama_pengguna = st.text_input("Nama Lengkap Sesuai Data Kepegawaian")
        nip_pengguna = st.text_input("Nomor Induk Pegawai (NIP)", max_chars=18)
        if st.button("Masuk Akun Pengelola"):
            if not nama_pengguna or not nip_pengguna:
                st.error("❌ Lengkapi Nama Lengkap dan NIP terlebih dahulu!")
            elif not validasi_nip(nip_pengguna):
                st.error("❌ Format NIP salah! Harus berisi 18 digit angka.")
            else:
                terdaftar, nama_terverifikasi = cek_akses_pengelola(nama_pengguna, nip_pengguna)
                if terdaftar:
                    st.session_state.sedang_login = True
                    st.session_state.nama_pengelola = nama_terverifikasi
                    st.rerun()
                else:
                    st.error("❌ Nama atau NIP tidak terdaftar sebagai pengelola aplikasi!")
else:
    st.sidebar.success(f"✅ Selamat datang, **{st.session_state.nama_pengelola}**")
    if st.sidebar.button("🚪 Keluar Akun"):
        st.session_state.sedang_login = False
        st.session_state.nama_pengelola = ""
        st.rerun()

    # === MENU PENGELOLA: TAMBAH & UBAH PELATIHAN ===
    st.markdown("---")
    st.header("⚙️ Pengelolaan Pelatihan (Hanya Pengelola)")
    
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

# ==============================================
# BAGIAN KHUSUS: ALAT CAPAIAN OUTPUT BJKW VI MAKASSAR
# ==============================================
st.markdown("---")
st.header("📊 Alat Capaian Output & Indikator Anggaran")
st.markdown("""
<div class="pu-info">
Alat ini berfungsi untuk menghitung, menampilkan uraian rinci, serta memvisualisasikan capaian kinerja anggaran Balai Jasa Konstruksi Wilayah VI Makassar.
Tersedia dua cara pengisian: **unggah file Excel** atau **masukan data secara manual**.
</div>
""", unsafe_allow_html=True)

# Pilih Cara Pengisian
cara_isi = st.radio("Pilih Cara Pengisian Data:", ["📂 Unggah File Excel Format Standar", "✍️ Masukkan Data Secara Manual"])

# --- CARA 1: UNGGAH FILE ---
if cara_isi == "📂 Unggah File Excel Format Standar":
    if st.session_state.sedang_login:
        st.markdown("#### 🔼 Unggah File Indikator Pelaksanaan Anggaran (.xlsx)")
        st.info("Gunakan file dengan format persis seperti contoh yang diberikan: INDIKATOR PELAKSANAAN ANGGARAN SATKER")
        
        file_capaian = st.file_uploader("Pilih File", type=["xlsx"], key="unggah_capaian")
        if file_capaian:
            data_baru = olah_data_capaian(file_capaian)
            if data_baru is not None and not data_baru.empty:
                # Gabungkan data lama dan baru, hapus duplikat periode
                if not st.session_state.data_capaian.empty:
                    st.session_state.data_capaian = pd.concat([st.session_state.data_capaian, data_baru], ignore_index=True)
                    st.session_state.data_capaian = st.session_state.data_capaian.drop_duplicates(subset=["Periode"], keep="last")
                else:
                    st.session_state.data_capaian = data_baru
                st.success(f"✅ Data periode {data_baru['Periode'].iloc[0]} berhasil ditambahkan!")
                st.rerun()
        
        if not st.session_state.data_capaian.empty:
            if st.button("🗑️ Hapus Semua Data Capaian"):
                st.session_state.data_capaian = pd.DataFrame()
                st.success("✅ Data capaian telah dihapus!")
                st.rerun()
    else:
        st.warning("🔒 Hanya Pengelola yang dapat mengunggah file data capaian.")

# --- CARA 2: ISI MANUAL ---
else:
    st.markdown("#### ✍️ Masukkan Nilai Komponen Indikator")
    st.info("Isi semua nilai dengan rentang 0 s.d 100. Bobot penilaian sudah menggunakan standar yang berlaku.")
    
    with st.form("form_hitung_capaian"):
        nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                     "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        periode = st.selectbox("Pilih Periode Bulan", nama_bulan)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📌 Kualitas Perencanaan Anggaran")
            revisi_dipa = st.number_input("Nilai Revisi DIPA", min_value=0.0, max_value=100.0, value=100.0, step=0.01)
            deviasi_hal3 = st.number_input("Nilai Deviasi Halaman III DIPA", min_value=0.0, max_value=100.0, value=59.50, step=0.01)
            
            st.subheader("📌 Kualitas Pelaksanaan Anggaran")
            penyerapan = st.number_input("Nilai Penyerapan Anggaran", min_value=0.0, max_value=100.0, value=93.06, step=0.01)
            belanja_kontrak = st.number_input("Nilai Belanja Kontraktual", min_value=0.0, max_value=100.0, value=100.0, step=0.01)
            tagihan = st.number_input("Nilai Penyelesaian Tagihan", min_value=0.0, max_value=100.0, value=100.0, step=0.01)
            up_tup = st.number_input("Nilai Pengelolaan UP & TUP", min_value=0.0, max_value=100.0, value=89.53, step=0.01)
        
        with col2:
            st.subheader("📌 Kualitas Hasil Pelaksanaan")
            capaian_output = st.number_input("Nilai Capaian Output", min_value=0.0, max_value=100.0, value=66.49, step=0.01)
            dispensasi = st.number_input("Dispensasi SPM (Pengurangan)", min_value=0.0, max_value=100.0, value=0.0, step=0.01)
        
        hitung = st.form_submit_button("🔍 Hitung & Tampilkan Capaian")
        
        if hitung:
            data_input = {
                "revisi_dipa": revisi_dipa,
                "deviasi_hal3": deviasi_hal3,
                "penyerapan": penyerapan,
                "belanja_kontrak": belanja_kontrak,
                "tagihan": tagihan,
                "up_tup": up_tup,
                "capaian_output": capaian_output
            }
            hasil = hitung_nilai_capaian(data_input)
            
            # Tambahkan ke data sesi
            data_baru = pd.DataFrame([{
                "Periode": f"Bulan {periode}",
                "Revisi DIPA": revisi_dipa,
                "Deviasi Halaman III": deviasi_hal3,
                "Penyerapan Anggaran": penyerapan,
                "Belanja Kontraktual": belanja_kontrak,
                "Penyelesaian Tagihan": tagihan,
                "Pengelolaan UP & TUP": up_tup,
                "Capaian Output": capaian_output,
                "Nilai Akhir": hasil["nilai_akhir"]
            }])
            
            if not st.session_state.data_capaian.empty:
                st.session_state.data_capaian = pd.concat([st.session_state.data_capaian, data_baru], ignore_index=True)
                st.session_state.data_capaian = st.session_state.data_capaian.drop_duplicates(subset=["Periode"], keep="last")
            else:
                st.session_state.data_capaian = data_baru
            
            st.success(f"✅ Perhitungan periode Bulan {periode} selesai!")

# --- TAMPILAN HASIL, URAIAN & GRAFIK ---
if not st.session_state.data_capaian.empty:
    st.markdown("---")
    st.subheader("📋 Uraian Lengkap Capaian Kinerja")
    
    # Ambil data terakhir untuk uraian rinci
    data_terakhir = st.session_state.data_capaian.iloc[-1]
    periode_terakhir = data_terakhir["Periode"]
    
    # Kartu Ringkasan Nilai Utama
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(f"""
        <div class="card-hasil" style="text-align:center;">
            <h4>Nilai Perencanaan</h4>
            <h2 style="color:#004B87;">{round((data_terakhir['Revisi DIPA']*10 + data_terakhir['Deviasi Halaman III']*15)/25,2)}</h2>
            <p>Bobot 25%</p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown(f"""
        <div class="card-hasil" style="text-align:center;">
            <h4>Nilai Pelaksanaan</h4>
            <h2 style="color:#0071BC;">{round((data_terakhir['Penyerapan Anggaran']*10 + data_terakhir['Belanja Kontraktual']*10 + data_terakhir['Penyelesaian Tagihan']*10 + data_terakhir['Pengelolaan UP & TUP']*10)/40,2)}</h2>
            <p>Bobot 40%</p>
        </div>
        """, unsafe_allow_html=True)
    with col_c:
        st.markdown(f"""
        <div class="card-hasil" style="text-align:center;">
            <h4>Nilai Capaian Output</h4>
            <h2 style="color:#059669;">{round(data_terakhir['Capaian Output'],2)}</h2>
            <p>Bobot 25%</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="pu-sukses" style="text-align:center; margin-top:1rem;">
        <h3>Nilai Akhir Indikator Anggaran {periode_terakhir}: <span style="font-size:28px;">{round(data_terakhir['Nilai Akhir'],2)}</span></h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabel Data Lengkap Semua Periode
    st.subheader("📑 Data Lengkap Seluruh Periode")
    st.dataframe(st.session_state.data_capaian, use_container_width=True, hide_index=True)
    
    # GRAFIK & DIAGRAM
    st.subheader("📈 Visualisasi Grafik & Diagram")
    
    col1, col2 = st.columns(2)
    
    # 1. Grafik Garis Perkembangan Nilai Akhir
    with col1:
        fig_akhir = px.line(
            st.session_state.data_capaian, 
            x="Periode", 
            y="Nilai Akhir",
            title=f"Perkembangan Nilai Akhir Indikator Anggaran",
            markers=True,
            color_discrete_sequence=["#004B87"],
            text="Nilai Akhir"
        )
        fig_akhir.update_layout(yaxis_title="Nilai", yaxis_range=[0,100])
        fig_akhir.update_traces(textposition="top center")
        st.plotly_chart(fig_akhir, use_container_width=True)
    
    # 2. Grafik Batang Capaian Output
    with col2:
        fig_output = px.bar(
            st.session_state.data_capaian,
            x="Periode",
            y="Capaian Output",
            title="Realisasi Capaian Output Per Periode",
            color_discrete_sequence=["#059669"],
            text="Capaian Output"
        )
        fig_output.update_layout(yaxis_title="Nilai Capaian", yaxis_range=[0,100])
        fig_output.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig_output, use_container_width=True)
    
    # 3. Diagram Lingkaran Komposisi Nilai Terakhir
    col3, col4 = st.columns(2)
    with col3:
        # Hitung komposisi nilai aspek terakhir
        nilai_perencanaan = round((data_terakhir['Revisi DIPA']*10 + data_terakhir['Deviasi Halaman III']*15)/100,2)
        nilai_pelaksanaan = round((data_terakhir['Penyerapan Anggaran']*10 + data_terakhir['Belanja Kontraktual']*10 + 
                                  data_terakhir['Penyelesaian Tagihan']*10 + data_terakhir['Pengelolaan UP & TUP']*10)/100,2)
        nilai_hasil = round(data_terakhir['Capaian Output']*25/100,2)
        
        fig_pie = px.pie(
            values=[nilai_perencanaan, nilai_pelaksanaan, nilai_hasil],
            names=["Perencanaan", "Pelaksanaan", "Capaian Output"],
            title=f"Komposisi Nilai Indikator {periode_terakhir}",
            color_discrete_map={"Perencanaan":"#004B87", "Pelaksanaan":"#0071BC", "Capaian Output":"#059669"}
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # 4. Grafik Perbandingan Semua Indikator
    with col4:
        fig_banding = go.Figure()
        fig_banding.add_trace(go.Scatter(
            x=st.session_state.data_capaian["Periode"],
            y=st.session_state.data_capaian["Revisi DIPA"],
            name="Revisi DIPA", line=dict(color="#004B87", dash="solid")
        ))
        fig_banding.add_trace(go.Scatter(
            x=st.session_state.data_capaian["Periode"],
            y=st.session_state.data_capaian["Penyerapan Anggaran"],
            name="Penyerapan", line=dict(color="#0071BC", dash="dash")
        ))
        fig_banding.add_trace(go.Scatter(
            x=st.session_state.data_capaian["Periode"],
            y=st.session_state.data_capaian["Capaian Output"],
            name="Capaian Output", line=dict(color="#059669", dash="dot")
        ))
        fig_banding.update_layout(title="Perbandingan Indikator Utama", yaxis_title="Nilai", yaxis_range=[0,100])
        st.plotly_chart(fig_banding, use_container_width=True)

else:
    st.info("ℹ️ Belum ada data capaian yang ditampilkan. Silakan unggah file atau isi data secara manual di atas.")

# --- SISA BAGIAN APLIKASI (DAFTAR PELATIHAN & PENDAFTARAN) ---
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
if pelatihan_
