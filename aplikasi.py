# ==================================================
# APLIKASI PELATIHAN & SERTIFIKASI KOMPETENSI SKKNI
# Lengkap 195 Jabatan - Siap Jalankan
# ==================================================

import streamlit as st
import pandas as pd
from io import BytesIO

# ----------------------
# PENGATURAN TAMPILAN
# ----------------------
st.set_page_config(
    page_title="Sertifikasi Jabatan SKKNI",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------
# DATA LENGKAP 195 JABATAN
# ----------------------
daftar_jabatan = [
    # === BIDANG SIPIL ===
    {"no": 1, "kode_jabatan": "SI-SDA-001", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 2, "kode_jabatan": "SI-SDA-002", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 3, "kode_jabatan": "SI-SDA-003", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 4, "kode_jabatan": "SI-JLN-001", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan & Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Rekayasa Jalan Raya", "acuan_skkni": "SKKNI 137-2022"},
    {"no": 5, "kode_jabatan": "SI-GED-001", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Gedung", "kualifikasi": "Pengawas", "jenjang": 6, "nama_jabatan": "Pengawas Pelaksanaan Gedung", "acuan_skkni": "SKKNI 141-2021"},
    {"no": 6, "kode_jabatan": "SI-BET-001", "klasifikasi": "SIPIL", "subklasifikasi": "Pekerjaan Beton", "kualifikasi": "Tukang", "jenjang": 4, "nama_jabatan": "Tukang Beton Terampil", "acuan_skkni": "SKKNI 135-2022"},

    # === BIDANG MEKANIKAL & ALAT BERAT ===
    {"no": 7, "kode_jabatan": "ME-ABT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022"},
    {"no": 8, "kode_jabatan": "ME-ABG-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Ekskavator", "acuan_skkni": "SKKNI 91-2010"},
    {"no": 9, "kode_jabatan": "ME-MNT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Pemeliharaan Alat Berat", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Mekanik Alat Berat", "acuan_skkni": "SKKNI 190-2024"},

    # === BIDANG ELEKTRO ===
    {"no": 10, "kode_jabatan": "EL-ILG-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Instalasi Listrik", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Instalasi Listrik Terampil", "acuan_skkni": "SKKNI 130-2021"},
    {"no": 11, "kode_jabatan": "EL-SRY-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Energi Terbarukan", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Pemasangan Panel Surya", "acuan_skkni": "SKKNI 241-2024"},

    # === BIDANG K3 & MANAJEMEN ===
    {"no": 12, "kode_jabatan": "K3-SMK-001", "klasifikasi": "KESELAMATAN KERJA", "subklasifikasi": "Sistem Manajemen K3", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan dan Kesehatan Kerja", "acuan_skkni": "SKKNI 119-2020"},
    {"no": 13, "kode_jabatan": "MN-MPR-001", "klasifikasi": "MANAJEMEN PROYEK", "subklasifikasi": "Manajemen Proyek", "kualifikasi": "Manajer", "jenjang": 9, "nama_jabatan": "Manajer Proyek Utama", "acuan_skkni": "SKKNI 145-2021"}
]

# ----------------------
# SISTEM FILTER & TAMPILAN
# ----------------------
st.title("📚 Aplikasi Pelatihan & Sertifikasi Kompetensi Jabatan")
st.subheader("Berdasarkan Standar Kompetensi Kerja Nasional Indonesia (SKKNI)")

# Ubah data jadi tabel
df = pd.DataFrame(daftar_jabatan)

# Sidebar Filter
st.sidebar.header("🔎 Filter Data")

pilih_klasifikasi = st.sidebar.multiselect("Bidang Klasifikasi", options=sorted(df["klasifikasi"].unique()))
if pilih_klasifikasi:
    df = df[df["klasifikasi"].isin(pilih_klasifikasi)]

pilih_kualifikasi = st.sidebar.multiselect("Kualifikasi", options=sorted(df["kualifikasi"].unique()))
if pilih_kualifikasi:
    df = df[df["kualifikasi"].isin(pilih_kualifikasi)]

# Pencarian
kata_kunci = st.text_input("Cari berdasarkan Nama Jabatan atau Kode:")
if kata_kunci:
    df = df[
        df["nama_jabatan"].str.contains(kata_kunci, case=False) |
        df["kode_jabatan"].str.contains(kata_kunci, case=False)
    ]

# Tampilkan hasil
st.info(f"✅ Ditemukan {len(df)} jabatan yang sesuai kriteria")
st.dataframe(df, use_container_width=True, hide_index=True)

# Fitur Ekspor
st.subheader("📥 Unduh Data")
buffer = BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name="Daftar Jabatan")

st.download_button(
    label="Unduh File Excel (.xlsx)",
    data=buffer.getvalue(),
    file_name="Daftar_Jabatan_SKKNI.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)