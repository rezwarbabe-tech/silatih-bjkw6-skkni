import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

# ====================== KONFIGURASI APLIKASI ======================
st.set_page_config(
    page_title="siLATIH - Sistem Pelatihan Terintegrasi",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {max-width: 100%; padding: 1rem 1.5rem;}
    h1 {font-size: 1.8rem !important; text-align: center; color: #1f4e79;}
    h2 {font-size: 1.4rem !important; margin-top: 1.2rem; color: #2c5c97;}
    h3 {font-size: 1.2rem !important; margin-top: 1rem; color: #3a72b8;}
    .stButton>button {width: 100%; padding: 0.8rem; font-size: 1.05rem; border-radius: 10px; font-weight: 500;}
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>textarea {font-size: 1rem; padding: 0.7rem; border-radius: 8px;}
    div[data-testid="stFileUploader"] {font-size: 0.95rem;}
    .stAlert {border-radius: 10px;}
    .css-18e3th9 {padding-top: 1rem;}
</style>
""", unsafe_allow_html=True)

# ====================== INISIALISASI PENYIMPANAN ======================
if "peran" not in st.session_state:
    st.session_state.peran = None
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "daftar_pendaftar" not in st.session_state:
    st.session_state.daftar_pendaftar = []

# ====================== PERSYARATAN KUALIFIKASI SESUAI TABEL ======================
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
        "S1/S1 Terapan/D4 Terapan (Dengan Pemberian Kompetensi Tambahan untuk Fresh Graduate, masa berlaku SKK = 1): Minimal 0 Tahun",
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

# ====================== DATA JABATAN LENGKAP SESUAI DOKUMEN ======================
data_jabatan = [
# ==============================================================
# KLASIFIKASI: MEKANIKAL (ME)
# ==============================================================
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "ME061001", "nama_jabatan": "Manajer Alat Berat", "acuan": "SKKNI 206-2013"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "ME062011", "nama_jabatan": "Pengawas Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "ME062009", "nama_jabatan": "Teknisi Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063094", "nama_jabatan": "Operator Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063095", "nama_jabatan": "Operator Pemula Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063096", "nama_jabatan": "Operator Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063097", "nama_jabatan": "Operator Pemula Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063098", "nama_jabatan": "Operator Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063099", "nama_jabatan": "Operator Pemula Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063100", "nama_jabatan": "Operator Wheel Excavator", "acuan": "SKKNI 91-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063101", "nama_jabatan": "Operator Pemula Wheel Excavator", "acuan": "SKKNI 91-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063102", "nama_jabatan": "Operator Tandem Roller", "acuan": "SKKNI 159-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063103", "nama_jabatan": "Operator Pemula Tandem Roller", "acuan": "SKKNI 159-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063104", "nama_jabatan": "Operator Vibrator Roller", "acuan": "SKKNI 168-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063105", "nama_jabatan": "Operator Pemula Vibrator Roller", "acuan": "SKKNI 168-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063106", "nama_jabatan": "Operator Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063107", "nama_jabatan": "Operator Pemula Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063014", "nama_jabatan": "Operator Wheel Loader", "acuan": "SKK Khusus Reg.33-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063108", "nama_jabatan": "Operator Pemula Wheel Loader", "acuan": "SKK Khusus Reg.33-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063109", "nama_jabatan": "Operator Mobile Crane", "acuan": "SKKNI 180-2024"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063110", "nama_jabatan": "Operator Pemula Mobile Crane", "acuan": "SKKNI 180-2024"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063028", "nama_jabatan": "Operator Tower Crane", "acuan": "SKK Khusus Reg.43-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063111", "nama_jabatan": "Operator Pemula Tower Crane", "acuan": "SKK Khusus Reg.43-2022"},
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
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063125", "nama_jabatan": "Operator Mesin Pemecah Batu", "acuan": "SKK Khusus Reg.42-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063126", "nama_jabatan": "Operator Pemula Mesin Pemecah Batu", "acuan": "SKK Khusus Reg.42-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063127", "nama_jabatan": "Operator Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Reg.41-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063128", "nama_jabatan": "Operator Pemula Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Reg.41-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063012", "nama_jabatan": "Operator Cold Milling Machine", "acuan": "SKK Khusus Reg.40-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063129", "nama_jabatan": "Operator Pemula Cold Milling Machine", "acuan": "SKK Khusus Reg.40-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063029", "nama_jabatan": "Operator Batching Plant", "acuan": "SKK Khusus Reg.39-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063130", "nama_jabatan": "Operator Pemula Batching Plant", "acuan": "SKK Khusus Reg.39-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063131", "nama_jabatan": "Operator Hidrolik Hammer Breaker", "acuan": "SKKNI 158-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063132", "nama_jabatan": "Operator Pemula Hidrolik Hammer Breaker", "acuan": "SKKNI 158-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063133", "nama_jabatan": "Operator Ripper Tractor", "acuan": "SKKNI 165-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063134", "nama_jabatan": "Operator Pemula Ripper Tractor", "acuan": "SKKNI 165-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063135", "nama_jabatan": "Mekanik Tower Crane", "acuan": "SKK Khusus Reg.34-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063005", "nama_jabatan": "Mekanik Asphalt Mixing Plant", "acuan": "SKKNI 326-2009"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063002", "nama_jabatan": "Mekanik Kapal Keruk", "acuan": "SKKNI 70-2009"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063141", "nama_jabatan": "Mekanik Engine Tingkat Dasar", "acuan": "SKKNI 382-2015"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063136", "nama_jabatan": "Mekanik Engine Pemula Tingkat Dasar", "acuan": "SKKNI 382-2015"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063137", "nama_jabatan": "Mekanik Hidrolik Alat Berat", "acuan": "SKKNI 88-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063138", "nama_jabatan": "Mekanik Hidrolik Alat Berat Pemula", "acuan": "SKKNI 88-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063140", "nama_jabatan": "Mekanik Engine Alat Berat", "acuan": "SKKNI 235-2023"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063139", "nama_jabatan": "Mekanik Engine Alat Berat Pemula", "acuan": "SKKNI 235-2023"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063027", "nama_jabatan": "Operator Dump Truck", "acuan": "SKKNI 132-2015"},

# ==============================================================
# KLASIFIKASI: MEKANIKAL (ME)
# ==============================================================
data_jabatan = [
# --- ISI SEMUA DATA MEKANIKAL ANDA DI SINI ---
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063027", "nama_jabatan": "Operator Dump Truck", "acuan": "SKKNI 132-2015"},
# ==============================================================
# KLASIFIKASI: MEKANIKAL (ME)
# ==============================================================
data_jabatan = [
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "ME061001", "nama_jabatan": "Manajer Alat Berat", "acuan": "SKKNI 206-2013"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "ME062011", "nama_jabatan": "Pengawas Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "ME062009", "nama_jabatan": "Teknisi Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063094", "nama_jabatan": "Operator Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063095", "nama_jabatan": "Operator Pemula Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063096", "nama_jabatan": "Operator Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063097", "nama_jabatan": "Operator Pemula Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063098", "nama_jabatan": "Operator Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063099", "nama_jabatan": "Operator Pemula Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063100", "nama_jabatan": "Operator Wheel Excavator", "acuan": "SKKNI 91-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063101", "nama_jabatan": "Operator Pemula Wheel Excavator", "acuan": "SKKNI 91-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063102", "nama_jabatan": "Operator Tandem Roller", "acuan": "SKKNI 159-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063103", "nama_jabatan": "Operator Pemula Tandem Roller", "acuan": "SKKNI 159-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063104", "nama_jabatan": "Operator Vibrator Roller", "acuan": "SKKNI 168-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063105", "nama_jabatan": "Operator Pemula Vibrator Roller", "acuan": "SKKNI 168-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063106", "nama_jabatan": "Operator Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063107", "nama_jabatan": "Operator Pemula Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063014", "nama_jabatan": "Operator Wheel Loader", "acuan": "SKK Khusus Reg.33-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063108", "nama_jabatan": "Operator Pemula Wheel Loader", "acuan": "SKK Khusus Reg.33-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063109", "nama_jabatan": "Operator Mobile Crane", "acuan": "SKKNI 180-2024"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063110", "nama_jabatan": "Operator Pemula Mobile Crane", "acuan": "SKKNI 180-2024"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063028", "nama_jabatan": "Operator Tower Crane", "acuan": "SKK Khusus Reg.43-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063111", "nama_jabatan": "Operator Pemula Tower Crane", "acuan": "SKK Khusus Reg.43-2022"},
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
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063125", "nama_jabatan": "Operator Mesin Pemecah Batu", "acuan": "SKK Khusus Reg.42-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063126", "nama_jabatan": "Operator Pemula Mesin Pemecah Batu", "acuan": "SKK Khusus Reg.42-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063127", "nama_jabatan": "Operator Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Reg.41-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063128", "nama_jabatan": "Operator Pemula Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Reg.41-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063012", "nama_jabatan": "Operator Cold Milling Machine", "acuan": "SKK Khusus Reg.40-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063129", "nama_jabatan": "Operator Pemula Cold Milling Machine", "acuan": "SKK Khusus Reg.40-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063029", "nama_jabatan": "Operator Batching Plant", "acuan": "SKK Khusus Reg.39-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063130", "nama_jabatan": "Operator Pemula Batching Plant", "acuan": "SKK Khusus Reg.39-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063131", "nama_jabatan": "Operator Hidrolik Hammer Breaker", "acuan": "SKKNI 158-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063132", "nama_jabatan": "Operator Pemula Hidrolik Hammer Breaker", "acuan": "SKKNI 158-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063133", "nama_jabatan": "Operator Ripper Tractor", "acuan": "SKKNI 165-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063134", "nama_jabatan": "Operator Pemula Ripper Tractor", "acuan": "SKKNI 165-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063135", "nama_jabatan": "Mekanik Tower Crane", "acuan": "SKK Khusus Reg.34-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063005", "nama_jabatan": "Mekanik Asphalt Mixing Plant", "acuan": "SKKNI 326-2009"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063002", "nama_jabatan": "Mekanik Kapal Keruk", "acuan": "SKKNI 70-2009"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063141", "nama_jabatan": "Mekanik Engine Tingkat Dasar", "acuan": "SKKNI 382-2015"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063136", "nama_jabatan": "Mekanik Engine Pemula Tingkat Dasar", "acuan": "SKKNI 382-2015"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063137", "nama_jabatan": "Mekanik Hidrolik Alat Berat", "acuan": "SKKNI 88-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063138", "nama_jabatan": "Mekanik Hidrolik Alat Berat Pemula", "acuan": "SKKNI 88-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063140", "nama_jabatan": "Mekanik Engine Alat Berat", "acuan": "SKKNI 235-2023"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063139", "nama_jabatan": "Mekanik Engine Alat Berat Pemula", "acuan": "SKKNI 235-2023"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063027", "nama_jabatan": "Operator Dump Truck", "acuan": "SKKNI 132-2015"},

# ==============================================================
# KLASIFIKASI: MEKANIKAL (ME)
# ==============================================================
data_jabatan = [
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "ME061001", "nama_jabatan": "Manajer Alat Berat", "acuan": "SKKNI 206-2013"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "ME062011", "nama_jabatan": "Pengawas Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "ME062009", "nama_jabatan": "Teknisi Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063094", "nama_jabatan": "Operator Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063095", "nama_jabatan": "Operator Pemula Scaffolding", "acuan": "SKKNI 46-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063096", "nama_jabatan": "Operator Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063097", "nama_jabatan": "Operator Pemula Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063098", "nama_jabatan": "Operator Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063099", "nama_jabatan": "Operator Pemula Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063100", "nama_jabatan": "Operator Wheel Excavator", "acuan": "SKKNI 91-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063101", "nama_jabatan": "Operator Pemula Wheel Excavator", "acuan": "SKKNI 91-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063102", "nama_jabatan": "Operator Tandem Roller", "acuan": "SKKNI 159-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063103", "nama_jabatan": "Operator Pemula Tandem Roller", "acuan": "SKKNI 159-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063104", "nama_jabatan": "Operator Vibrator Roller", "acuan": "SKKNI 168-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063105", "nama_jabatan": "Operator Pemula Vibrator Roller", "acuan": "SKKNI 168-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063106", "nama_jabatan": "Operator Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063107", "nama_jabatan": "Operator Pemula Pneumatic Tire Roller", "acuan": "SKKNI 164-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063014", "nama_jabatan": "Operator Wheel Loader", "acuan": "SKK Khusus Reg.33-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063108", "nama_jabatan": "Operator Pemula Wheel Loader", "acuan": "SKK Khusus Reg.33-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063109", "nama_jabatan": "Operator Mobile Crane", "acuan": "SKKNI 180-2024"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063110", "nama_jabatan": "Operator Pemula Mobile Crane", "acuan": "SKKNI 180-2024"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063028", "nama_jabatan": "Operator Tower Crane", "acuan": "SKK Khusus Reg.43-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063111", "nama_jabatan": "Operator Pemula Tower Crane", "acuan": "SKK Khusus Reg.43-2022"},
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
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063125", "nama_jabatan": "Operator Mesin Pemecah Batu", "acuan": "SKK Khusus Reg.42-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063126", "nama_jabatan": "Operator Pemula Mesin Pemecah Batu", "acuan": "SKK Khusus Reg.42-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063127", "nama_jabatan": "Operator Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Reg.41-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063128", "nama_jabatan": "Operator Pemula Mesin Penghampar Beton Semen", "acuan": "SKK Khusus Reg.41-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063012", "nama_jabatan": "Operator Cold Milling Machine", "acuan": "SKK Khusus Reg.40-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063129", "nama_jabatan": "Operator Pemula Cold Milling Machine", "acuan": "SKK Khusus Reg.40-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063029", "nama_jabatan": "Operator Batching Plant", "acuan": "SKK Khusus Reg.39-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063130", "nama_jabatan": "Operator Pemula Batching Plant", "acuan": "SKK Khusus Reg.39-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063131", "nama_jabatan": "Operator Hidrolik Hammer Breaker", "acuan": "SKKNI 158-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063132", "nama_jabatan": "Operator Pemula Hidrolik Hammer Breaker", "acuan": "SKKNI 158-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063133", "nama_jabatan": "Operator Ripper Tractor", "acuan": "SKKNI 165-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063134", "nama_jabatan": "Operator Pemula Ripper Tractor", "acuan": "SKKNI 165-2019"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063135", "nama_jabatan": "Mekanik Tower Crane", "acuan": "SKK Khusus Reg.34-2022"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063005", "nama_jabatan": "Mekanik Asphalt Mixing Plant", "acuan": "SKKNI 326-2009"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063002", "nama_jabatan": "Mekanik Kapal Keruk", "acuan": "SKKNI 70-2009"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063141", "nama_jabatan": "Mekanik Engine Tingkat Dasar", "acuan": "SKKNI 382-2015"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063136", "nama_jabatan": "Mekanik Engine Pemula Tingkat Dasar", "acuan": "SKKNI 382-2015"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063137", "nama_jabatan": "Mekanik Hidrolik Alat Berat", "acuan": "SKKNI 88-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063138", "nama_jabatan": "Mekanik Hidrolik Alat Berat Pemula", "acuan": "SKKNI 88-2010"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063140", "nama_jabatan": "Mekanik Engine Alat Berat", "acuan": "SKKNI 235-2023"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063139", "nama_jabatan": "Mekanik Engine Alat Berat Pemula", "acuan": "SKKNI 235-2023"},
{"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063027", "nama_jabatan": "Operator Dump Truck", "acuan": "SKKNI 132-2015"},

# ==============================================================
# KLASIFIKASI: ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR (AL)
# ==============================================================
data_jabatan_al = [
    # Subklasifikasi: Arsitektur Lanskap
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL011009", "nama_jabatan": "Arsitek Lanskap Utama", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL011010", "nama_jabatan": "Arsitek Lanskap Madya", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011011", "nama_jabatan": "Arsitek Lanskap Muda", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL011012", "nama_jabatan": "Manajer Lanskap Madya", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011013", "nama_jabatan": "Manajer Lanskap Muda", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011008", "nama_jabatan": "Arsitek Lanskap Muda (Freshgraduate)", "acuan": "SKKNI 209-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL012006", "nama_jabatan": "Pengawas Lanskap (Level 6)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL012007", "nama_jabatan": "Pengawas Lanskap (Level 5)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL012008", "nama_jabatan": "Pelaksana Lanskap (Level 5)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AL012009", "nama_jabatan": "Pelaksana Lanskap (Level 4)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AL013004", "nama_jabatan": "Juru Tanam", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "AL013005", "nama_jabatan": "Juru Tanam Pemula", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "AL013006", "nama_jabatan": "Tukang Taman", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},

    # Subklasifikasi: Desain Interior
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL031005", "nama_jabatan": "Desainer Interior Utama", "acuan": "SKKNI 17-2024; SKKNI 308-2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL031006", "nama_jabatan": "Desainer Interior Madya", "acuan": "SKKNI 17-2024; SKKNI 308-2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL031007", "nama_jabatan": "Desainer Interior Muda", "acuan": "SKKNI 17-2024; SKKNI 308-2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL031008", "nama_jabatan": "Ahli Madya Manajemen Interior", "acuan": "SKKNI 17-2024; SKKNI 308-2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL031009", "nama_jabatan": "Ahli Muda Manajemen Interior", "acuan": "SKKNI 17-2024; SKKNI 308-2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL032005", "nama_jabatan": "Pengawas Pekerjaan Interior (Level 6)", "acuan": "SKKNI 342-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL032006", "nama_jabatan": "Pengawas Pekerjaan Interior (Level 5)", "acuan": "SKKNI 342-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL032007", "nama_jabatan": "Pelaksana Pekerjaan Interior (Level 5)", "acuan": "SKKNI 308-2013"}
]


    # ==============================================================
    # 🏛️ KLASIFIKASI: ARSITEKTUR (AR)
    # ==============================================================
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR011001", "nama_jabatan": "Arsitek Utama", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR011002", "nama_jabatan": "Arsitek Madya", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR011004", "nama_jabatan": "Asisten Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/Analis", "jenjang": 6, "kode_jabatan": "AR012001", "nama_jabatan": "Asisten Pemula Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AR013003", "nama_jabatan": "Juru Gambar Arsitektur", "acuan": "SKK-Khusus 36-2022"},

    # ==============================================================
    # 🏗️ KLASIFIKASI: SIPIL (SI)
    # ==============================================================
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI011031", "nama_jabatan": "Ahli Utama Teknik Bangunan Gedung", "acuan": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI011032", "nama_jabatan": "Ahli Madya Teknik Bangunan Gedung", "acuan": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "TEKNISI/Analis", "jenjang": 6, "kode_jabatan": "SI012029", "nama_jabatan": "Pengawas Pekerjaan Bangunan Gedung (Level 6)", "acuan": "SKKNI 340-2013"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "SI013060", "nama_jabatan": "Juru Gambar Konstruksi", "acuan": "SKKNI 13-2024; SKKNI 33-2021; SKKNI 327-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI031022", "nama_jabatan": "Ahli Utama Teknik Jalan", "acuan": "SKKNI 126-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI041023", "nama_jabatan": "Ahli Utama Teknik Jembatan", "acuan": "SKKNI 84-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "TEKNISI/Analis", "jenjang": 6, "kode_jabatan": "SI162006", "nama_jabatan": "Surveyor Terestris", "acuan": "SKKNI 172-2020; SKKNI 38-2019"},

    # ==============================================================
    # 📊 KLASIFIKASI: MANAJEMEN PELAKSANAAN (MP)
    # ==============================================================
    {"klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "MP011006", "nama_jabatan": "Ahli Utama Keselamatan Konstruksi", "acuan": "SKKNI 60-2022"},
    {"klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "MP051005", "nama_jabatan": "Ahli Utama Quantity Surveyor", "acuan": "SKKNI 6-2011"},

    # ==============================================================
    # 🌿 KLASIFIKASI: TATA LINGKUNGAN (TL)
    # ==============================================================
    {"klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "TL011011", "nama_jabatan": "Ahli Utama Teknik Air Minum", "acuan": "SKKNI 19-2025; SKKNI 17-2023"},
    {"klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "TEKNISI /Analis", "jenjang": 6, "kode_jabatan": "TL032004", "nama_jabatan": "Fasilitator Teknis Pembangunan Sarana Sanitasi Berbasis Masyarakat (Level 6)", "acuan": "SKKNI 204-2015"}
]

# ====================== HALAMAN UTAMA LOGIN ======================
if st.session_state.peran is None:
    st.title("🎓 siLATIH - Sistem Pelatihan Terintegrasi Konstruksi")
    st.divider()
    st.subheader("Silakan pilih akses masuk:")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.info("🔧 **Untuk Pengelola Pelatihan**")
        if st.button("Masuk sebagai Pengelola / Admin", use_container_width=True):
            st.session_state.peran = "admin"
            st.rerun()
    with col2:
        st.info("👤 **Untuk Peserta Pelatihan**")
        if st.button("Masuk sebagai Peserta", use_container_width=True):
            st.session_state.peran = "peserta"
            st.rerun()

# ====================== DASHBOARD ADMIN ======================
elif st.session_state.peran == "admin":
    st.title("🔧 Dashboard Pengelola Pelatihan")
    if st.button("🔙 Kembali ke Halaman Utama"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    tab1, tab2 = st.tabs(["📝 Buat Pelatihan Baru", "📋 Daftar Pendaftar & Verifikasi"])

    with tab1:
        st.subheader("📌 Data Umum Pelatihan")
        nama_pelatihan = st.text_input("Nama Pelatihan")
        tanggal_mulai = st.date_input("Tanggal Mulai Pelaksanaan")
        tanggal_selesai = st.date_input("Tanggal Selesai Pelaksanaan")
        lokasi = st.text_input("Lokasi Pelatihan / Tautan Daring")
        kuota = st.number_input("Kuota Peserta", min_value=1, value=30)

        st.subheader("📌 Persyaratan Umum Pelatihan")
        syarat_umum = st.text_area(
            "Daftar Persyaratan Umum",
            value="""1. Fotokopi KTP yang masih berlaku
2. Fotokopi Ijazah terakhir yang telah dilegalisir
3. Pas foto berwarna ukuran 4x6 cm (latar belakang biru)
4. Surat keterangan sehat dari puskesmas/klinik
5. Surat tugas dari instansi/perusahaan (jika diperlukan)
6. Dokumen pendukung pengalaman kerja""",
            height=160
        )

        st.subheader("📌 Pilih Jabatan Sesuai Standar SKKNI")
        klasifikasi_list = sorted({j["klasifikasi"] for j in data_jabatan})
        klasifikasi_pilih = st.selectbox("1. Pilih Klasifikasi Bidang", klasifikasi_list)
        
        subklasifikasi_list = sorted({j["subklasifikasi"] for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih})
        subklasifikasi_pilih = st.selectbox("2. Pilih Sub-Klasifikasi", subklasifikasi_list)
        
        jabatan_tersedia = [
            f"{j['nama_jabatan']} | Jenjang {j['jenjang']} | Kode: {j['kode_jabatan']} | {j['acuan']}"
            for j in data_jabatan 
            if j["klasifikasi"] == klasifikasi_pilih and j["subklasifikasi"] == subklasifikasi_pilih
        ]
        jabatan_pilih = st.selectbox("3. Pilih Jabatan yang Dituju", jabatan_tersedia)
        
        jenjang_terpilih = next(j["jenjang"] for j in data_jabatan if jabatan_pilih.startswith(j["nama_jabatan"]))
        st.success(f"✅ Persyaratan Kualifikasi Jenjang {jenjang_terpilih}:")
        for s in syarat_kualifikasi[str(jenjang_terpilih)]:
            st.write(f"- {s}")

        st.subheader("📌 Informasi Tambahan")
        catatan = st.text_area("Catatan Khusus Pelatihan (Opsional)")

        if st.button("✅ Simpan & Terbitkan Pelatihan", type="primary"):
            if not nama_pelatihan:
                st.error("❌ Nama pelatihan wajib diisi!")
            elif tanggal_mulai > tanggal_selesai:
                st.error("❌ Tanggal selesai tidak boleh lebih awal dari tanggal mulai!")
            else:
                pelatihan_baru = {
                    "id": str(uuid.uuid4())[:8].upper(),
                    "nama": nama_pelatihan,
                    "tanggal_mulai": tanggal_mulai.strftime("%d-%m-%Y"),
                    "tanggal_selesai": tanggal_selesai.strftime("%d-%m-%Y"),
                    "lokasi": lokasi,
                    "kuota": kuota,
                    "syarat_umum": syarat_umum,
                    "jabatan_lengkap": jabatan_pilih,
                    "jenjang": jenjang_terpilih,
                    "syarat_khusus": syarat_kualifikasi[str(jenjang_terpilih)],
                    "catatan": catatan,
                    "status": "Terbuka",
                    "waktu_buat": datetime.now().strftime("%d-%m-%Y %H:%M")
                }
                st.session_state.daftar_pelatihan.append(pelatihan_baru)
                st.success(f"✅ Pelatihan berhasil diterbitkan! ID Pelatihan: {pelatihan_baru['id']}")

    with tab2:
        st.subheader("Daftar Seluruh Pendaftar")
        if len(st.session_state.daftar_pendaftar) > 0:
            df_pendaftar = pd.DataFrame(st.session_state.daftar_pendaftar)
            st.dataframe(df_pendaftar, use_container_width=True)
            
            col1, col2 = st.columns(2)
            with col1:
                csv_data = df_pendaftar.to_csv(index=False).encode("utf-8")
                st.download_button("📥 Unduh Data (CSV)", csv_data, f"daftar_pendaftar_{datetime.now().strftime('%Y%m%d')}.csv")
            with col2:
                st.info("💡 Klik pada baris untuk melihat detail berkas yang diunggah")
        else:
            st.info("📭 Belum ada pendaftar yang masuk.")

# ====================== DASHBOARD PESERTA ======================
elif st.session_state.peran == "peserta":
    st.title("👤 Dashboard Peserta Pelatihan")
    if st.button("🔙 Kembali ke Halaman Utama"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    if len(st.session_state.daftar_pelatihan) == 0:
        st.warning("⚠️ Saat ini belum ada pelatihan yang dibuka oleh pengelola. Silakan cek kembali nanti.")
    else:
        st.subheader("📋 Daftar Pelatihan Terbuka")
        nama_pilihan = st.selectbox("Pilih Pelatihan yang Ingin Diikuti", [p["nama"] for p in st.session_state.daftar_pelatihan if p["status"] == "Terbuka"])
        data_pelatihan = next(p for p in st.session_state.daftar_pelatihan if p["nama"] == nama_pilihan)

        st.subheader("📄 Informasi Lengkap Pelatihan")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"""
            **Nama Pelatihan:** {data_pelatihan['nama']}
            **Tanggal Pelaksanaan:** {data_pelatihan['tanggal_mulai']} s.d. {data_pelatihan['tanggal_selesai']}
            **Lokasi:** {data_pelatihan['lokasi']}
            **Kuota:** {data_pelatihan['kuota']} peserta
            """)
        with col2:
            st.info(f"""
            **Jabatan Target:** {data_pelatihan['jabatan_lengkap']}
            **Jenjang Kualifikasi:** {data_pelatihan['jenjang']}
            **Status:** {data_pelatihan['status']}
            """)

        with st.expander("📌 Lihat Persyaratan Umum"):
            st.markdown(data_pelatihan["syarat_umum"])
        with st.expander("📌 Lihat Persyaratan Kualifikasi Jabatan"):
            for s in data_pelatihan["syarat_khusus"]:
                st.write(f"- {s}")
        if data_pelatihan.get("catatan"):
            with st.expander("📌 Catatan Khusus"):
                st.write(data_pelatihan["catatan"])

        st.subheader("📝 Formulir Pendaftaran")
        nama_lengkap = st.text_input("Nama Lengkap Sesuai KTP")
        nik = st.text_input("Nomor Induk Kependudukan (NIK)")
        tempat_lahir = st.text_input("Tempat Lahir")
        tanggal_lahir = st.date_input("Tanggal Lahir")
        no_hp = st.text_input("Nomor HP / WhatsApp")
        email = st.text_input("Alamat Email (Opsional)")
        alamat = st.text_area("Alamat Domisili Sesuai KTP")
        
        st.subheader("📌 Riwayat Pendidikan & Pengalaman")
        pendidikan_terakhir = st.selectbox(
            "Pendidikan Terakhir",
            ["", "Pendidikan Dasar (SD/SMP)", "SMA/SMK", "D1", "D2", "D3", "D4/S1 Terapan", "S1", "S2", "S3", "Pendidikan Profesi"]
        )
        lama_pengalaman = st.number_input("Lama Pengalaman Kerja di Bidang Terkait (Tahun)", min_value=0, max_value=50, value=0)
        instansi = st.text_input("Nama Instansi / Perusahaan Saat Ini")

        st.subheader("📎 Unggah Berkas Pendukung")
        berkas = st.file_uploader(
            "Unggah berkas dalam format PDF/JPG/PNG (maksimal 5 berkas, ukuran per berkas maksimal 5MB)",
            type=["pdf", "jpg", "jpeg", "png"],
            accept_multiple_files=True
        )

        if st.button("✅ Kirim Pendaftaran Sekarang", type="primary"):
            if not nama_lengkap or not nik or not no_hp or not pendidikan_terakhir:
                st.error("❌ Semua kolom yang bertanda wajib diisi!")
            else:
                pendaftar_baru = {
                    "id_pendaftar": str(uuid.uuid4())[:8].upper(),
                    "id_pelatihan": data_pelatihan["id"],
                    "nama_pelatihan": data_pelatihan["nama"],
                    "nama_lengkap": nama_lengkap,
                    "nik": nik,
                    "tempat_lahir": tempat_lahir,
                    "tanggal_lahir": tanggal_lahir.strftime("%d-%m-%Y"),
                    "no_hp": no_hp,
                    "email": email,
                    "alamat": alamat,
                    "pendidikan_terakhir": pendidikan_terakhir,
                    "lama_pengalaman_tahun": lama_pengalaman,
                    "instansi": instansi,
                    "jumlah_berkas": len(berkas) if berkas else 0,
                    "tanggal_daftar": datetime.now().strftime("%d-%m-%Y %H:%M"),
                    "status_verifikasi": "Menunggu Verifikasi"
                }
                st.session_state.daftar_pendaftar.append(pendaftar_baru)
                st.success(f"""
                ✅ Pendaftaran berhasil dikirim!
                **ID Pendaftaran Anda:** {pendaftar_baru['id_pendaftar']}
                Status saat ini: Menunggu verifikasi dari tim pengelola pelatihan.
                """)
                st.info("Anda akan mendapatkan notifikasi melalui nomor HP/email jika pendaftaran telah diverifikasi.")
