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
        "S2/S2 Terapan/Pendidikan Spesialis 1: Minimal 0 Tahun",
        "Pendidikan Profesi: Minimal 5 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 6 Tahun"
    ],
    "7": [
        "Pendidikan Profesi: Minimal 0 Tahun",
        "S1/S1 Terapan/D4 Terapan (Fresh Graduate): Minimal 0 Tahun",
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

# ====================== DATA JABATAN LENGKAP ======================
data_jabatan = [
    # ==============================================================
    # 🏗️ KLASIFIKASI: SIPIL — LENGKAP SELURUH SUBKLASIFIKASI
    # ==============================================================
    # --- Subklasifikasi: Air Tanah dan Air Baku ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101015", "nama_jabatan": "Ahli Utama Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101014", "nama_jabatan": "Ahli Madya Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101013", "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101003", "nama_jabatan": "Ahli Utama Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101002", "nama_jabatan": "Ahli Madya Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101001", "nama_jabatan": "Ahli Muda Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101018", "nama_jabatan": "Ahli Utama Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101021", "nama_jabatan": "Ahli Madya Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101020", "nama_jabatan": "Ahli Muda Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI102005", "nama_jabatan": "Pengawas Pengeboran Air Tanah (Level 6)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI102006", "nama_jabatan": "Pengawas Pengeboran Air Tanah (Level 5)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI102007", "nama_jabatan": "Pelaksana Pengeboran Air Tanah (Level 5)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI102008", "nama_jabatan": "Pelaksana Pengeboran Air Tanah (Level 4)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101019", "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate)", "acuan": "SKKNI 124-2021"},

    # --- Subklasifikasi: Bangunan Air Baku ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI111001", "nama_jabatan": "Ahli Utama Teknik Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI111002", "nama_jabatan": "Ahli Madya Teknik Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI111003", "nama_jabatan": "Ahli Muda Teknik Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI112001", "nama_jabatan": "Pengawas Konstruksi Bangunan Air Baku", "acuan": "SKKNI 125-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI112002", "nama_jabatan": "Pelaksana Konstruksi Bangunan Air Baku", "acuan": "SKKNI 125-2021"},

    # --- Subklasifikasi: Bangunan Air Limbah ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI121101", "nama_jabatan": "Ahli Utama Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI121102", "nama_jabatan": "Ahli Madya Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI121001", "nama_jabatan": "Ahli Muda Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI122001", "nama_jabatan": "Pengawas Lapangan SPALD", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI122003", "nama_jabatan": "Pelaksana Lapangan SPALD Permukiman (Level 5)", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI122004", "nama_jabatan": "Pelaksana Lapangan SPALD Permukiman (Level 4)", "acuan": "SKKNI 312-2009"},

    # --- Subklasifikasi: Bangunan Pengairan ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI131001", "nama_jabatan": "Ahli Utama Teknik Pengairan", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI131002", "nama_jabatan": "Ahli Madya Teknik Pengairan", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI131003", "nama_jabatan": "Ahli Muda Teknik Pengairan", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI132001", "nama_jabatan": "Pengawas Irigasi", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI132002", "nama_jabatan": "Pelaksana Irigasi", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI133001", "nama_jabatan": "Operator Jaringan Irigasi", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pengairan", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI133002", "nama_jabatan": "Operator Pemula Jaringan Irigasi", "acuan": "SKKNI 126-2021"},

    # --- Subklasifikasi: Bangunan Pantai dan Pelabuhan ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI191004", "nama_jabatan": "Ahli Utama Teknik Dermaga", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI191006", "nama_jabatan": "Ahli Madya Teknik Dermaga", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI191005", "nama_jabatan": "Ahli Muda Teknik Dermaga", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI192001", "nama_jabatan": "Pengawas Konstruksi Pelabuhan", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pantai dan Pelabuhan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI192002", "nama_jabatan": "Pelaksana Konstruksi Pelabuhan", "acuan": "SKKNI 320–2016"},

    # --- Subklasifikasi: Bangunan Jalan dan Jembatan ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI201001", "nama_jabatan": "Ahli Utama Teknik Jalan Raya", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI201002", "nama_jabatan": "Ahli Madya Teknik Jalan Raya", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI201003", "nama_jabatan": "Ahli Muda Teknik Jalan Raya", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI202001", "nama_jabatan": "Pengawas Konstruksi Jalan", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI202002", "nama_jabatan": "Pelaksana Konstruksi Jalan", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI203001", "nama_jabatan": "Operator Perawatan Jalan", "acuan": "SKKNI 127-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Jalan dan Jembatan", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "SI203002", "nama_jabatan": "Operator Pemula Perawatan Jalan", "acuan": "SKKNI 127-2021"},

    # --- Subklasifikasi: Geoteknik ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI211001", "nama_jabatan": "Ahli Utama Teknik Geoteknik", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI211002", "nama_jabatan": "Ahli Madya Teknik Geoteknik", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI211003", "nama_jabatan": "Ahli Muda Teknik Geoteknik", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI212001", "nama_jabatan": "Pengawas Penyelidikan Tanah", "acuan": "SKKNI 152-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI212002", "nama_jabatan": "Pelaksana Penyelidikan Tanah", "acuan": "SKKNI 152-2019"},

    # --- Subklasifikasi: Manajemen Konstruksi ---
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI221001", "nama_jabatan": "Ahli Utama Manajemen Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI221002", "nama_jabatan": "Ahli Madya Manajemen Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI221003", "nama_jabatan": "Ahli Muda Manajemen Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI222001", "nama_jabatan": "Pengawas Keselamatan Konstruksi", "acuan": "SKKNI 153-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Manajemen Konstruksi", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI222002", "nama_jabatan": "Petugas Keselamatan Konstruksi", "acuan": "SKKNI 153-2019"},

    # ==============================================================
    # 🏛️ KLASIFIKASI: ARSITEKTUR — LENGKAP SELURUH SUBKLASIFIKASI
    # ==============================================================
    # --- Subklasifikasi: Perancangan Arsitektural ---
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR011001", "nama_jabatan": "Arsitek Utama", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR011002", "nama_jabatan": "Arsitek Madya", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR011003", "nama_jabatan": "Arsitek Muda", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR011004", "nama_jabatan": "Asisten Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR012001", "nama_jabatan": "Asisten Pemula Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AR012002", "nama_jabatan": "Pengawas Lapangan Arsitektur", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AR012003", "nama_jabatan": "Pelaksana Gambar Kerja Arsitektur", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Perancangan Arsitektural", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AR013001", "nama_jabatan": "Operator Pembuatan Gambar Arsitektur", "acuan": "SKKNI 196-2021"},

    # --- Subklasifikasi: Desain Interior ---
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR021001", "nama_jabatan": "Desainer Interior Utama", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR021002", "nama_jabatan": "Desainer Interior Madya", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR021003", "nama_jabatan": "Desainer Interior Muda", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR022001", "nama_jabatan": "Pengawas Pengerjaan Interior", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AR022002", "nama_jabatan": "Pelaksana Desain Interior", "acuan": "SKKNI 211-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AR022003", "nama_jabatan": "Pelaksana Pemasangan Elemen Interior", "acuan": "SKKNI 211-2022"},

    # --- Subklasifikasi: Konservasi Bangunan Bersejarah ---
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Konservasi Bangunan Bersejarah", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR031001", "nama_jabatan": "Ahli Utama Konservasi Bangunan Bersejarah", "acuan": "SKKNI 250-2019"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Konservasi Bangunan Bersejarah", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR031002", "nama_jabatan": "Ahli Madya Konservasi Bangunan Bersejarah", "acuan": "SKKNI 250-2019"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Konservasi Bangunan Bersejarah", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR031003", "nama_jabatan": "Ahli Muda Konservasi Bangunan Bersejarah", "acuan": "SKKNI 250-2019"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Konservasi Bangunan Bersejarah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR032001", "nama_jabatan": "Pengawas Pemeliharaan Bangunan Bersejarah", "acuan": "SKKNI 250-2019"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Konservasi Bangunan Bersejarah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AR032002", "nama_jabatan": "Pelaksana Pemeliharaan Bangunan Bersejarah", "acuan": "SKKNI 250-2019"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Konservasi Bangunan Bersejarah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AR032003", "nama_jabatan": "Teknisi Restorasi Bangunan Bersejarah", "acuan": "SKKNI 250-2019"},

    # --- Subklasifikasi: Fasilitas dan Kenyamanan Bangunan ---
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Fasilitas dan Kenyamanan Bangunan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR041001", "nama_jabatan": "Ahli Utama Fasilitas Bangunan", "acuan": "SKKNI 287-2020"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Fasilitas dan Kenyamanan Bangunan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR041002", "nama_jabatan": "Ahli Madya Fasilitas Bangunan", "acuan": "SKKNI 287-2020"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Fasilitas dan Kenyamanan Bangunan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR041003", "nama_jabatan": "Ahli Muda Fasilitas Bangunan", "acuan": "SKKNI 287-2020"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Fasilitas dan Kenyamanan Bangunan", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR042001", "nama_jabatan": "Pengawas Pemeliharaan Fasilitas Bangunan", "acuan": "SKKNI 287-2020"},

    # ==============================================================
    # 🌿 KLASIFIKASI: ARSITEKTUR LANSKAP — LENGKAP SELURUH SUBKLASIFIKASI
    # ==============================================================
    # --- Subklasifikasi: Perancangan Lanskap ---
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perancangan Lanskap", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL011001", "nama_jabatan": "Arsitek Lanskap Utama", "acuan": "SKKNI 31-2025"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perancangan Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL011002", "nama_jabatan": "Arsitek Lanskap Madya", "acuan": "SKKNI 31-2025"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perancangan Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011003", "nama_jabatan": "Arsitek Lanskap Muda", "acuan": "SKKNI 31-2025"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perancangan Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011004", "nama_jabatan": "Asisten Arsitek Lanskap", "acuan": "SKKNI 31-2025"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perancangan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL012001", "nama_jabatan": "Asisten Pemula Arsitek Lanskap", "acuan": "SKKNI 31-2025"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perancangan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL012002", "nama_jabatan": "Pengawas Lapangan Lanskap", "acuan": "SKKNI 31-2025"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Perancangan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AL012003", "nama_jabatan": "Pelaksana Gambar Kerja Lanskap", "acuan": "SKKNI 31-2025"},

    # --- Subklasifikasi: Pembangunan & Pemeliharaan Lanskap ---
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pembangunan & Pemeliharaan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL022001", "nama_jabatan": "Pengawas Konstruksi Lanskap", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pembangunan & Pemeliharaan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL022002", "nama_jabatan": "Pelaksana Konstruksi Lanskap", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pembangunan & Pemeliharaan Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AL022003", "nama_jabatan": "Pelaksana Penanaman & Perawatan Taman", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pembangunan & Pemeliharaan Lanskap", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AL023001", "nama_jabatan": "Operator Perawatan Taman", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Pembangunan & Pemeliharaan Lanskap", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "AL023002", "nama_jabatan": "Operator Pemula Perawatan Taman", "acuan": "SKKNI 29-2023"},

    # --- Subklasifikasi: Konservasi Sumber Daya Lanskap ---
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Konservasi Sumber Daya Lanskap", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL031001", "nama_jabatan": "Ahli Utama Konservasi Lanskap", "acuan": "SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Konservasi Sumber Daya Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL031002", "nama_jabatan": "Ahli Madya Konservasi Lanskap", "acuan": "SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Konservasi Sumber Daya Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL031003", "nama_jabatan": "Ahli Muda Konservasi Lanskap", "acuan": "SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Konservasi Sumber Daya Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL032001", "nama_jabatan": "Pengawas Konservasi Lanskap", "acuan": "SKKNI 17-2023"}
]

# ==============================================================
    # ⚙️ KLASIFIKASI: MEKANIKAL — LENGKAP SELURUH SUBKLASIFIKASI
    # ==============================================================
    # --- Subklasifikasi: Instalasi Mekanikal Gedung ---
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Instalasi Mekanikal Gedung", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "MK011001", "nama_jabatan": "Ahli Utama Teknik Instalasi Mekanikal", "acuan": "SKKNI 134-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Instalasi Mekanikal Gedung", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "MK011002", "nama_jabatan": "Ahli Madya Teknik Instalasi Mekanikal", "acuan": "SKKNI 134-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Instalasi Mekanikal Gedung", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "MK011003", "nama_jabatan": "Ahli Muda Teknik Instalasi Mekanikal", "acuan": "SKKNI 134-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Instalasi Mekanikal Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "MK012001", "nama_jabatan": "Pengawas Instalasi Mekanikal", "acuan": "SKKNI 134-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Instalasi Mekanikal Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "MK012002", "nama_jabatan": "Pelaksana Instalasi Mekanikal", "acuan": "SKKNI 134-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Instalasi Mekanikal Gedung", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "MK012003", "nama_jabatan": "Pelaksana Instalasi Mekanikal Dasar", "acuan": "SKKNI 134-2021"},

    # --- Subklasifikasi: Sistem Pendingin & Tata Udara ---
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Sistem Pendingin & Tata Udara", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "MK021001", "nama_jabatan": "Ahli Utama Sistem Tata Udara", "acuan": "SKKNI 135-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Sistem Pendingin & Tata Udara", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "MK021002", "nama_jabatan": "Ahli Madya Sistem Tata Udara", "acuan": "SKKNI 135-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Sistem Pendingin & Tata Udara", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "MK021003", "nama_jabatan": "Ahli Muda Sistem Tata Udara", "acuan": "SKKNI 135-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Sistem Pendingin & Tata Udara", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "MK022001", "nama_jabatan": "Pengawas Pemasangan AC & Ventilasi", "acuan": "SKKNI 135-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Sistem Pendingin & Tata Udara", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "MK022002", "nama_jabatan": "Teknisi Pemasangan Sistem Tata Udara", "acuan": "SKKNI 135-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Sistem Pendingin & Tata Udara", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "MK023001", "nama_jabatan": "Operator Perawatan Sistem Pendingin", "acuan": "SKKNI 135-2021"},

    # --- Subklasifikasi: Perpipaan & Sistem Fluida ---
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Perpipaan & Sistem Fluida", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "MK031001", "nama_jabatan": "Ahli Utama Teknik Perpipaan", "acuan": "SKKNI 189-2020"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Perpipaan & Sistem Fluida", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "MK031002", "nama_jabatan": "Ahli Madya Teknik Perpipaan", "acuan": "SKKNI 189-2020"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Perpipaan & Sistem Fluida", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "MK031003", "nama_jabatan": "Ahli Muda Teknik Perpipaan", "acuan": "SKKNI 189-2020"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Perpipaan & Sistem Fluida", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "MK032001", "nama_jabatan": "Pengawas Pemasangan Perpipaan", "acuan": "SKKNI 189-2020"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Perpipaan & Sistem Fluida", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "MK032002", "nama_jabatan": "Pelaksana Pemasangan Perpipaan", "acuan": "SKKNI 189-2020"},
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

        st.subheader("📌 Pilih Jabatan Lengkap")
        klasifikasi_list = sorted({j["klasifikasi"] for j in data_jabatan})
        klasifikasi_pilih = st.selectbox("Pilih Klasifikasi", klasifikasi_list)
        
        subklasifikasi_list = sorted({j["subklasifikasi"] for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih})
        subklasifikasi_pilih = st.selectbox("Pilih Subklasifikasi", subklasifikasi_list)
        
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
        pendidikan = st.text_input("Pendidikan Terakhir")
        pengalaman = st.number_input("Lama Pengalaman (Tahun)", min_value=0)

        st.subheader("📎 Unggah Berkas")
        ktp = st.file_uploader("KTP", type=["jpg","png","pdf"])
        ijazah = st.file_uploader("Ijazah Terakhir", type=["jpg","png","pdf"])
        foto = st.file_uploader("Pas Foto", type=["jpg","png"])

        if st.checkbox("Data sudah benar") and st.button("✅ Kirim Pendaftaran", type="primary"):
            nomor_daftar = f"REG-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:4].upper()}"
            st.session_state.daftar_pendaftar.append({
                "Nomor Daftar": nomor_daftar,
                "Pelatihan": pilihan,
                "Nama": nama,
                "NIK": nik,
                "HP": no_hp,
                "Pendidikan": pendidikan,
                "Pengalaman": pengalaman
            })
            st.success(f"🎉 Pendaftaran Berhasil! Nomor: {nomor_daftar}")
