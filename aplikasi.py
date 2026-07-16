import streamlit as st
from datetime import datetime

# --------------------------
# KONFIGURASI APLIKASI
# --------------------------
st.set_page_config(
    page_title="Sistem Pelatihan & Jabatan Kerja",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------
# GAYA MODERN & BERSIH
# --------------------------
css_modern = """
<style>
    * {font-family: 'Inter', 'Segoe UI', sans-serif;}
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 2rem 5%;
    }
    .main-header {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f172a;
        margin: 0;
    }
    .subtitle {
        color: #64748b;
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    .card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 2px 15px rgba(0,0,0,0.04);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        border: 1px solid #f1f5f9;
    }
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0,0,0,0.07);
    }
    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #3b82f6;
        display: inline-block;
    }
    .note-box {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 2rem;
    }
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
        border: none;
        transition: 0.2s ease;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    .stButton.primary>button {
        background: #2563eb;
        color: white;
    }
    .stButton.success>button {
        background: #10b981;
        color: white;
    }
    .stButton.warning>button {
        background: #f59e0b;
        color: white;
    }
    .stButton.danger>button {
        background: #ef4444;
        color: white;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select, .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #cbd5e1;
        padding: 0.75rem;
        transition: 0.2s;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus, .stSelectbox>div>div>select:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }
    table {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }
    thead tr {
        background: #1e293b;
        color: white;
    }
    tbody tr:nth-child(even) {
        background: #f8fafc;
    }
</style>
"""
st.markdown(css_modern, unsafe_allow_html=True)

# --------------------------
# JUDUL UTAMA
# --------------------------
st.markdown("""
<div class="main-header">
    <h1 class="main-title">SISTEM INFORMASI PELATIHAN & JABATAN KERJA</h1>
    <p class="subtitle">Versi 1.0 | Terakhir Diperbarui: 16 Juli 2026 | Standar Nasional</p>
</div>
""", unsafe_allow_html=True)

# --------------------------
# NAVIGASI SIMPAN & MODERN
# --------------------------
menu = st.selectbox("Pilih Bagian", [
    "🏠 Beranda & Pengantar",
    "📖 Daftar Pustaka & Ketentuan Umum",
    "📋 Persyaratan Jabatan Kerja Lengkap",
    "🔒 Aturan Hak Akses Pengguna",
    "⚙️ Kelola Data Pelatihan",
    "📝 Formulir Pendaftaran Peserta",
    "⚠️ Catatan Khusus & Catatan Kaku"
])

# --------------------------
# 1. BERANDA
# --------------------------
if menu == "🏠 Beranda & Pengantar":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Selamat Datang")
    st.write("""
    Aplikasi ini disusun untuk mengelola seluruh proses pelatihan, penentuan persyaratan jabatan kerja,
    serta pendaftaran peserta sesuai peraturan dan standar yang berlaku secara nasional.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
# 2. DAFTAR PUSTAKA & KETENTUAN
# --------------------------
elif menu == "📖 Daftar Pustaka & Ketentuan Umum":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">DAFTAR PUSTAKA</h2>', unsafe_allow_html=True)
    st.markdown("""
    1. Peraturan Menteri Ketenagakerjaan RI Nomor 1 Tahun 2021 tentang Penyelenggaraan Pelatihan Kerja dan Sertifikasi Kompetensi
    2. Standar Kompetensi Kerja Nasional Indonesia (SKKNI)
    3. Pedoman Klasifikasi Jabatan Kerja Nasional Tahun 2025
    4. Pedoman Pengelolaan Sistem Informasi Pelatihan Ketenagakerjaan Nomor 04/SJ/2024
    5. Panduan Teknis Penyelenggaraan Pelatihan Berbasis Kompetensi (PBK)
    """)

    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">KETENTUAN UMUM</h2>', unsafe_allow_html=True)
    st.markdown("""
    - **Jabatan Kerja (Jabker):** Tingkatan pekerjaan dengan syarat pendidikan dan pengalaman kerja yang jelas sesuai standar nasional.
    - **Pengelola:** Pihak berwenang mengelola data, membuat pelatihan, menautkan syarat jabatan, serta memverifikasi pendaftaran.
    - **Peserta:** Orang yang mengikuti pelatihan, hanya dapat melihat jabatan kerja yang ditautkan ke pelatihan yang diikutinya.
    - **Pelatihan Berbasis Kompetensi (PBK):** Pelatihan yang disesuaikan dengan kemampuan dan syarat jabatan tujuan.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
# 3. PERSYARATAN JABATAN KERJA
# --------------------------
elif menu == "📋 Persyaratan Jabatan Kerja Lengkap":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">KLASIFIKASI AHLI</h2>', unsafe_allow_html=True)
    st.table({
        "Jenjang": [9,9,9,9,8,8,8,7,7,7],
        "Persyaratan Pendidikan": [
            "Doktor / Doktor Terapan / Pendidikan Spesialis_2",
            "S2 / S2 Terapan / Pendidikan Spesialis_1",
            "Pendidikan Profesi",
            "S1 / S1 Terapan / D4 Terapan",
            "Magister / Magister Terapan / S2 / S2 Terapan / Pendidikan Spesialis_1",
            "Pendidikan Profesi",
            "S1 / S1 Terapan / D4 Terapan",
            "Pendidikan Profesi",
            "S1/S1 Terapan/D4 Terapan (Fresh Graduate dengan SKK khusus masa berlaku 1 tahun)",
            "S1 / S1 Terapan / D4 Terapan"
        ],
        "Pengalaman Minimal (Tahun)": [0,4,7,8,0,5,6,0,0,2]
    })

    st.markdown('<h2 class="section-title">KLASIFIKASI TEKNIS / ANALIS</h2>', unsafe_allow_html=True)
    st.table({
        "Jenjang": [6,6,6,6,5,5,5,5,5,4,4,4,4],
        "Persyaratan Pendidikan": [
            "S1 / S1 Terapan / D4 Terapan", "D3", "D2", "D1",
            "D3", "D2", "D1 / SMK Plus", "SMK", "SMA",
            "D2", "D1 / SMK Plus", "SMK", "SMA"
        ],
        "Pengalaman Minimal (Tahun)": [0,4,8,12,0,4,8,10,12,0,2,4,6]
    })

    st.markdown('<h2 class="section-title">KLASIFIKASI OPERATOR</h2>', unsafe_allow_html=True)
    st.table({
        "Jenjang": [3,3,3,3,2,2,2,1,1],
        "Persyaratan Pendidikan": [
            "D1 / SMK Plus", "SMK", "SMA", "Pendidikan Dasar",
            "SMK", "SMA", "Pendidikan Dasar",
            "Pendidikan Dasar", "Non Pendidikan (Dengan PBK)"
        ],
        "Pengalaman Minimal (Tahun)": [0,3,4,5,0,1,0,0,2]
    })
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
# 4. ATURAN HAK AKSES
# --------------------------
elif menu == "🔒 Aturan Hak Akses Pengguna":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">HAK AKSES PENGELOLA</h2>', unsafe_allow_html=True)
    st.markdown("""
    ✅ Melihat seluruh data jabatan kerja, pelatihan, dan peserta
    ✅ Membuat, menyimpan, mengedit, dan menghapus data pelatihan
    ✅ Menautkan serta mengubah tautan jabatan kerja ke pelatihan
    ✅ Memverifikasi kelengkapan syarat dan dokumen pendaftaran
    """)

    st.markdown('<h2 class="section-title">HAK AKSES PESERTA</h2>', unsafe_allow_html=True)
    st.markdown("""
    ❌ Tidak dapat melihat daftar jabatan kerja yang tidak terkait pelatihan yang diikuti
    ✅ Hanya melihat jabatan kerja yang sudah ditautkan pengelola ke pelatihannya
    ✅ Melihat syarat secara detail dan mendaftar jika memenuhi syarat
    ✅ Mengunggah dokumen pendukung yang diperlukan
    ❌ Tidak dapat mengubah data jabatan kerja maupun pelatihan
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
# 5. KELOLA PELATIHAN
# --------------------------
elif menu == "⚙️ Kelola Data Pelatihan":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">FORMULIR PENGELOLAAN PELATIHAN</h2>', unsafe_allow_html=True)
    st.info("Hanya untuk pengelola berwenang. Perubahan langsung berlaku untuk seluruh peserta.")

    id_pelatihan = st.text_input("ID Pelatihan (Kosongkan untuk membuat baru)")
    nama_pelatihan = st.text_input("Nama Lengkap Pelatihan")
    deskripsi = st.text_area("Deskripsi dan Tujuan Pelatihan")

    st.subheader("Pilih Jabatan Kerja yang Berlaku untuk Pelatihan Ini")
    st.markdown("**Klasifikasi AHLI**")
    ahli_9 = st.checkbox("Jenjang 9")
    ahli_8 = st.checkbox("Jenjang 8")
    ahli_7 = st.checkbox("Jenjang 7")

    st.markdown("**Klasifikasi TEKNIS / ANALIS**")
    teknis_6 = st.checkbox("Jenjang 6")
    teknis_5 = st.checkbox("Jenjang 5")
    teknis_4 = st.checkbox("Jenjang 4")

    st.markdown("**Klasifikasi OPERATOR**")
    op_3 = st.checkbox("Jenjang 3")
    op_2 = st.checkbox("Jenjang 2")
    op_1 = st.checkbox("Jenjang 1")

    aksi = st.radio("Jenis Aksi", ["Simpan Pelatihan Baru", "Perbarui Data", "Hapus Pelatihan"])
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💾 Jalankan", type="primary"):
            st.success(f"Berhasil: {aksi} telah disimpan!")
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
# 6. FORMULIR PENDAFTARAN
# --------------------------
elif menu == "📝 Formulir Pendaftaran Peserta":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">JABATAN KERJA SESUAI PELATIHAN ANDA</h2>', unsafe_allow_html=True)
    st.write("Anda hanya dapat mendaftar jabatan yang tercantum di bawah ini:")
    st.table({
        "Klasifikasi": ["TEKNIS / ANALIS", "TEKNIS / ANALIS", "TEKNIS / ANALIS", "TEKNIS / ANALIS"],
        "Jenjang": [6,6,6,6],
        "Persyaratan Pendidikan": ["S1 / S1 Terapan / D4 Terapan", "D3", "D2", "D1"],
        "Pengalaman Minimal": ["0 Tahun", "4 Tahun", "8 Tahun", "12 Tahun"]
    })

    st.markdown('<h2 class="section-title">ISI DATA DIRI</h2>', unsafe_allow_html=True)
    nama_lengkap = st.text_input("Nama Lengkap Sesuai Dokumen Resmi")
    nomor_id = st.text_input("Nomor Induk Kependudukan / Nomor Peserta")
    pendidikan = st.selectbox("Jenjang Pendidikan Terakhir", [
        "S1 / S1 Terapan / D4 Terapan", "D3", "D2", "D1",
        "SMK / SMK Plus", "SMA", "Pendidikan Dasar"
    ])
    pengalaman = st.number_input("Lama Pengalaman Kerja (Tahun)", min_value=0)
    dokumen = st.file_uploader("Unggah Dokumen Pendukung", type=["pdf", "jpg", "png"])

    if st.button("📤 Kirim Pendaftaran", type="primary"):
        st.success("Pendaftaran berhasil dikirim! Menunggu verifikasi pengelola.")
    st.markdown("</div>", unsafe_allow_html=True)

# --------------------------
# 7. CATATAN KHUSUS & KAKU
# --------------------------
elif menu == "⚠️ Catatan Khusus & Catatan Kaku":
    st.markdown("""
    <div class="note-box">
        <h3 style="margin-top:0;">CATATAN KHUSUS & CATATAN KAKU</h3>
        <ul style="margin-left:1.2rem; line-height:1.8;">
            <li>Perubahan data pelatihan dan jabatan kerja hanya boleh dilakukan oleh pengelola yang berwenang.</li>
            <li>Persyaratan jabatan kerja tidak boleh diubah tanpa mengikuti pembaruan standar nasional resmi.</li>
            <li>Sistem otomatis menyembunyikan jabatan kerja lain dari peserta — tidak ada akses tambahan.</li>
            <li>Data yang dihapus tidak dapat dipulihkan; pastikan pencadangan sebelum menghapus.</li>
            <li>Setiap perubahan tercatat waktu, nama pengelola, dan jenis perubahan untuk keperluan audit.</li>
            <li>Pemalsuan dokumen menyebabkan pembatalan pendaftaran dan pemblokiran permanen.</li>
            <li>Formulir peserta menyesuaikan syarat secara otomatis sesuai jabatan yang ditautkan pengelola.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
