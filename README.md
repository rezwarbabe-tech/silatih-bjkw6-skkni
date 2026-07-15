# ==============================================
# 1. MUAT PUSTAKA (WAJIB PALING ATAS)
# ==============================================
import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime, date

# ==============================================
# 2. KONFIGURASI APLIKASI
# ==============================================
st.set_page_config(
    page_title="Aplikasi Pelatihan & Sertifikasi UJI Kompetensi BJKW VI Makassar (siLATIH)",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Judul Utama
st.title("🏛️ Aplikasi Pelatihan & Sertifikasi UJI Kompetensi BJKW VI Makassar")
st.subheader("siLATIH - Sistem Informasi Pelatihan Terintegrasi")
st.markdown("---")

# ----------------------
# DATA JABATAN & PELATIHAN TERKAIT
# ----------------------
daftar_jabatan = [
    {"no": 1, "kode_jabatan": "SI-SDA-001", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021", "pelatihan": "Pelatihan Tingkat Lanjut Perencanaan & Pengelolaan Sumber Daya Air"},
    {"no": 2, "kode_jabatan": "SI-SDA-002", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021", "pelatihan": "Pelatihan Perencanaan Teknis Infrastruktur Air"},
    {"no": 3, "kode_jabatan": "SI-SDA-003", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021", "pelatihan": "Pelatihan Dasar Pemetaan & Analisis Sumber Daya Air"},
    {"no": 4, "kode_jabatan": "SI-JLN-001", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan & Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Rekayasa Jalan Raya", "acuan_skkni": "SKKNI 137-2022", "pelatihan": "Pelatihan Desain & Manajemen Proyek Jalan Utama"},
    {"no": 5, "kode_jabatan": "SI-GED-001", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Gedung", "kualifikasi": "Pengawas", "jenjang": 6, "nama_jabatan": "Pengawas Pelaksanaan Gedung", "acuan_skkni": "SKKNI 141-2021", "pelatihan": "Pelatihan Pengawasan Kualitas & Keselamatan Konstruksi Gedung"},
    {"no": 6, "kode_jabatan": "SI-BET-001", "klasifikasi": "SIPIL", "subklasifikasi": "Pekerjaan Beton", "kualifikasi": "Tukang", "jenjang": 4, "nama_jabatan": "Tukang Beton Terampil", "acuan_skkni": "SKKNI 135-2022", "pelatihan": "Pelatihan Teknik Pengecoran & Pengerjaan Beton"},
    {"no": 7, "kode_jabatan": "ME-ABT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022", "pelatihan": "Pelatihan Operasional & Perawatan Dasar Bulldozer"},
    {"no": 8, "kode_jabatan": "ME-ABG-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Ekskavator", "acuan_skkni": "SKKNI 91-2010", "pelatihan": "Pelatihan Teknik Operasi & Keselamatan Ekskavator"},
    {"no": 9, "kode_jabatan": "ME-MNT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Pemeliharaan Alat Berat", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Mekanik Alat Berat", "acuan_skkni": "SKKNI 190-2024", "pelatihan": "Pelatihan Diagnosa & Perbaikan Mesin Alat Berat"},
    {"no": 10, "kode_jabatan": "EL-ILG-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Instalasi Listrik", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Instalasi Listrik Terampil", "acuan_skkni": "SKKNI 130-2021", "pelatihan": "Pelatihan Instalasi Listrik Bangunan & Keamanan"},
    {"no": 11, "kode_jabatan": "EL-SRY-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Energi Terbarukan", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Pemasangan Panel Surya", "acuan_skkni": "SKKNI 241-2024", "pelatihan": "Pelatihan Pemasangan & Perawatan Sistem Panel Surya"},
    {"no": 12, "kode_jabatan": "K3-SMK-001", "klasifikasi": "KESELAMATAN KERJA", "subklasifikasi": "Sistem Manajemen K3", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan dan Kesehatan Kerja", "acuan_skkni": "SKKNI 119-2020", "pelatihan": "Pelatihan Audit & Penerapan Sistem Manajemen K3"},
    {"no": 13, "kode_jabatan": "MN-MPR-001", "klasifikasi": "MANAJEMEN PROYEK", "subklasifikasi": "Manajemen Proyek", "kualifikasi": "Manajer", "jenjang": 9, "nama_jabatan": "Manajer Proyek Utama", "acuan_skkni": "SKKNI 145-2021", "pelatihan": "Pelatihan Manajemen Risiko & Pengendalian Proyek"}
]

df = pd.DataFrame(daftar_jabatan)

# ----------------------
# NAVIGASI APLIKASI
# ----------------------
tab1, tab2, tab3 = st.tabs(["📚 Daftar Jabatan & Pelatihan", "📝 Formulir Pendaftaran", "📋 Data Pendaftar"])

# ==============================================
# TAB 1: DAFTAR JABATAN & PELATIHAN
# ==============================================
with tab1:
    st.header("Daftar Jabatan dan Pelatihan Terkait")
    st.subheader("Berdasarkan Standar Kompetensi Kerja Nasional Indonesia (SKKNI)")

    # Filter
    st.sidebar.header("🔎 Filter Data")
    pilih_klasifikasi = st.sidebar.multiselect("Bidang Klasifikasi", options=sorted(df["klasifikasi"].unique()))
    df_filter = df.copy()
    if pilih_klasifikasi:
        df_filter = df_filter[df_filter["klasifikasi"].isin(pilih_klasifikasi)]

    pilih_kualifikasi = st.sidebar.multiselect("Kualifikasi", options=sorted(df_filter["kualifikasi"].unique()))
    if pilih_kualifikasi:
        df_filter = df_filter[df_filter["kualifikasi"].isin(pilih_kualifikasi)]

    kata_kunci = st.text_input("Cari Nama Jabatan / Kode / Pelatihan:")
    if kata_kunci:
        df_filter = df_filter[
            df_filter["nama_jabatan"].str.contains(kata_kunci, case=False) |
            df_filter["kode_jabatan"].str.contains(kata_kunci, case=False) |
            df_filter["pelatihan"].str.contains(kata_kunci, case=False)
        ]

    st.info(f"✅ Ditemukan {len(df_filter)} jabatan dengan pelatihan terkait")
    st.dataframe(df_filter, use_container_width=True, hide_index=True)

    # Unduh Data
    st.subheader("📥 Unduh Daftar Lengkap")
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df_filter.to_excel(writer, index=False, sheet_name="Daftar Pelatihan")
    st.download_button(
        label="Unduh Excel (.xlsx)",
        data=buffer.getvalue(),
        file_name="Daftar_Pelatihan_SKKNI.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ==============================================
# TAB 2: FORMULIR PENDAFTARAN
# ==============================================
with tab2:
    st.header("Formulir Pendaftaran Pelatihan")
    st.subheader("Pilih jabatan yang sesuai, lalu isi data diri Anda")

    # Pilih Jabatan & Pelatihan Otomatis
    pilihan_jabatan = st.selectbox("Pilih Jabatan Kerja", options=df["nama_jabatan"])
    data_terpilih = df[df["nama_jabatan"] == pilihan_jabatan].iloc[0]

    st.info(f"📋 Pelatihan yang tersedia untuk jabatan ini: **{data_terpilih['pelatihan']}**")
    st.write(f"Kode Jabatan: {data_terpilih['kode_jabatan']} | Acuan SKKNI: {data_terpilih['acuan_skkni']}")

    # Isian Data Peserta
    with st.form("form_pendaftaran"):
        st.subheader("Data Diri Peserta")
        nama_lengkap = st.text_input("Nama Lengkap *")
        nik = st.text_input("NIK / Nomor Identitas *")
        instansi = st.text_input("Instansi / Perusahaan / Sekolah *")
        jabatan_sekarang = st.text_input("Jabatan yang diemban sekarang")
        no_hp = st.text_input("Nomor HP / WhatsApp *")
        email = st.text_input("Alamat Email *")
        alamat = st.text_area("Alamat Lengkap")
        pengalaman = st.slider("Pengalaman Kerja (Tahun)", 0, 30, 1)

        tombol_kirim = st.form_submit_button("✅ Kirim Pendaftaran")

        if tombol_kirim:
            if not all([nama_lengkap, nik, instansi, no_hp, email]):
                st.error("❌ Isian bertanda * wajib diisi semua!")
            else:
                waktu_daftar = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                data_baru = {
                    "Waktu Daftar": waktu_daftar,
                    "Nama Lengkap": nama_lengkap,
                    "NIK": nik,
                    "Instansi": instansi,
                    "Jabatan Terpilih": pilihan_jabatan,
                    "Pelatihan yang Diambil": data_terpilih['pelatihan'],
                    "Kode Jabatan": data_terpilih['kode_jabatan'],
                    "Jabatan Sekarang": jabatan_sekarang,
                    "No HP/WA": no_hp,
                    "Email": email,
                    "Alamat": alamat,
                    "Pengalaman (Tahun)": pengalaman
                }
                st.session_state.data_pendaftaran.append(data_baru)
                st.success(f"🎉 Pendaftaran Anda berhasil dicatat! Terima kasih {nama_lengkap}.")
                st.balloons()

# ==============================================
# TAB 3: DATA PENDAFTAR
# ==============================================
with tab3:
    st.header("Daftar Peserta yang Sudah Mendaftar")
    if len(st.session_state.data_pendaftaran) == 0:
        st.info("Belum ada pendaftar baru. Silakan tunggu peserta mengisi formulir.")
    else:
        df_pendaftar = pd.DataFrame(st.session_state.data_pendaftaran)
        st.dataframe(df_pendaftar, use_container_width=True, hide_index=True)
        st.info(f"Total pendaftar: {len(df_pendaftar)} orang")

        # Unduh Data Pendaftar
        buffer2 = BytesIO()
        with pd.ExcelWriter(buffer2, engine='openpyxl') as writer:
            df_pendaftar.to_excel(writer, index=False, sheet_name="Data Pendaftar")
        st.download_button(
            label="Unduh Data Pendaftar Excel (.xlsx)",
            data=buffer2.getvalue(),
            file_name="Data_Pendaftaran_Pelatihan.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
