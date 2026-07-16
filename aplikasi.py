import streamlit as st
from datetime import datetime

# --------------------------
# KONFIGURASI UTAMA APLIKASI
# --------------------------
st.set_page_config(
    page_title="Sistem Informasi Pelatihan & Jabatan Kerja",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------
# GAYA VISUAL APLIKASI (TIDAK MENGUBAH ISI)
# --------------------------
css_aplikasi = """
<style>
    .stApp {background-color: #f8fafc;}
    .css-18e3th9 {padding-top: 1rem;}
    .sidebar .sidebar-content {background-color: #1e293b; color: white;}
    .sidebar .sidebar-content a {color: #cbd5e1;}
    .sidebar .sidebar-content a:hover {color: white;}
    .judul-utama {color: #1e40af; font-weight: 700; margin-bottom: 0.5rem;}
    .sub-judul {color: #334155; font-weight: 600; margin-top: 1.5rem;}
    .kartu {background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 1.5rem;}
    .catatan-khusus {background: #fffbeb; border-left: 5px solid #f59e0b; padding: 1rem; border-radius: 8px;}
    .info-sistem {background: #eff6ff; border-left: 5px solid #3b82f6; padding: 1rem; border-radius: 8px;}
    .stButton>button {border-radius: 6px; font-weight: 500;}
    .stButton.utama>button {background-color: #2563eb; color: white; width: 100%;}
    .stButton.sukses>button {background-color: #16a34a; color: white;}
    .stButton.peringatan>button {background-color: #f59e0b; color: white;}
    .stButton.bahaya>button {background-color: #dc2626; color: white;}
    hr {border: 1px solid #e2e8f0; margin: 1.5rem 0;}
</style>
"""
st.markdown(css_aplikasi, unsafe_allow_html=True)

# --------------------------
# MENU NAVIGASI APLIKASI
# --------------------------
with st.sidebar:
    st.image("https://via.placeholder.com/250x60?text=LOGO+PELATIHAN", use_column_width=True)
    st.title("📋 Menu Aplikasi")
    menu = st.radio("Pilih Halaman", [
        "🏠 Beranda",
        "📖 Daftar Pustaka & Ketentuan",
        "📊 Persyaratan Jabatan Kerja",
        "🔐 Aturan Hak Akses",
        "⚙️ Pengelolaan Pelatihan",
        "📝 Pendaftaran Peserta",
        "⚠️ Catatan Khusus & Kaku"
    ])
    st.markdown("---")
    st.info(f"Versi Aplikasi: 1.0 | Terakhir Diperbarui: 16 Juli 2026")

# --------------------------
# HALAMAN BERANDA
# --------------------------
if menu == "🏠 Beranda":
    st.markdown('<h1 class="judul-utama">SISTEM INFORMASI PELATIHAN & JABATAN KERJA</h1>', unsafe_allow_html=True)
    st.markdown('<div class="info-sistem">', unsafe_allow_html=True)
    st.subheader("Selamat Datang di Aplikasi")
    st.write("""
    Aplikasi ini digunakan untuk mengelola data pelatihan, menautkan persyaratan jabatan kerja,
    serta memfasilitasi pendaftaran peserta sesuai ketentuan yang berlaku.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="kartu">', unsafe_allow_html=True)
        st.metric("Total Klasifikasi Jabatan", "3")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="kartu">', unsafe_allow_html=True)
        st.metric("Total Jenjang Jabatan", "9")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="kartu">', unsafe_allow_html=True)
        st.metric("Status Sistem", "Aktif")
        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# HALAMAN DAFTAR PUSTAKA & KETENTUAN
# --------------------------
elif menu == "📖 Daftar Pustaka & Ketentuan":
    st.markdown('<h2 class="judul-utama">DAFTAR PUSTAKA</h2>', unsafe_allow_html=True)
    st.markdown('<div class="kartu">', unsafe_allow_html=True)
    st.markdown("""
    1. Peraturan Menteri Ketenagakerjaan Republik Indonesia Nomor 1 Tahun 2021 tentang Penyelenggaraan Pelatihan Kerja dan Sertifikasi Kompetensi
    2. Standar Kompetensi Kerja Nasional Indonesia (SKKNI) Bidang Pelatihan & Pengembangan SDM
    3. Pedoman Klasifikasi Jabatan Kerja Nasional Tahun 2025
    4. Pedoman Pengelolaan Sistem Informasi Pelatihan Ketenagakerjaan Nomor 04/SJ/2024
    5. Panduan Teknis Penyelenggaraan Pelatihan Berbasis Kompetensi (PBK)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<h2 class="sub-judul">KETENTUAN UMUM</h2>', unsafe_allow_html=True)
    st.markdown('<div class="kartu">', unsafe_allow_html=True)
    st.markdown("""
    - **Jabatan Kerja (Jabker):** Susunan tingkatan pekerjaan yang memiliki syarat pendidikan dan pengalaman kerja yang jelas sesuai standar nasional.
    - **Pengelola:** Pihak yang berwenang mengelola seluruh data sistem, membuat pelatihan, menautkan persyaratan jabatan kerja, serta memverifikasi pendaftaran.
    - **Peserta:** Orang yang mengikuti pelatihan berhak mendaftar jabatan kerja sesuai tautan yang ditetapkan pengelola.
    - **Pelatihan Berbasis Kompetensi (PBK):** Pelatihan yang disesuaikan dengan kemampuan dan syarat jabatan yang dituju.
    - **SKK:** Sertifikat Kompetensi Kerja yang menjadi bukti pengakuan kemampuan peserta.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# HALAMAN PERSYARATAN JABATAN KERJA
# --------------------------
elif menu == "📊 Persyaratan Jabatan Kerja":
    st.markdown('<h2 class="judul-utama">PERSYARATAN JABATAN KERJA LENGKAP</h2>', unsafe_allow_html=True)

    st.markdown('<h3 class="sub-judul">🟡 Klasifikasi: AHLI</h3>', unsafe_allow_html=True)
    st.markdown('<div class="kartu">', unsafe_allow_html=True)
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
            "S1/S1 Terapan/D4 Terapan (Dengan Pemberian Kompetensi Tambahan untuk Fresh Graduated, masa berlaku SKK = 1)",
            "S1 / S1 Terapan / D4 Terapan"
        ],
        "Pengalaman Minimal (Tahun)": [0,4,7,8,0,5,6,0,0,2]
    })
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<h3 class="sub-judul">🔵 Klasifikasi: TEKNIS / ANALIS</h3>', unsafe_allow_html=True)
    st.markdown('<div class="kartu">', unsafe_allow_html=True)
    st.table({
        "Jenjang": [6,6,6,6,5,5,5,5,5,4,4,4,4],
        "Persyaratan Pendidikan": [
            "S1 / S1 Terapan / D4 Terapan", "D3", "D2", "D1",
            "D3", "D2", "D1 / SMK Plus", "SMK", "SMA",
            "D2", "D1 / SMK Plus", "SMK", "SMA"
        ],
        "Pengalaman Minimal (Tahun)": [0,4,8,12,0,4,8,10,12,0,2,4,6]
    })
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<h3 class="sub-judul">🟢 Klasifikasi: OPERATOR</h3>', unsafe_allow_html=True)
    st.markdown('<div class="kartu">', unsafe_allow_html=True)
    st.table({
        "Jenjang": [3,3,3,3,2,2,2,1,1],
        "Persyaratan Pendidikan": [
            "D1 / SMK Plus", "SMK", "SMA", "Pendidikan Dasar",
            "SMK", "SMA", "Pendidikan Dasar",
            "Pendidikan Dasar", "Non Pendidikan (Dengan PBK)"
        ],
        "Pengalaman Minimal (Tahun)": [0,3,4,5,0,1,0,0,2]
    })
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# HALAMAN ATURAN HAK AKSES
# --------------------------
elif menu == "🔐 Aturan Hak Akses":
    st.markdown('<h2 class="judul-utama">ATURAN HAK AKSES PENGGUNA</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="kartu">', unsafe_allow_html=True)
        st.subheader("✅ Hak Akses Pengelola")
        st.markdown("""
        - Melihat seluruh daftar jabatan kerja, pelatihan, dan data peserta
        - Membuat, menyimpan, mengedit, dan menghapus data pelatihan
        - Menautkan serta mengubah tautan jabatan kerja ke pelatihan
        - Memverifikasi kelengkapan syarat pendaftaran peserta
        - Mengubah status pelatihan dan pendaftaran
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="kartu">', unsafe_allow_html=True)
        st.subheader("✅ Hak Akses Peserta")
        st.markdown("""
        - ❌ Tidak dapat melihat seluruh daftar jabatan kerja yang tidak terkait pelatihan yang diikuti
        - ✅ Hanya melihat jabatan kerja yang sudah ditautkan pengelola ke pelatihannya
        - ✅ Melihat persyaratan secara detail dan mendaftar jika memenuhi syarat
        - ✅ Mengunggah dokumen pendukung sesuai syarat
        - ❌ Tidak dapat mengubah data jabatan kerja maupun pelatihan
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# HALAMAN PENGELOLAAN PELATIHAN
# --------------------------
elif menu == "⚙️ Pengelolaan Pelatihan":
    st.markdown('<h2 class="judul-utama">KELOLA DATA PELATIHAN</h2>', unsafe_allow_html=True)
    st.markdown('<div class="kartu">', unsafe_allow_html=True)
    st.info("Hanya untuk Pengelola Berwenang. Perubahan langsung berlaku untuk peserta.")

    id_pelatihan = st.text_input("ID Pelatihan (Kosongkan untuk buat baru)")
    nama_pelatihan = st.text_input("Nama Lengkap Pelatihan")
    deskripsi = st.text_area("Deskripsi & Tujuan Pelatihan")

    st.subheader("Pilih Jabatan Kerja yang Berlaku untuk Pelatihan Ini")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("**Klasifikasi AHLI**")
        ahli_9 = st.checkbox("Jenjang 9")
        ahli_8 = st.checkbox("Jenjang 8")
        ahli_7 = st.checkbox("Jenjang 7")
    with col_b:
        st.markdown("**Klasifikasi TEKNIS / ANALIS**")
        teknis_6 = st.checkbox("Jenjang 6")
        teknis_5 = st.checkbox("Jenjang 5")
        teknis_4 = st.checkbox("Jenjang 4")
    with col_c:
        st.markdown("**Klasifikasi OPERATOR**")
        op_3 = st.checkbox("Jenjang 3")
        op_2 = st.checkbox("Jenjang 2")
        op_1 = st.checkbox("Jenjang 1")

    aksi_pilih = st.radio("Jenis Aksi", ["Simpan Pelatihan Baru", "Perbarui Data Pelatihan", "Hapus Pelatihan"])
    col_simpan, col_ubah, col_hapus = st.columns(3)
    with col_simpan:
        if st.button("💾 Simpan", type="primary"):
            st.success("✅ Data pelatihan berhasil disimpan!")
    with col_ubah:
        if st.button("🔄 Perbarui"):
            st.success("✅ Data pelatihan berhasil diperbarui!")
    with col_hapus:
        if st.button("🗑️ Hapus"):
            st.warning("⚠️ Data pelatihan berhasil dihapus!")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# HALAMAN PENDAFTARAN PESERTA
# --------------------------
elif menu == "📝 Pendaftaran Peserta":
    st.markdown('<h2 class="judul-utama">FORMULIR PENDAFTARAN JABATAN KERJA</h2>', unsafe_allow_html=True)
    st.markdown('<div class="info-sistem">', unsafe_allow_html=True)
    st.subheader("Jabatan Kerja Sesuai Pelatihan yang Anda Ikuti")
    st.write("Anda hanya dapat mendaftar jabatan yang tercantum di bawah ini:")
    st.table({
        "Klasifikasi": ["TEKNIS / ANALIS", "TEKNIS / ANALIS", "TEKNIS / ANALIS", "TEKNIS / ANALIS"],
        "Jenjang": [6,6,6,6],
        "Persyaratan Pendidikan": ["S1 / S1 Terapan / D4 Terapan", "D3", "D2", "D1"],
        "Pengalaman Minimal": ["0 Tahun", "4 Tahun", "8 Tahun", "12 Tahun"]
    })
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="kartu">', unsafe_allow_html=True)
    st.subheader("Isi Data Diri & Dokumen")
    nama_lengkap = st.text_input("Nama Lengkap Sesuai Dokumen Resmi")
    nomor_id = st.text_input("Nomor Induk Kependudukan / Nomor Peserta")
    pendidikan = st.selectbox("Jenjang Pendidikan Terakhir", [
        "S1 / S1 Terapan / D4 Terapan", "D3", "D2", "D1",
        "SMK / SMK Plus", "SMA", "Pendidikan Dasar"
    ])
    pengalaman = st.number_input("Lama Pengalaman Kerja (Tahun)", min_value=0, step=1)
    dokumen = st.file_uploader("Unggah Dokumen Pendukung (Ijazah, SK Kerja, Sertifikat)", type=["pdf", "jpg", "png"])

    if st.button("📤 Kirim Pendaftaran", type="primary"):
        st.success("✅ Pendaftaran berhasil dikirim! Menunggu verifikasi pengelola.")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# HALAMAN CATATAN KHUSUS & KAKU
# --------------------------
elif menu == "⚠️ Catatan Khusus & Kaku":
    st.markdown('<h2 class="judul-utama">CATATAN KHUSUS & CATATAN KAKU</h2>', unsafe_allow_html=True)
    st.markdown('<div class="catatan-khusus">', unsafe_allow_html=True)
    st.markdown("""
    - **Kewenangan**: Hanya pengelola yang memiliki akun terdaftar dan diverifikasi yang dapat mengubah data pelatihan dan jabatan kerja.
    - **Kesesuaian Standar**: Seluruh persyaratan jabatan kerja tidak boleh diubah kecuali mengikuti pembaruan standar nasional yang resmi.
    - **Pembatasan Akses**: Sistem otomatis menyembunyikan seluruh data jabatan kerja yang tidak ditautkan ke pelatihan peserta — tidak ada cara lain untuk mengaksesnya.
    - **Pencatatan Perubahan**: Setiap penyimpanan, perubahan, maupun penghapusan data akan tercatat waktu, nama pengelola, dan jenis perubahannya dalam log sistem.
    - **Pemulihan Data**: Data yang sudah dihapus secara permanen tidak dapat dipulihkan, pengelola wajib mencadangkan data sebelum melakukan penghapusan.
    - **Kebenaran Data**: Pengelola wajib memastikan kesesuaian tautan jabatan kerja dengan isi pelatihan agar tidak menyesatkan peserta.
    - **Keamanan**: Semua data dikirim dalam bentuk terenkripsi, dan formulir pendaftaran hanya dapat diakses saat sesi login masih berlaku.
    - **Dokumen Palsu**: Jika ditemukan pemalsuan dokumen, pendaftaran akan dibatalkan dan peserta diblokir permanen.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
