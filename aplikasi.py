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
# DATA MASTER JABATAN KERJA - SESUAI FILE LENGKAP
# ==============================================================
DATA_MASTER_JABKER = [
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":9,"id_jabatan":"SI101015","jabatan_kerja":"Ahli Utama Bidang Keahlian Teknik Sumber Daya Air","acuan":"SKKNI 124-2021"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"SI101014","jabatan_kerja":"Ahli Madya Bidang Keahlian Teknik Sumber Daya Air","acuan":"SKKNI 124-2021"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI101013","jabatan_kerja":"Ahli Muda Bidang Keahlian Teknik Sumber Daya Air","acuan":"SKKNI 124-2021"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":9,"id_jabatan":"SI101003","jabatan_kerja":"Ahli Utama Hidrologi","acuan":"SKKNI 32-2014"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"SI101002","jabatan_kerja":"Ahli Madya Hidrologi","acuan":"SKKNI 32-2014"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI101001","jabatan_kerja":"Ahli Muda Hidrologi","acuan":"SKKNI 32-2014"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":9,"id_jabatan":"SI101018","jabatan_kerja":"Ahli Utama Hidrolika","acuan":"SKKNI 151-2019"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"SI101021","jabatan_kerja":"Ahli Madya Hidrolika","acuan":"SKKNI 151-2019"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI101020","jabatan_kerja":"Ahli Muda Hidrolika","acuan":"SKKNI 151-2019"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","jenjang":6,"id_jabatan":"SI102005","jabatan_kerja":"Pengawas Pengeboran Air Tanah (Level 6)","acuan":"SKKNI 128-2024; SKKNI 17-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"SI102006","jabatan_kerja":"Pengawas Pengeboran Air Tanah (Level 5)","acuan":"SKKNI 128-2024; SKKNI 17-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"SI102007","jabatan_kerja":"Pelaksana Pengeboran Air Tanah (Level 5)","acuan":"SKKNI 128-2024; SKKNI 17-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Teknisi/Analis","jenjang":4,"id_jabatan":"SI102008","jabatan_kerja":"Pelaksana Pengeboran Air Tanah (Level 4)","acuan":"SKKNI 128-2024; SKKNI 17-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Air Tanah dan Air Baku","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI101019","jabatan_kerja":"Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate)","acuan":"SKKNI 124-2021"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"ME061001","jabatan_kerja":"Manajer Alat Berat","acuan":"SKKNI 206-2013"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"ME062011","jabatan_kerja":"Pengawas Scaffolding","acuan":"SKKNI 46-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Teknisi/Analis","jenjang":4,"id_jabatan":"ME062009","jabatan_kerja":"Teknisi Scaffolding","acuan":"SKKNI 46-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063094","jabatan_kerja":"Operator Scaffolding","acuan":"SKKNI 46-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063095","jabatan_kerja":"Operator Pemula Scaffolding","acuan":"SKKNI 46-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063096","jabatan_kerja":"Operator Bulldozer","acuan":"SKK Khusus Reg.27-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063097","jabatan_kerja":"Operator Pemula Bulldozer","acuan":"SKK Khusus Reg.27-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063098","jabatan_kerja":"Operator Motor Grader","acuan":"SKK Khusus Reg.30-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063099","jabatan_kerja":"Operator Pemula Motor Grader","acuan":"SKK Khusus Reg.30-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063100","jabatan_kerja":"Operator Wheel Excavator","acuan":"SKKNI 91-2010"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063101","jabatan_kerja":"Operator Pemula Wheel Excavator","acuan":"SKKNI 91-2010"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063102","jabatan_kerja":"Operator Tandem Roller","acuan":"SKKNI 159-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063103","jabatan_kerja":"Operator Pemula Tandem Roller","acuan":"SKKNI 159-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063104","jabatan_kerja":"Operator Vibrator Roller","acuan":"SKKNI 168-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063105","jabatan_kerja":"Operator Pemula Vibrator Roller","acuan":"SKKNI 168-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063106","jabatan_kerja":"Operator Pneumatic Tire Roller","acuan":"SKKNI 164-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063107","jabatan_kerja":"Operator Pemula Pneumatic Tire Roller","acuan":"SKKNI 164-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063014","jabatan_kerja":"Operator Wheel Loader","acuan":"SKK Khusus Reg.33-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063108","jabatan_kerja":"Operator Pemula Wheel Loader","acuan":"SKK Khusus Reg.33-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063109","jabatan_kerja":"Operator Mobile Crane","acuan":"SKKNI 180-2024"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063110","jabatan_kerja":"Operator Pemula Mobile Crane","acuan":"SKKNI 180-2024"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063028","jabatan_kerja":"Operator Tower Crane","acuan":"SKK Khusus Reg.43-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063111","jabatan_kerja":"Operator Pemula Tower Crane","acuan":"SKK Khusus Reg.43-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063112","jabatan_kerja":"Operator Truck Mounted Crane","acuan":"SKKNI 85-2021"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063113","jabatan_kerja":"Operator Pemula Truck Mounted Crane","acuan":"SKKNI 85-2021"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063114","jabatan_kerja":"Operator Backhoe Loader","acuan":"SKKNI 89-2010"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063115","jabatan_kerja":"Operator Pemula Backhoe Loader","acuan":"SKKNI 89-2010"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063116","jabatan_kerja":"Operator Pile Drive Hammer","acuan":"SKKNI 150-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063117","jabatan_kerja":"Operator Pemula Pile Drive Hammer","acuan":"SKKNI 150-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063142","jabatan_kerja":"Operator Pompa Beton","acuan":"SKKNI 381-2013"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063118","jabatan_kerja":"Operator Pemula Pompa Beton","acuan":"SKKNI 381-2013"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063119","jabatan_kerja":"Operator Bore Pile","acuan":"SKKNI 111-2015"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063120","jabatan_kerja":"Operator Pemula Bore Pile","acuan":"SKKNI 111-2015"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063121","jabatan_kerja":"Operator Mesin Pencampur Aspal","acuan":"SKKNI 382-2013"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063122","jabatan_kerja":"Operator Pemula Mesin Pencampur Aspal","acuan":"SKKNI 382-2013"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063123","jabatan_kerja":"Operator Mesin Penggelar Aspal","acuan":"SKKNI 383-2013"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063124","jabatan_kerja":"Operator Pemula Mesin Penggelar Aspal","acuan":"SKKNI 383-2013"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063125","jabatan_kerja":"Operator Mesin Pemecah Batu","acuan":"SKK Khusus Reg.42-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063126","jabatan_kerja":"Operator Pemula Mesin Pemecah Batu","acuan":"SKK Khusus Reg.42-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063127","jabatan_kerja":"Operator Mesin Penghampar Beton Semen","acuan":"SKK Khusus Reg.41-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063128","jabatan_kerja":"Operator Pemula Mesin Penghampar Beton Semen","acuan":"SKK Khusus Reg.41-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063012","jabatan_kerja":"Operator Cold Milling Machine","acuan":"SKK Khusus Reg.40-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063129","jabatan_kerja":"Operator Pemula Cold Milling Machine","acuan":"SKK Khusus Reg.40-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063029","jabatan_kerja":"Operator Batching Plant","acuan":"SKK Khusus Reg.39-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063130","jabatan_kerja":"Operator Pemula Batching Plant","acuan":"SKK Khusus Reg.39-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063131","jabatan_kerja":"Operator Hydrolic Hammer Breaker","acuan":"SKKNI 158-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063132","jabatan_kerja":"Operator Pemula Hydrolic Hammer Breaker","acuan":"SKKNI 158-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063133","jabatan_kerja":"Operator Ripper Tractor","acuan":"SKKNI 165-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063134","jabatan_kerja":"Operator Pemula Ripper Tractor","acuan":"SKKNI 165-2019"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063135","jabatan_kerja":"Mekanik Tower Crane","acuan":"SKK Khusus Reg.34-2022"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063005","jabatan_kerja":"Mekanik Asphalt Mixing Plant","acuan":"SKKNI 326-2009"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063002","jabatan_kerja":"Mekanik Kapal Keruk","acuan":"SKKNI 70-2009"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063141","jabatan_kerja":"Mekanik Engine Tingkat Dasar","acuan":"SKKNI 382-2015"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063136","jabatan_kerja":"Mekanik Engine Pemula Tingkat Dasar","acuan":"SKKNI 382-2015"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063137","jabatan_kerja":"Mekanik Hidrolik Alat Berat","acuan":"SKKNI 88-2010"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063138","jabatan_kerja":"Mekanik Hidrolik Alat Berat Pemula","acuan":"SKKNI 88-2010"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":3,"id_jabatan":"ME063140","jabatan_kerja":"Mekanik Engine Alat Berat","acuan":"SKKNI 235-2023"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063139","jabatan_kerja":"Mekanik Engine Alat Berat Pemula","acuan":"SKKNI 235-2023"},
    {"kode_klasifikasi":"ME","klasifikasi":"MEKANIKAL","sub_klasifikasi":"Alat Berat","kualifikasi":"Operator","jenjang":2,"id_jabatan":"ME063027","jabatan_kerja":"Operator Dump Truck","acuan":"SKKNI 132-2015"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","jenjang":9,"id_jabatan":"AL011009","jabatan_kerja":"Arsitek Lanskap Utama","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"AL011010","jabatan_kerja":"Arsitek Lanskap Madya","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"AL011011","jabatan_kerja":"Arsitek Lanskap Muda","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"AL011012","jabatan_kerja":"Manajer Lanskap Madya","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"AL011013","jabatan_kerja":"Manajer Lanskap Muda","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi/Analis","jenjang":6,"id_jabatan":"AL012006","jabatan_kerja":"Pengawas Lanskap (Level 6)","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"AL012007","jabatan_kerja":"Pengawas Lanskap (Level 5)","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"AL012008","jabatan_kerja":"Pelaksana Lanskap (Level 5)","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Teknisi/Analis","jenjang":4,"id_jabatan":"AL012009","jabatan_kerja":"Pelaksana Lanskap (Level 4)","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Operator","jenjang":3,"id_jabatan":"AL013004","jabatan_kerja":"Juru Tanam","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Operator","jenjang":2,"id_jabatan":"AL013005","jabatan_kerja":"Juru Tanam Pemula","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Operator","jenjang":1,"id_jabatan":"AL013006","jabatan_kerja":"Tukang Taman","acuan":"SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"kode_klasifikasi":"AL","klasifikasi":"ARSITEKTUR LANSKAP, TEKNIK ILUMINASI, DESAIN INTERIOR","sub_klasifikasi":"Arsitektur Lanskap","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"AL011008","jabatan_kerja":"Arsitek Lanskap Muda (Freshgraduate)","acuan":"SKKNI 209-2013"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Ahli","jenjang":9,"id_jabatan":"AR011001","jabatan_kerja":"Arsitek Utama","acuan":"SKKNI 196-2021"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"AR011002","jabatan_kerja":"Arsitek Madya","acuan":"SKKNI 196-2021"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"AR011004","jabatan_kerja":"Asisten Arsitek","acuan":"SKKNI 196-2021"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Teknisi/Analis","jenjang":6,"id_jabatan":"AR012001","jabatan_kerja":"Asisten Pemula Arsitek","acuan":"SKKNI 196-2021"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Teknisi/Analis","jenjang":6,"id_jabatan":"AR012003","jabatan_kerja":"Pengawas Lapangan Bidang Arsitektur (Level 6)","acuan":"SKKNI 196-2021"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"AR012004","jabatan_kerja":"Pengawas Lapangan Bidang Arsitektur (Level 5)","acuan":"SKKNI 196-2021"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Teknisi/Analis","jenjang":4,"id_jabatan":"AR012005","jabatan_kerja":"Juru Gambar Kepala Bidang Arsitektur","acuan":"SKK-Khusus 36-2022"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Operator","jenjang":3,"id_jabatan":"AR013003","jabatan_kerja":"Juru Gambar Arsitektur","acuan":"SKK-Khusus 36-2022"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Operator","jenjang":2,"id_jabatan":"AR013004","jabatan_kerja":"Juru Gambar Pemula Arsitektur","acuan":"SKK-Khusus 36-2022"},
    {"kode_klasifikasi":"AR","klasifikasi":"ARSITEKTUR","sub_klasifikasi":"Arsitektural","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"AR011005","jabatan_kerja":"Asisten Arsitek (Freshgraduate)","acuan":"SKKNI 196-2021"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Air Limbah","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"SI121102","jabatan_kerja":"Ahli Madya Teknik Bangunan Air Limbah (SPALD)","acuan":"SKKNI 29-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Air Limbah","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI121001","jabatan_kerja":"Ahli Muda Teknik Bangunan Air Limbah (SPALD)","acuan":"SKKNI 29-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Air Limbah","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"SI122003","jabatan_kerja":"Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Level 5)","acuan":"SKKNI 312-2009"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Air Limbah","kualifikasi":"Teknisi/Analis","jenjang":4,"id_jabatan":"SI122004","jabatan_kerja":"Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Level 4)","acuan":"SKKNI 312-2009"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Pelabuhan","kualifikasi":"Ahli","jenjang":9,"id_jabatan":"SI191004","jabatan_kerja":"Ahli Utama Teknik Dermaga","acuan":"SKKNI 320–2016"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Pelabuhan","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"SI191006","jabatan_kerja":"Ahli Madya Teknik Dermaga","acuan":"SKKNI 320–2016"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Pelabuhan","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI191005","jabatan_kerja":"Ahli Muda Teknik Dermaga","acuan":"SKKNI 320–2016"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Pelabuhan","kualifikasi":"Teknisi/Analis","jenjang":6,"id_jabatan":"SI192004","jabatan_kerja":"Pelaksana Perawatan Fasilitas Pelabuhan (Level 6)","acuan":"SKKNI 234 – 2019"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Pelabuhan","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"SI192005","jabatan_kerja":"Pelaksana Perawatan Fasilitas Pelabuhan (Level 5)","acuan":"SKKNI 234 – 2019"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Persampahan","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"SI131004","jabatan_kerja":"Ahli Madya Teknik Bangunan Persampahan (TPA)","acuan":"SKKNI 29-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Persampahan","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI131003","jabatan_kerja":"Ahli Muda Teknik Bangunan Persampahan (TPA)","acuan":"SKKNI 29-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Persampahan","kualifikasi":"Teknisi/Analis","jenjang":5,"id_jabatan":"SI132008","jabatan_kerja":"Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 5)","acuan":"SKKNI 29-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bangunan Persampahan","kualifikasi":"Teknisi/Analis","jenjang":4,"id_jabatan":"SI132009","jabatan_kerja":"Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 4)","acuan":"SKKNI 29-2023"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bendung dan Bendungan","kualifikasi":"Ahli","jenjang":9,"id_jabatan":"SI071012","jabatan_kerja":"Ahli Utama Teknik Bendungan Besar","acuan":"SKKNI 308–2016; SKKNI 124-2021"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bendung dan Bendungan","kualifikasi":"Ahli","jenjang":8,"id_jabatan":"SI071013","jabatan_kerja":"Ahli Madya Teknik Bendungan Besar","acuan":"SKKNI 308–2016; SKKNI 124-2021"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bendung dan Bendungan","kualifikasi":"Ahli","jenjang":7,"id_jabatan":"SI071014","jabatan_kerja":"Ahli Muda Teknik Bendungan Besar","acuan":"SKKNI 308–2016; SKKNI 124-2021"},
    {"kode_klasifikasi":"SI","klasifikasi":"SIPIL","sub_klasifikasi":"Bendung dan Bendungan","kualifikasi":"Ahli","jenjang":9,"id_jabatan
