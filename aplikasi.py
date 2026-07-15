# ==============================================
# APLIKASI SI LATIH LENGKAP + PEMANTAUAN CAPAIAN ANGGARAN
# Balai Jasa Konstruksi Wilayah VI Makassar
# Kementerian Pekerjaan Umum
# ==============================================

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO
from datetime import datetime, date
import re
from dateutil.relativedelta import relativedelta

# ==============================================
# 1. GAYA TAMPILAN RESMI KEMENTERIAN PEKERJAAN UMUM
# ==============================================
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
    font-family: 'Segoe UI', Roboto, sans-serif;
}

h1, h2, h3, h4 { color: var(--pu-biru-utama); font-weight: 700; }
p, div, span { color: var(--pu-teks); }

.stButton>button, .stDownloadButton>button {
    background-color: var(--pu-biru-utama);
    color: white;
    border-radius: 6px;
    border: 2px solid var(--pu-biru-utama);
    padding: 0.5rem 1.2rem;
    font-weight: 500;
    transition: all 0.3s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: var(--pu-biru-terang);
    border-color: var(--pu-biru-terang);
    transform: translateY(-1px);
}

.pu-info {
    background: white;
    border-left: 6px solid var(--pu-biru-utama);
    padding: 1.2rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,75,135,0.08);
    margin-bottom: 1rem;
}
.pu-sukses {
    background: #F0FDF4;
    border-left: 6px solid var(--pu-hijau);
    padding: 1.2rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}
.pu-tolak {
    background: #FEF2F2;
    border-left: 6px solid var(--pu-merah);
    padding: 1.2rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}
.pu-kotak {
    background: white;
    border-left: 6px solid var(--pu-biru-utama);
    padding: 1.2rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}

section[data-testid="stSidebar"] {
    background-color: white;
    border-right: 3px solid var(--pu-biru-muda);
}
.stDataFrame { border-radius: 8px; border: 1px solid var(--pu-biru-muda); }
</style>
""", unsafe_allow_html=True)

# ==============================================
# 2. KONFIGURASI UTAMA & MENU NAVIGASI
# ==============================================
st.set_page_config(
    page_title="siLATIH & Capaian Anggaran - BJKW VI Makassar",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.markdown("---")
st.sidebar.header("📋 Menu Utama")
menu = st.sidebar.radio("Pilih Halaman", [
    "🏠 Beranda",
    "📚 Daftar Jabatan SKKNI",
    "📝 Pendaftaran Pelatihan",
    "📊 Pemantauan Capaian Output Anggaran",
    "🔐 Pengelola Aplikasi"
])

# ==============================================
# 3. DATA REFERENSI LENGKAP
# ==============================================
daftar_jabatan = [
    {"no": 1, "kode_jabatan": "SI-SDA-001", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 2, "kode_jabatan": "SI-SDA-002", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 3, "kode_jabatan": "SI-SDA-003", "klasifikasi": "SIPIL", "subklasifikasi": "Sumber Daya Air", "kualifikasi": "Ahli", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Sumber Daya Air", "acuan_skkni": "SKKNI 124-2021"},
    {"no": 4, "kode_jabatan": "SI-JLN-001", "klasifikasi": "SIPIL", "subklasifikasi": "Jalan & Jembatan", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Rekayasa Jalan Raya", "acuan_skkni": "SKKNI 137-2022"},
    {"no": 5, "kode_jabatan": "SI-GED-001", "klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Gedung", "kualifikasi": "Pengawas", "jenjang": 6, "nama_jabatan": "Pengawas Pelaksanaan Gedung", "acuan_skkni": "SKKNI 141-2021"},
    {"no": 6, "kode_jabatan": "SI-BET-001", "klasifikasi": "SIPIL", "subklasifikasi": "Pekerjaan Beton", "kualifikasi": "Tukang", "jenjang": 4, "nama_jabatan": "Tukang Beton Terampil", "acuan_skkni": "SKKNI 135-2022"},
    {"no": 7, "kode_jabatan": "ME-ABT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Bulldozer", "acuan_skkni": "SKK Khusus Reg.27-2022"},
    {"no": 8, "kode_jabatan": "ME-ABG-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Operator Alat Berat", "kualifikasi": "Operator", "jenjang": 3, "nama_jabatan": "Operator Ekskavator", "acuan_skkni": "SKKNI 91-2010"},
    {"no": 9, "kode_jabatan": "ME-MNT-001", "klasifikasi": "MEKANIKAL", "subklasifikasi": "Pemeliharaan Alat Berat", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Mekanik Alat Berat", "acuan_skkni": "SKKNI 190-2024"},
    {"no": 10, "kode_jabatan": "EL-ILG-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Instalasi Listrik", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Instalasi Listrik Terampil", "acuan_skkni": "SKKNI 130-2021"},
    {"no": 11, "kode_jabatan": "EL-SRY-001", "klasifikasi": "ELEKTRO", "subklasifikasi": "Energi Terbarukan", "kualifikasi": "Teknisi", "jenjang": 5, "nama_jabatan": "Teknisi Pemasangan Panel Surya", "acuan_skkni": "SKKNI 241-2024"},
    {"no": 12, "kode_jabatan": "K3-SMK-001", "klasifikasi": "KESELAMATAN KERJA", "subklasifikasi": "Sistem Manajemen K3", "kualifikasi": "Ahli", "jenjang": 9, "nama_jabatan": "Ahli Utama Keselamatan dan Kesehatan Kerja", "acuan_skkni": "SKKNI 119-2020"},
    {"no": 13, "kode_jabatan": "MN-MPR-001", "klasifikasi": "MANAJEMEN PROYEK", "subklasifikasi": "Manajemen Proyek", "kualifikasi": "Manajer", "jenjang": 9, "nama_jabatan": "Manajer Proyek Utama", "acuan_skkni": "SKKNI 145-2021"}
]

persyaratan_pengalaman = {
    "Ahli Utama Teknik Sumber Daya Air": {"jenjang":9,"min_tahun":{"Doktor/Doktor Terapan/Pendidikan Spesialis_2":0,"S2/S2 Terapan/Pendidikan Spesialis_1":4,"Pendidikan Profesi":7,"S1/S1 Terapan/D4 Terapan":8}},
    "Ahli Madya Teknik Sumber Daya Air": {"jenjang":8,"min_tahun":{"Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1":0,"Pendidikan Profesi":5,"S1/S1 Terapan/D4 Terapan":6}},
    "Ahli Muda Teknik Sumber Daya Air": {"jenjang":7,"min_tahun":{"Pendidikan Profesi":0,"S1/S1 Terapan/D4 Terapan (Fresh Graduate)":0,"S1/S1 Terapan/D4 Terapan":2}},
    "Ahli Utama Rekayasa Jalan Raya": {"jenjang":9,"min_tahun":{"Doktor/Doktor Terapan/Pendidikan Spesialis_2":0,"S2/S2 Terapan/Pendidikan Spesialis_1":4,"Pendidikan Profesi":7,"S1/S1 Terapan/D4 Terapan":8}},
    "Pengawas Pelaksanaan Gedung": {"jenjang":6,"min_tahun":{"S1/S1 Terapan/D4 Terapan":0,"D3":4,"D2":8,"D1":12}},
    "Tukang Beton Terampil": {"jenjang":4,"min_tahun":{"D2":0,"D1/SMK Plus":2,"SMK":4,"SMA":6}},
    "Operator Bulldozer": {"jenjang":3,"min_tahun":{"D1/SMK Plus":0,"SMK":3,"SMA":4,"Pendidikan Dasar":5}},
    "Operator Ekskavator": {"jenjang":3,"min_tahun":{"D1/SMK Plus":0,"SMK":3,"SMA":4,"Pendidikan Dasar":5}},
    "Teknisi Mekanik Alat Berat": {"jenjang":5,"min_tahun":{"D3":0,"D2":4,"D1/SMK Plus":8,"SMK":10,"SMA":12}},
    "Teknisi Instalasi Listrik Terampil": {"jenjang":5,"min_tahun":{"D3":0,"D2":4,"D1/SMK Plus":8,"SMK":10,"SMA":12}},
    "Teknisi Pemasangan Panel Surya": {"jenjang":5,"min_tahun":{"D3":0,"D2":4,"D1/SMK Plus":8,"SMK":10,"SMA":12}},
    "Ahli Utama Keselamatan dan Kesehatan Kerja": {"jenjang":9,"min_tahun":{"Doktor/Doktor Terapan/Pendidikan Spesialis_2":0,"S2/S2 Terapan/Pendidikan Spesialis_1":4,"Pendidikan Profesi":7,"S1/S1 Terapan/D4 Terapan":8}},
    "Manajer Proyek Utama": {"jenjang":9,"min_tahun":{"Doktor/Doktor Terapan/Pendidikan Spesialis_2":0,"S2/S2 Terapan/Pendidikan Spesialis_1":4,"Pendidikan Profesi":7,"S1/S1 Terapan/D4 Terapan":8}}
}

if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
akun_admin = {"username": "admin_silatih", "password": "pupr_bjkw6_2026"}

# ==============================================
# 4. FUNGSI VERIFIKASI & PENGOLAHAN DATA
# ==============================================
def ekstrak_tahun_pengalaman(berkas_list):
    total_tahun = 0
    try:
        for berkas in berkas_list:
            nama_berkas = berkas.name.lower()
            pola_tanggal = r'(\d{4})'
            tahun = re.findall(pola_tanggal, nama_berkas)
            if len(tahun)>=2:
                mulai = int(tahun[0])
                selesai = int(tahun[1]) if int(tahun[1])<=datetime.now().year else datetime.now().year
                total_tahun += max(0, selesai - mulai)
            elif len(tahun)==1:
                total_tahun += max(0, datetime.now().year - int(tahun[0]))
        return round(total_tahun,1) if total_tahun>0 else 0
    except:
        return 0

def cek_kesesuaian_ktp_ijazah(nama_ktp, nik_ktp, nama_ijazah, nik_ijazah=""):
    if not nama_ktp or not nama_ijazah: return False, "Nama lengkap wajib diisi pada kedua berkas"
    nama_sama = nama_ktp.lower().strip() == nama_ijazah.lower().strip()
    nik_sama = nik_ktp.strip() == nik_ijazah.strip() if nik_ijazah else True
    if nama_sama and nik_sama: return True, "✅ Data KTP dan Ijazah sesuai"
    elif not nama_sama: return False, "❌ Nama lengkap pada KTP tidak sama dengan Ijazah"
    else: return False, "❌ Nomor identitas pada KTP tidak sesuai dengan Ijazah"

def verifikasi_syarat(jabatan_pilihan, jenjang_pendidikan, total_pengalaman):
    if jabatan_pilihan not in persyaratan_pengalaman: return True, "ℹ️ Syarat belum tercantum, diterima sementara"
    syarat = persyaratan_pengalaman[jabatan_pilihan]
    jenjang_terdekat = next((k for k in syarat["min_tahun"].keys() if jenjang_pendidikan.lower() in k.lower()), None)
    if not jenjang_terdekat: return False, f"❌ Jenjang pendidikan {jenjang_pendidikan} tidak sesuai untuk jabatan ini"
    butuh = syarat["min_tahun"][jenjang_terdekat]
    if total_pengalaman >= butuh: return True, f"✅ Pengalaman kerja {total_pengalaman} tahun memenuhi syarat minimal {butuh} tahun"
    else: return False, f"❌ Pengalaman kerja {total_pengalaman} tahun belum memenuhi syarat minimal {butuh} tahun"

# ==============================================
# 5. HALAMAN BERANDA
# ==============================================
if menu == "🏠 Beranda":
    st.markdown("<hr style='border:3px solid #004B87; border-radius:2px; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    st.title("🏛️ Sistem Informasi Pelatihan & Pemantauan Kinerja")
    st.subheader("Balai Jasa Konstruksi Wilayah VI Makassar")
    st.markdown("<h3 style='color:#004B87;'>Kementerian Pekerjaan Umum</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="pu-info">
    📢 <strong>Selamat Datang di Aplikasi siLATIH!</strong><br>
    Layanan pendaftaran pelatihan uji kompetensi konstruksi serta pemantauan capaian output pelaksanaan anggaran Satuan Kerja.
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="pu-kotak"><h4>📚 Layanan Pelatihan</h4><ul><li>Daftar jabatan SKKNI</li><li>Pendaftaran daring</li><li>Verifikasi otomatis berkas</li></ul></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="pu-kotak"><h4>📊 Capaian Anggaran</h4><ul><li>Unggah data indikator</li><li>Grafik capaian bulanan</li><li>Analisis perbandingan</li></ul></div>""", unsafe_allow_html=True)

# ==============================================
# 6. HALAMAN DAFTAR JABATAN
# ==============================================
elif menu == "📚 Daftar Jabatan SKKNI":
    st.markdown("<hr style='border:3px solid #004B87; border-radius:2px; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    st.header("📋 Daftar Jabatan Berdasarkan SKKNI")
    df = pd.DataFrame(daftar_jabatan)
    st.sidebar.header("🔎 Saring Data")
    pilih_klasifikasi = st.sidebar.multiselect("Bidang Klasifikasi", options=sorted(df["klasifikasi"].unique()))
    if pilih_klasifikasi: df = df[df["klasifikasi"].isin(pilih_klasifikasi)]
    pilih_kualifikasi = st.sidebar.multiselect("Tingkat Kualifikasi", options=sorted(df["kualifikasi"].unique()))
    if pilih_kualifikasi: df = df[df["kualifikasi"].isin(pilih_kualifikasi)]
    kata_kunci = st.text_input("🔍 Cari Jabatan/Kode Jabatan:")
    if kata_kunci: df = df[df["nama_jabatan"].str.contains(kata_kunci, case=False) | df["kode_jabatan"].str.contains(kata_kunci, case=False)]
    st.info(f"✅ Menampilkan {len(df)} jabatan")
    st.dataframe(df, use_container_width=True, hide_index=True)
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as w: df.to_excel(w, index=False, sheet_name="Daftar Jabatan")
    st.download_button("📂 Unduh Excel", buffer.getvalue(), "Daftar_Jabatan_SKKNI.xlsx")

# ==============================================
# 7. HALAMAN PENDAFTARAN PELATIHAN
# ==============================================
elif menu == "📝 Pendaftaran Pelatihan":
    st.markdown("<hr style='border:3px solid #004B87; border-radius:2px; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    st.header("📚 Pelatihan Sedang Dibuka")
    if st.session_state.daftar_pelatihan:
        for l in st.session_state.daftar_pelatihan:
            st.markdown(f"""<div class="pu-info"><h4>{l['nama']}</h4><p>Jabatan: {l['jabatan']}<br>Batas Daftar: {l['tutup']} | Kuota: {l['kuota']} | Lokasi: {l['lokasi']}</p></div>""", unsafe_allow_html=True)
    else: st.info("ℹ️ Belum ada pelatihan dibuka.")
    
    st.markdown("---")
    st.header("📝 Formulir Pendaftaran")
    with st.form("form_daftar"):
        st.subheader("👤 Data Diri")
        c1,c2 = st.columns(2)
        with c1: nama = st.text_input("Nama Lengkap Sesuai KTP *"); nik = st.text_input("NIK / KTP *")
        with c2: kontak = st.text_input("Nomor HP/WA *"); email = st.text_input("Email")
        alamat = st.text_area("Alamat Lengkap")
        
        st.subheader("🎓 Pendidikan & Ijazah")
        jenjang = st.selectbox("Jenjang Pendidikan Terakhir *", ["Pilih...", "Pendidikan Dasar", "SMA", "SMK", "SMK Plus/D1", "D2", "D3", "D4/S1", "Profesi", "S2", "Spesialis_1", "Doktor/Spesialis_2"])
        nama_ijazah = st.text_input("Nama Sesuai Ijazah *"); nik_ijazah = st.text_input("Nomor Identitas di Ijazah")
        berkas_ijazah = st.file_uploader("Unggah Ijazah *", type=["pdf","jpg","jpeg","png","doc","docx"])
        
        st.subheader("📎 Bukti Pendukung")
        berkas_ktp = st.file_uploader("Unggah KTP *", type=["pdf","jpg","jpeg","png","doc","docx"])
        bukti_ig = st.file_uploader("Bukti Follow @bjkw6_makassar *", type=["pdf","jpg","jpeg","png"])
        link_pddikti = st.text_input("Link PDDIKTI *", placeholder="https://pddikti.kemdikbud.go.id/...")
        
        st.subheader("💼 Bukti Pengalaman Kerja")
        st.info("Format diterima: PDF, Gambar, Word, Excel, RAR/ZIP")
        bukti_pengalaman = st.file_uploader("Unggah Bukti Pengalaman Kerja *", type=["pdf","jpg","jpeg","png","doc","docx","xls","xlsx","rar","zip"], accept_multiple_files=True)
        
        st.subheader("🎓 Pilihan Pelatihan")
        if st.session_state.daftar_pelatihan:
            pilihan = st.selectbox("Pilih Pelatihan *", [f"{p['nama']} — {p['jabatan']}" for p in st.session_state.daftar_pelatihan])
            jabatan_pilihan = pilihan.split(" — ")[1]
        else: pilihan = "Belum ada pelatihan"; jabatan_pilihan = ""; st.warning("Pendaftaran ditutup.")
        
        kirim = st.form_submit_button("✅ Kirim & Verifikasi")
        
        if kirim:
            if not nama or not nik or not kontak or not nama_ijazah or not berkas_ijazah or not bukti_ig or not link_pddikti or not bukti_pengalaman or not berkas_ktp or jenjang=="Pilih..." or pilihan=="Belum ada pelatihan":
                st.error("⚠️ Lengkapi semua kolom bertanda *!")
            else:
                ok1, pesan1 = cek_kesesuaian_ktp_ijazah(nama, nik, nama_ijazah, nik_ijazah)
                if not ok1: st.markdown(f'<div class="pu-tolak"><h4>❌ Ditolak</h4><p>{pesan1}</p></div>', unsafe_allow_html=True); st.stop()
                total_pengalaman = ekstrak_tahun_pengalaman(bukti_pengalaman)
                st.info(f"🔍 Akumulasi pengalaman kerja: {total_pengalaman} tahun")
                ok2, pesan2 = verifikasi_syarat(jabatan_pilihan, jenjang, total_pengalaman)
                if not ok2: st.markdown(f'<div class="pu-tolak"><h4>❌ Ditolak</h4><p>{pesan2}</p></div>', unsafe_allow_html=True); st.stop()
                st.balloons()
                st.markdown(f'<div class="pu-sukses"><h4>🎉 Diterima!</h4><p>Terima kasih {nama} untuk {pilihan}<br>{pesan1}<br>{pesan2}<br>Kami hubungi lewat {kontak} maksimal 3 hari kerja.</p></div>', unsafe_allow_html=True)

# ==============================================
# 8. HALAMAN PEMANTAUAN CAPAIAN OUTPUT ANGGARAN (LENGKAP)
# ==============================================
elif menu == "📊 Pemantauan Capaian Output Anggaran":
    st.markdown("<hr style='border:3px solid #004B87; border-radius:2px; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    st.header("📊 Pemantauan Indikator Pelaksanaan Anggaran")
    st.subheader("Balai Jasa Konstruksi Wilayah VI Makassar")
    
    st.subheader("📂 Unggah Berkas Data")
    berkas_anggaran = st.file_uploader("Pilih berkas Excel Indikator Pelaksanaan Anggaran Satker", type=["xlsx","xls"])
    
    # Data contoh sesuai berkas yang kamu kirim
    data_contoh = pd.DataFrame([{
        "Bulan": "Juli", "Tahun": 2026, "Kode KPPN": "054", "Kode BA": "145", "Kode Satker": "694413", "Nama Satker": "BALAI JASA KONSTRUKSI WILAYAH VI MAKASSAR",
        "Revisi DIPA": 100.00, "Deviasi Halaman III DIPA": 59.50, "Nilai Perencanaan": 79.75,
        "Penyerapan Anggaran": 93.06, "Belanja Kontraktual": 100.00, "Penyelesaian Tagihan": 100.00, "Pengelolaan UP TUP": 89.53, "Nilai Pelaksanaan": 95.65,
        "Capaian Output": 66.49, "Nilai Akhir": 66.49
    }])
    
    if berkas_anggaran:
        try:
            df_anggaran = pd.read_excel(berkas_anggaran)
            st.success("✅ Berkas berhasil dibaca!")
        except:
            st.warning("⚠️ Format berkas tidak sesuai, menampilkan data contoh Juli 2026")
            df_anggaran = data_contoh
    else:
        st.info("ℹ️ Belum ada berkas diunggah, menampilkan data contoh Juli 2026")
        df_anggaran = data_contoh
    
    st.markdown("---")
    st.subheader("📋 Ringkasan Data Capaian Bulanan")
    st.dataframe(df_anggaran, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.subheader("📈 Visualisasi Capaian Selama Satu Tahun Berjalan")
    if len(df_anggaran) < 12:
        st.info("📝 Unggah berkas lengkap 12 bulan untuk melihat grafik utuh satu tahun berjalan.")
    
    # Grafik Garis Perkembangan Nilai Utama
    st.subheader("Perkembangan Nilai Utama Tiap Bulan")
    kolom_garis = ["Nilai Perencanaan", "Nilai Pelaksanaan", "Capaian Output", "Nilai Akhir"]
    fig_garis = px.line(
        df_anggaran, x="Bulan", y=kolom_garis, markers=True,
        color_discrete_sequence=["#004B87", "#0071BC", "#F59E0B", "#059669"],
        labels={"value":"Nilai (0-100)", "variable":"Indikator"}
    )
    fig_garis.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="#2C3E50")
    st.plotly_chart(fig_garis, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        # Diagram Batang Perbandingan Komponen
        st.subheader("Perbandingan Komponen Indikator")
        kolom_batang = ["Revisi DIPA", "Deviasi Halaman III DIPA", "Penyerapan Anggaran", "Belanja Kontraktual", "Penyelesaian Tagihan", "Pengelolaan UP TUP"]
        fig_batang = px.bar(
            df_anggaran.melt(id_vars="Bulan", value_vars=kolom_batang),
            x="variable", y="value", color="Bulan", barmode="group",
            labels={"value":"Nilai Capaian", "variable":"Komponen"}
        )
        fig_batang.update_layout(plot_bgcolor="white", paper_bgcolor="white", xaxis_tickangle=-45)
        st.plotly_chart(fig_batang, use_container_width=True)
    
    with col2:
        # Diagram Lingkaran Komposisi Nilai
        st.subheader("Komposisi Pembentukan Nilai Akhir")
        fig_pie = px.pie(
            values=[20, 40, 40], names=["Kualitas Perencanaan", "Kualitas Pelaksanaan", "Capaian Output"],
            color_discrete_sequence=["#004B87", "#0071BC", "#F59E0B"]
        )
        fig_pie.update_layout(paper_bgcolor="white")
        st.plotly_chart(fig_pie, use_container_width=True)

# ==============================================
# 9. HALAMAN PENGELOLA APLIKASI
# ==============================================
elif menu == "🔐 Pengelola Aplikasi":
    st.markdown("<hr style='border:3px solid #004B87; border-radius:2px; margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    st.header("⚙️ Pengaturan Pengelolaan")
    with st.sidebar.expander("🔑 Masuk Admin"):
        user = st.text_input("Nama Pengguna")
        sandi = st.text_input("Kata Sandi", type="password")
        login_ok = st.button("Masuk")
    
    if login_ok and user == akun_admin["username"] and sandi == akun_admin["password"]:
        st.success("✅ Mode Pengelola Aktif")
        st.subheader("📅 Tambah Pelatihan Baru")
        with st.form("tambah_pelatihan", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1: nama = st.text_input("Nama Pelatihan *"); jabatan = st.selectbox("Jabatan Terkait *", pd.DataFrame(daftar_jabatan)["nama_jabatan"].unique()); lokasi = st.text_input("Lokasi")
            with c2: tgl_buka = st.date_input("Tanggal Buka"); tgl_tutup = st.date_input("Tanggal Tutup"); kuota = st.number_input("Kuota", min_value=1, value=25)
            simpan = st.form_submit_button("➕ Simpan")
            if simpan:
                st.session_state.daftar_pelatihan.append({"nama":nama,"jabatan":jabatan,"buka":tgl_buka,"tutup":tgl_tutup,"kuota":kuota,"lokasi":lokasi})
                st.success("✅ Pelatihan ditambahkan!"); st.rerun()
        st.markdown("---")
        st.subheader("📋 Daftar Pelatihan Aktif")
        if st.session_state.daftar_pelatihan:
            for i, l in enumerate(st.session_state.daftar_pelatihan,1):
                with st.expander(f"{i}. {l['nama']}"):
                    st.write(f"Jabatan: {l['jabatan']} | Periode: {l['buka']}–{l['tutup']} | Kuota: {l['kuota']} | Lokasi: {l['lokasi']}")
                    if st.button(f"🗑️ Hapus", key=f"hapus_{i}"): st.session_state.daftar_pelatihan.pop(i-1); st.rerun()
        else: st.info("ℹ️ Belum ada pelatihan.")
    elif login_ok: st.error("❌ Nama pengguna atau kata sandi salah!")

# ==============================================
# 10. KAKI HALAMAN RESMI
# ==============================================
st.markdown("<hr style='border:2px solid #004B87; margin-top:2rem;'>", unsafe_allow_html=True)
st.caption("© 2026 Balai Jasa Konstruksi Wilayah VI Makassar — Kementerian Pekerjaan Umum | siLATIH v2.0 Lengkap")
