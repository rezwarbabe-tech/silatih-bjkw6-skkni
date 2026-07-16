# ==============================================================
# JUDUL APLIKASI
# ==============================================================
"""
====================================================================
                Aplikasi Pelatihan & Sertifikasi UJI Kompetensi
                      Balai Jasa Konstruksi Wilayah VI Makassar
                       siLATIH - Sistem Informasi Pelatihan Terintegrasi
====================================================================
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# ==============================================================
# KONFIGURASI TAMPILAN & CSS KUSTOM
# ==============================================================
st.set_page_config(
    page_title="siLATIH - Sistem Informasi Pelatihan Terintegrasi",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

CSS_STYLE = """
<style>
* {
    font-family: 'Segoe UI', Roboto, Arial, sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f0f7ff 0%, #e6f0ff 100%);
}

.header-box {
    background: linear-gradient(135deg, #0056b3 0%, #003d7a 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 86, 179, 0.25);
    margin-bottom: 2rem;
}
.header-box h1 {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.header-box h2 {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #ffd700;
}
.header-box p {
    font-size: 17px;
    opacity: 0.95;
}

.menu-pengelola {
    background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}
.menu-peserta {
    background: linear-gradient(135deg, #17a2b8 0%, #117a8b 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

.kategori-ahli {
    background-color: #fff9e6;
    border-left: 5px solid #ffc107;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
}
.kategori-teknis {
    background-color: #e6f2ff;
    border-left: 5px solid #007bff;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
}
.kategori-operator {
    background-color: #e6fff2;
    border-left: 5px solid #28a745;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
}

.syarat-box {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
}

.footer-box {
    background: #2c3e50;
    color: white;
    text-align: center;
    padding: 1.2rem;
    border-radius: 8px;
    margin-top: 3rem;
    font-size: 14px;
    font-weight: 500;
}

strong {
    font-weight: 700;
    font-size: 15px;
}
</style>
"""
st.markdown(CSS_STYLE, unsafe_allow_html=True)

# ==============================================================
# DATA MASTER JABATAN KERJA (JabKer) - SESUAI FILE EXCEL UTUH
# ==============================================================
DATA_MASTER_JABKER = [
    # === SIPIL - AIR TANAH DAN AIR BAKU ===
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101015","jabatan_kerja":"Ahli Utama Bidang Keahlian Teknik Sumber Daya Air","jenjang":9,"acuan":"SKKNI 124-2021","keterangan":"Tabel.S.09.1"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101014","jabatan_kerja":"Ahli Madya Bidang Keahlian Teknik Sumber Daya Air","jenjang":8,"acuan":"SKKNI 124-2021","keterangan":"Tabel.S.09.2"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101013","jabatan_kerja":"Ahli Muda Bidang Keahlian Teknik Sumber Daya Air","jenjang":7,"acuan":"SKKNI 124-2021","keterangan":"Tabel.S.09.3"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101003","jabatan_kerja":"Ahli Utama Hidrologi","jenjang":9,"acuan":"SKKNI 32-2014","keterangan":"Tabel.S.09.4"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101002","jabatan_kerja":"Ahli Madya Hidrologi","jenjang":8,"acuan":"SKKNI 32-2014","keterangan":"Tabel.S.09.5"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101001","jabatan_kerja":"Ahli Muda Hidrologi","jenjang":7,"acuan":"SKKNI 32-2014","keterangan":"Tabel.S.09.6"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101018","jabatan_kerja":"Ahli Utama Hidrolika","jenjang":9,"acuan":"SKKNI 151-2019","keterangan":"Tabel.S.09.7"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101021","jabatan_kerja":"Ahli Madya Hidrolika","jenjang":8,"acuan":"SKKNI 151-2019","keterangan":"Tabel.S.09.8"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101020","jabatan_kerja":"Ahli Muda Hidrolika","jenjang":7,"acuan":"SKKNI 151-2019","keterangan":"Tabel.S.09.9"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","id_jabatan":"SI102005","jabatan_kerja":"Pengawas Pengeboran Air Tanah (Level 6)","jenjang":6,"acuan":"SKKNI 128-2024; SKKNI 17-2023","keterangan":"Tabel.S.09.10"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","id_jabatan":"SI102006","jabatan_kerja":"Pengawas Pengeboran Air Tanah (Level 5)","jenjang":5,"acuan":"SKKNI 128-2024; SKKNI 17-2023","keterangan":"Tabel.S.09.11"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","id_jabatan":"SI102007","jabatan_kerja":"Pelaksana Pengeboran Air Tanah (Level 5)","jenjang":5,"acuan":"SKKNI 128-2024; SKKNI 17-2023","keterangan":"Tabel.S.09.12"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","id_jabatan":"SI102008","jabatan_kerja":"Pelaksana Pengeboran Air Tanah (Level 4)","jenjang":4,"acuan":"SKKNI 128-2024; SKKNI 17-2023","keterangan":"Tabel.S.09.13"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","id_jabatan":"SI101019","jabatan_kerja":"Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate)","jenjang":7,"acuan":"SKKNI 124-2021","keterangan":"Tabel.S.04.1.FG"},
    
    # === MEKANIKAL - ALAT BERAT ===
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Ahli","id_jabatan":"ME061001","jabatan_kerja":"Manajer Alat Berat","jenjang":8,"acuan":"SKKNI 206-2013","keterangan":"Tabel.M.06.1"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Teknisi/Analis","id_jabatan":"ME062011","jabatan_kerja":"Pengawas Scaffolding","jenjang":5,"acuan":"SKKNI 46-2022","keterangan":"Tabel.M.06.2"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Teknisi/Analis","id_jabatan":"ME062009","jabatan_kerja":"Teknisi Scaffolding","jenjang":4,"acuan":"SKKNI 46-2022","keterangan":"Tabel.M.06.3"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063094","jabatan_kerja":"Operator Scaffolding","jenjang":3,"acuan":"SKKNI 46-2022","keterangan":"Tabel.M.06.4"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063095","jabatan_kerja":"Operator Pemula Scaffolding","jenjang":2,"acuan":"SKKNI 46-2022","keterangan":"Tabel.M.06.5"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063096","jabatan_kerja":"Operator Bulldozer","jenjang":3,"acuan":"SKK Khusus Reg.27-2022","keterangan":"Tabel.M.06.6"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063097","jabatan_kerja":"Operator Pemula Bulldozer","jenjang":2,"acuan":"SKK Khusus Reg.27-2022","keterangan":"Tabel.M.06.7"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063098","jabatan_kerja":"Operator Motor Grader","jenjang":3,"acuan":"SKK Khusus Reg.30-2022","keterangan":"Tabel.M.06.8"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063099","jabatan_kerja":"Operator Pemula Motor Grader","jenjang":2,"acuan":"SKK Khusus Reg.30-2022","keterangan":"Tabel.M.06.9"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063100","jabatan_kerja":"Operator Wheel Excavator","jenjang":3,"acuan":"SKKNI 91-2010","keterangan":"Tabel.M.06.10"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063101","jabatan_kerja":"Operator Pemula Wheel Excavator","jenjang":2,"acuan":"SKKNI 91-2010","keterangan":"Tabel.M.06.11"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063102","jabatan_kerja":"Operator Tandem Roller","jenjang":3,"acuan":"SKKNI 159-2019","keterangan":"Tabel.M.06.12"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063103","jabatan_kerja":"Operator Pemula Tandem Roller","jenjang":2,"acuan":"SKKNI 159-2019","keterangan":"Tabel.M.06.13"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063104","jabatan_kerja":"Operator Vibrator Roller","jenjang":3,"acuan":"SKKNI 168-2019","keterangan":"Tabel.M.06.14"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063105","jabatan_kerja":"Operator Pemula Vibrator Roller","jenjang":2,"acuan":"SKKNI 168-2019","keterangan":"Tabel.M.06.15"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063106","jabatan_kerja":"Operator Pneumatic Tire Roller","jenjang":3,"acuan":"SKKNI 164-2019","keterangan":"Tabel.M.06.16"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063107","jabatan_kerja":"Operator Pemula Pneumatic Tire Roller","jenjang":2,"acuan":"SKKNI 164-2019","keterangan":"Tabel.M.06.17"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063014","jabatan_kerja":"Operator Wheel Loader","jenjang":3,"acuan":"SKK Khusus Reg.33-2022","keterangan":"Tabel.M.06.18"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063108","jabatan_kerja":"Operator Pemula Wheel Loader","jenjang":2,"acuan":"SKK Khusus Reg.33-2022","keterangan":"Tabel.M.06.19"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063109","jabatan_kerja":"Operator Mobile Crane","jenjang":3,"acuan":"SKKNI 180-2024","keterangan":"Tabel.M.06.20"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063110","jabatan_kerja":"Operator Pemula Mobile Crane","jenjang":2,"acuan":"SKKNI 180-2024","keterangan":"Tabel.M.06.21"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063028","jabatan_kerja":"Operator Tower Crane","jenjang":3,"acuan":"SKK Khusus Reg.43-2022","keterangan":"Tabel.M.06.22"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063111","jabatan_kerja":"Operator Pemula Tower Crane","jenjang":2,"acuan":"SKK Khusus Reg.43-2022","keterangan":"Tabel.M.06.23"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063112","jabatan_kerja":"Operator Truck Mounted Crane","jenjang":3,"acuan":"SKKNI 85-2021","keterangan":"Tabel.M.06.24"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063113","jabatan_kerja":"Operator Pemula Truck Mounted Crane","jenjang":2,"acuan":"SKKNI 85-2021","keterangan":"Tabel.M.06.25"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063114","jabatan_kerja":"Operator Backhoe Loader","jenjang":3,"acuan":"SKKNI 89-2010","keterangan":"Tabel.M.06.26"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063115","jabatan_kerja":"Operator Pemula Backhoe Loader","jenjang":2,"acuan":"SKKNI 89-2010","keterangan":"Tabel.M.06.27"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063116","jabatan_kerja":"Operator Pile Drive Hammer","jenjang":3,"acuan":"SKKNI 150-2019","keterangan":"Tabel.M.06.28"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063117","jabatan_kerja":"Operator Pemula Pile Drive Hammer","jenjang":2,"acuan":"SKKNI 150-2019","keterangan":"Tabel.M.06.29"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063142","jabatan_kerja":"Operator Pompa Beton","jenjang":3,"acuan":"SKKNI 381-2013","keterangan":"Tabel.M.06.30"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063118","jabatan_kerja":"Operator Pemula Pompa Beton","jenjang":2,"acuan":"SKKNI 381-2013","keterangan":"Tabel.M.06.31"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063119","jabatan_kerja":"Operator Bore Pile","jenjang":3,"acuan":"SKKNI 111-2015","keterangan":"Tabel.M.06.32"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063120","jabatan_kerja":"Operator Pemula Bore Pile","jenjang":2,"acuan":"SKKNI 111-2015","keterangan":"Tabel.M.06.33"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063121","jabatan_kerja":"Operator Mesin Pencampur Aspal","jenjang":3,"acuan":"SKKNI 382-2013","keterangan":"Tabel.M.06.34"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063122","jabatan_kerja":"Operator Pemula Mesin Pencampur Aspal","jenjang":2,"acuan":"SKKNI 382-2013","keterangan":"Tabel.M.06.35"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063123","jabatan_kerja":"Operator Mesin Penggelar Aspal","jenjang":3,"acuan":"SKKNI 383-2013","keterangan":"Tabel.M.06.36"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063124","jabatan_kerja":"Operator Pemula Mesin Penggelar Aspal","jenjang":2,"acuan":"SKKNI 383-2013","keterangan":"Tabel.M.06.37"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063125","jabatan_kerja":"Operator Mesin Pemecah Batu","jenjang":3,"acuan":"SKK Khusus Reg.42-2022","keterangan":"Tabel.M.06.38"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063126","jabatan_kerja":"Operator Pemula Mesin Pemecah Batu","jenjang":2,"acuan":"SKK Khusus Reg.42-2022","keterangan":"Tabel.M.06.39"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063127","jabatan_kerja":"Operator Mesin Penghampar Beton Semen","jenjang":3,"acuan":"SKK Khusus Reg.41-2022","keterangan":"Tabel.M.06.40"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063128","jabatan_kerja":"Operator Pemula Mesin Penghampar Beton Semen","jenjang":2,"acuan":"SKK Khusus Reg.41-2022","keterangan":"Tabel.M.06.41"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063012","jabatan_kerja":"Operator Cold Milling Machine","jenjang":3,"acuan":"SKK Khusus Reg.40-2022","keterangan":"Tabel.M.06.42"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063129","jabatan_kerja":"Operator Pemula Cold Milling Machine","jenjang":2,"acuan":"SKK Khusus Reg.40-2022","keterangan":"Tabel.M.06.43"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063029","jabatan_kerja":"Operator Batching Plant","jenjang":3,"acuan":"SKK Khusus Reg.39-2022","keterangan":"Tabel.M.06.44"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063130","jabatan_kerja":"Operator Pemula Batching Plant","jenjang":2,"acuan":"SKK Khusus Reg.39-2022","keterangan":"Tabel.M.06.45"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063131","jabatan_kerja":"Operator Hydrolic Hammer Breaker","jenjang":3,"acuan":"SKKNI 158-2019","keterangan":"Tabel.M.06.46"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063132","jabatan_kerja":"Operator Pemula Hydrolic Hammer Breaker","jenjang":2,"acuan":"SKKNI 158-2019","keterangan":"Tabel.M.06.47"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063133","jabatan_kerja":"Operator Ripper Tractor","jenjang":3,"acuan":"SKKNI 165-2019","keterangan":"Tabel.M.06.48"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063134","jabatan_kerja":"Operator Pemula Ripper Tractor","jenjang":2,"acuan":"SKKNI 165-2019","keterangan":"Tabel.M.06.49"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063135","jabatan_kerja":"Mekanik Tower Crane","jenjang":3,"acuan":"SKK Khusus Reg.34-2022","keterangan":"Tabel.M.06.50"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063005","jabatan_kerja":"Mekanik Asphalt Mixing Plant","jenjang":3,"acuan":"SKKNI 326-2009","keterangan":"Tabel.M.06.51"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063002","jabatan_kerja":"Mekanik Kapal Keruk","jenjang":3,"acuan":"SKKNI 70-2009","keterangan":"Tabel.M.06.52"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063141","jabatan_kerja":"Mekanik Engine Tingkat Dasar","jenjang":3,"acuan":"SKKNI 382-2015","keterangan":"Tabel.M.06.53"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063136","jabatan_kerja":"Mekanik Engine Pemula Tingkat Dasar","jenjang":2,"acuan":"SKKNI 382-2015","keterangan":"Tabel.M.06.54"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063137","jabatan_kerja":"Mekanik Hidrolik Alat Berat","jenjang":3,"acuan":"SKKNI 88-2010","keterangan":"Tabel.M.06.55"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063138","jabatan_kerja":"Mekanik Hidrolik Alat Berat Pemula","jenjang":2,"acuan":"SKKNI 88-2010","keterangan":"Tabel.M.06.56"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063140","jabatan_kerja":"Mekanik Engine Alat Berat","jenjang":3,"acuan":"SKKNI 235-2023","keterangan":"Tabel.M.06.57"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063139","jabatan_kerja":"Mekanik Engine Alat Berat Pemula","jenjang":2,"acuan":"SKKNI 235-2023","keterangan":"Tabel.M.06.58"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","id_jabatan":"ME063027","jabatan_kerja":"Operator Dump Truck","jenjang":2,"acuan":"SKKNI 132-2015","keterangan":"Tabel.M.06.59"},
    
    # === ARSITEKTUR LANSKAP ===
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","id_jabatan":"AL011009","jabatan_kerja":"Arsitek Lanskap Utama","jenjang":9,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.1a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","id_jabatan":"AL011010","jabatan_kerja":"Arsitek Lanskap Madya","jenjang":8,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.2a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","id_jabatan":"AL011011","jabatan_kerja":"Arsitek Lanskap Muda","jenjang":7,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.3a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","id_jabatan":"AL011012","jabatan_kerja":"Manajer Lanskap Madya","jenjang":8,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.4a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","id_jabatan":"AL011013","jabatan_kerja":"Manajer Lanskap Muda","jenjang":7,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.5a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi /Analis","id_jabatan":"AL012006","jabatan_kerja":"Pengawas Lanskap (Level 6)","jenjang":6,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.6a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi /Analis","id_jabatan":"AL012007","jabatan_kerja":"Pengawas Lanskap (Level 5)","jenjang":5,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.7a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi /Analis","id_jabatan":"AL012008","jabatan_kerja":"Pelaksana Lanskap (Level 5)","jenjang":5,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.8a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi /Analis","id_jabatan":"AL012009","jabatan_kerja":"Pelaksana Lanskap (Level 4)","jenjang":4,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.9a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Operator","id_jabatan":"AL013004","jabatan_kerja":"Juru Tanam","jenjang":3,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.10a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Operator","id_jabatan":"AL013005","jabatan_kerja":"Juru Tanam Pemula","jenjang":2,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.11a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Operator","id_jabatan":"AL013006","jabatan_kerja":"Tukang Taman","jenjang":1,"acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023","keterangan":"Tabel.AL.01.12a"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","id_jabatan":"AL011008","jabatan_kerja":"Arsitek Lanskap Muda (Freshgraduate)","jenjang":7,"acuan":"SKKNI 209-2013","keterangan":"Tabel.AL.01.1.FG"}
]

# ==============================================================
# PENYIMPANAN DATA PELATIHAN
# ==============================================================
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []

# ==============================================================
# FUNGSI PENGELOLAAN PELATIHAN
# ==============================================================
def simpan_pelatihan(data):
    data["id"] = datetime.now().timestamp()
    data["tanggal_dibuat"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["status"] = "Tersedia"
    st.session_state.daftar_pelatihan.append(data)
    return True

def ubah_pelatihan(id_pelatihan, data_baru):
    for idx, pelatihan in enumerate(st.session_state.daftar_pelatihan):
        if pelatihan["id"] == id_pelatihan:
            st.session_state.daftar_pelatihan[idx].update(data_baru)
            st.session_state.daftar_pelatihan[idx]["tanggal_diubah"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    return False

def hapus_pelatihan(id_pelatihan):
    st.session_state.daftar_pelatihan = [p for p in st.session_state.daftar_pelatihan if p["id"] != id_pelatihan]
    return True

# ==============================================================
# TAMPILAN JUDUL UTAMA
# ==============================================================
st.markdown("""
<div class="header-box">
    <h1>Aplikasi Pelatihan & Sertifikasi UJI Kompetensi</h1>
    <h2>Balai Jasa Konstruksi Wilayah VI Makassar</h2>
    <p>siLATIH - Sistem Informasi Pelatihan Terintegrasi</p>
</div>
""", unsafe_allow_html=True)

# ==============================================================
# PILIH PERAN PENGGUNA
# ==============================================================
peran = st.sidebar.selectbox("Pilih Peran Anda", ["Pengelola", "Peserta"])

# ==============================================================
# MENU PENGELOLA
# ==============================================================
if peran == "Pengelola":
    st.markdown("""
    <div class="menu-pengelola">
        <h3>🔧 Menu Pengelola</h3>
        <p>Pilih Jabatan Kerja dari Master Data — klasifikasi, subklasifikasi, jenjang, dan acuan terisi otomatis</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📝 Buat Pelatihan Berdasarkan Jabatan Kerja")

    # Filter bertingkat: Klasifikasi → Subklasifikasi → Jabatan Kerja
    daftar_klasifikasi = sorted(list({j["klasifikasi"] for j in DATA_MASTER_JABKER}))
    klasifikasi_terpilih = st.selectbox("Pilih Klasifikasi Bidang", daftar_klasifikasi)
    
    daftar_subklasifikasi = sorted(list({j["sub_klasifikasi"] for j in DATA_MASTER_JABKER if j["klasifikasi"] == klasifikasi_terpilih}))
    subklasifikasi_terpilih = st.selectbox("Pilih Sub Klasifikasi", daftar_subklasifikasi)
    
    daftar_jabatan = [j for j in DATA_MASTER_JABKER if j["klasifikasi"] == klasifikasi_terpilih and j["sub_klasifikasi"] == subklasifikasi_terpilih]
    pilihan_jabatan = [f"{j['id_jabatan']} - {j['jabatan_kerja']} (Jenjang {j['jenjang']})" for j in daftar_jabatan]
    jabatan_terpilih_teks = st.selectbox("Pilih Jabatan Kerja", pilihan_jabatan)
    
    # Ambil data lengkap jabatan yang dipilih
    data_jabatan = next(j for j in daftar_jabatan if jabatan_terpilih_teks.startswith(j["id_jabatan"]))

    # Tampilkan data otomatis sesuai master data
    st.markdown("### 📋 Data Jabatan (Terpetakan Otomatis dari Master Data)")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Kode & Klasifikasi**: {data_jabatan['kode_klasifikasi']} - {data_jabatan['klasifikasi']}")
        st.info(f"**Sub Klasifikasi**: {data_jabatan['sub_klasifikasi']}")
        st.info(f"**Kualifikasi**: {data_jabatan['kualifikasi']}")
    with col2:
        st.info(f"**ID Jabatan**: {data_jabatan['id_jabatan']}")
        st.info(f"**Jenjang Jabatan**: {data_jabatan['jenjang']}")
        st.info(f"**Acuan SKKNI**: {data_jabatan['acuan']}")
    
    st.markdown(f"**Keterangan**: {data_jabatan['keterangan']}")

    # Form detail pelatihan
    st.markdown("### 📝 Isi Detail Pelatihan")
    with st.form("form_pelatihan_jabatan"):
        nama_pelatihan = st.text_input("Nama Pelatihan", value=f"Pelatihan Sertifikasi {data_jabatan['jabatan_kerja']}")
        deskripsi = st.text_area("Deskripsi & Tujuan Pelatihan")
        tanggal_pelaksanaan = st.date_input("Tanggal Pelaksanaan")
        lokasi = st.text_input("Lokasi Pelatihan")
        kuota = st.number_input("Kuota Peserta", min_value=1, value=30)
        tombol_simpan = st.form
