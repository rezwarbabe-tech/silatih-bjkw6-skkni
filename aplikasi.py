import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

# ====================== KONFIGURASI APLIKASI ======================
st.set_page_config(
    page_title="siLATIH - Sistem Pelatihan Terintegrasi",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {max-width: 100%; padding: 1rem 1.2rem;}
    h1 {font-size: 1.7rem !important; text-align: center;}
    h2 {font-size: 1.3rem !important; margin-top: 1rem;}
    .stButton>button {width: 100%; padding: 0.8rem; font-size: 1.1rem; border-radius: 10px;}
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>textarea {font-size: 1rem; padding: 0.7rem; border-radius: 8px;}
    div[data-testid="stFileUploader"] {font-size: 0.95rem;}
    .stAlert {border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# ====================== INISIALISASI PENYIMPANAN ======================
if "peran" not in st.session_state:
    st.session_state.peran = None
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "daftar_pendaftar" not in st.session_state:
    st.session_state.daftar_pendaftar = []

# ====================== PERSYARATAN KUALIFIKASI LENGKAP JENJANG 1-9 ======================
syarat_kualifikasi = {
    "9": [
        "Doktor/Doktor Terapan/Pendidikan Spesialis 2: Minimal 0 Tahun",
        "S2/S2 Terapan/Pendidikan Spesialis 1: Minimal 4 Tahun",
        "Pendidikan Profesi: Minimal 7 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 8 Tahun"
    ],
    "8": [
        "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis 1: Minimal 0 Tahun",
        "Pendidikan Profesi: Minimal 5 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 6 Tahun"
    ],
    "7": [
        "Pendidikan Profesi: Minimal 0 Tahun",
        "S1/S1 Terapan/D4 Terapan (Dengan Pemberian Kompetensi Tambahan untuk Fresh Graduate, masa berlaku SKX = 1): Minimal 0 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 2 Tahun"
    ],
    "6": [
        "S1/S1 Terapan/D4 Terapan: Minimal 0 Tahun",
        "D3: Minimal 4 Tahun",
        "D2: Minimal 8 Tahun",
        "D1: Minimal 12 Tahun"
    ],
    "5": [
        "D3: Minimal 0 Tahun",
        "D2: Minimal 4 Tahun",
        "D1/SMK Plus: Minimal 8 Tahun",
        "SMK: Minimal 10 Tahun",
        "SMA: Minimal 12 Tahun"
    ],
    "4": [
        "D2: Minimal 0 Tahun",
        "D1/SMK Plus: Minimal 2 Tahun",
        "SMK: Minimal 4 Tahun",
        "SMA: Minimal 6 Tahun"
    ],
    "3": [
        "D1/SMK Plus: Minimal 0 Tahun",
        "SMK: Minimal 3 Tahun",
        "SMA: Minimal 4 Tahun",
        "Pendidikan Dasar: Minimal 5 Tahun"
    ],
    "2": [
        "SMK: Minimal 0 Tahun",
        "SMA: Minimal 1 Tahun",
        "Pendidikan Dasar: Minimal 0 Tahun"
    ],
    "1": [
        "Pendidikan Dasar: Minimal 0 Tahun",
        "Non Pendidikan (Dengan PBK): Minimal 2 Tahun"
    ]
}

# ====================== DATA JABATAN LENGKAP SEMUA KLASIFIKASI ======================
data_jabatan = [
    # ==============================================================
    # 🏗️ KLASIFIKASI: SIPIL (SI) — LENGKAP SESUAI DATA MASTER
    # ==============================================================
    
    # --- Sub-bidang: Air Tanah dan Air Baku ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101015", "nama_jabatan": "Ahli Utama Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101014", "nama_jabatan": "Ahli Madya Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101013", "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101003", "nama_jabatan": "Ahli Utama Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101002", "nama_jabatan": "Ahli Madya Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101001", "nama_jabatan": "Ahli Muda Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101018", "nama_jabatan": "Ahli Utama Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101021", "nama_jabatan": "Ahli Madya Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101020", "nama_jabatan": "Ahli Muda Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101019", "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Lulusan Baru)", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI102005", "nama_jabatan": "Pengawas Pengeboran Air Tanah Tingkat 6", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI102006", "nama_jabatan": "Pengawas Pengeboran Air Tanah Tingkat 5", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI102007", "nama_jabatan": "Pelaksana Pengeboran Air Tanah Tingkat 5", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI102008", "nama_jabatan": "Pelaksana Pengeboran Air Tanah Tingkat 4", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},

    # --- Sub-bidang: Gedung ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI111001", "nama_jabatan": "Ahli Utama Teknik Bangunan Gedung", "acuan": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI111002", "nama_jabatan": "Ahli Madya Teknik Bangunan Gedung", "acuan": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111003", "nama_jabatan": "Ahli Muda Teknik Bangunan Gedung", "acuan": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111004", "nama_jabatan": "Manajer Pengelolaan Bangunan Gedung", "acuan": "SKKNI 115-2015; SKKNI 46-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI111005", "nama_jabatan": "Ahli Utama Penilai Laik Fungsi Bangunan Gedung", "acuan": "SKKNI 113-2015; SKKNI 7-2024"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111006", "nama_jabatan": "Ahli Muda Perencana Beton Pracetak Struktur Gedung", "acuan": "SKKNI 160-2024"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI111007", "nama_jabatan": "Ahli Utama Bangunan Gedung Hijau", "acuan": "SKKNI 2-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI111008", "nama_jabatan": "Ahli Madya Bangunan Gedung Hijau", "acuan": "SKKNI 2-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111009", "nama_jabatan": "Ahli Muda Bangunan Gedung Hijau", "acuan": "SKKNI 2-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI112001", "nama_jabatan": "Analis Struktur Bangunan RISHA", "acuan": "SKKNI 221-2018"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI112002", "nama_jabatan": "Pengawas Pekerjaan Bangunan Gedung Tingkat 6", "acuan": "SKKNI 340-2013"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI112003", "nama_jabatan": "Pengawas Pekerjaan Bangunan Gedung Tingkat 5", "acuan": "SKKNI 340-2013"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI112004", "nama_jabatan": "Pelaksana Lapangan Pekerjaan Gedung Tingkat 6", "acuan": "SKKNI 193-2021; SKKNI 108-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI112005", "nama_jabatan": "Pelaksana Lapangan Pekerjaan Gedung Tingkat 5", "acuan": "SKKNI 193-2021; SKKNI 108-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI112006", "nama_jabatan": "Pelaksana Lapangan Pekerjaan Gedung Tingkat 4", "acuan": "SKKNI 193-2021; SKKNI 108-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 4, "kode_jabatan": "SI113001", "nama_jabatan": "Juru Gambar Kepala Bidang Konstruksi", "acuan": "SKKNI 13-2024; SKKNI 33-2021; SKKNI 327-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI113002", "nama_jabatan": "Juru Gambar Konstruksi", "acuan": "SKKNI 13-2024; SKKNI 33-2021; SKKNI 327-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI113003", "nama_jabatan": "Juru Gambar Pemula Konstruksi", "acuan": "SKKNI 13-2024; SKKNI 33-2021; SKKNI 327-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI113004", "nama_jabatan": "Mandor Konstruksi Bangunan Gedung", "acuan": "SKK Khusus Regulasi 32-2022"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI113005", "nama_jabatan": "Aplikator Bangunan RISHA Tingkat 3", "acuan": "SKKNI 221-2018"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI113006", "nama_jabatan": "Aplikator Bangunan RISHA Tingkat 2", "acuan": "SKKNI 221-2018"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI113007", "nama_jabatan": "Kepala Tukang Bangunan Gedung", "acuan": "SKKNI 31-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI113008", "nama_jabatan": "Kepala Tukang Perancah dan Acuan Beton", "acuan": "SKKNI 54-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113009", "nama_jabatan": "Tukang Perancah dan Acuan Beton", "acuan": "SKKNI 54-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113010", "nama_jabatan": "Tukang Bata dan Plesteran", "acuan": "SKKNI 317-2016; SKKNI 307-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113011", "nama_jabatan": "Tukang Pasang Ubin/Keramik", "acuan": "SKKNI 309-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113012", "nama_jabatan": "Tukang Besi Beton", "acuan": "SKKNI 319-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113013", "nama_jabatan": "Tukang Kayu Konstruksi", "acuan": "SKKNI 85-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113014", "nama_jabatan": "Tukang Cat Bangunan Gedung", "acuan": "SKKNI 310-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113015", "nama_jabatan": "Tukang Pasang Pelapis Anti Bocor", "acuan": "SKKNI 377-2013"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113016", "nama_jabatan": "Tukang Pasang Rangka Baja Ringan", "acuan": "SKKNI 184-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "SI113017", "nama_jabatan": "Tukang Pasang Penutup Atap", "acuan": "SKKNI 21-2024; SKKNI 16-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111010", "nama_jabatan": "Pengelola Teknis Pembangunan Gedung Negara", "acuan": "SKK Khusus Regulasi 3-2020"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111011", "nama_jabatan": "Ahli Muda Pengelola Rumah Susun", "acuan": "SKKNI 255-2019; SKKNI 115-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111012", "nama_jabatan": "Ahli Muda Teknik Bangunan Gedung (Lulusan Baru)", "acuan": "SKKNI 192-2016"},

    # --- Sub-bidang: Bangunan Air Baku ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI121001", "nama_jabatan": "Ahli Utama Teknik Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI121002", "nama_jabatan": "Ahli Madya Teknik Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI121003", "nama_jabatan": "Ahli Muda Teknik Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI122001", "nama_jabatan": "Pengawas Konstruksi Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI122002", "nama_jabatan": "Pelaksana Konstruksi Bangunan Air Baku", "acuan": "SKKNI 125-2021"},

    # --- Sub-bidang: Bangunan Air Limbah ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI131101", "nama_jabatan": "Ahli Utama Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI131102", "nama_jabatan": "Ahli Madya Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI131001", "nama_jabatan": "Ahli Muda Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI132001", "nama_jabatan": "Pengawas Lapangan SPALD", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI132003", "nama_jabatan": "Pelaksana Lapangan SPALD Permukiman (Level 5)", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI132004", "nama_jabatan": "Pelaksana Lapangan SPALD Permukiman (Level 4)", "acuan": "SKKNI 312-2009"},

    # --- Sub-bidang: Bangunan Pengairan ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI141001", "nama_jabatan": "Ahli Utama Teknik Pengairan", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI141002", "nama_jabatan": "Ahli Madya Teknik Pengairan", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI141003", "nama_jabatan": "Ahli Muda Teknik Pengairan", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI142001", "nama_jabatan": "Pengawas Irigasi", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI142002", "nama_jabatan": "Pelaksana Irigasi", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI143001", "nama_jabatan": "Operator Jaringan Irigasi", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI143002", "nama_jabatan": "Operator Pemula Jaringan Irigasi", "acuan": "SKKNI 126-2021"},

    # --- Sub-bidang: Bangunan Pantai dan Pelabuhan ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI151004", "nama_jabatan": "Ahli Utama Teknik Dermaga", "acuan": "SKKNI 320-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI151006", "nama_jabatan": "Ahli Madya Teknik Dermaga", "acuan": "SKKNI 320-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI151005", "nama_jabatan": "Ahli Muda Teknik Dermaga", "acuan": "SKKNI 320-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI152001", "nama_jabatan": "Pengawas Konstruksi Pelabuhan", "acuan": "SKKNI 320-2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI152002", "nama_jabatan": "Pelaksana Konstruksi Pelabuhan", "acuan": "SKKNI 320-2016"},

    # --- Sub-bidang: Bangunan Jalan dan Jembatan ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI161001", "nama_jabatan": "Ahli Utama Teknik Jalan Raya", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI161002", "nama_jabatan": "Ahli Madya Teknik Jalan Raya", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI161003", "nama_jabatan": "Ahli Muda Teknik Jalan Raya", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI162001", "nama_jabatan": "Pengawas Konstruksi Jalan", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI162002", "nama_jabatan": "Pelaksana Konstruksi Jalan", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI163001", "nama_jabatan": "Operator Perawatan Jalan", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI163002", "nama_jabatan": "Operator Pemula Perawatan Jalan", "acuan": "SKKNI 127-2021"},

    # --- Sub-bidang: Geoteknik ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI171001", "nama_jabatan": "Ahli Utama Teknik Geoteknik", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI171002", "nama_jabatan": "Ahli Madya Teknik Geoteknik", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI171003", "nama_jabatan": "Ahli Muda Teknik Geoteknik", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI172001", "nama_jabatan": "Pengawas Penyelidikan Tanah", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI172002", "nama_jabatan": "Pelaksana Penyelidikan Tanah", "acuan": "SKKNI 152-2019"},

    # --- Sub-bidang: Manajemen Konstruksi ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI181001", "nama_jabatan": "Ahli Utama Manajemen Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI181002", "nama_jabatan": "Ahli Madya Manajemen Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI181003", "nama_jabatan": "Ahli Muda Manajemen Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI182001", "nama_jabatan": "Pengawas Keselamatan Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI182002", "nama_jabatan": "Petugas Keselamatan Konstruksi", "acuan": "SKKNI 153-2019"},

    # ==============================================================
    # 🔧 KLASIFIKASI: MEKANIKAL (ME) — LENGKAP
    # ==============================================================
    
    # --- Sub-bidang: Alat Berat ---
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "ME061001", "nama_jabatan": "Manajer Alat Berat", "acuan": "SKKNI 206-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "ME062011", "nama_jabatan": "Pengawas Perancah (Scaffolding)", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "ME062009", "nama_jabatan": "Teknisi Perancah (Scaffolding)", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063094", "nama_jabatan": "Operator Perancah (Scaffolding)", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063095", "nama_jabatan": "Operator Pemula Perancah (Scaffolding)", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063096", "nama_jabatan": "Operator Bulldozer", "acuan": "SKK Khusus Regulasi 27-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063097", "nama_jabatan": "Operator Pemula Bulldozer", "acuan": "SKK Khusus Regulasi 27-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063098", "nama_jabatan": "Operator Motor Grader", "acuan": "SKK Khusus Regulasi 30-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063099", "nama_jabatan": "Operator Pemula Motor Grader", "acuan": "SKK Khusus Regulasi 30-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063100", "nama_jabatan": "Operator Wheel Excavator", "acuan": "SKKNI 91-2010"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063101", "nama_jabatan": "Operator Pemula Wheel Excavator", "acuan": "SKKNI 91-2010"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063102", "nama_jabatan": "Operator Tandem Roller", "acuan": "SKKNI 159-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063103", "nama_jabatan": "Operator Pemula Tandem Roller", "acuan": "SKKNI 159-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063104", "nama_jabatan": "Operator Vibrator Roller", "acuan": "SKKNI 168-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063105", "nama_jabatan": "Operator Pemula Vibrator Roller", "acuan": "SKKNI 168-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063106", "nama_jabatan": "Operator Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063107", "nama_jabatan": "Operator Pemula Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063014", "nama_jabatan": "Operator Wheel Loader", "acuan": "SKK Khusus Regulasi 33-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063108", "nama_jabatan": "Operator Pemula Wheel Loader", "acuan": "SKK Khusus Regulasi 33-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063109", "nama_jabatan": "Operator Mobile Crane", "acuan": "SKKNI 180-2024"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063110", "nama_jabatan": "Operator Pemula Mobile Crane", "acuan": "SKKNI 180-2024"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063028", "nama_jabatan": "Operator Tower Crane", "acuan": "SKK Khusus Regulasi 43-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063111", "nama_jabatan": "Operator Pemula Tower Crane", "acuan": "SKK Khusus Regulasi 43-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063112", "nama_jabatan": "Operator Truck Mounted Crane", "acuan": "SKKNI 85-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063113", "nama_jabatan": "Operator Pemula Truck Mounted Crane", "acuan": "SKKNI 85-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063114", "nama_jabatan": "Operator Backhoe Loader", "acuan": "SKKNI 89-2010"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063115", "nama_jabatan": "Operator Pemula Backhoe Loader", "acuan": "SKKNI 89-2010"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063116", "nama_jabatan": "Operator Pile Drive Hammer", "acuan": "SKKNI 150-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063117", "nama_jabatan": "Operator Pemula Pile Drive Hammer", "acuan": "SKKNI 150-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063142", "nama_jabatan": "Operator Pompa Beton", "acuan": "SKKNI 381-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063118", "nama_jabatan": "Operator Pemula Pompa Beton", "acuan": "SKKNI 381-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063119", "nama_jabatan": "Operator Bore Pile", "acuan": "SKKNI 111-2015"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063120", "nama_jabatan": "Operator Pemula Bore Pile", "acuan": "SKKNI 111-2015"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063121", "nama_jabatan": "Operator Mesin Pencampur Aspal", "acuan": "SKKNI 382-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063122", "nama_jabatan": "Operator Pemula Mesin Pencampur Aspal", "acuan": "SKKNI 382-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063123", "nama_jabatan": "Operator Mesin Penggelar Aspal", "acuan": "SKKNI 383-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063124", "nama_jabatan": "Operator Pemula Mesin Penggelar Aspal", "acuan": "SKKNI 383-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063125", "nama_jabatan": "Operator Mesin Pemecah Batu", "acuan": "SKK Khusus Regulasi 42-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063126", "nama_jabatan": "Operator Pemula Mesin Pemecah Batu", "acuan": "SKK Khusus Regulasi 42-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063127", "nama_jabatan": "Operator Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Regulasi 41-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063128", "nama_jabatan": "Operator Pemula Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Regulasi 41-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063012", "nama_jabatan": "Operator Cold Milling Machine", "acuan": "SKK Khusus Regulasi 40-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063129", "nama_jabatan": "Operator Pemula Cold Milling Machine", "acuan": "SKK Khusus Regulasi 40-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063029", "nama_jabatan": "Operator Batching Plant", "acuan": "SKK Khusus Regulasi 39-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063130", "nama_jabatan": "Operator Pemula Batching Plant", "acuan": "SKK Khusus Regulasi 39-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063131", "nama_jabatan": "Operator Hydrolic Hammer Breaker", "acuan": "SKKNI 158-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063132", "nama_jabatan": "Operator Pemula Hydrolic Hammer Breaker", "acuan": "SKKNI 158-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063133", "nama_jabatan": "Operator Ripper Tractor", "acuan": "SKKNI 165-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063134", "nama_jabatan": "Operator Pemula Ripper Tractor", "acuan": "SKKNI 165-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063135", "nama_jabatan": "Mekanik Tower Crane", "acuan": "SKK Khusus Regulasi 34-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063005", "nama_jabatan": "Mekanik Pabrik Aspal (Asphalt Mixing Plant)", "acuan": "SKKNI 326-2009"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063002", "nama_jabatan": "Mekanik Kapal Keruk", "acuan": "SKKNI 70-2009"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063141", "nama_jabatan": "Mekanik Engine Tingkat Dasar", "acuan": "SKKNI 382-2015"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063136", "nama_jabatan": "Mekanik Engine Pemula Tingkat Dasar", "acuan": "SKKNI 382-2015"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063137", "nama_jabatan": "Mekanik Hidrolik Alat Berat", "acuan": "SKKNI 88-2010"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063138", "nama_jabatan": "Mekanik Hidrolik Alat Berat Pemula", "acuan": "SKKNI 88-2010"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063140", "nama_jabatan": "Mekanik Engine Alat Berat", "acuan": "SKKNI 235-2023"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063139", "nama_jabatan": "Mekanik Engine Alat Berat Pemula", "acuan": "SKKNI 235-2023"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063027", "nama_jabatan": "Operator Dump Truck", "acuan": "SKKNI 132-2015"},

    # ==============================================================
    # 🏛️ KLASIFIKASI: ARSITEKTUR (AR) — LENGKAP
    # ==============================================================
    
    # --- Sub-bidang: Arsitektural ---
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR011001", "nama_jabatan": "Arsitek Utama", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR011002", "nama_jabatan": "Arsitek Madya", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR011003", "nama_jabatan": "Arsitek Muda", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR012001", "nama_jabatan": "Asisten Pemula Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AR012004", "nama_jabatan": "Pengawas Lapangan Arsitektur", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "OPERATOR", "jenjang": 4, "kode_jabatan": "AR012005", "nama_jabatan": "Pelaksana Gambar Kerja Arsitektur", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AR012006", "nama_jabatan": "Operator Pembuatan Gambar Arsitektur", "acuan": "SKKNI 196-2021"},

    # --- Sub-bidang: Desain Interior ---
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR021001", "nama_jabatan": "Desainer Interior Utama", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR021002", "nama_jabatan": "Desainer Interior Madya", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR021003", "nama_jabatan": "Desainer Interior Muda", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR022001", "nama_jabatan": "Asisten Desain Interior", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AR022002", "nama_jabatan": "Pengawas Pemasangan Interior", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "OPERATOR", "jenjang": 4, "kode_jabatan": "AR022003", "nama_jabatan": "Pelaksana Pemasangan Interior", "acuan": "SKKNI 211-2022"},

    # ==============================================================
    # 🌳 KLASIFIKASI: ARSITEKTUR LANSKAP (AL) — LENGKAP
    # ==============================================================
    
    # --- Sub-bidang: Perencanaan Lanskap ---
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perencanaan Lanskap", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL011001", "nama_jabatan": "Arsitek Lanskap Utama", "acuan": "SKKNI 197-2021"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perencanaan Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL011002", "nama_jabatan": "Arsitek Lanskap Madya", "acuan": "SKKNI 197-2021"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perencanaan Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011003", "nama_jabatan": "Arsitek Lanskap Muda", "acuan": "SKKNI 197-2021"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perencanaan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL012001", "nama_jabatan": "Asisten Arsitek Lanskap", "acuan": "SKKNI 197-2021"},
    
    # --- Sub-bidang: Pelaksanaan Lanskap ---
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pelaksanaan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL022001", "nama_jabatan": "Pengawas Konstruksi Lanskap", "acuan": "SKKNI 197-2021"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pelaksanaan Lanskap", "kualifikasi": "OPERATOR", "jenjang": 4, "kode_jabatan": "AL022002", "nama_jabatan": "Pelaksana Konstruksi Lanskap", "acuan": "SKKNI 197-2021"},
    
    # --- Sub-bidang: Pemeliharaan Lanskap ---
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pemeliharaan Lanskap", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AL033001", "nama_jabatan": "Teknisi Taman", "acuan": "SKKNI 197-2021"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pemeliharaan Lanskap", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "AL033002", "nama_jabatan": "Pekerja Taman Pemula", "acuan": "SKKNI 197-2021"},
]

# ====================== HALAMAN UTAMA LOGIN ======================
if st.session_state.peran is None:
    st.title("🎓 siLATIH - Sistem Pelatihan Terintegrasi")
    st.divider()
    st.subheader("Pilih Akses Masuk:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔧 Pengelola / Admin", use_container_width=True):
            st.session_state.peran = "admin"
            st.rerun()
    with col2:
        if st.button("👤 Peserta", use_container_width=True):
            st.session_state.peran = "peserta"
            st.rerun()

# ====================== DASHBOARD ADMIN ======================
elif st.session_state.peran == "admin":
    st.title("🔧 Dashboard Pengelola Pelatihan")
    if st.button("🔙 Kembali ke Halaman Utama"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    tab1, tab2 = st.tabs(["📝 Buat Pelatihan Baru", "📋 Daftar Pendaftar"])

    with tab1:
        st.subheader("Data Umum Pelatihan")
        nama_pelatihan = st.text_input("Nama Pelatihan")
        tanggal_pelatihan = st.date_input("Tanggal Pelaksanaan")
        lokasi = st.text_input("Lokasi / Tautan Pelatihan")

        st.subheader("📌 Persyaratan Umum")
        syarat_umum = st.text_area(
            "Daftar Persyaratan Umum",
            value="1. Fotokopi KTP masih berlaku\n2. Fotokopi Ijazah Terakhir dilegalisir\n3. Pas foto 4x6 cm\n4. Surat keterangan sehat\n5. Surat tugas instansi (jika diperlukan)",
            height=150
        )

        st.subheader("📌 Pilih Jabatan Lengkap Sesuai SKKNI")
        klasifikasi_list = sorted({j["klasifikasi"] for j in data_jabatan})
        klasifikasi_pilih = st.selectbox("Pilih Klasifikasi", klasifikasi_list)
        
        subklasifikasi_list = sorted({j["subklasifikasi"] for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih})
        subklasifikasi_pilih = st.selectbox("Pilih Sub-Klasifikasi", subklasifikasi_list)
        
        jabatan_list = [f"{j['nama_jabatan']} | Jenjang {j['jenjang']} | {j['kode_jabatan']}" 
                       for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih and j["subklasifikasi"] == subklasifikasi_pilih]
        jabatan_pilih = st.selectbox("Pilih Nama Jabatan", jabatan_list)
        
        jenjang_terpilih = next(j["jenjang"] for j in data_jabatan if f"{j['nama_jabatan']} | Jenjang {j['jenjang']} | {j['kode_jabatan']}" == jabatan_pilih)
        st.info(f"✅ Persyaratan Kualifikasi Jenjang {jenjang_terpilih}:")
        for s in syarat_kualifikasi[str(jenjang_terpilih)]:
            st.write(f"- {s}")

        if st.button("✅ Simpan Pelatihan", type="primary"):
            if nama_pelatihan == "":
                st.error("Nama pelatihan wajib diisi!")
            else:
                pelatihan_baru = {
                    "id": str(uuid.uuid4())[:8].upper(),
                    "nama": nama_pelatihan,
                    "tanggal": tanggal_pelatihan.strftime("%d-%m-%Y"),
                    "lokasi": lokasi,
                    "syarat_umum": syarat_umum,
                    "jabatan": jabatan_pilih,
                    "jenjang": jenjang_terpilih,
                    "syarat_khusus": syarat_kualifikasi[str(jenjang_terpilih)]
                }
                st.session_state.daftar_pelatihan.append(pelatihan_baru)
                st.success("✅ Pelatihan berhasil dibuat lengkap!")

    with tab2:
        st.subheader("Daftar Seluruh Pendaftar")
        if len(st.session_state.daftar_pendaftar) > 0:
            df = pd.DataFrame(st.session_state.daftar_pendaftar)
            st.dataframe(df, use_container_width=True)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Unduh CSV", csv, "daftar_pendaftar.csv")
        else:
            st.info("Belum ada pendaftar.")

# ====================== DASHBOARD PESERTA ======================
elif st.session_state.peran == "peserta":
    st.title("👤 Dashboard Peserta Pelatihan")
    if st.button("🔙 Kembali ke Halaman Utama"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    if len(st.session_state.daftar_pelatihan) == 0:
        st.warning("⚠️ Belum ada pelatihan dibuka.")
    else:
        pilihan = st.selectbox("Pilih Pelatihan", [p["nama"] for p in st.session_state.daftar_pelatihan])
        data_pilih = next(p for p in st.session_state.daftar_pelatihan if p["nama"] == pilihan)

        st.subheader("📋 Informasi Lengkap")
        st.info(f"**Pelatihan:** {data_pilih['nama']}\n**Tanggal:** {data_pilih['tanggal']}\n**Lokasi:** {data_pilih['lokasi']}")
        
        with st.expander("📌 Persyaratan Umum"):
            st.markdown(data_pilih["syarat_umum"])
        with st.expander("📌 Persyaratan Jabatan & Kualifikasi"):
            st.write(f"**Jabatan:** {data_pilih['jabatan']}")
            st.write(f"**Jenjang:** {data_pilih['jenjang']}")
            for s in data_pilih["syarat_khusus"]:
                st.write(f"- {s}")

        st.subheader("📝 Isi Pendaftaran")
        nama = st.text_input("Nama Lengkap Sesuai KTP")
        nik = st.text_input("NIK")
        no_hp = st.text_input("Nomor HP/WA")
        pendidikan = st.selectbox("Pendidikan Terakhir", ["", "Pendidikan Dasar", "SMA", "SMK", "D1", "D2", "D3", "D4/S1 Terapan", "S1", "S2", "S3"])
        pengalaman = st.number_input("Lama Pengalaman (Tahun)", min_value=0, max_value=60, value=0)

        st.subheader("📎 Unggah Berkas")
        st.write("Unggah dokumen pendukung yang diperlukan (KTP, Ijazah, dll)")
        uploaded_files = st.file_uploader(
            "Pilih file",
            accept_multiple_files=True,
            type=["pdf", "jpg", "jpeg", "png"]
        )

        if st.button("✅ Daftar Sekarang", type="primary"):
            if nama == "" or nik == "" or no_hp == "" or pendidikan == "":
                st.error("❌ Semua data wajib diisi!")
            else:
                pendaftar_baru = {
                    "id_pendaftar": str(uuid.uuid4())[:8].upper(),
                    "id_pelatihan": data_pilih["id"],
                    "nama_pelatihan": data_pilih["nama"],
                    "nama_pendaftar": nama,
                    "nik": nik,
                    "no_hp": no_hp,
                    "pendidikan": pendidikan,
                    "pengalaman": pengalaman,
                    "tanggal_daftar": datetime.now().strftime("%d-%m-%Y %H:%M"),
                    "status": "Menunggu Verifikasi",
                    "jumlah_berkas": len(uploaded_files) if uploaded_files else 0
                }
                st.session_state.daftar_pendaftar.append(pendaftar_baru)
                st.success(f"✅ Pendaftaran berhasil! ID Pendaftar: {pendaftar_baru['id_pendaftar']}")
                st.info("Status: Menunggu verifikasi dari admin")
