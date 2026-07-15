# ==============================================
# APLIKASI siLATIH - BJKW VI MAKASSAR (VERSI 2.1)
# Balai Jasa Konstruksi Wilayah VI Makassar - PUPR
# Perubahan: Login Pengelola pakai Nama & NIP
# Diperbarui: Daftar Jabatan Lengkap & Fitur Terintegrasi
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
# 2. KONFIGURASI & DATA REFERENSI LENGKAP
# ==============================================
st.set_page_config(page_title="siLATIH - BJKW VI Makassar", page_icon="🏗️", layout="wide", initial_sidebar_state="expanded")

# === DAFTAR PENGELOLA YANG DIPERBOLEHKAN ===
daftar_pengelola = [
    {
        "nama_lengkap": "Muhamad Reza Bugis",
        "nip": "197904142009111002"
    }
]

# === TABEL PERSYARATAN PENGALAMAN KERJA ===
persyaratan = {
    "Ahli Utama Bidang Keahlian Teknik Sumber Daya Air": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Bidang Keahlian Teknik Sumber Daya Air": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Hidrologi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Hidrologi": {
        "jenjang": 8,
        "min_tahun": {
            "S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Hidrologi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Hidrolika": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Hidrolika": {
        "jenjang": 8,
        "min_tahun": {
            "S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Hidrolika": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Pengeboran Air Tanah (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pengeboran Air Tanah (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 2,
            "D2": 6,
            "D1": 10
        }
    },
    "Pelaksana Pengeboran Air Tanah (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10
        }
    },
    "Pelaksana Pengeboran Air Tanah (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Manajer Alat Berat": {
        "jenjang": 8,
        "min_tahun": {
            "S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 3,
            "S1/S1 Terapan/D4 Terapan": 5
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
    "Operator Pemula Bulldozer": {
        "jenjang": 2,
        "min_tahun": {
            "SMK": 0,
            "SMA": 2,
            "Pendidikan Dasar": 3
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

# === DAFTAR JABATAN LENGKAP ===
daftar_jabatan = [
    # --- SIPIL - SUMBER DAYA AIR ---
    {"no": 1, "kode_jabatan": "SI101015", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Bidang Keahlian Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 2, "kode_jabatan": "SI101014", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Bidang Keahlian Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 3, "kode_jabatan": "SI101013", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 4, "kode_jabatan": "SI101003", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Hidrologi", "acuan_skkni": "SKKNI 32-2014"},
    {"no": 5, "kode_jabatan": "SI101002", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Hidrologi", "acuan_skkni": "SKKNI 32-2014"},
    {"no": 6, "kode_jabatan": "SI101001", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Hidrologi", "acuan_skkni": "SKKNI 32-2014"},
    {"no": 7, "kode_jabatan": "SI101018", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Hidrolika", "acuan_skkni": "SKKNI 151-2019"},
    {"no": 8, "kode_jabatan": "SI101021", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Hidrolika", "acuan_skkni": "SKKNI 151-2019"},
    {"no": 9, "kode_jabatan": "SI101020", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Hidrolika", "acuan_skkni": "SKKNI 151-2019"},
    {"no": 10, "kode_jabatan": "SI102005", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pengeboran Air Tanah (Level 6)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 11, "kode_jabatan": "SI102006", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pengeboran Air Tanah (Level 5)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 12, "kode_jabatan": "SI102007", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Pengeboran Air Tanah (Level 5)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 13, "kode_jabatan": "SI102008", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Pengeboran Air Tanah (Level 4)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 14, "kode_jabatan": "SI101019", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate)", "acuan_skkni": "SKKNI 124-2021"},
    # --- SIPIL - JALAN & JEMBATAN ---
    {"no": 15, "kode_jabatan": "SI-JLN-001", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan & Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Rekayasa Jalan Raya", "acuan_skkni": "SKKNI 137-2022"},
    # --- SIPIL - BANGUNAN GEDUNG ---
    {"no": 16, "kode_jabatan": "SI-GED-001", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Gedung", "kualifikasi": "Pengawas", "jenjang": 6, "nama_jabatan": "Pengawas Pelaksanaan Gedung", "acuan_skkni": "SKKNI 141-2021"},
    # --- SIPIL - PEKERJAAN BETON ---
    {"no": 17, "kode_jabatan": "SI-BET-001", "klasifikasi": "SIPIL", "subklasifikasi": "Pekerjaan Beton", "kualifikasi": "Tukang", "jenjang": 4, "nama_jabatan": "Tukang Beton Terampil", "acuan_skkni": "SKKNI 135-2022"},
    # --- MEKANIKAL - ALAT BERAT ---
    {"no": 18, "kode_jabatan": "ME061001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Manajer Alat Berat", "acuan_skkni": "SKKNI 206-2013"},
    {"no": 19, "kode_jabatan": "ME062011", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Scaffolding", "acuan_skkni": "SKKNI 46-2022"},
    {"no": 20, "kode_jabatan": "ME062009", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Scaffolding", "acuan_skkni": "SKKNI 46-2022"},
    {"no": 21, "kode_jabatan": "ME063094", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Scaffolding", "acuan_skkni": "SKKNI 46-2022"},
    {"no": 22, "kode_jabatan": "ME063096", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022"},
    {"no": 23, "kode_jabatan": "ME063098", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Motor Grader", "acuan_skkni": "SKK Khusus Reg.30-2022"},
    {"no": 24, "kode_jabatan": "ME063100", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Wheel Excavator", "acuan_skkni": "SKKNI 91-2010"},
    {"no": 25, "kode_jabatan": "ME063102", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Tandem Roller", "acuan_skkni": "SKKNI 159-2019"},
    {"no": 26, "kode_jabatan": "ME063104", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Vibrator Roller", "acuan_skkni": "SKKNI 168-2019"},
    {"no": 27, "kode_jabatan": "ME063106", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Pneumatic Tire Roller", "acuan_skkni": "SKKNI 164-2019"},
    {"no": 28, "kode_jabatan": "ME063014", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Wheel Loader", "acuan_skkni": "SKK Khusus Reg.33-2022"},
    {"no": 29, "kode_jabatan": "ME063109", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mobile Crane", "acuan_skkni": "SKKNI 180-2024"},
    {"no": 30, "kode_jabatan": "ME063028", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Tower Crane", "acuan_skkni": "SKK Khusus Reg.43-2022"},
    {"no": 31, "kode_jabatan": "ME063112", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Truck Mounted Crane", "acuan_skkni": "SKKNI 85-2021"},
    {"no": 32, "kode_jabatan": "ME063114", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Backhoe Loader", "acuan_skkni": "SKKNI 89-2010"},
    {"no": 33, "kode_jabatan": "ME063116", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Pile Drive Hammer", "acuan_skkni": "SKKNI 150-2019"},
    {"no": 34, "kode_jabatan": "ME063142", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Pompa Beton", "acuan_skkni": "SKKNI 381-2013"},
    {"no": 35, "kode_jabatan": "ME063119", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bore Pile", "acuan_skkni": "SKKNI 111-2015"},
    {"no": 36, "kode_jabatan": "ME063121", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Pencampur Aspal", "acuan_skkni": "SKKNI 382-2013"},
    {"no": 37, "kode_jabatan": "ME063123", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Penggelar Aspal", "acuan_skkni": "SKKNI 383-2013"},
    {"no": 38, "kode_jabatan": "ME063125", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Pemecah Batu", "acuan_skkni": "SKK Khusus Reg.42-2022"},
    {"no": 39, "kode_jabatan": "ME063127", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Penghampar Beton Semen", "acuan_skkni": "SKK Khusus Reg.41-2022"},
    {"no": 40, "kode_jabatan": "ME063012", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Cold Milling Machine", "acuan_skkni": "SKK Khusus Reg.40-2022"},
    {"no": 41, "kode_jabatan": "ME063029", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Batching Plant", "acuan_skkni": "SKK Khusus Reg.39-2022"},
    {"no": 42, "kode_jabatan": "ME063131", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Hydrolic Hammer Breaker", "acuan_skkni": "SKKNI 158-2019"},
    {"no": 43, "kode_jabatan": "ME063133", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Ripper Tractor", "acuan_skkni": "SKKNI 165-2019"},
    {"no": 44, "kode_jabatan": "ME-MNT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Pemeliharaan Alat Berat", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Mekanik Alat Berat", "acuan_skkni": "SKKNI 190-2024"},
    # --- ELEKTRO ---
    {"no": 45, "kode_jabatan": "EL-ILG-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Instalasi Listrik", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Instalasi Listrik Terampil", "acuan_skkni": "SKKNI 130-2021"},
    {"no": 46, "kode_jabatan": "EL-SRY-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Energi Terbarukan", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Pemasangan Panel Surya", "acuan_skkni": "SKKNI 241-2024"},
    # --- KESELAMATAN KERJA ---
    {"no": 47, "kode_jabatan": "K3-SMK-001", "klasifikasi": "KESELAMATAN KERJA", "subklasifikasi": "Sistem Manajemen K3", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan dan Kesehatan Kerja", "acuan_skkni": "SKKNI 119-2020"},
    # --- MANAJEMEN PROYEK ---
    {"no": 48, "kode_jabatan": "MN-MPR-001", "klasifikasi": "MANAJEMEN PROYEK", "subklasifikasi": "Manajemen Proyek", "kualifikasi": "Manajer", "jenjang": 9, "nama_jabatan": "Manajer Proyek Utama", "acuan_skkni": "SKKNI 145-2021"},
    # --- ARSITEKTUR LANSKAP ---
    {"no": 49, "kode_jabatan": "AL011009", "klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Arsitek Lanskap Utama", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 50, "kode_jabatan": "AL011010", "klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Arsitek Lanskap Madya", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 51, "kode_jabatan": "AL011011", "klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Arsitek Lanskap Muda", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    # --- ARSITEKTUR ---
    {"no": 52, "kode_jabatan": "AR011001", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Arsitek Utama", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 53, "kode_jabatan": "AR011002", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Arsitek Madya", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 54, "kode_jabatan": "AR011004", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Asisten Arsitek", "acuan_skkni": "SKKNI 196-2021"}
]

# Inisialisasi State
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "sedang_login" not in st.session_state:
    st.session_state.sedang_login = False
if "nama_pengelola" not in st.session_state:
    st.session_state.nama_pengelola = ""

# ==============================================
# 3. FUNGSI BANTUAN & VALIDASI
# ==============================================

def cek_akses_pengelola(nama, nip):
    """Memverifikasi apakah nama dan NIP terdaftar sebagai pengelola"""
    nama_bersih = nama.strip().lower()
    nip_bersih = nip.strip()
    for pengelola in daftar_pengelola:
        if (pengelola["nama_lengkap"].lower() == nama_bersih and 
            pengelola["nip"] == nip_bersih):
            return True, pengelola["nama_lengkap"]
    return False, ""

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

def validasi_nip(nip):
    """Memeriksa format NIP PNS 18 digit angka"""
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
                 st.success("✅ Pelatihan berhasil ditambahkan ke daftar!")
                st.rerun()

    # Tampilkan Daftar Pelatihan
    st.subheader("📑 Daftar Pelatihan yang Telah Dibuat")
    if not st.session_state.daftar_pelatihan:
        st.info("📭 Belum ada pelatihan yang ditambahkan. Silakan isi formulir di atas.")
    else:
        for idx, latih in enumerate(st.session_state.daftar_pelatihan, 1):
            status = tentukan_status(latih["mulai"], latih["selesai"])
            with st.expander(f"{idx}. {latih['nama']} — {status}"):
                st.write(f"**Jabatan Terkait:** {latih['jabatan']}")
                st.write(f"**Lokasi:** {latih['lokasi']}")
                st.write(f"**Kuota Peserta:** {latih['kuota']} orang")
                st.write(f"**Pendaftaran:** {latih['buka_daftar'].strftime('%d/%m/%Y')} s.d. {latih['tutup_daftar'].strftime('%d/%m/%Y')}")
                st.write(f"**Pelaksanaan:** {latih['mulai'].strftime('%d/%m/%Y')} s.d. {latih['selesai'].strftime('%d/%m/%Y')}")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"🗑️ Hapus Pelatihan #{idx}", type="secondary"):
                        del st.session_state.daftar_pelatihan[idx-1]
                        st.rerun()
                with col2:
                    st.download_button(
                        label=f"📄 Unduh Formulir Pendaftaran #{idx}",
                        data=f"Formulir Pendaftaran: {latih['nama']}\nJabatan: {latih['jabatan']}\nLokasi: {latih['lokasi']}",
                        file_name=f"Formulir_{latih['nama'].replace(' ', '_')}.txt"
                    )

# ==============================================
# 5. HALAMAN PENDAFTARAN PESERTA
# ==============================================
st.markdown("---")
st.header("📝 Pendaftaran Pelatihan & Uji Kompetensi")

if not st.session_state.daftar_pelatihan:
    st.warning("⏳ Pendaftaran belum dibuka. Silakan tunggu pengelola menambahkan jadwal pelatihan.")
else:
    pelatihan_pilihan = st.selectbox("Pilih Pelatihan yang Diikuti", options=[p["nama"] for p in st.session_state.daftar_pelatihan])
    data_pilih = next(p for p in st.session_state.daftar_pelatihan if p["nama"] == pelatihan_pilihan)
    
    st.info(f"📅 Jadwal: {data_pilih['mulai'].strftime('%d/%m/%Y')} s.d. {data_pilih['selesai'].strftime('%d/%m/%Y')} | Lokasi: {data_pilih['lokasi']}")
    
    with st.form("form_pendaftaran_peserta", clear_on_submit=True):
        st.subheader("Data Diri Peserta")
        col1, col2 = st.columns(2)
        with col1:
            nama_lengkap = st.text_input("Nama Lengkap Sesuai KTP *")
            nik = st.text_input("Nomor Induk Kependudukan (NIK) *", max_chars=16)
            tempat_lahir = st.text_input("Tempat Lahir *")
            tgl_lahir = st.date_input("Tanggal Lahir *")
        with col2:
            jenjang_pendidikan = st.selectbox("Jenjang Pendidikan Terakhir *", [
                "S3/S3 Terapan", "S2/S2 Terapan", "Pendidikan Profesi",
                "S1/S1 Terapan/D4 Terapan", "D3", "D2", "D1/SMK Plus", "SMK", "SMA", "Pendidikan Dasar"
            ])
            no_hp = st.text_input("Nomor HP/WhatsApp *")
            email = st.text_input("Alamat Email")
            alamat_lengkap = st.text_area("Alamat Domisili Lengkap *")
        
        st.subheader("Dokumen Pendukung")
        berkas_ktp = st.file_uploader("Unggah Scan KTP *", type=["pdf", "jpg", "png"])
        berkas_ijazah = st.file_uploader("Unggah Scan Ijazah Terakhir *", type=["pdf", "jpg", "png"])
        berkas_pengalaman = st.file_uploader("Unggah Bukti Pengalaman Kerja (Sertifikat/SK) *", type=["pdf", "jpg", "png"], accept_multiple_files=True)
        link_pddikti = st.text_input("Link Verifikasi PDDIKTI (Untuk Lulusan Perguruan Tinggi)")
        
        kirim = st.form_submit_button("✅ Kirim Pendaftaran")
        if kirim:
            # Validasi Data
            if not nama_lengkap or not nik or not tempat_lahir or not alamat_lengkap:
                st.error("❌ Lengkapi semua kolom bertanda * terlebih dahulu!")
            elif not validasi_nik(nik):
                st.error("❌ NIK harus berisi 16 digit angka!")
            elif not validasi_no_hp(no_hp):
                st.error("❌ Format nomor HP salah! Mulai dengan 0 atau +62 dan panjang 10-14 digit.")
            elif email and not validasi_email(email):
                st.error("❌ Format email tidak valid!")
            elif berkas_ktp is None or berkas_ijazah is None or len(berkas_pengalaman) == 0:
                st.error("❌ Unggah semua dokumen pendukung yang diminta!")
            elif link_pddikti and not validasi_link_pddikti(link_pddikti):
                st.error("❌ Link PDDIKTI harus dimulai dengan https://pddikti.kemdikbud.go.id/")
            else:
                # Verifikasi Syarat Jabatan
                total_tahun = ekstrak_tahun_pengalaman(berkas_pengalaman)
                layak, catatan = verifikasi_syarat(data_pilih["jabatan"], jenjang_pendidikan, total_tahun)
                
                st.markdown("---")
                st.subheader("📋 Hasil Pemeriksaan Pendaftaran")
                if layak:
                    st.success(f"✅ {catatan}")
                    st.success("🎉 Pendaftaran Anda diterima! Berkas akan diverifikasi oleh tim BJKW VI Makassar paling lambat 3 hari kerja.")
                else:
                    st.error(f"❌ {catatan}")
                    st.error("⚠️ Pendaftaran belum dapat diterima. Silakan lengkapi syarat atau pilih jabatan yang sesuai kualifikasi Anda.")

# ==============================================
# 6. INFORMASI TAMBAHAN & KONTAK
# ==============================================
st.markdown("---")
st.markdown("""
<div class="pu-info">
<strong>🏢 Kontak Kami:</strong><br>
Balai Jasa Konstruksi Wilayah VI Makassar<br>
Jl. Perintis Kemerdekaan Km. 17, Tamalanrea, Makassar, Sulawesi Selatan<br>
📞 Telp: (0411) 585123 | 📧 Email: bjkwsulsel@pu.go.id<br>
⏰ Jam Layanan: Senin - Jumat, 08.00 - 16.00 WITA
</div>
""", unsafe_allow_html=True)

st.caption("© 2026 Balai Jasa Konstruksi Wilayah VI Makassar - Kementerian PUPR RI | Versi 2.1 Final")
