# ==============================================
# APLIKASI siLATIH - BJKW VI MAKASSAR (VERSI 2.2 PERBAIKAN)
# Perubahan: Tampilan Terpisah Pengelola & Peserta
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
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
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
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
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
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pengeboran Air Tanah (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
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
    "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Manajer Alat Berat": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Pengawas Scaffolding": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Scaffolding": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Operator Scaffolding": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Scaffolding": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
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
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Motor Grader": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Motor Grader": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Wheel Excavator": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Wheel Excavator": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Tandem Roller": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Tandem Roller": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Vibrator Roller": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Vibrator Roller": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pneumatic Tire Roller": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Pneumatic Tire Roller": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Wheel Loader": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Wheel Loader": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Mobile Crane": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Mobile Crane": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Tower Crane": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Tower Crane": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Truck Mounted Crane": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Truck Mounted Crane": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Backhoe Loader": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Backhoe Loader": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pile Drive Hammer": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Pile Drive Hammer": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pompa Beton": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Pompa Beton": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Bore Pile": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Bore Pile": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Mesin Pencampur Aspal": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Mesin Pencampur Aspal": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Mesin Penggelar Aspal": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Mesin Penggelar Aspal": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Mesin Pemecah Batu": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Mesin Pemecah Batu": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Mesin Penghampar Beton Semen (Concrete Paver Operator)": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Mesin Penghampar Beton Semen (Concrete Paver Operator Pemula)": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Cold Milling Machine": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Cold Milling Machine": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Batching Plant": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Batching Plant": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Hydrolic Hammer Breaker": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Hydrolic Hammer Breaker": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Ripper Tractor": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Ripper Tractor": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Tower Crane": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Asphalt Mixing Plant (Asphalt Mixing Plant Mechanic)": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Kapal Keruk": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Engine Tingkat Dasar": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Engine Pemula Tingkat Dasar": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Hidrolik Alat Berat": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Hidrolik Alat Berat Pemula": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Engine Alat Berat": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mekanik Engine Alat Berat Pemula": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Dump Truck": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Arsitek Lanskap Utama": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Arsitek Lanskap Madya": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Arsitek Lanskap Muda": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Manajer Lanskap Madya": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Manajer Lanskap Muda": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Lanskap (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Lanskap (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lanskap (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lanskap (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Juru Tanam": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Juru Tanam Pemula": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Taman": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Arsitek Lanskap Muda (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Arsitek Utama": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Arsitek Madya": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Asisten Arsitek": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Asisten Pemula Arsitek": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Lapangan Bidang Arsitektur (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Lapangan Bidang Arsitektur (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Juru Gambar Kepala Bidang Arsitektur": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Juru Gambar Arsitektur": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Juru Gambar Pemula Arsitektur": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Asisten Arsitek (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Madya Teknik Bangunan Air Limbah (SPALD)": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Bangunan Air Limbah (SPALD)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Setempat dan Terpusat) (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Setempat dan Terpusat) (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Teknik Dermaga": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Dermaga": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Dermaga": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Perawatan Fasilitas Pelabuhan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Perawatan Fasilitas Pelabuhan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Ahli Madya Teknik Bangunan Persampahan (TPA)": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Bangunan Persampahan (TPA)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Teknik Bendungan Besar": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Bendungan Besar": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Bendungan Besar": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Operasi dan Pemeliharaan Bendungan Tipe Urukan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Operasi dan Pemeliharaan Bendungan Tipe Urukan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Madya Pengawas Pelaksanaan Konstruksi Bangunan Sipil Pembangkit Listrik Tenaga Mini Hidro": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Inspektur Bendungan Urukan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Inspektur Bendungan Urukan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Bendungan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Bendungan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Mandor Pekerjaan Timbunan Tubuh Bendungan Tipe Urugan": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Desainer Interior Utama": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Desainer Interior Madya": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Desainer Interior Muda": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Madya Manajemen Interior": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Manajemen Interior": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Pekerjaan Interior (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Interior (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pekerjaan Interior (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pekerjaan Interior (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ilustrator Desain Interior": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Spesifikator Desain Interior": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Juru Gambar Desain Interior": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Juru Gambar Pemula Desain Interior": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Desainer Interior Muda (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Manajemen Interior (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Perencanaan Jaringan Drainase": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencanaan Jaringan Drainase": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Perencanaan Jaringan Drainase": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Lapangan Pekerjaan Drainase Perkotaan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Lapangan Pekerjaan Drainase Perkotaan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Drainase Perkotaan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Drainase Perkotaan (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Quantity Surveyor": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Quantity Surveyor": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Quantity Surveyor": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Estimator Biaya Bidang Konstruksi (Cost Estimator) (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Estimator Biaya Bidang Konstruksi (Cost Estimator) (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Quantity Surveyor (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Quantity Surveyor (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Ahli Utama Teknik Bangunan Gedung": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Bangunan Gedung": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Bangunan Gedung": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Manajer Pengelolaan Bangunan Gedung": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Penilai Laik Fungsi Bangunan Gedung": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Muda Perencana Beton Pracetak Untuk Struktur Bangunan Gedung": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Bangunan Gedung Hijau": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Bangunan Gedung Hijau": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Bangunan Gedung Hijau": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Analis Struktur Bangunan RISHA": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Bangunan Gedung (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Bangunan Gedung (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Gedung (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Gedung (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Gedung (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Juru Gambar Kepala Bidang Konstruksi": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Juru Gambar Konstruksi": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Juru Gambar Pemula Konstruksi": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Mandor Konstruksi Bangunan Gedung": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Aplikator Bangunan RISHA (Level 3)": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Aplikator Bangunan RISHA (Level 2)": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Kepala Tukang Bangunan Gedung": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Kepala Tukang Pasang Perancah dan Acuan/Cetakan Beton": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Pasang Perancah dan Acuan/Cetakan Beton": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Pasang Bata dan Plesteran": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Pasang Ubin/Keramik": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Besi Beton": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Kayu Konstruksi": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Cat Bangunan Gedung": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Pasang Water Proofing": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Pasang Rangka Baja Ringan": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Pasang Penutup Atap": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Pengelola Teknis Pembangunan Bangunan Gedung Negara": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Pengelola Rumah Susun": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Teknik Bangunan Gedung (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Survei Terestris": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Survei Terestris": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Survei Terestris": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Madya Hidrografi Lepas Pantai": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Hidrografi Pesisir": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Survei Pemetaan Udara": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Madya Sistem Informasi Geografis": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Spesialis SIG": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Kewilayahan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Kewilayahan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Manager Proyek Survei dan Pemetaan Wilayah": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Surveyor Terestris": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Surveyor Rekayasa": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Teknisi Survei Terestris": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Operator Utama Survei Terestris": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Operator Madya Survei Terestris": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Muda Survei Terestris": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Juru Ukur Konstruksi": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Utama Geologi Pekerjaan Konstruksi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Geologi Pekerjaan Konstruksi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Utama Geoteknik": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Geoteknik": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Geoteknik": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Teknisi Geoteknik (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Teknisi Geoteknik (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Sondir (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Sondir (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Teknisi Pengeboran Pengujian Tanah (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Pengeboran Pengujian Tanah (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Operator Alat Penyelidikan Tanah (Soil Investigation Operator)": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Alat Penyelidikan Tanah (Soil Investigation Operator)": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Muda Geoteknik (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Madya Grouting": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Grouting": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Lapangan Pekerjaan Grouting (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Operator Grouting": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Utama Kontrak Kerja Konstruksi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Kontrak Kerja Konstruksi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Utama Perencanaan Proyek Infrastruktur": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencanaan Proyek Infrastruktur": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Rekayasa Nilai (Value Engineering)": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Utama Teknik Irigasi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Irigasi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Irigasi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Teknik Perencanaan Irigasi Rawa": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Perencanaan Irigasi Rawa": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Utama Teknik Rawa": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Rawa": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Rawa": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Lapangan Pekerjaan Saluran Irigasi (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Saluran Irigasi (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Pengamat Irigasi": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Pemasangan Pintu Air (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Pemasangan Pintu Air (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Pengairan": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Teknik Jalan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Jalan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Jalan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Keselamatan Jalan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Keselamatan Jalan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Keselamatan Jalan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Lapangan Pekerjaan Jalan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Jalan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Jalan (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Mandor Pemeliharaan Jalan": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Madya Auditor Keselamatan Jalan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Auditor Keselamatan Jalan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengendali Pelaksanaan Pekerjaan Jalan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Uji Laik Fungsi Jalan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Ahli Muda Teknik Jalan (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Teknik Jalan Rel": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Jalan Rel": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Jalan Rel": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Pekerjaan Pengelasan Rel Kereta Api (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Pengelasan Rel Kereta Api (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Teknik Jembatan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Jembatan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Jembatan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Perencanaan Jembatan Rangka Baja": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencanaan Jembatan Rangka Baja": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Perencanaan Jembatan Rangka Baja": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Pemeliharaan Jembatan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Pemeliharaan Jembatan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pemeliharaan Jembatan (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Pengawas Lapangan Pekerjaan Jembatan Rangka Baja Panel Darurat": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja Panel Darurat": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Kepala Tukang Pasang/Perakit Jembatan Rangka Baja Panel Darurat": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Tukang Pasang/Perakit Jembatan Rangka Baja Panel Darurat": {
        "jenjang": 1,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Pengendali Pelaksanaan Pekerjaan Jembatan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Pemeriksaan Jembatan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Teknik Jembatan (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Keselamatan Konstruksi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Keselamatan Konstruksi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Keselamatan Konstruksi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama K3 Konstruksi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya K3 Konstruksi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda K3 Konstruksi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Manajer Keselamatan Kebakaran Bangunan Gedung": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Supervisor K3 Konstruksi (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Supervisor K3 Konstruksi (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Personil Keselamatan dan Kesehatan Kerja": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Petugas Keselamatan Konstruksi": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Petugas K3 Konstruksi": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Muda K3 Konstruksi (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Keselamatan Konstruksi (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Manager BIM Madya": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Manager BIM Muda": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Koordinator BIM": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Modeler BIM (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Modeler BIM (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Juru Gambar BIM": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Juru Gambar Pemula BIM": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Utama Material Jalan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Material Jalan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Material Jalan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Konstruksi, Fabrikasi, Sipil dan Struktur": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Teknisi Laboratorium Beton Aspal (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Teknisi Laboratorium Beton Aspal (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Laboratorium Beton Aspal (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Teknisi Laboratorium Tanah (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Teknisi Laboratorium Tanah (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Laboratorium Tanah (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Pelaksana Produksi Campuran Aspal Panas (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Produksi Campuran Aspal Panas (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Teknisi Laboratorium Beton (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Teknisi Laboratorium Beton (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Laboratorium Beton (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Pelaksanaan Pembongkaran Bangunan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Pelaksanaan Pembongkaran Bangunan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Pelaksanaan Pembongkaran Bangunan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Sistem Manajemen Mutu Konstruksi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Sistem Manajemen Mutu Konstruksi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Sistem Manajemen Mutu Konstruksi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Quality Engineer (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Quality Engineer (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pengendali Mutu Jalan dan Jembatan": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Quality Assurance Engineer (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Quality Assurance Engineer (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Asesor Badan Usaha Jasa Konstruksi": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Ahli Muda Perencana Wilayah Pesisir dan Pulau-Pulau Kecil": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Penyusunan Peraturan Zonasi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Penyusunan Peraturan Zonasi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Utama Perencana Tata Bangunan dan Lingkungan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencana Tata Bangunan dan Lingkungan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Utama Perencana Tata Ruang Wilayah dan Kota": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencana Tata Ruang Wilayah dan Kota": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Perencana Tata Ruang Wilayah dan Kota": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Penyusun Rencana Pengembangan Infrastruktur Wilayah": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Perencana Tata Ruang Wilayah dan Kota (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Teknik Plambing dan Pompa Mekanik": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Plambing dan Pompa Mekanik": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Plambing dan Pompa Mekanik": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Pekerjaan Plambing (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Plambing (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Teknik Plambing (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Teknik Plambing (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Mandor Plambing": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Asisten Pelaksana Plambing dan Pompa Mekanik": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Asisten Pemula Pelaksana Plambing dan Pompa Mekanik": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Utama Pengkaji Teknis Proteksi Kebakaran": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Pengkaji Teknis Proteksi Kebakaran": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Pengkaji Teknis Proteksi Kebakaran": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Teknisi Fire Alarm": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Teknik Pantai": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Pantai": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Pantai": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pelaksana Pekerjaan Pemeliharaan Sungai (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pekerjaan Pemeliharaan Sungai (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Teknisi Pengerukan": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Perencana Sistem Sanitasi Lingkungan (Air Limbah Pemukiman)": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencana Sistem Sanitasi Lingkungan (Air Limbah Pemukiman)": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Perencana Sistem Sanitasi Lingkungan (Air Limbah Pemukiman)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Fasilitator Teknis Dalam Pembangunan Sarana Sanitasi Berbasis Masyarakat (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Fasilitator Teknis Dalam Pembangunan Sarana Sanitasi Berbasis Masyarakat (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pengawas Operasi Instalasi Pengolahan Lumpur Tinja (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pengawas Operasi Perpipaan Air Limbah Domestik (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pengawas Operasi Instalasi Pengolahan Air Limbah Domestik (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Operasi Instalasi Pengolahan Lumpur Tinja (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Pelaksana Operasi Perpipaan Air Limbah Domestik (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Pelaksana Operasi Instalasi Pengolahan Air Limbah Domestik (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Asisten Pelaksana Instalasi Pengolahan Lumpur Tinja": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Asisten Pelaksana Perpipaan Air Limbah Domestik": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Asisten Pelaksana Instalasi Pengolahan Air Limbah Domestik": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Utama Teknik Air Minum": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Air Minum": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Air Minum": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Penanggulangan Kehilangan Air": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Penanggulangan Kehilangan Air": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Utama Deteksi Kebocoran dan Commissioning Jaringan Perpipaan SPAM": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Analis Commissioning IPA (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Analis Commissioning IPA (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Operasi dan Pemeliharaan Unit Pelayanan Air Minum (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Operasi dan Pemeliharaan Unit Pelayanan Air Minum (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Kepala Laboratorium Air Minum": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Analis Laboratorium Air Minum (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Analis Laboratorium Air Minum (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Supervisor Mekanikal Elektrikal Air Minum": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Pengawas Lapangan Konstruksi SPAM": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Lapangan Konstruksi SPAM": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Asisten Pelaksana Instalatur Unit Pelayanan Air Minum": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Asisten Pemula Pelaksana Instalatur Unit Pelayanan Air Minum": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Instalasi Pengolahan Air Minum": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Muda Teknik Air Minum (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Perencanaan Iluminasi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Pengawas Pekerjaan Iluminasi (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Iluminasi (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pekerjaan Iluminasi (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Asisten Pelaksana Iluminasi": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Muda Perencanaan Iluminasi (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Madya Launching Girder": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Launching Girder": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Lifting Engineer": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Lifting Supervisor": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Launching Gantry": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Launching Gantry": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Erection Girder": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Erection Girder": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Operator Gondola pada Bangunan Gedung": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Gondola pada Bangunan Gedung": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Launching Gantry": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Slinging and Rigging": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Operator Pemula Forklift": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Utama Teknik Lingkungan Bidang Jasa Konstruksi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Lingkungan Bidang Jasa Konstruksi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Teknik Lingkungan Bidang Jasa Konstruksi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Teknik Lingkungan Bidang Jasa Konstruksi (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Bidang Keahlian Teknik Mekanikal": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Bidang Keahlian Teknik Mekanikal": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Bidang Keahlian Teknik Mekanikal": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Elektrikal Konstruksi Bangunan Gedung": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Elektrikal Konstruksi Bangunan Gedung": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Elektrikal Konstruksi Bangunan Gedung": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Pekerjaan Mekanikal Bangunan Gedung (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Mekanikal Bangunan Gedung (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Mekanikal (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Mekanikal (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Teknisi Prestressing Equipment": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Teknisi Penyambung Pipa Polietilena Dengan Fusi Panas": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Juru Las": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Juru Las Pemula": {
        "jenjang": 2,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Asisten Mekanik Heating, Ventilation, dan Air Condition (HVAC)": {
        "jenjang": 3,
        "min_tahun": {
            "D1/SMK Plus": 0,
            "SMK": 3,
            "SMA": 4,
            "Pendidikan Dasar": 5
        }
    },
    "Ahli Muda Bidang Keahlian Teknik Mekanikal (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Elektrikal Konstruksi Bangunan Gedung (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Bidang Teknik Perpipaan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Bidang Teknik Perpipaan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Bidang Teknik Perpipaan": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Pekerjaan Teknik Perpipaan (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pekerjaan Teknik Perpipaan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Perpipaan (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Lapangan Pekerjaan Perpipaan (Level 4)": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Perencana Pengelolaan Sampah": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencana Pengelolaan Sampah": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Perencana Pengelolaan Sampah": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Pengawas Pengelolaan Tempat Pemrosesan Akhir (TPA) Sampah (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Pengawas Pengelolaan Tempat Pemrosesan Akhir (TPA) Sampah (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Pelaksana Pengelolaan TPA Sampah": {
        "jenjang": 4,
        "min_tahun": {
            "D2": 0,
            "D1/SMK Plus": 2,
            "SMK": 4,
            "SMA": 6
        }
    },
    "Ahli Utama Perencanaan Sistem Tata Udara": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Perencanaan Sistem Tata Udara": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Perencanaan Sistem Tata Udara": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Teknik Terowongan": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Teknik Terowongan": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Inspektur Terowongan": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Ahli Utama Pesawat Lift dan Eskalator": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Pesawat Lift dan Eskalator": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Pesawat Lift dan Eskalator": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Pesawat Lift dan Eskalator (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Bidang Keahlian Manajemen Konstruksi": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Bidang Keahlian Manajemen Konstruksi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Bidang Keahlian Manajemen Konstruksi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Utama Manajemen Proyek": {
        "jenjang": 9,
        "min_tahun": {
            "Doktor/Doktor Terapan/Pendidikan Spesialis_2": 0,
            "S2/S2 Terapan/Pendidikan Spesialis_1": 4,
            "Pendidikan Profesi": 7,
            "S1/S1 Terapan/D4 Terapan": 8
        }
    },
    "Ahli Madya Manajemen Proyek": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    },
    "Ahli Muda Manajemen Proyek": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Manajer Logistik Proyek": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Fasilitator Teknis Dalam Pembangunan Infrastruktur Berbasis Masyarakat (Level 6)": {
        "jenjang": 6,
        "min_tahun": {
            "S1/S1 Terapan/D4 Terapan": 0,
            "D3": 4,
            "D2": 8,
            "D1": 12
        }
    },
    "Fasilitator Teknis Dalam Pembangunan Infrastruktur Berbasis Masyarakat (Level 5)": {
        "jenjang": 5,
        "min_tahun": {
            "D3": 0,
            "D2": 4,
            "D1/SMK Plus": 8,
            "SMK": 10,
            "SMA": 12
        }
    },
    "Ahli Muda Bidang Keahlian Manajemen Konstruksi (Freshgraduate)": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Muda Perencanaan Iluminasi": {
        "jenjang": 7,
        "min_tahun": {
            "Pendidikan Profesi": 0,
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate)": 0,
            "S1/S1 Terapan/D4 Terapan": 2
        }
    },
    "Ahli Madya Perencanaan Iluminasi": {
        "jenjang": 8,
        "min_tahun": {
            "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1": 0,
            "Pendidikan Profesi": 5,
            "S1/S1 Terapan/D4 Terapan": 6
        }
    }
}


daftar_jabatan = [
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
    {"no": 14, "kode_jabatan": "SI101019", "klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah Dan Air Baku", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate)", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 15, "kode_jabatan": "ME061001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Manajer Alat Berat", "acuan_skkni": "SKKNI 206-2013"},
    {"no": 16, "kode_jabatan": "ME062011", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Scaffolding", "acuan_skkni": "SKKNI 46-2022"},
    {"no": 17, "kode_jabatan": "ME062009", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Scaffolding", "acuan_skkni": "SKKNI 46-2022"},
    {"no": 18, "kode_jabatan": "ME063094", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Scaffolding", "acuan_skkni": "SKKNI 46-2022"},
    {"no": 19, "kode_jabatan": "ME063095", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Scaffolding", "acuan_skkni": "SKKNI 46-2022"},
    {"no": 20, "kode_jabatan": "ME063096", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022"},
    {"no": 21, "kode_jabatan": "ME063097", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022"},
    {"no": 22, "kode_jabatan": "ME063098", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Motor Grader", "acuan_skkni": "SKK Khusus Reg.30-2022"},
    {"no": 23, "kode_jabatan": "ME063099", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Motor Grader", "acuan_skkni": "SKK Khusus Reg.30-2022"},
    {"no": 24, "kode_jabatan": "ME063100", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Wheel Excavator", "acuan_skkni": "SKKNI 91-2010"},
    {"no": 25, "kode_jabatan": "ME063101", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Wheel Excavator", "acuan_skkni": "SKKNI 91-2010"},
    {"no": 26, "kode_jabatan": "ME063102", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Tandem Roller", "acuan_skkni": "SKKNI 159-2019"},
    {"no": 27, "kode_jabatan": "ME063103", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Tandem Roller", "acuan_skkni": "SKKNI 159-2019"},
    {"no": 28, "kode_jabatan": "ME063104", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Vibrator Roller", "acuan_skkni": "SKKNI 168-2019"},
    {"no": 29, "kode_jabatan": "ME063105", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Vibrator Roller", "acuan_skkni": "SKKNI 168-2019"},
    {"no": 30, "kode_jabatan": "ME063106", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Pneumatic Tire Roller", "acuan_skkni": "SKKNI 164-2019"},
    {"no": 31, "kode_jabatan": "ME063107", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Pneumatic Tire Roller", "acuan_skkni": "SKKNI 164-2019"},
    {"no": 32, "kode_jabatan": "ME063014", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Wheel Loader", "acuan_skkni": "SKK Khusus Reg.33-2022"},
    {"no": 33, "kode_jabatan": "ME063108", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Wheel Loader", "acuan_skkni": "SKK Khusus Reg.33-2022"},
    {"no": 34, "kode_jabatan": "ME063109", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mobile Crane", "acuan_skkni": "SKKNI 180-2024"},
    {"no": 35, "kode_jabatan": "ME063110", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Mobile Crane", "acuan_skkni": "SKKNI 180-2024"},
    {"no": 36, "kode_jabatan": "ME063028", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Tower Crane", "acuan_skkni": "SKK Khusus Reg.43-2022"},
    {"no": 37, "kode_jabatan": "ME063111", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Tower Crane", "acuan_skkni": "SKK Khusus Reg.43-2022"},
    {"no": 38, "kode_jabatan": "ME063112", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Truck Mounted Crane", "acuan_skkni": "SKKNI 85-2021"},
    {"no": 39, "kode_jabatan": "ME063113", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Truck Mounted Crane", "acuan_skkni": "SKKNI 85-2021"},
    {"no": 40, "kode_jabatan": "ME063114", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Backhoe Loader", "acuan_skkni": "SKKNI 89-2010"},
    {"no": 41, "kode_jabatan": "ME063115", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Backhoe Loader", "acuan_skkni": "SKKNI 89-2010"},
    {"no": 42, "kode_jabatan": "ME063116", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Pile Drive Hammer", "acuan_skkni": "SKKNI 150-2019"},
    {"no": 43, "kode_jabatan": "ME063117", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Pile Drive Hammer", "acuan_skkni": "SKKNI 150-2019"},
    {"no": 44, "kode_jabatan": "ME063142", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Pompa Beton", "acuan_skkni": "SKKNI 381-2013"},
    {"no": 45, "kode_jabatan": "ME063118", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Pompa Beton", "acuan_skkni": "SKKNI 381-2013"},
    {"no": 46, "kode_jabatan": "ME063119", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bore Pile", "acuan_skkni": "SKKNI 111-2015"},
    {"no": 47, "kode_jabatan": "ME063120", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Bore Pile", "acuan_skkni": "SKKNI 111-2015"},
    {"no": 48, "kode_jabatan": "ME063121", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Pencampur Aspal", "acuan_skkni": "SKKNI 382-2013"},
    {"no": 49, "kode_jabatan": "ME063122", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Mesin Pencampur Aspal", "acuan_skkni": "SKKNI 382-2013"},
    {"no": 50, "kode_jabatan": "ME063123", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Penggelar Aspal", "acuan_skkni": "SKKNI 383-2013"},
    {"no": 51, "kode_jabatan": "ME063124", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Mesin Penggelar Aspal", "acuan_skkni": "SKKNI 383-2013"},
    {"no": 52, "kode_jabatan": "ME063125", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Pemecah Batu", "acuan_skkni": "SKK Khusus Reg.42-2022"},
    {"no": 53, "kode_jabatan": "ME063126", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Mesin Pemecah Batu", "acuan_skkni": "SKK Khusus Reg.42-2022"},
    {"no": 54, "kode_jabatan": "ME063127", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Mesin Penghampar Beton Semen (Concrete Paver Operator)", "acuan_skkni": "SKK Khusus Reg.41-2022"},
    {"no": 55, "kode_jabatan": "ME063128", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Mesin Penghampar Beton Semen (Concrete Paver Operator Pemula)", "acuan_skkni": "SKK Khusus Reg.41-2022"},
    {"no": 56, "kode_jabatan": "ME063012", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Cold Milling Machine", "acuan_skkni": "SKK Khusus Reg.40-2022"},
    {"no": 57, "kode_jabatan": "ME063129", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Cold Milling Machine", "acuan_skkni": "SKK Khusus Reg.40-2022"},
    {"no": 58, "kode_jabatan": "ME063029", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Batching Plant", "acuan_skkni": "SKK Khusus Reg.39-2022"},
    {"no": 59, "kode_jabatan": "ME063130", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Batching Plant", "acuan_skkni": "SKK Khusus Reg.39-2022"},
    {"no": 60, "kode_jabatan": "ME063131", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Hydrolic Hammer Breaker", "acuan_skkni": "SKKNI 158-2019"},
    {"no": 61, "kode_jabatan": "ME063132", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Hydrolic Hammer Breaker", "acuan_skkni": "SKKNI 158-2019"},
    {"no": 62, "kode_jabatan": "ME063133", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Ripper Tractor", "acuan_skkni": "SKKNI 165-2019"},
    {"no": 63, "kode_jabatan": "ME063134", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Ripper Tractor", "acuan_skkni": "SKKNI 165-2019"},
    {"no": 64, "kode_jabatan": "ME063135", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mekanik Tower Crane", "acuan_skkni": "SKK Khusus Reg.34-2022"},
    {"no": 65, "kode_jabatan": "ME063005", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mekanik Asphalt Mixing Plant (Asphalt Mixing Plant Mechanic)", "acuan_skkni": "SKKNI 326-2009"},
    {"no": 66, "kode_jabatan": "ME063002", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mekanik Kapal Keruk", "acuan_skkni": "SKKNI 70-2009"},
    {"no": 67, "kode_jabatan": "ME063141", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mekanik Engine Tingkat Dasar", "acuan_skkni": "SKKNI 382-2015"},
    {"no": 68, "kode_jabatan": "ME063136", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Mekanik Engine Pemula Tingkat Dasar", "acuan_skkni": "SKKNI 382-2015"},
    {"no": 69, "kode_jabatan": "ME063137", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mekanik Hidrolik Alat Berat", "acuan_skkni": "SKKNI 88-2010"},
    {"no": 70, "kode_jabatan": "ME063138", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Mekanik Hidrolik Alat Berat Pemula", "acuan_skkni": "SKKNI 88-2010"},
    {"no": 71, "kode_jabatan": "ME063140", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mekanik Engine Alat Berat", "acuan_skkni": "SKKNI 235-2023"},
    {"no": 72, "kode_jabatan": "ME063139", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Mekanik Engine Alat Berat Pemula", "acuan_skkni": "SKKNI 235-2023"},
    {"no": 73, "kode_jabatan": "ME063027", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Dump Truck", "acuan_skkni": "SKKNI 132-2015"},
    {"no": 74, "kode_jabatan": "AL011009", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Arsitek Lanskap Utama", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 75, "kode_jabatan": "AL011010", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Arsitek Lanskap Madya", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 76, "kode_jabatan": "AL011011", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Arsitek Lanskap Muda", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 77, "kode_jabatan": "AL011012", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Manajer Lanskap Madya", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 78, "kode_jabatan": "AL011013", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Manajer Lanskap Muda", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 79, "kode_jabatan": "AL012006", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Pengawas Lanskap (Level 6)", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 80, "kode_jabatan": "AL012007", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Lanskap (Level 5)", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 81, "kode_jabatan": "AL012008", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lanskap (Level 5)", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 82, "kode_jabatan": "AL012009", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lanskap (Level 4)", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 83, "kode_jabatan": "AL013004", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Juru Tanam", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 84, "kode_jabatan": "AL013005", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Juru Tanam Pemula", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 85, "kode_jabatan": "AL013006", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Taman", "acuan_skkni": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"no": 86, "kode_jabatan": "AL011008", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Arsitek Lanskap Muda (Freshgraduate)", "acuan_skkni": "SKKNI 209-2013"},
    {"no": 87, "kode_jabatan": "AR011001", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Arsitek Utama", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 88, "kode_jabatan": "AR011002", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Arsitek Madya", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 89, "kode_jabatan": "AR011004", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Asisten Arsitek", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 90, "kode_jabatan": "AR012001", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Asisten Pemula Arsitek", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 91, "kode_jabatan": "AR012003", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Lapangan Bidang Arsitektur (Level 6)", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 92, "kode_jabatan": "AR012004", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Lapangan Bidang Arsitektur (Level 5)", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 93, "kode_jabatan": "AR012005", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Juru Gambar Kepala Bidang Arsitektur", "acuan_skkni": "SKK-Khusus 36-2022"},
    {"no": 94, "kode_jabatan": "AR013003", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Juru Gambar Arsitektur", "acuan_skkni": "SKK-Khusus 36-2022"},
    {"no": 95, "kode_jabatan": "AR013004", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Juru Gambar Pemula Arsitektur", "acuan_skkni": "SKK-Khusus 36-2022"},
    {"no": 96, "kode_jabatan": "AR011005", "klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Asisten Arsitek (Freshgraduate)", "acuan_skkni": "SKKNI 196-2021"},
    {"no": 97, "kode_jabatan": "SI121102", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Bangunan Air Limbah (SPALD)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 98, "kode_jabatan": "SI121001", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Bangunan Air Limbah (SPALD)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 99, "kode_jabatan": "SI122003", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Setempat dan Terpusat) (Level 5)", "acuan_skkni": "SKKNI 312-2009"},
    {"no": 100, "kode_jabatan": "SI122004", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Setempat dan Terpusat) (Level 4)", "acuan_skkni": "SKKNI 312-2009"},
    {"no": 101, "kode_jabatan": "SI191004", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Dermaga", "acuan_skkni": "SKKNI 320–2016"},
    {"no": 102, "kode_jabatan": "SI191006", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Dermaga", "acuan_skkni": "SKKNI 320–2016"},
    {"no": 103, "kode_jabatan": "SI191005", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Dermaga", "acuan_skkni": "SKKNI 320–2016"},
    {"no": 104, "kode_jabatan": "SI192004", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Perawatan Fasilitas Pelabuhan (Level 6)", "acuan_skkni": "SKKNI 234 – 2019"},
    {"no": 105, "kode_jabatan": "SI192005", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Perawatan Fasilitas Pelabuhan (Level 5)", "acuan_skkni": "SKKNI 234 – 2019"},
    {"no": 106, "kode_jabatan": "SI131004", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Persampahan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Bangunan Persampahan (TPA)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 107, "kode_jabatan": "SI131003", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Persampahan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Bangunan Persampahan (TPA)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 108, "kode_jabatan": "SI132008", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Persampahan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 5)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 109, "kode_jabatan": "SI132009", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Persampahan", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 4)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 110, "kode_jabatan": "SI071012", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Bendungan Besar", "acuan_skkni": "SKKNI 308–2016; SKKNI 124-2021"},
    {"no": 111, "kode_jabatan": "SI071013", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Bendungan Besar", "acuan_skkni": "SKKNI 308–2016; SKKNI 124-2021"},
    {"no": 112, "kode_jabatan": "SI071014", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Bendungan Besar", "acuan_skkni": "SKKNI 308–2016; SKKNI 124-2021"},
    {"no": 113, "kode_jabatan": "SI071015", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Operasi dan Pemeliharaan Bendungan Tipe Urukan", "acuan_skkni": "SKKNI 375-2013"},
    {"no": 114, "kode_jabatan": "SI071016", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Operasi dan Pemeliharaan Bendungan Tipe Urukan", "acuan_skkni": "SKKNI 375-2013"},
    {"no": 115, "kode_jabatan": "SI071005", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Pengawas Pelaksanaan Konstruksi Bangunan Sipil Pembangkit Listrik Tenaga Mini Hidro", "acuan_skkni": "SKKNI 335-2013"},
    {"no": 116, "kode_jabatan": "SI072009", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Inspektur Bendungan Urukan (Level 6)", "acuan_skkni": "SKKNI 68-2009"},
    {"no": 117, "kode_jabatan": "SI072010", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Inspektur Bendungan Urukan (Level 5)", "acuan_skkni": "SKKNI 68-2009"},
    {"no": 118, "kode_jabatan": "SI072011", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Bendungan (Level 6)", "acuan_skkni": "SKKNI 81-2015; SKK-Khusus Reg.26-2022"},
    {"no": 119, "kode_jabatan": "SI072012", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Bendungan (Level 5)", "acuan_skkni": "SKKNI 81-2015; SKK-Khusus Reg.26-2022"},
    {"no": 120, "kode_jabatan": "SI073001", "klasifikasi": "SIPIL", "subklasifikasi": "Bendung dan Bendungan", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mandor Pekerjaan Timbunan Tubuh Bendungan Tipe Urugan", "acuan_skkni": "SKKNI 180-2019"},
    {"no": 121, "kode_jabatan": "AL031005", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Desainer Interior Utama", "acuan_skkni": "SKKNI 17-2024; SKKNI 308 – 2013; SKKNI 17-2023"},
    {"no": 122, "kode_jabatan": "AL031006", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Desainer Interior Madya", "acuan_skkni": "SKKNI 17-2024; SKKNI 308 – 2013; SKKNI 17-2023"},
    {"no": 123, "kode_jabatan": "AL031007", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Desainer Interior Muda", "acuan_skkni": "SKKNI 17-2024; SKKNI 308 – 2013; SKKNI 17-2023"},
    {"no": 124, "kode_jabatan": "AL031008", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Manajemen Interior", "acuan_skkni": "SKKNI 17-2024; SKKNI 308 – 2013; SKKNI 17-2023"},
    {"no": 125, "kode_jabatan": "AL031009", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Manajemen Interior", "acuan_skkni": "SKKNI 17-2024; SKKNI 308 – 2013; SKKNI 17-2023"},
    {"no": 126, "kode_jabatan": "AL032005", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pekerjaan Interior (Level 6)", "acuan_skkni": "SKKNI 342-2013"},
    {"no": 127, "kode_jabatan": "AL032006", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pekerjaan Interior (Level 5)", "acuan_skkni": "SKKNI 342-2013"},
    {"no": 128, "kode_jabatan": "AL032007", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Pekerjaan Interior (Level 5)", "acuan_skkni": "SKKNI 308-2013"},
    {"no": 129, "kode_jabatan": "AL032008", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Pekerjaan Interior (Level 4)", "acuan_skkni": "SKKNI 308-2013"},
    {"no": 130, "kode_jabatan": "AL032009", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Ilustrator Desain Interior", "acuan_skkni": "SKKNI 17-2024; SKKNI 17-2023"},
    {"no": 131, "kode_jabatan": "AL032010", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Spesifikator Desain Interior", "acuan_skkni": "SKKNI 17-2024; SKKNI 17-2023"},
    {"no": 132, "kode_jabatan": "AL033001", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Juru Gambar Desain Interior", "acuan_skkni": "SKKNI 17-2024; SKKNI 17-2023"},
    {"no": 133, "kode_jabatan": "AL033002", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Juru Gambar Pemula Desain Interior", "acuan_skkni": "SKKNI 17-2024; SKKNI 17-2023"},
    {"no": 134, "kode_jabatan": "AL031010", "klasifikasi": "ARSITEKTUR LANSKAP, ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Desainer Interior Muda (Freshgraduate)", "acuan_skkni": "SKKNI 17-2024; SKKNI 17-2023; SKKNI 308-2013"},
    {"no": 135, "kode_jabatan": "AL031011", "klasifikasi": "ARSITEKTUR LANSKAP, ILUMINASI, DESAIN INTERIOR", "subklasifikasi": "Desain Interior", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Manajemen Interior (Freshgraduate)", "acuan_skkni": "SKKNI 17-2024; SKKNI 17-2023; SKKNI 308-2013"},
    {"no": 136, "kode_jabatan": "SI141004", "klasifikasi": "SIPIL", "subklasifikasi": "Drainase Perkotaan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencanaan Jaringan Drainase", "acuan_skkni": "SKKNI 86-2015"},
    {"no": 137, "kode_jabatan": "SI141006", "klasifikasi": "SIPIL", "subklasifikasi": "Drainase Perkotaan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencanaan Jaringan Drainase", "acuan_skkni": "SKKNI 86-2015"},
    {"no": 138, "kode_jabatan": "SI141005", "klasifikasi": "SIPIL", "subklasifikasi": "Drainase Perkotaan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencanaan Jaringan Drainase", "acuan_skkni": "SKKNI 86-2015"},
    {"no": 139, "kode_jabatan": "SI142004", "klasifikasi": "SIPIL", "subklasifikasi": "Drainase Perkotaan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Lapangan Pekerjaan Drainase Perkotaan (Level 6)", "acuan_skkni": "SKKNI 95-2015"},
    {"no": 140, "kode_jabatan": "SI142005", "klasifikasi": "SIPIL", "subklasifikasi": "Drainase Perkotaan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Lapangan Pekerjaan Drainase Perkotaan (Level 5)", "acuan_skkni": "SKKNI 95-2015"},
    {"no": 141, "kode_jabatan": "SI142006", "klasifikasi": "SIPIL", "subklasifikasi": "Drainase Perkotaan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Drainase Perkotaan (Level 5)", "acuan_skkni": "SKKNI 197 – 2013"},
    {"no": 142, "kode_jabatan": "SI142007", "klasifikasi": "SIPIL", "subklasifikasi": "Drainase Perkotaan", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Drainase Perkotaan (Level 4)", "acuan_skkni": "SKKNI 197 – 2013"},
    {"no": 143, "kode_jabatan": "MP051005", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Quantity Surveyor", "acuan_skkni": "SKKNI 6-2011"},
    {"no": 144, "kode_jabatan": "MP051004", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Quantity Surveyor", "acuan_skkni": "SKKNI 6-2011"},
    {"no": 145, "kode_jabatan": "MP051003", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Quantity Surveyor", "acuan_skkni": "SKKNI 6-2011"},
    {"no": 146, "kode_jabatan": "MP052010", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Estimator Biaya Bidang Konstruksi (Cost Estimator) (Level 6)", "acuan_skkni": "SKKNI 51-2022"},
    {"no": 147, "kode_jabatan": "MP052011", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Estimator Biaya Bidang Konstruksi (Cost Estimator) (Level 5)", "acuan_skkni": "SKKNI 51-2022"},
    {"no": 148, "kode_jabatan": "MP052012", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Quantity Surveyor (Level 6)", "acuan_skkni": "SKKNI 6-2011"},
    {"no": 149, "kode_jabatan": "MP052013", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Estimasi Biaya Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Quantity Surveyor (Level 5)", "acuan_skkni": "SKKNI 6-2011"},
    {"no": 150, "kode_jabatan": "SI011031", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Bangunan Gedung", "acuan_skkni": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"no": 151, "kode_jabatan": "SI011032", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Bangunan Gedung", "acuan_skkni": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"no": 152, "kode_jabatan": "SI011033", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Bangunan Gedung", "acuan_skkni": "SKKNI 192-2016; SKKNI 255-2019; SKKNI 106-2015"},
    {"no": 153, "kode_jabatan": "SI011034", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Manajer Pengelolaan Bangunan Gedung", "acuan_skkni": "SKKNI 115-2015; SKKNI 46-2015"},
    {"no": 154, "kode_jabatan": "SI011035", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Penilai Laik Fungsi Bangunan Gedung", "acuan_skkni": "SKKNI 113-2015; SKKNI 7-2024"},
    {"no": 155, "kode_jabatan": "SI011036", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencana Beton Pracetak Untuk Struktur Bangunan Gedung", "acuan_skkni": "SKKNI 160-2024"},
    {"no": 156, "kode_jabatan": "SI011042", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Bangunan Gedung Hijau", "acuan_skkni": "SKKNI 2-2023"},
    {"no": 157, "kode_jabatan": "SI011041", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Bangunan Gedung Hijau", "acuan_skkni": "SKKNI 2-2023"},
    {"no": 158, "kode_jabatan": "SI011040", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bangunan Gedung Hijau", "acuan_skkni": "SKKNI 2-2023"},
    {"no": 159, "kode_jabatan": "SI012028", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Analis Struktur Bangunan RISHA", "acuan_skkni": "SKKNI 221-2018"},
    {"no": 160, "kode_jabatan": "SI012029", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pekerjaan Bangunan Gedung (Level 6)", "acuan_skkni": "SKKNI 340–2013"},
    {"no": 161, "kode_jabatan": "SI012030", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pekerjaan Bangunan Gedung (Level 5)", "acuan_skkni": "SKKNI 340–2013"},
    {"no": 162, "kode_jabatan": "SI012031", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Gedung (Level 6)", "acuan_skkni": "SKKNI 193-2021; SKKNI 108-2015"},
    {"no": 163, "kode_jabatan": "SI012032", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Gedung (Level 5)", "acuan_skkni": "SKKNI 193-2021; SKKNI 108-2015"},
    {"no": 164, "kode_jabatan": "SI012033", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Gedung (Level 4)", "acuan_skkni": "SKKNI 193-2021; SKKNI 108-2015"},
    {"no": 165, "kode_jabatan": "SI012034", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Juru Gambar Kepala Bidang Konstruksi", "acuan_skkni": "SKKNI 13-2024; SKKNI 33-2021; SKKNI 327-2009"},
    {"no": 166, "kode_jabatan": "SI013060", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Juru Gambar Konstruksi", "acuan_skkni": "SKKNI 13-2024; SKKNI 33-2021; SKKNI 327-2009"},
    {"no": 167, "kode_jabatan": "SI013061", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Juru Gambar Pemula Konstruksi", "acuan_skkni": "SKKNI 13-2024; SKKNI 33-2021; SKKNI 327-2009"},
    {"no": 168, "kode_jabatan": "SI013062", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mandor Konstruksi Bangunan Gedung", "acuan_skkni": "SKK-Khusus Reg.32-2022"},
    {"no": 169, "kode_jabatan": "SI013063", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Aplikator Bangunan RISHA (Level 3)", "acuan_skkni": "SKKNI 221-2018"},
    {"no": 170, "kode_jabatan": "SI013064", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Aplikator Bangunan RISHA (Level 2)", "acuan_skkni": "SKKNI 221-2018"},
    {"no": 171, "kode_jabatan": "SI013065", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Kepala Tukang Bangunan Gedung", "acuan_skkni": "SKKNI 31–2014"},
    {"no": 172, "kode_jabatan": "SI013066", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Kepala Tukang Pasang Perancah dan Acuan/Cetakan Beton", "acuan_skkni": "SKKNI 54–2015"},
    {"no": 173, "kode_jabatan": "SI013067", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Pasang Perancah dan Acuan/Cetakan Beton", "acuan_skkni": "SKKNI 54–2015"},
    {"no": 174, "kode_jabatan": "SI013068", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Pasang Bata dan Plesteran", "acuan_skkni": "SKKNI 317–2016;SKKNI 307–2016"},
    {"no": 175, "kode_jabatan": "SI013069", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Pasang Ubin/Keramik", "acuan_skkni": "SKKNI 309–2016"},
    {"no": 176, "kode_jabatan": "SI013070", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Besi Beton", "acuan_skkni": "SKKNI 319–2016"},
    {"no": 177, "kode_jabatan": "SI013071", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Kayu Konstruksi", "acuan_skkni": "SKKNI 85–2015"},
    {"no": 178, "kode_jabatan": "SI013072", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Cat Bangunan Gedung", "acuan_skkni": "SKKNI 310–2016"},
    {"no": 179, "kode_jabatan": "SI013073", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Pasang Water Proofing", "acuan_skkni": "SKKNI 377-2013"},
    {"no": 180, "kode_jabatan": "SI013074", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Pasang Rangka Baja Ringan", "acuan_skkni": "SKKNI 184–2016"},
    {"no": 181, "kode_jabatan": "SI013075", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Pasang Penutup Atap", "acuan_skkni": "SKKNI 21-2024; SKKNI 16-2023"},
    {"no": 182, "kode_jabatan": "SI011037", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Pengelola Teknis Pembangunan Bangunan Gedung Negara", "acuan_skkni": "SKK-Khusus Reg.3-2020"},
    {"no": 183, "kode_jabatan": "SI011038", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Pengelola Rumah Susun", "acuan_skkni": "SKKNI 255-2019; SKKNI 115-2015"},
    {"no": 184, "kode_jabatan": "SI011039", "klasifikasi": "SIPIL", "subklasifikasi": "Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Bangunan Gedung (Freshgraduate)", "acuan_skkni": "SKKNI 192-2016"},
    {"no": 185, "kode_jabatan": "SI161015", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Survei Terestris", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 186, "kode_jabatan": "SI161016", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Survei Terestris", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 187, "kode_jabatan": "SI161017", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Survei Terestris", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 188, "kode_jabatan": "SI161011", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Hidrografi Lepas Pantai", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 189, "kode_jabatan": "SI161023", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Hidrografi Pesisir", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 190, "kode_jabatan": "SI161008", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Survei Pemetaan Udara", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 191, "kode_jabatan": "SI161018", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Sistem Informasi Geografis", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 192, "kode_jabatan": "SI161019", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Spesialis SIG", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 193, "kode_jabatan": "SI161020", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Kewilayahan", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 194, "kode_jabatan": "SI161021", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Kewilayahan", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 195, "kode_jabatan": "SI161022", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Manager Proyek Survei dan Pemetaan Wilayah", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 196, "kode_jabatan": "SI162006", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Surveyor Terestris", "acuan_skkni": "SKKNI 172-2020; SKKNI 38-2019"},
    {"no": 197, "kode_jabatan": "SI162005", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Surveyor Rekayasa", "acuan_skkni": "SKKNI 172-2020; SKKNI 38-2019"},
    {"no": 198, "kode_jabatan": "SI162007", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Survei Terestris", "acuan_skkni": "SKKNI 172-2020; SKKNI 38-2019"},
    {"no": 199, "kode_jabatan": "SI162003", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Operator Utama Survei Terestris", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 200, "kode_jabatan": "SI163010", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Madya Survei Terestris", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 201, "kode_jabatan": "SI163009", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Muda Survei Terestris", "acuan_skkni": "SKKNI 172-2020"},
    {"no": 202, "kode_jabatan": "SI163008", "klasifikasi": "SIPIL", "subklasifikasi": "Geodesi", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Juru Ukur Konstruksi", "acuan_skkni": "SKKNI 158-2024"},
    {"no": 203, "kode_jabatan": "SI151012", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Geologi Pekerjaan Konstruksi", "acuan_skkni": "SKKNI 149-2019"},
    {"no": 204, "kode_jabatan": "SI151017", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Geologi Pekerjaan Konstruksi", "acuan_skkni": "SKKNI 149-2019"},
    {"no": 205, "kode_jabatan": "SI151013", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Geoteknik", "acuan_skkni": "SKKNI 305–2016"},
    {"no": 206, "kode_jabatan": "SI151014", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Geoteknik", "acuan_skkni": "SKKNI 305–2016"},
    {"no": 207, "kode_jabatan": "SI151015", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Geoteknik", "acuan_skkni": "SKKNI 305–2016"},
    {"no": 208, "kode_jabatan": "SI152005", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Teknisi Geoteknik (Level 6)", "acuan_skkni": "SKKNI 181–2009"},
    {"no": 209, "kode_jabatan": "SI152006", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Geoteknik (Level 5)", "acuan_skkni": "SKKNI 181–2009"},
    {"no": 210, "kode_jabatan": "SI152007", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Sondir (Level 5)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 211, "kode_jabatan": "SI152008", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Sondir (Level 4)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 212, "kode_jabatan": "SI152009", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Pengeboran Pengujian Tanah (Level 5)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 213, "kode_jabatan": "SI152010", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Pengeboran Pengujian Tanah (Level 4)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 214, "kode_jabatan": "SI153003", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Alat Penyelidikan Tanah (Soil Investigation Operator)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 215, "kode_jabatan": "SI153004", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik dan Pondasi", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Alat Penyelidikan Tanah (Soil Investigation Operator)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 216, "kode_jabatan": "SI151016", "klasifikasi": "SIPIL", "subklasifikasi": "Geoteknik Dan Pondasi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Geoteknik (Freshgraduate)", "acuan_skkni": "SKKNI 305–2016"},
    {"no": 217, "kode_jabatan": "SI231003", "klasifikasi": "SIPIL", "subklasifikasi": "Grouting", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Grouting", "acuan_skkni": "SKKNI 17-2023"},
    {"no": 218, "kode_jabatan": "SI231002", "klasifikasi": "SIPIL", "subklasifikasi": "Grouting", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Grouting", "acuan_skkni": "SKKNI 17-2023"},
    {"no": 219, "kode_jabatan": "SI232003", "klasifikasi": "SIPIL", "subklasifikasi": "Grouting", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Grouting (Level 5)", "acuan_skkni": "SKKNI 17-2023"},
    {"no": 220, "kode_jabatan": "SI233003", "klasifikasi": "SIPIL", "subklasifikasi": "Grouting", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Grouting", "acuan_skkni": "SKKNI 17-2023"},
    {"no": 221, "kode_jabatan": "MP031003", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Hukum Kontrak Konstruksi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Kontrak Kerja Konstruksi", "acuan_skkni": "SKKNI 88-2015"},
    {"no": 222, "kode_jabatan": "MP031002", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Hukum Kontrak Konstruksi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Kontrak Kerja Konstruksi", "acuan_skkni": "SKKNI 88-2015"},
    {"no": 223, "kode_jabatan": "SR011006", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Investasi Infrastruktur", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencanaan Proyek Infrastruktur", "acuan_skkni": "SKKNI 372-2013"},
    {"no": 224, "kode_jabatan": "SR011007", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Investasi Infrastruktur", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencanaan Proyek Infrastruktur", "acuan_skkni": "SKKNI 372-2013"},
    {"no": 225, "kode_jabatan": "SR011002", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Investasi Infrastruktur", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Rekayasa Nilai (Value Engineering)", "acuan_skkni": "SKKNl 159-2015"},
    {"no": 226, "kode_jabatan": "SI081014", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Irigasi", "acuan_skkni": "SKKNI 337-2013; SKKNI 53-2015"},
    {"no": 227, "kode_jabatan": "SI081015", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Irigasi", "acuan_skkni": "SKKNI 337-2013; SKKNI 53-2015"},
    {"no": 228, "kode_jabatan": "SI081016", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Irigasi", "acuan_skkni": "SKKNI 337-2013; SKKNI 53-2015"},
    {"no": 229, "kode_jabatan": "SI081017", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Perencanaan Irigasi Rawa", "acuan_skkni": "SKKNI 51-2015"},
    {"no": 230, "kode_jabatan": "SI081019", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Perencanaan Irigasi Rawa", "acuan_skkni": "SKKNI 51-2015"},
    {"no": 231, "kode_jabatan": "SI081018", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Rawa", "acuan_skkni": "SKKNI 169-2019"},
    {"no": 232, "kode_jabatan": "SI081021", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Rawa", "acuan_skkni": "SKKNI 169-2019"},
    {"no": 233, "kode_jabatan": "SI081020", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Rawa", "acuan_skkni": "SKKNI 169-2019"},
    {"no": 234, "kode_jabatan": "SI082014", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Saluran Irigasi (Level 5)", "acuan_skkni": "SKKNI 378–2013; SKKNI 55–2022"},
    {"no": 235, "kode_jabatan": "SI082015", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Saluran Irigasi (Level 4)", "acuan_skkni": "SKKNI 378–2013; SKKNI 55–2022"},
    {"no": 236, "kode_jabatan": "SI082013", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengamat Irigasi", "acuan_skkni": "SKK-Khusus Reg. 01-2022"},
    {"no": 237, "kode_jabatan": "SI082016", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Pemasangan Pintu Air (Level 6)", "acuan_skkni": "SKKNI 183-2009"},
    {"no": 238, "kode_jabatan": "SI082017", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Pemasangan Pintu Air (Level 5)", "acuan_skkni": "SKKNI 183-2009"},
    {"no": 239, "kode_jabatan": "SI082018", "klasifikasi": "SIPIL", "subklasifikasi": "Irigasi dan Rawa", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Pengairan", "acuan_skkni": "SKK-Khusus Reg. 02-2022"},
    {"no": 240, "kode_jabatan": "SI031022", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Jalan", "acuan_skkni": "SKKNI 126-2021"},
    {"no": 241, "kode_jabatan": "SI031023", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Jalan", "acuan_skkni": "SKKNI 126-2021"},
    {"no": 242, "kode_jabatan": "SI031024", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Jalan", "acuan_skkni": "SKKNI 126-2021"},
    {"no": 243, "kode_jabatan": "SI031025", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan Jalan", "acuan_skkni": "SKKNI 324–2013"},
    {"no": 244, "kode_jabatan": "SI031026", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Keselamatan Jalan", "acuan_skkni": "SKKNI 324–2013"},
    {"no": 245, "kode_jabatan": "SI031027", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Keselamatan Jalan", "acuan_skkni": "SKKNI 324–2013"},
    {"no": 246, "kode_jabatan": "SI032023", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Jalan (Level 6)", "acuan_skkni": "SKKNI 145–2024; SKKNI 192-2021; SKKNI 57-2021"},
    {"no": 247, "kode_jabatan": "SI032024", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Jalan (Level 5)", "acuan_skkni": "SKKNI 145–2024; SKKNI 192-2021; SKKNI 57-2021"},
    {"no": 248, "kode_jabatan": "SI032025", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Jalan (Level 4)", "acuan_skkni": "SKKNI 145–2024; SKKNI 192-2021; SKKNI 57-2021"},
    {"no": 249, "kode_jabatan": "SI033016", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mandor Pemeliharaan Jalan", "acuan_skkni": "SKKNI 217-2023"},
    {"no": 250, "kode_jabatan": "SI031031", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Auditor Keselamatan Jalan", "acuan_skkni": "SKK-Khusus Reg. 12- 2025"},
    {"no": 251, "kode_jabatan": "SI031030", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Auditor Keselamatan Jalan", "acuan_skkni": "SKK-Khusus Reg. 12- 2025"},
    {"no": 252, "kode_jabatan": "SI031028", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Pengendali Pelaksanaan Pekerjaan Jalan", "acuan_skkni": "SKKNI 371-2013"},
    {"no": 253, "kode_jabatan": "SI032026", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Uji Laik Fungsi Jalan (Level 6)", "acuan_skkni": "SKK Khusus Reg.13-2024"},
    {"no": 254, "kode_jabatan": "SI031029", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Jalan (Freshgraduate)", "acuan_skkni": "SKKNI 126-2021"},
    {"no": 255, "kode_jabatan": "SI171008", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan Rel", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Jalan Rel", "acuan_skkni": "SKKNI 332-2013; SKKNI 388-2013"},
    {"no": 256, "kode_jabatan": "SI171009", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan Rel", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Jalan Rel", "acuan_skkni": "SKKNI 332-2013; SKKNI 388-2013"},
    {"no": 257, "kode_jabatan": "SI171010", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan Rel", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Jalan Rel", "acuan_skkni": "SKKNI 332-2013; SKKNI 388-2013"},
    {"no": 258, "kode_jabatan": "SI172006", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan Rel", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pekerjaan Pengelasan Rel Kereta Api (Level 6)", "acuan_skkni": "SKKNI 54 – 2021"},
    {"no": 259, "kode_jabatan": "SI172007", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan Rel", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pekerjaan Pengelasan Rel Kereta Api (Level 5)", "acuan_skkni": "SKKNI 54 – 2021"},
    {"no": 260, "kode_jabatan": "SI172008", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan Rel", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel (Level 5)", "acuan_skkni": "SKKNI 194-2013"},
    {"no": 261, "kode_jabatan": "SI172009", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan Rel", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel (Level 4)", "acuan_skkni": "SKKNI 194-2013"},
    {"no": 262, "kode_jabatan": "SI041023", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Jembatan", "acuan_skkni": "SKKNI 84–2021"},
    {"no": 263, "kode_jabatan": "SI041024", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Jembatan", "acuan_skkni": "SKKNI 84–2021"},
    {"no": 264, "kode_jabatan": "SI041025", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Jembatan", "acuan_skkni": "SKKNI 84–2021"},
    {"no": 265, "kode_jabatan": "SI041026", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencanaan Jembatan Rangka Baja", "acuan_skkni": "SKKNI 130-2015"},
    {"no": 266, "kode_jabatan": "SI041030", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencanaan Jembatan Rangka Baja", "acuan_skkni": "SKKNI 130-2015"},
    {"no": 267, "kode_jabatan": "SI041029", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencanaan Jembatan Rangka Baja", "acuan_skkni": "SKKNI 130-2015"},
    {"no": 268, "kode_jabatan": "SI042014", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Pemeliharaan Jembatan (Level 6)", "acuan_skkni": "SKKNI 195-2015"},
    {"no": 269, "kode_jabatan": "SI042015", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Pemeliharaan Jembatan (Level 5)", "acuan_skkni": "SKKNI 195-2015"},
    {"no": 270, "kode_jabatan": "SI042016", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Pemeliharaan Jembatan (Level 4)", "acuan_skkni": "SKKNI 195-2015"},
    {"no": 271, "kode_jabatan": "SI042017", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Lapangan Pekerjaan Jembatan Rangka Baja Panel Darurat", "acuan_skkni": "SKKNI 16-2023"},
    {"no": 272, "kode_jabatan": "SI042018", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja Panel Darurat", "acuan_skkni": "SKKNI 16-2023"},
    {"no": 273, "kode_jabatan": "SI042019", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja (Level 6)", "acuan_skkni": "SKKNI 316–2009"},
    {"no": 274, "kode_jabatan": "SI042020", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja (Level 5)", "acuan_skkni": "SKKNI 316–2009"},
    {"no": 275, "kode_jabatan": "SI043003", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Kepala Tukang Pasang/Perakit Jembatan Rangka Baja Panel Darurat", "acuan_skkni": "SKKNI 16-2023"},
    {"no": 276, "kode_jabatan": "SI043004", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Operator", "jenjang": 1, "nama_jabatan": "Tukang Pasang/Perakit Jembatan Rangka Baja Panel Darurat", "acuan_skkni": "SKKNI 16-2023"},
    {"no": 277, "kode_jabatan": "SI041013", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Pengendali Pelaksanaan Pekerjaan Jembatan", "acuan_skkni": "SKKNI 371-2013"},
    {"no": 278, "kode_jabatan": "SI041027", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Pemeriksaan Jembatan", "acuan_skkni": "SKKNI 84-2021; SKKNI 51-2022"},
    {"no": 279, "kode_jabatan": "SI041028", "klasifikasi": "SIPIL", "subklasifikasi": "Jembatan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Jembatan (Freshgraduate)", "acuan_skkni": "SKKNI 84-2021"},
    {"no": 280, "kode_jabatan": "MP011006", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan Konstruksi", "acuan_skkni": "SKKNI 60-2022"},
    {"no": 281, "kode_jabatan": "MP011005", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Keselamatan Konstruksi", "acuan_skkni": "SKKNI 60-2022"},
    {"no": 282, "kode_jabatan": "MP011004", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Keselamatan Konstruksi", "acuan_skkni": "SKKNI 60-2022"},
    {"no": 283, "kode_jabatan": "MP011003", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama K3 Konstruksi", "acuan_skkni": "SKKNI 350-2014"},
    {"no": 284, "kode_jabatan": "MP011002", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya K3 Konstruksi", "acuan_skkni": "SKKNI 350-2014"},
    {"no": 285, "kode_jabatan": "MP011001", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda K3 Konstruksi", "acuan_skkni": "SKKNI 350-2014"},
    {"no": 286, "kode_jabatan": "MP011009", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Manajer Keselamatan Kebakaran Bangunan Gedung", "acuan_skkni": "SKKNI 136-2023"},
    {"no": 287, "kode_jabatan": "MP012004", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Supervisor K3 Konstruksi (Level 6)", "acuan_skkni": "SKKNI 350-2014"},
    {"no": 288, "kode_jabatan": "MP012005", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Supervisor K3 Konstruksi (Level 5)", "acuan_skkni": "SKKNI 350-2014"},
    {"no": 289, "kode_jabatan": "MP012001", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Personil Keselamatan dan Kesehatan Kerja", "acuan_skkni": "SKKNI 38-2019"},
    {"no": 290, "kode_jabatan": "MP013002", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Petugas Keselamatan Konstruksi", "acuan_skkni": "SKKNI 48-2022"},
    {"no": 291, "kode_jabatan": "MP013003", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Petugas K3 Konstruksi", "acuan_skkni": "SKKNI 13-2024"},
    {"no": 292, "kode_jabatan": "MP011007", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda K3 Konstruksi (Freshgraduate)", "acuan_skkni": "SKKNI 350–2014"},
    {"no": 293, "kode_jabatan": "MP011008", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Keselamatan Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Keselamatan Konstruksi (Freshgraduate)", "acuan_skkni": "SKKNI 60–2022"},
    {"no": 294, "kode_jabatan": "SR021005", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Komputasi Konstruksi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Manager BIM Madya", "acuan_skkni": "SKKNI 3-2023"},
    {"no": 295, "kode_jabatan": "SR021004", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Komputasi Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Manager BIM Muda", "acuan_skkni": "SKKNI 3-2023"},
    {"no": 296, "kode_jabatan": "SR022004", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Komputasi Konstruksi", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Koordinator BIM", "acuan_skkni": "SKKNI 3-2023"},
    {"no": 297, "kode_jabatan": "SR022005", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Komputasi Konstruksi", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Modeler BIM (Level 5)", "acuan_skkni": "SKKNI 3-2023"},
    {"no": 298, "kode_jabatan": "SR022006", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Komputasi Konstruksi", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Modeler BIM (Level 4)", "acuan_skkni": "SKKNI 3-2023"},
    {"no": 299, "kode_jabatan": "SR023002", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Komputasi Konstruksi", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Juru Gambar BIM", "acuan_skkni": "SKKNI 3-2023"},
    {"no": 300, "kode_jabatan": "SR023003", "klasifikasi": "SAINS DAN REKAYASA TEKNIK", "subklasifikasi": "Komputasi Konstruksi", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Juru Gambar Pemula BIM", "acuan_skkni": "SKKNI 3-2023"},
    {"no": 301, "kode_jabatan": "SI021007", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Material Jalan", "acuan_skkni": "SKKNI 163-2024"},
    {"no": 302, "kode_jabatan": "SI021008", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Material Jalan", "acuan_skkni": "SKKNI 163-2024"},
    {"no": 303, "kode_jabatan": "SI021009", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Material Jalan", "acuan_skkni": "SKKNI 163-2024"},
    {"no": 304, "kode_jabatan": "SI022016", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Konstruksi, Fabrikasi, Sipil dan Struktur", "acuan_skkni": "SKKNI 171-2018"},
    {"no": 305, "kode_jabatan": "SI022017", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Teknisi Laboratorium Beton Aspal (Level 6)", "acuan_skkni": "SKKNI 196-2013"},
    {"no": 306, "kode_jabatan": "SI022018", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Laboratorium Beton Aspal (Level 5)", "acuan_skkni": "SKKNI 196-2013"},
    {"no": 307, "kode_jabatan": "SI022019", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Laboratorium Beton Aspal (Level 4)", "acuan_skkni": "SKKNI 196-2013"},
    {"no": 308, "kode_jabatan": "SI022020", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Teknisi Laboratorium Tanah (Level 6)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 309, "kode_jabatan": "SI022021", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Laboratorium Tanah (Level 5)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 310, "kode_jabatan": "SI022022", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Laboratorium Tanah (Level 4)", "acuan_skkni": "SKKNI 128-2024; SKKNI 17-2023"},
    {"no": 311, "kode_jabatan": "SI022023", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Produksi Campuran Aspal Panas (Level 5)", "acuan_skkni": "SKKNI 384-2013"},
    {"no": 312, "kode_jabatan": "SI022024", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Produksi Campuran Aspal Panas (Level 4)", "acuan_skkni": "SKKNI 384-2013"},
    {"no": 313, "kode_jabatan": "SI022025", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Teknisi Laboratorium Beton (Level 6)", "acuan_skkni": "SKK-Khusus Reg. 14-2024"},
    {"no": 314, "kode_jabatan": "SI022026", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Laboratorium Beton (Level 5)", "acuan_skkni": "SKK-Khusus Reg. 14-2024"},
    {"no": 315, "kode_jabatan": "SI022027", "klasifikasi": "SIPIL", "subklasifikasi": "Material", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Laboratorium Beton (Level 4)", "acuan_skkni": "SKK-Khusus Reg. 14-2024"},
    {"no": 316, "kode_jabatan": "SI221004", "klasifikasi": "SIPIL", "subklasifikasi": "Pembongkaran Bangunan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Pelaksanaan Pembongkaran Bangunan", "acuan_skkni": "SKKNI 96–2015"},
    {"no": 317, "kode_jabatan": "SI221006", "klasifikasi": "SIPIL", "subklasifikasi": "Pembongkaran Bangunan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Pelaksanaan Pembongkaran Bangunan", "acuan_skkni": "SKKNI 96–2015"},
    {"no": 318, "kode_jabatan": "SI221005", "klasifikasi": "SIPIL", "subklasifikasi": "Pembongkaran Bangunan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Pelaksanaan Pembongkaran Bangunan", "acuan_skkni": "SKKNI 96–2015"},
    {"no": 319, "kode_jabatan": "MP041014", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Sistem Manajemen Mutu Konstruksi", "acuan_skkni": "SKKNI 145-2019"},
    {"no": 320, "kode_jabatan": "MP041016", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Sistem Manajemen Mutu Konstruksi", "acuan_skkni": "SKKNI 145-2019"},
    {"no": 321, "kode_jabatan": "MP041015", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Sistem Manajemen Mutu Konstruksi", "acuan_skkni": "SKKNI 145-2019"},
    {"no": 322, "kode_jabatan": "MP042007", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Quality Engineer (Level 6)", "acuan_skkni": "SKKNI 333-2013"},
    {"no": 323, "kode_jabatan": "MP042008", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Quality Engineer (Level 5)", "acuan_skkni": "SKKNI 333-2013"},
    {"no": 324, "kode_jabatan": "MP042009", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Pengendali Mutu Jalan dan Jembatan", "acuan_skkni": "SKKNI 49-2022; SKKNI 45-2022"},
    {"no": 325, "kode_jabatan": "MP042010", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Quality Assurance Engineer (Level 6)", "acuan_skkni": "SKKNI 387-2013"},
    {"no": 326, "kode_jabatan": "MP042011", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Quality Assurance Engineer (Level 5)", "acuan_skkni": "SKKNI 387-2013"},
    {"no": 327, "kode_jabatan": "MP042004", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Pengendalian Mutu Pekerjaan Konstruksi", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Asesor Badan Usaha Jasa Konstruksi", "acuan_skkni": "SKKNI 273-2024"},
    {"no": 328, "kode_jabatan": "PW011004", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencana Wilayah Pesisir dan Pulau-Pulau Kecil", "acuan_skkni": "SKKNI 376-2013"},
    {"no": 329, "kode_jabatan": "PW011010", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Penyusunan Peraturan Zonasi", "acuan_skkni": "SKKNI 380-2013"},
    {"no": 330, "kode_jabatan": "PW011015", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Penyusunan Peraturan Zonasi", "acuan_skkni": "SKKNI 380-2013"},
    {"no": 331, "kode_jabatan": "PW011011", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencana Tata Bangunan dan Lingkungan", "acuan_skkni": "SKKNI 82-2015"},
    {"no": 332, "kode_jabatan": "PW011012", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencana Tata Bangunan dan Lingkungan", "acuan_skkni": "SKKNI 82-2015"},
    {"no": 333, "kode_jabatan": "PW011003", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencana Tata Ruang Wilayah dan Kota", "acuan_skkni": "SKKNI 177-2015"},
    {"no": 334, "kode_jabatan": "PW011002", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencana Tata Ruang Wilayah dan Kota", "acuan_skkni": "SKKNI 177-2015"},
    {"no": 335, "kode_jabatan": "PW011001", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencana Tata Ruang Wilayah dan Kota", "acuan_skkni": "SKKNI 177-2015"},
    {"no": 336, "kode_jabatan": "PW011013", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Penyusun Rencana Pengembangan Infrastruktur Wilayah", "acuan_skkni": "SKKNI 177-2015; SKKNI 11 - 2019"},
    {"no": 337, "kode_jabatan": "PW011014", "klasifikasi": "PERENCANAAN WILAYAH DAN KOTA", "subklasifikasi": "Perencanaan Wilayah", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencana Tata Ruang Wilayah dan Kota (Freshgraduate)", "acuan_skkni": "SKKNI 177-2015"},
    {"no": 338, "kode_jabatan": "ME021004", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Plambing dan Pompa Mekanik", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 339, "kode_jabatan": "ME021005", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Plambing dan Pompa Mekanik", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 340, "kode_jabatan": "ME021006", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Plambing dan Pompa Mekanik", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 341, "kode_jabatan": "ME022006", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pekerjaan Plambing (Level 6)", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 342, "kode_jabatan": "ME022007", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pekerjaan Plambing (Level 5)", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 343, "kode_jabatan": "ME022008", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Teknik Plambing (Level 5)", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 344, "kode_jabatan": "ME022009", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Teknik Plambing (Level 4)", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 345, "kode_jabatan": "ME023006", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Mandor Plambing", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 346, "kode_jabatan": "ME023007", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Asisten Pelaksana Plambing dan Pompa Mekanik", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 347, "kode_jabatan": "ME023008", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Plumbing dan Pompa Mekanik", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Asisten Pemula Pelaksana Plambing dan Pompa Mekanik", "acuan_skkni": "SKKNI 58-2024; SKKNI 28-2023; SKKNI 17-2023"},
    {"no": 348, "kode_jabatan": "ME031005", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Proteksi Kebakaran", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Pengkaji Teknis Proteksi Kebakaran", "acuan_skkni": "SKKNI 127-2015"},
    {"no": 349, "kode_jabatan": "ME031006", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Proteksi Kebakaran", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Pengkaji Teknis Proteksi Kebakaran", "acuan_skkni": "SKKNI 127-2015"},
    {"no": 350, "kode_jabatan": "ME031007", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Proteksi Kebakaran", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Pengkaji Teknis Proteksi Kebakaran", "acuan_skkni": "SKKNI 127-2015"},
    {"no": 351, "kode_jabatan": "ME032002", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Proteksi Kebakaran", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Fire Alarm", "acuan_skkni": "SKKNI 125-2023"},
    {"no": 352, "kode_jabatan": "SI091011", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Pantai", "acuan_skkni": "SKKNI 97-2015; SKKNI 206-2019"},
    {"no": 353, "kode_jabatan": "SI091012", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Pantai", "acuan_skkni": "SKKNI 97-2015; SKKNI 206-2019"},
    {"no": 354, "kode_jabatan": "SI091013", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Pantai", "acuan_skkni": "SKKNI 97-2015; SKKNI 206-2019"},
    {"no": 355, "kode_jabatan": "SI091014", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai", "acuan_skkni": "SKKNI 50-2015"},
    {"no": 356, "kode_jabatan": "SI091016", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai", "acuan_skkni": "SKKNI 50-2015"},
    {"no": 357, "kode_jabatan": "SI091015", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai", "acuan_skkni": "SKKNI 50-2015"},
    {"no": 358, "kode_jabatan": "SI092006", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Pekerjaan Pemeliharaan Sungai (Level 5)", "acuan_skkni": "SKKNI 365-2013; SKKNI 87-2015"},
    {"no": 359, "kode_jabatan": "SI092007", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Pekerjaan Pemeliharaan Sungai (Level 4)", "acuan_skkni": "SKKNI 365-2013; SKKNI 87-2015"},
    {"no": 360, "kode_jabatan": "SI092008", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai (Level 5)", "acuan_skkni": "SKKNI 69-2009"},
    {"no": 361, "kode_jabatan": "SI092009", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai (Level 4)", "acuan_skkni": "SKKNI 69-2009"},
    {"no": 362, "kode_jabatan": "SI092010", "klasifikasi": "SIPIL", "subklasifikasi": "Sungai dan Pantai", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Pengerukan", "acuan_skkni": "SKK-Khusus 28-2022"},
    {"no": 363, "kode_jabatan": "TL031006", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencana Sistem Sanitasi Lingkungan (Air Limbah Pemukiman)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 364, "kode_jabatan": "TL031007", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencana Sistem Sanitasi Lingkungan (Air Limbah Pemukiman)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 365, "kode_jabatan": "TL031008", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencana Sistem Sanitasi Lingkungan (Air Limbah Pemukiman)", "acuan_skkni": "SKKNI 29-2023"},
    {"no": 366, "kode_jabatan": "TL032004", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Fasilitator Teknis Dalam Pembangunan Sarana Sanitasi Berbasis Masyarakat (Level 6)", "acuan_skkni": "SKKNI 204-2015"},
    {"no": 367, "kode_jabatan": "TL032005", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Fasilitator Teknis Dalam Pembangunan Sarana Sanitasi Berbasis Masyarakat (Level 5)", "acuan_skkni": "SKKNI 204-2015"},
    {"no": 368, "kode_jabatan": "TL032006", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Operasi Instalasi Pengolahan Lumpur Tinja (Level 5)", "acuan_skkni": "SKKNI 277-2018; SKKNI 28-2023"},
    {"no": 369, "kode_jabatan": "TL032007", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Operasi Perpipaan Air Limbah Domestik (Level 5)", "acuan_skkni": "SKKNI 277-2018; SKKNI 28-2023"},
    {"no": 370, "kode_jabatan": "TL032008", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Operasi Instalasi Pengolahan Air Limbah Domestik (Level 5)", "acuan_skkni": "SKKNI 277-2018"},
    {"no": 371, "kode_jabatan": "TL032009", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Operasi Instalasi Pengolahan Lumpur Tinja (Level 4)", "acuan_skkni": "SKKNI 277-2018; SKKNI 381-2020"},
    {"no": 372, "kode_jabatan": "TL032010", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Operasi Perpipaan Air Limbah Domestik (Level 4)", "acuan_skkni": "SKKNI 277-2018; SKKNI 28-2023"},
    {"no": 373, "kode_jabatan": "TL032011", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Operasi Instalasi Pengolahan Air Limbah Domestik (Level 4)", "acuan_skkni": "SKKNI 277-2018; SKKNI 381-2020"},
    {"no": 374, "kode_jabatan": "TL033003", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Asisten Pelaksana Instalasi Pengolahan Lumpur Tinja", "acuan_skkni": "SKKNI 277-2018"},
    {"no": 375, "kode_jabatan": "TL033004", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Asisten Pelaksana Perpipaan Air Limbah Domestik", "acuan_skkni": "SKKNI 277-2018"},
    {"no": 376, "kode_jabatan": "TL033005", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Limbah", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Asisten Pelaksana Instalasi Pengolahan Air Limbah Domestik", "acuan_skkni": "SKKNI 277-2018"},
    {"no": 377, "kode_jabatan": "TL011011", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Air Minum", "acuan_skkni": "SKKNI 19 -2025; SKKNI 17-2023"},
    {"no": 378, "kode_jabatan": "TL011012", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Air Minum", "acuan_skkni": "SKKNI 19 -2025; SKKNI 17-2023"},
    {"no": 379, "kode_jabatan": "TL011013", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Air Minum", "acuan_skkni": "SKKNI 19 -2025; SKKNI 17-2023"},
    {"no": 380, "kode_jabatan": "TL011008", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Penanggulangan Kehilangan Air", "acuan_skkni": "SKKNI 169-2010"},
    {"no": 381, "kode_jabatan": "TL011009", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Penanggulangan Kehilangan Air", "acuan_skkni": "SKKNI 169-2010"},
    {"no": 382, "kode_jabatan": "TL011010", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Deteksi Kebocoran dan Commissioning Jaringan Perpipaan SPAM", "acuan_skkni": "SKKNI 167-2010"},
    {"no": 383, "kode_jabatan": "TL012014", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Analis Commissioning IPA (Level 6)", "acuan_skkni": "SKKNI 141-2010"},
    {"no": 384, "kode_jabatan": "TL012015", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Analis Commissioning IPA (Level 5)", "acuan_skkni": "SKKNI 141-2010"},
    {"no": 385, "kode_jabatan": "TL012016", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Teknisi Operasi dan Pemeliharaan Unit Pelayanan Air Minum (Level 5)", "acuan_skkni": "SKKNI 334-2013"},
    {"no": 386, "kode_jabatan": "TL012017", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Operasi dan Pemeliharaan Unit Pelayanan Air Minum (Level 4)", "acuan_skkni": "SKKNI 334-2013"},
    {"no": 387, "kode_jabatan": "TL012018", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Kepala Laboratorium Air Minum", "acuan_skkni": "SKKNI 381-2020"},
    {"no": 388, "kode_jabatan": "TL012019", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Analis Laboratorium Air Minum (Level 5)", "acuan_skkni": "SKKNI 381-2020"},
    {"no": 389, "kode_jabatan": "TL012020", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Analis Laboratorium Air Minum (Level 4)", "acuan_skkni": "SKKNI 381-2020"},
    {"no": 390, "kode_jabatan": "TL012021", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Supervisor Mekanikal Elektrikal Air Minum", "acuan_skkni": "SKKNI 422-2014; SKKNI 51-2015;"},
    {"no": 391, "kode_jabatan": "TL012022", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Lapangan Konstruksi SPAM", "acuan_skkni": "SKKNI 19 -2025; SKKNI 17-2023"},
    {"no": 392, "kode_jabatan": "TL012023", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Konstruksi SPAM", "acuan_skkni": "SKKNI 19 -2025; SKKNI 17-2023"},
    {"no": 393, "kode_jabatan": "TL013005", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Asisten Pelaksana Instalatur Unit Pelayanan Air Minum", "acuan_skkni": "SKKNI 346-2013"},
    {"no": 394, "kode_jabatan": "TL013006", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Asisten Pemula Pelaksana Instalatur Unit Pelayanan Air Minum", "acuan_skkni": "SKKNI 346-2013"},
    {"no": 395, "kode_jabatan": "TL013007", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Instalasi Pengolahan Air Minum", "acuan_skkni": "SKKNI 45-2017; SKKNI 422-2014; SKKNI 51-2015;"},
    {"no": 396, "kode_jabatan": "TL011014", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Air Minum", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Air Minum (Freshgraduate)", "acuan_skkni": "SKKNI 19 - 2025;"},
    {"no": 397, "kode_jabatan": "AL021005", "klasifikasi": "ARSITEKTUR LANSKAP, ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencanaan Iluminasi", "acuan_skkni": "SKKNI 379-2013"},
    {"no": 398, "kode_jabatan": "AL022003", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pekerjaan Iluminasi (Level 6)", "acuan_skkni": "SKKNI 339-2013"},
    {"no": 399, "kode_jabatan": "AL022004", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pekerjaan Iluminasi (Level 5)", "acuan_skkni": "SKKNI 339-2013"},
    {"no": 400, "kode_jabatan": "AL022005", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Pekerjaan Iluminasi (Level 4)", "acuan_skkni": "SKKNI 312-2013"},
    {"no": 401, "kode_jabatan": "AL023004", "klasifikasi": "ARSITEKTUR LANSKAP, TEKNIK ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Asisten Pelaksana Iluminasi", "acuan_skkni": "SKKNI 312-2013"},
    {"no": 402, "kode_jabatan": "AL021006", "klasifikasi": "ARSITEKTUR LANSKAP, ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencanaan Iluminasi (Freshgraduate)", "acuan_skkni": "SKKNI 379–2013"},
    {"no": 403, "kode_jabatan": "ME071004", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Launching Girder", "acuan_skkni": "SKKNI 18-2023"},
    {"no": 404, "kode_jabatan": "ME071003", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Launching Girder", "acuan_skkni": "SKKNI 18-2023"},
    {"no": 405, "kode_jabatan": "ME071002", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Lifting Engineer", "acuan_skkni": "SKKNI 246-2023"},
    {"no": 406, "kode_jabatan": "ME072006", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Lifting Supervisor", "acuan_skkni": "SKKNI 219-2023"},
    {"no": 407, "kode_jabatan": "ME072003", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Launching Gantry", "acuan_skkni": "SKKNI 18-2023"},
    {"no": 408, "kode_jabatan": "ME072002", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Launching Gantry", "acuan_skkni": "SKKNI 18-2023"},
    {"no": 409, "kode_jabatan": "ME072005", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Erection Girder", "acuan_skkni": "SKKNI 18-2023"},
    {"no": 410, "kode_jabatan": "ME072004", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Erection Girder", "acuan_skkni": "SKKNI 18-2023"},
    {"no": 411, "kode_jabatan": "ME073007", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Gondola pada Bangunan Gedung", "acuan_skkni": "SKKNI 296-2009"},
    {"no": 412, "kode_jabatan": "ME073008", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Gondola pada Bangunan Gedung", "acuan_skkni": "SKKNI 296-2009"},
    {"no": 413, "kode_jabatan": "ME073003", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Launching Gantry", "acuan_skkni": "SKKNI 18-2023"},
    {"no": 414, "kode_jabatan": "ME073009", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Slinging and Rigging", "acuan_skkni": "SKKNI 180-2024"},
    {"no": 415, "kode_jabatan": "ME073010", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Lifting", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Operator Pemula Forklift", "acuan_skkni": "SKKNI 180-2024"},
    {"no": 416, "kode_jabatan": "TL021004", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Lingkungan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Lingkungan Bidang Jasa Konstruksi", "acuan_skkni": "SKKNI 109-2015"},
    {"no": 417, "kode_jabatan": "TL021005", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Lingkungan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Lingkungan Bidang Jasa Konstruksi", "acuan_skkni": "SKKNI 109-2015"},
    {"no": 418, "kode_jabatan": "TL021006", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Lingkungan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Lingkungan Bidang Jasa Konstruksi", "acuan_skkni": "SKKNI 109-2015"},
    {"no": 419, "kode_jabatan": "TL021007", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Lingkungan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Lingkungan Bidang Jasa Konstruksi (Freshgraduate)", "acuan_skkni": "SKKNI 109-2015"},
    {"no": 420, "kode_jabatan": "ME051011", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Bidang Keahlian Teknik Mekanikal", "acuan_skkni": "SKKNI 391-2015; SKKNI 173-2024"},
    {"no": 421, "kode_jabatan": "ME051012", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Bidang Keahlian Teknik Mekanikal", "acuan_skkni": "SKKNI 391-2015; SKKNI 173-2024"},
    {"no": 422, "kode_jabatan": "ME051013", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Mekanikal", "acuan_skkni": "SKKNI 391-2015; SKKNI 173-2024"},
    {"no": 423, "kode_jabatan": "ME051014", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Elektrikal Konstruksi Bangunan Gedung", "acuan_skkni": "SKKNI 162-2019; SKKNI 208-2013"},
    {"no": 424, "kode_jabatan": "ME051015", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Elektrikal Konstruksi Bangunan Gedung", "acuan_skkni": "SKKNI 162-2019; SKKNI 208-2013"},
    {"no": 425, "kode_jabatan": "ME051016", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Elektrikal Konstruksi Bangunan Gedung", "acuan_skkni": "SKKNI 162-2019; SKKNI 208-2013"},
    {"no": 426, "kode_jabatan": "ME052009", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pekerjaan Mekanikal Bangunan Gedung (Level 6)", "acuan_skkni": "SKKNI 107-2015"},
    {"no": 427, "kode_jabatan": "ME052010", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pekerjaan Mekanikal Bangunan Gedung (Level 5)", "acuan_skkni": "SKKNI 107-2015"},
    {"no": 428, "kode_jabatan": "ME052011", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Mekanikal (Level 6)", "acuan_skkni": "SKKNI 61-2014"},
    {"no": 429, "kode_jabatan": "ME052012", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Teknisi/Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Mekanikal (Level 5)", "acuan_skkni": "SKKNI 61-2014"},
    {"no": 430, "kode_jabatan": "ME052014", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Prestressing Equipment", "acuan_skkni": "SKKNI 91-2015"},
    {"no": 431, "kode_jabatan": "ME052013", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Teknisi/Analis", "jenjang": 4, "nama_jabatan": "Teknisi Penyambung Pipa Polietilena Dengan Fusi Panas", "acuan_skkni": "SKKNI 29-2021"},
    {"no": 432, "kode_jabatan": "ME053018", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Juru Las", "acuan_skkni": "SKKNI 98-2018"},
    {"no": 433, "kode_jabatan": "ME053019", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Operator", "jenjang": 2, "nama_jabatan": "Juru Las Pemula", "acuan_skkni": "SKKNI 98-2018"},
    {"no": 434, "kode_jabatan": "ME053020", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Asisten Mekanik Heating, Ventilation, dan Air Condition (HVAC)", "acuan_skkni": "SKKNI 298-2009"},
    {"no": 435, "kode_jabatan": "ME051017", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Mekanikal (Freshgraduate)", "acuan_skkni": "SKKNI 391–2015"},
    {"no": 436, "kode_jabatan": "ME051018", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Mekanikal", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Elektrikal Konstruksi Bangunan Gedung (Freshgraduate)", "acuan_skkni": "SKKNI 162-2019"},
    {"no": 437, "kode_jabatan": "TL041003", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Perpipaan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Bidang Teknik Perpipaan", "acuan_skkni": "SKKNI 28–2023"},
    {"no": 438, "kode_jabatan": "TL041002", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Perpipaan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Bidang Teknik Perpipaan", "acuan_skkni": "SKKNI 28–2023"},
    {"no": 439, "kode_jabatan": "TL041001", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Perpipaan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Teknik Perpipaan", "acuan_skkni": "SKKNI 28–2023"},
    {"no": 440, "kode_jabatan": "TL042014", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Perpipaan", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pekerjaan Teknik Perpipaan (Level 6)", "acuan_skkni": "SKKNI 28–2023"},
    {"no": 441, "kode_jabatan": "TL042015", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Perpipaan", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pekerjaan Teknik Perpipaan (Level 5)", "acuan_skkni": "SKKNI 28–2023"},
    {"no": 442, "kode_jabatan": "TL042016", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Perpipaan", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Perpipaan (Level 5)", "acuan_skkni": "SKKNI 28–2023"},
    {"no": 443, "kode_jabatan": "TL042017", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Perpipaan", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Lapangan Pekerjaan Perpipaan (Level 4)", "acuan_skkni": "SKKNI 28–2023"},
    {"no": 444, "kode_jabatan": "TL051005", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Persampahan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencana Pengelolaan Sampah", "acuan_skkni": "SKKNI 205-2010"},
    {"no": 445, "kode_jabatan": "TL051006", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Persampahan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencana Pengelolaan Sampah", "acuan_skkni": "SKKNI 205-2010"},
    {"no": 446, "kode_jabatan": "TL051007", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Persampahan", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencana Pengelolaan Sampah", "acuan_skkni": "SKKNI 205-2010"},
    {"no": 447, "kode_jabatan": "TL052009", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Persampahan", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Pengawas Pengelolaan Tempat Pemrosesan Akhir (TPA) Sampah (Level 6)", "acuan_skkni": "SKKNI 329-2013"},
    {"no": 448, "kode_jabatan": "TL052010", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Persampahan", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Pengawas Pengelolaan Tempat Pemrosesan Akhir (TPA) Sampah (Level 5)", "acuan_skkni": "SKKNI 329-2013"},
    {"no": 449, "kode_jabatan": "TL052011", "klasifikasi": "TATA LINGKUNGAN", "subklasifikasi": "Teknik Persampahan", "kualifikasi": "Teknisi /Analis", "jenjang": 4, "nama_jabatan": "Pelaksana Pengelolaan TPA Sampah", "acuan_skkni": "SKKNI 338-2013; SKKNI 345-2013"},
    {"no": 450, "kode_jabatan": "ME011004", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Tata Udara dan Refrigasi", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Perencanaan Sistem Tata Udara", "acuan_skkni": "SKKNI 131–2015"},
    {"no": 451, "kode_jabatan": "ME011005", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Tata Udara dan Refrigasi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencanaan Sistem Tata Udara", "acuan_skkni": "SKKNI 131–2015"},
    {"no": 452, "kode_jabatan": "ME011006", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Teknik Tata Udara dan Refrigasi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencanaan Sistem Tata Udara", "acuan_skkni": "SKKNI 131–2015"},
    {"no": 453, "kode_jabatan": "SI061009", "klasifikasi": "SIPIL", "subklasifikasi": "Terowongan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Terowongan", "acuan_skkni": "SKKNI 20-2025; SKKNI 17-2023"},
    {"no": 454, "kode_jabatan": "SI061010", "klasifikasi": "SIPIL", "subklasifikasi": "Terowongan", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Terowongan", "acuan_skkni": "SKKNI 20-2025; SKKNI 17-2023"},
    {"no": 455, "kode_jabatan": "SI062005", "klasifikasi": "SIPIL", "subklasifikasi": "Terowongan", "kualifikasi": "Teknisi/Analis", "jenjang": 6, "nama_jabatan": "Inspektur Terowongan", "acuan_skkni": "SKKNI 20-2025; SKKNI 17-2023"},
    {"no": 456, "kode_jabatan": "ME041004", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Transportasi Dalam Gedung", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Pesawat Lift dan Eskalator", "acuan_skkni": "SKKNI 297-2009"},
    {"no": 457, "kode_jabatan": "ME041005", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Transportasi Dalam Gedung", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Pesawat Lift dan Eskalator", "acuan_skkni": "SKKNI 297-2009"},
    {"no": 458, "kode_jabatan": "ME041006", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Transportasi Dalam Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Pesawat Lift dan Eskalator", "acuan_skkni": "SKKNI 297-2009"},
    {"no": 459, "kode_jabatan": "ME041007", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Transportasi Dalam Gedung", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Pesawat Lift dan Eskalator (Freshgraduate)", "acuan_skkni": "SKKNI 297–2009"},
    {"no": 460, "kode_jabatan": "MP021008", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Bidang Keahlian Manajemen Konstruksi", "acuan_skkni": "SKKNI 390-2015"},
    {"no": 461, "kode_jabatan": "MP021007", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Bidang Keahlian Manajemen Konstruksi", "acuan_skkni": "SKKNI 390-2015"},
    {"no": 462, "kode_jabatan": "MP021006", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Keahlian Manajemen Konstruksi", "acuan_skkni": "SKKNI 390-2015"},
    {"no": 463, "kode_jabatan": "MP021012", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Manajemen Proyek", "acuan_skkni": "SKK Khusus Reg. 35-2022"},
    {"no": 464, "kode_jabatan": "MP021011", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Manajemen Proyek", "acuan_skkni": "SKK Khusus Reg. 35-2022"},
    {"no": 465, "kode_jabatan": "MP021010", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Manajemen Proyek", "acuan_skkni": "SKK Khusus Reg. 35-2022"},
    {"no": 466, "kode_jabatan": "MP021002", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Manajer Logistik Proyek", "acuan_skkni": "SKKNI 386-2013"},
    {"no": 467, "kode_jabatan": "MP022007", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Teknisi /Analis", "jenjang": 6, "nama_jabatan": "Fasilitator Teknis Dalam Pembangunan Infrastruktur Berbasis Masyarakat (Level 6)", "acuan_skkni": "SKKNI 260-2018"},
    {"no": 468, "kode_jabatan": "MP022008", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Teknisi /Analis", "jenjang": 5, "nama_jabatan": "Fasilitator Teknis Dalam Pembangunan Infrastruktur Berbasis Masyarakat (Level 5)", "acuan_skkni": "SKKNI 260-2018"},
    {"no": 469, "kode_jabatan": "MP021013", "klasifikasi": "MANAJEMEN PELAKSANAAN", "subklasifikasi": "Manajemen Konstruksi/Manajemen Proyek", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Bidang Keahlian Manajemen Konstruksi (Freshgraduate)", "acuan_skkni": "SKKNI 390–2015"},
    {"no": 470, "kode_jabatan": "AL021007", "klasifikasi": "ARSITEKTUR LANSKAP, ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Perencanaan Iluminasi", "acuan_skkni": "SKKNI 379-2013"},
    {"no": 471, "kode_jabatan": "AL021004", "klasifikasi": "ARSITEKTUR LANSKAP, ILUMINASI DAN DESAIN INTERIOR", "subklasifikasi": "Teknik Iluminasi", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Perencanaan Iluminasi", "acuan_skkni": "SKKNI 379-2013"}
]


# Inisialisasi State
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "sedang_login" not in st.session_state:
    st.session_state.sedang_login = False
if "nama_pengelola" not in st.session_state:
    st.session_state.nama_pengelola = ""
if "menu_aktif" not in st.session_state:
    st.session_state.menu_aktif = "🏠 Halaman Utama"

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

# ==============================================
# 4. NAVIGASI & MENU UTAMA
# ==============================================
st.markdown("<hr style='border: 3px solid #004B87; border-radius: 2px; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)
st.title("🏛️ Aplikasi Pelatihan & Sertifikasi UJI Kompetensi")
st.subheader("Balai Jasa Konstruksi Wilayah VI Makassar")
st.markdown("<h3 style='color:#004B87;'>siLATIH - Sistem Informasi Pelatihan Terintegrasi</h3>", unsafe_allow_html=True)

# --- MENU NAVIGASI DI SAMPING ---
st.sidebar.markdown("---")
st.sidebar.header("📋 Menu Utama")

# Menu untuk semua pengguna
menu_umum = ["🏠 Halaman Utama", "📋 Daftar Jabatan SKKNI", "📚 Jadwal Pelatihan", "📝 Pendaftaran Pelatihan"]
# Menu tambahan jika sudah login pengelola
menu_pengelola = ["⚙️ Pengelolaan Pelatihan"] if st.session_state.sedang_login else []

# Gabungkan menu
semua_menu = menu_umum + menu_pengelola
pilihan_menu = st.sidebar.radio("Pilih Halaman", semua_menu, index=semua_menu.index(st.session_state.menu_aktif))
st.session_state.menu_aktif = pilihan_menu

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
        st.session_state.menu_aktif = "🏠 Halaman Utama"
        st.rerun()

# ==============================================
# 5. ISI HALAMAN SESUAI MENU YANG DIPILIH
# ==============================================

# --- HALAMAN UTAMA ---
if pilihan_menu == "🏠 Halaman Utama":
    st.markdown("""
    <div class="pu-info">
    📢 <strong>Selamat Datang di siLATIH!</strong><br>
    Aplikasi resmi Balai Jasa Konstruksi Wilayah VI Makassar untuk informasi jabatan, jadwal pelatihan, dan pendaftaran uji kompetensi tenaga kerja konstruksi.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card-hasil" style="text-align:center;">
            <h3>📋 13 Jabatan</h3>
            <p>Terstandarisasi SKKNI</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card-hasil" style="text-align:center;">
            <h3>📚 Jadwal Teratur</h3>
            <p>Pelatihan rutin setiap bulan</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="card-hasil" style="text-align:center;">
            <h3>✅ Sertifikat Resmi</h3>
            <p>Diakui industri konstruksi</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("💡 Gunakan menu di sebelah kiri untuk melihat daftar jabatan, jadwal pelatihan, atau mengisi formulir pendaftaran.")

# --- HALAMAN DAFTAR JABATAN ---
elif pilihan_menu == "📋 Daftar Jabatan SKKNI":
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
    
    st.subheader("📥 Unduh Daftar Jabatan")
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer: df.to_excel(writer, index=False, sheet_name="Daftar Jabatan SKKNI")
    st.download_button(label="📂 Unduh File Excel (.xlsx)", data=buffer.getvalue(), file_name="Daftar_Jabatan_SKKNI_BJKW6_PUPR.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# --- HALAMAN JADWAL PELATIHAN ---
elif pilihan_menu == "📚 Jadwal Pelatihan":
    st.header("📚 Informasi Jadwal Pelatihan")
    
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
    
    st.subheader("⚪ Pelatihan Telah Selesai")
    if pelatihan_selesai:
        for latih, status in pelatihan_selesai:
            st.markdown(f"""
            <div style="background: #F9FAFB; border-left: 6px solid #9CA3AF; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <h4 style="color: #6B7280;">{latih['nama']}</h4>
            <p>Jabatan: {latih['jabatan']}<br>
            Pelatihan dilaksanakan: {latih['mulai']} s.d {latih['selesai']}<br>
            Lokasi: {latih['lokasi']}</p>
            </div>""", unsafe_allow_html=True)
    else:
        st.info("ℹ️ Belum ada riwayat pelatihan selesai.")

# --- HALAMAN PENDAFTARAN ---
elif pilihan_menu == "📝 Pendaftaran Pelatihan":
    st.header("📝 Formulir Pendaftaran Uji Kompetensi")
    
    pilihan_pendaftaran = []
    for latih in st.session_state.daftar_pelatihan:
        status = tentukan_status(latih["mulai"], latih["selesai"])
        if "Akan Datang" in status:
            pilihan_pendaftaran.append(f"{latih['nama']} — {latih['jabatan']}")
    
    if not pilihan_pendaftaran:
        st.warning("⏳ Saat ini tidak ada pelatihan yang menerima pendaftaran. Silakan cek kembali di menu Jadwal Pelatihan nanti.")
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

# --- HALAMAN PENGELOLAAN PELATIHAN ---
elif pilihan_menu == "⚙️ Pengelolaan Pelatihan":
    st.header("⚙️ Pengelolaan Pelatihan (Hanya Pengelola)")
    
    with st.form("form_pelatihan_baru", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nama_pelatihan = st.text_input("Nama Pelatihan *")
            df_jabatan = pd.DataFrame(daftar_jabatan)
            jabatan_terkait = st.selectbox("Jabatan Terkait *", df_jabatan["nama_jabatan"].unique())
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
                        ubah_jabatan = st.selectbox("Jabatan Terkait *", df_jabatan["nama_jabatan"].unique(), index=df_jabatan["nama_jabatan"].tolist().index(latih["jabatan"]))
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

# --- KAKI HALAMAN ---
st.markdown("<hr style='border: 2px solid #004B87; margin-top: 2rem;'>", unsafe_allow_html=True)
st.caption("© 2026 Balai Jasa Konstruksi Wilayah VI Makassar — Kementerian Pekerjaan Umum | siLATIH v2.2")
