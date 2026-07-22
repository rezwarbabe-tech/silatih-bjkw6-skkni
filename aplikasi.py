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

# Gaya tampilan dioptimalkan untuk HP & Komputer
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

# ====================== INISIALISASI PENYIMPANAN DATA ======================
if "peran" not in st.session_state:
    st.session_state.peran = None
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "daftar_pendaftar" not in st.session_state:
    st.session_state.daftar_pendaftar = []

# ====================== DATA SELURUH JABATAN KERJA LENGKAP ======================
data_jabatan = [
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
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063131", "nama_jabatan": "Operator Hydrolic Hammer Breaker", "acuan": "SKKNI 158-2019"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063132", "nama_jabatan": "Operator Pemula Hydrolic Hammer Breaker", "acuan": "SKKNI 158-2019"},
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
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL011009", "nama_jabatan": "Arsitek Lanskap Utama", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL011010", "nama_jabatan": "Arsitek Lanskap Madya", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011011", "nama_jabatan": "Arsitek Lanskap Muda", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL011012", "nama_jabatan": "Manajer Lanskap Madya", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011013", "nama_jabatan": "Manajer Lanskap Muda", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL012006", "nama_jabatan": "Pengawas Lanskap (Level 6)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL012007", "nama_jabatan": "Pengawas Lanskap (Level 5)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL012008", "nama_jabatan": "Pelaksana Lanskap (Level 5)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AL012009", "nama_jabatan": "Pelaksana Lanskap (Level 4)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AL013004", "nama_jabatan": "Juru Tanam", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "AL013005", "nama_jabatan": "Juru Tanam Pemula", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "AL013006", "nama_jabatan": "Tukang Taman", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL031005", "nama_jabatan": "Desainer Interior Utama", "acuan": "SKKNI 17-2024; SKKNI 308–2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL031006", "nama_jabatan": "Desainer Interior Madya", "acuan": "SKKNI 17-2024; SKKNI 308–2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL031007", "nama_jabatan": "Desainer Interior Muda", "acuan": "SKKNI 17-2024; SKKNI 308–2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL031008", "nama_jabatan": "Ahli Madya Manajemen Interior", "acuan": "SKKNI 17-2024; SKKNI 308–2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL031009", "nama_jabatan": "Ahli Muda Manajemen Interior", "acuan": "SKKNI 17-2024; SKKNI 308–2013; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL032005", "nama_jabatan": "Pengawas Pekerjaan Interior (Level 6)", "acuan": "SKKNI 342-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL032006", "nama_jabatan": "Pengawas Pekerjaan Interior (Level 5)", "acuan": "SKKNI 342-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL032007", "nama_jabatan": "Pelaksana Pekerjaan Interior (Level 5)", "acuan": "SKKNI 308-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AL032008", "nama_jabatan": "Pelaksana Pekerjaan Interior (Level 4)", "acuan": "SKKNI 308-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AL032009", "nama_jabatan": "Ilustrator Desain Interior", "acuan": "SKKNI 17-2024; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AL032010", "nama_jabatan": "Spesifikator Desain Interior", "acuan": "SKKNI 17-2024; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AL033001", "nama_jabatan": "Juru Gambar Desain Interior", "acuan": "SKKNI 17-2024; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "AL033002", "nama_jabatan": "Juru Gambar Pemula Desain Interior", "acuan": "SKKNI 17-2024; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL031010", "nama_jabatan": "Desainer Interior Muda (Freshgraduate)", "acuan": "SKKNI 17-2024; SKKNI 17-2023; SKKNI 308-2013"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Desain Interior", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL031011", "nama_jabatan": "Ahli Muda Manajemen Interior (Freshgraduate)", "acuan": "SKKNI 17-2024; SKKNI 17-2023; SKKNI 308-2013"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR011001", "nama_jabatan": "Arsitek Utama", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR011002", "nama_jabatan": "Arsitek Madya", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR011004", "nama_jabatan": "Asisten Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR012001", "nama_jabatan": "Asisten Pemula Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR012003", "nama_jabatan": "Pengawas Lapangan Bidang Arsitektur (Level 6)", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AR012004", "nama_jabatan": "Pengawas Lapangan Bidang Arsitektur (Level 5)", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "AR012005", "nama_jabatan": "Juru Gambar Kepala Bidang Arsitektur", "acuan": "SKK-Khusus 36-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "AR013003", "nama_jabatan": "Juru Gambar Arsitektur", "acuan": "SKK-Khusus 36-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "AR013004", "nama_jabatan": "Juru Gambar Pemula Arsitektur", "acuan": "SKK-Khusus 36-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR011005", "nama_jabatan": "Asisten Arsitek (Freshgraduate)", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI121102", "nama_jabatan": "Ahli Madya Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI121001", "nama_jabatan": "Ahli Muda Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI122003", "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Level 5)", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI122004", "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Level 4)", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI191004", "nama_jabatan": "Ahli Utama Teknik Dermaga", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI191006", "nama_jabatan": "Ahli Madya Teknik Dermaga", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi
