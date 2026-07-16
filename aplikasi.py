import streamlit as st

# --------------------------
# KONFIGURASI HALAMAN
# --------------------------
st.set_page_config(
    page_title="Sistem Pelatihan & Jabatan Kerja",
    page_icon="📋",
    layout="wide"
)

# --------------------------
# CSS KUSTOM (DIPISAHKAN DENGAN BENAR)
# --------------------------
css_style = """
<style>
* {box-sizing:border-box; font-family:'Segoe UI', Arial, sans-serif; margin:0; padding:0;}
.container {max-width:1200px; margin:0 auto; padding:20px;}
h1, h2, h3, h4 {margin:20px 0 10px 0; color:#2c3e50;}
p {line-height:1.6; margin-bottom:10px;}
hr {border:1px solid #eee; margin:30px 0;}
table {border-collapse:collapse; width:100%; margin:15px 0;}
th, td {border:1px solid #ddd; padding:12px; text-align:left; vertical-align:top;}
th {background:#f8f9fa; font-weight:bold;}
.ahli {background:#fff9cc; padding:8px; border-radius:4px;}
.teknis {background:#d7e3f5; padding:8px; border-radius:4px;}
.operator {background:#d9ead3; padding:8px; border-radius:4px;}
.info-box {background:#e8f4fd; padding:15px; border-radius:4px; margin:15px 0; border-left:4px solid #2980b9;}
.catatan {background:#fff3cd; padding:15px; border-radius:4px; margin-top:30px; border-left:4px solid #ffc107;}
ul {margin-left:20px; line-height:1.7;}
</style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# --------------------------
# JUDUL UTAMA
# --------------------------
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.title("DOKUMEN SISTEM PENGELOLAAN PELATIHAN & JABATAN KERJA")
st.write("**Versi:** 1.0 | **Tanggal:** 16 Juli 2026 | **Status:** Final Siap Terapkan")

# --------------------------
# 1. DAFTAR PUSTAKA
# --------------------------
st.header("1. DAFTAR PUSTAKA")
st.markdown("""
- Peraturan Menteri Ketenagakerjaan RI Nomor 1 Tahun 2021 tentang Pelatihan Kerja & Sertifikasi Kompetensi
- Standar Kompetensi Kerja Nasional Indonesia (SKKNI)
- Pedoman Klasifikasi Jabatan Kerja Nasional Tahun 2025
- Pedoman Pengelolaan Sistem Informasi Pelatihan Nomor 04/SJ/2024
- Panduan Teknis Pelatihan Berbasis Kompetensi (PBK)
""")

# --------------------------
# 2. KETENTUAN UMUM
# --------------------------
st.header("2. KETENTUAN UMUM")
st.markdown("""
- **Jabatan Kerja (Jabker):** Tingkatan pekerjaan dengan syarat pendidikan & pengalaman jelas sesuai standar.
- **Pengelola:** Pihak berwenang mengelola data, membuat pelatihan, menautkan jabatan kerja, dan verifikasi.
- **Peserta:** Orang yang mengikuti pelatihan, hanya melihat jabatan kerja yang ditautkan ke pelatihannya.
- **PBK:** Pelatihan Berbasis Kompetensi disesuaikan syarat jabatan tujuan.
""")

# --------------------------
# 3. PERSYARATAN JABATAN KERJA
# --------------------------
st.header("3. PERSYARATAN JABATAN KERJA LENGKAP")

st.subheader("KLASIFIKASI: AHLI")
tabel_ahli = """
| Jenjang | Persyaratan Pendidikan | Pengalaman Minimal |
|---|---|---|
| 9 | Doktor / Doktor Terapan / Pendidikan Spesialis_2 | 0 Tahun |
| 9 | S2 / S2 Terapan / Pendidikan Spesialis_1 | 4 Tahun |
| 9 | Pendidikan Profesi | 7 Tahun |
| 9 | S1 / S1 Terapan / D4 Terapan | 8 Tahun |
| 8 | Magister / Magister Terapan / S2 / S2 Terapan / Pendidikan Spesialis_1 | 0 Tahun |
| 8 | Pendidikan Profesi | 5 Tahun |
| 8 | S1 / S1 Terapan / D4 Terapan | 6 Tahun |
| 7 | Pendidikan Profesi | 0 Tahun |
| 7 | S1/S1 Terapan/D4 Terapan (Fresh Graduate dengan SKK Khusus) | 0 Tahun |
| 7 | S1 / S1 Terapan / D4 Terapan | 2 Tahun |
"""
st.markdown(tabel_ahli)

st.subheader("KLASIFIKASI: TEKNIS / ANALIS")
tabel_teknis = """
| Jenjang | Persyaratan Pendidikan | Pengalaman Minimal |
|---|---|---|
| 6 | S1 / S1 Terapan / D4 Terapan | 0 Tahun |
| 6 | D3 | 4 Tahun |
| 6 | D2 | 8 Tahun |
| 6 | D1 | 12 Tahun |
| 5 | D3 | 0 Tahun |
| 5 | D2 | 4 Tahun |
| 5 | D1 / SMK Plus | 8 Tahun |
| 5 | SMK | 10 Tahun |
| 5 | SMA | 12 Tahun |
| 4 | D2 | 0 Tahun |
| 4 | D1 / SMK Plus | 2 Tahun |
| 4 | SMK | 4 Tahun |
| 4 | SMA | 6 Tahun |
"""
st.markdown(tabel_teknis)

st.subheader("KLASIFIKASI: OPERATOR")
tabel_operator = """
| Jenjang | Persyaratan Pendidikan | Pengalaman Minimal |
|---|---|---|
| 3 | D1 / SMK Plus | 0 Tahun |
| 3 | SMK | 3 Tahun |
| 3 | SMA | 4 Tahun |
| 3 | Pendidikan Dasar | 5 Tahun |
| 2 | SMK | 0 Tahun |
| 2 | SMA | 1 Tahun |
| 2 | Pendidikan Dasar | 0 Tahun |
| 1 | Pendidikan Dasar | 0 Tahun |
| 1 | Non Pendidikan (Dengan PBK) | 2 Tahun |
"""
st.markdown(tabel_operator)

# --------------------------
# 4. ATURAN HAK AKSES
# --------------------------
st.header("4. ATURAN HAK AKSES")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Pengelola")
    st.markdown("""
    - Melihat seluruh data jabatan kerja & pelatihan
    - Membuat, menyimpan, mengedit, menghapus pelatihan
    - Menautkan/mengubah tautan jabatan kerja ke pelatihan
    - Memverifikasi pendaftaran peserta
    """)
with col2:
    st.subheader("Peserta")
    st.markdown("""
    - Tidak melihat jabatan kerja di luar pelatihan yang diikuti
    - Hanya melihat jabatan kerja yang ditautkan pengelola
    - Mendaftar jika memenuhi syarat & mengunggah dokumen
    - Tidak dapat mengubah data sistem
    """)

# --------------------------
# 5. HALAMAN PENGELOLA: KELOLA PELATIHAN
# --------------------------
st.header("HALAMAN PENGELOLA: KELOLA PELATIHAN")
id_pelatihan = st.text_input("ID Pelatihan (Kosongkan untuk baru)")
nama_pelatihan = st.text_input("Nama Pelatihan")
deskripsi = st.text_area("Deskripsi Pelatihan")

st.subheader("Pilih Jabatan Kerja yang Berlaku")
ahli_9 = st.checkbox("AHLI - Jenjang 9")
ahli_8 = st.checkbox("AHLI - Jenjang 8")
ahli_7 = st.checkbox("AHLI - Jenjang 7")
teknis_6 = st.checkbox("TEKNIS/ANALIS - Jenjang 6")
teknis_5 = st.checkbox("TEKNIS/ANALIS - Jenjang 5")
teknis_4 = st.checkbox("TEKNIS/ANALIS - Jenjang 4")
op_3 = st.checkbox("OPERATOR - Jenjang 3")
op_2 = st.checkbox("OPERATOR - Jenjang 2")
op_1 = st.checkbox("OPERATOR - Jenjang 1")

aksi = st.radio("Aksi", ["Simpan Baru", "Simpan Perubahan", "Hapus Pelatihan"])
if st.button("Jalankan Aksi"):
    st.success(f"Berhasil: Data pelatihan {aksi} telah disimpan!")

# --------------------------
# 6. HALAMAN PESERTA: FORMULIR PENDAFTARAN
# --------------------------
st.header("HALAMAN PESERTA: FORMULIR PENDAFTARAN")
st.markdown("""
<div class='info-box'>
<h4>Jabatan Kerja Sesuai Pelatihan Anda</h4>
<p>Berikut syarat yang berlaku untuk pelatihan <strong>Pelatihan Teknis Analisis Data</strong>:</p>
<table>
<tr><th>Klasifikasi</th><th>Jenjang</th><th>Persyaratan Pendidikan</th><th>Pengalaman Minimal</th></tr>
<tr><td>TEKNIS / ANALIS</td><td>6</td><td>S1 / S1 Terapan / D4 Terapan (0 thn) / D3 (4 thn) / D2 (8 thn) / D1 (12 thn)</td><td>Sesuai pendidikan</td></tr>
</table>
</div>
""", unsafe_allow_html=True)

nama_lengkap = st.text_input("Nama Lengkap Sesuai Dokumen")
nomor_id = st.text_input("Nomor Induk Peserta / NIK")
pendidikan = st.selectbox("Jenjang Pendidikan Terakhir", ["S1 / S1 Terapan / D4 Terapan", "D3", "D2", "D1", "SMK / SMK Plus", "SMA", "Pendidikan Dasar"])
pengalaman = st.number_input("Lama Pengalaman Kerja (Tahun)", min_value=0)
dokumen = st.file_uploader("Unggah Dokumen (Ijazah, SK Kerja, Sertifikat)", type=["pdf", "jpg", "png"])

if st.button("Kirim Pendaftaran"):
    st.success("Pendaftaran berhasil dikirim! Menunggu verifikasi pengelola.")

# --------------------------
# 7. CATATAN KHUSUS & KAKU
# --------------------------
st.markdown("""
<div class='catatan'>
<h3>CATATAN KHUSUS & CATATAN KAKU</h3>
<ul>
<li>Perubahan data pelatihan/jabatan kerja HANYA boleh dilakukan pengelola berwenang.</li>
<li>Persyaratan jabatan kerja tidak boleh diubah tanpa mengikuti standar nasional resmi.</li>
<li>Sistem otomatis menyembunyikan jabatan kerja lain dari peserta — tidak ada akses lain.</li>
<li>Data yang dihapus tidak dapat dipulihkan; pastikan cadangan sebelum menghapus.</li>
<li>Setiap perubahan tercatat waktu, nama pengelola, dan jenis perubahan untuk audit.</li>
<li>Dokumen palsu menyebabkan pembatalan pendaftaran & pemblokiran permanen.</li>
<li>Formulir peserta menyesuaikan syarat secara otomatis sesuai jabatan kerja yang ditautkan.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
