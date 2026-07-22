import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

# ====================== KONFIGURASI APLIKASI ======================
st.set_page_config(
    page_title="siLATIH - Sistem Pelatihan Terintegrasi",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Gaya tampilan
st.markdown("""
<style>
    .stApp {max-width: 100%; padding: 1rem 1.2rem;}
    h1 {font-size: 1.7rem !important; text-align: center;}
    h2 {font-size: 1.3rem !important; margin-top: 1rem;}
    .stButton>button {width: 100%; padding: 0.8rem; font-size: 1.1rem; border-radius: 10px;}
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>textarea {font-size: 1rem; padding: 0.7rem; border-radius: 8px;}
    div[data-testid="stFileUploader"] {font-size: 0.95rem;}
    .stAlert {border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# ====================== INISIALISASI PENYIMPANAN ======================
if "peran" not in st.session_state:
    st.session_state.peran = None
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "daftar_pendaftar" not in st.session_state:
    st.session_state.daftar_pendaftar = []

# ====================== DATA JABATAN & PERSYARATAN KUALIFIKASI ======================
data_jabatan = [
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101015", "nama_jabatan": "Ahli Utama Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101014", "nama_jabatan": "Ahli Madya Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101013", "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063096", "nama_jabatan": "Operator Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063097", "nama_jabatan": "Operator Pemula Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR011001", "nama_jabatan": "Arsitek Utama", "acuan": "SKKNI 196-2021"},
]

syarat_kualifikasi = {
    "9": [
        "Doktor/Doktor Terapan/Pendidikan Spesialis_2: Minimal 0 Tahun",
        "S2/S2 Terapan/Pendidikan Spesialis_1: Minimal 4 Tahun",
        "Pendidikan Profesi: Minimal 7 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 8 Tahun"
    ],
    "8": [
        "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1: Minimal 0 Tahun",
        "Pendidikan Profesi: Minimal 5 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 6 Tahun"
    ],
    "7": [
        "Pendidikan Profesi: Minimal 0 Tahun",
        "S1/S1 Terapan/D4 Terapan (Fresh Graduate): Minimal 0 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 2 Tahun"
    ],
    "6": [
        "S1/S1 Terapan/D4 Terapan: Minimal 0 Tahun",
        "D3: Minimal 4 Tahun",
        "D2: Minimal 8 Tahun",
        "D1: Minimal 12 Tahun"
    ],
    "5": [
        "D3: Minimal 0 Tahun",
        "D2: Minimal 4 Tahun",
        "D1/SMK Plus: Minimal 8 Tahun",
        "SMK: Minimal 10 Tahun",
        "SMA: Minimal 12 Tahun"
    ],
    "4": [
        "D2: Minimal 0 Tahun",
        "D1/SMK Plus: Minimal 2 Tahun",
        "SMK: Minimal 4 Tahun",
        "SMA: Minimal 6 Tahun"
    ],
    "3": [
        "D1/SMK Plus: Minimal 0 Tahun",
        "SMK: Minimal 3 Tahun",
        "SMA: Minimal 4 Tahun",
        "Pendidikan Dasar: Minimal 5 Tahun"
    ],
    "2": [
        "SMK: Minimal 0 Tahun",
        "SMA: Minimal 1 Tahun",
        "Pendidikan Dasar: Minimal 0 Tahun"
    ],
    "1": [
        "Pendidikan Dasar: Minimal 0 Tahun",
        "Non Pendidikan (Dengan PBK): Minimal 2 Tahun"
    ]
}

# ====================== HALAMAN UTAMA / LOGIN ======================
if st.session_state.peran is None:
    st.title("🎓 siLATIH - Sistem Pelatihan Terintegrasi")
    st.divider()
    st.subheader("Silakan pilih akses masuk:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔧 Masuk sebagai Pengelola / Admin", use_container_width=True):
            st.session_state.peran = "admin"
            st.rerun()
    with col2:
        if st.button("👤 Masuk sebagai Peserta", use_container_width=True):
            st.session_state.peran = "peserta"
            st.rerun()

# ====================== DASHBOARD ADMIN / PENGELOLA ======================
elif st.session_state.peran == "admin":
    st.title("🔧 Dashboard Pengelola Pelatihan")
    if st.button("🔙 Kembali ke Halaman Utama"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    tab1, tab2 = st.tabs(["📝 Buat Pelatihan Baru", "📋 Daftar Pendaftar"])

    with tab1:
        st.subheader("Isi Data & Persyaratan Pelatihan")
        
        nama_pelatihan = st.text_input("Nama Pelatihan")
        tanggal_pelatihan = st.date_input("Tanggal Pelaksanaan")
        lokasi = st.text_input("Lokasi / Tautan Pelatihan")
        
        st.subheader("📌 Persyaratan Umum (Wajib Bagi Semua Peserta)")
        syarat_umum = st.text_area(
            "Daftar Persyaratan Umum",
            value="1. Fotokopi KTP yang masih berlaku\n2. Fotokopi Ijazah Terakhir yang dilegalisir\n3. Pas foto berwarna ukuran 4x6 cm latar belakang merah/biru\n4. Surat keterangan sehat\n5. Surat tugas dari instansi (jika diperlukan)",
            height=150
        )
        
        st.subheader("📌 Persyaratan Jabatan & Kualifikasi")
        klasifikasi_pilih = st.selectbox("Pilih Klasifikasi", list({j["klasifikasi"] for j in data_jabatan}))
        subklasifikasi_pilih = st.selectbox("Pilih Subklasifikasi", list({j["subklasifikasi"] for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih}))
        jabatan_pilih = st.selectbox("Pilih Jabatan", [f"{j['nama_jabatan']} (Jenjang {j['jenjang']})" for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih and j["subklasifikasi"] == subklasifikasi_pilih])
        
        jenjang_terpilih = next(j["jenjang"] for j in data_jabatan if f"{j['nama_jabatan']} (Jenjang {j['jenjang']})" == jabatan_pilih)
        st.info(f"Persyaratan Kualifikasi Jenjang {jenjang_terpilih}:")
        for s in syarat_kualifikasi[str(jenjang_terpilih)]:
            st.write(f"- {s}")
        
        if st.button("✅ Simpan Pelatihan", type="primary"):
            if nama_pelatihan == "":
                st.error("Nama pelatihan tidak boleh kosong!")
            else:
                pelatihan_baru = {
                    "id": str(uuid.uuid4())[:8].upper(),
                    "nama": nama_pelatihan,
                    "tanggal": tanggal_pelatihan.strftime("%d-%m-%Y"),
                    "lokasi": lokasi,
                    "syarat_umum": syarat_umum,
                    "jabatan": jabatan_pilih,
                    "jenjang": jenjang_terpilih,
                    "syarat_kualifikasi": syarat_kualifikasi[str(jenjang_terpilih)]
                }
                st.session_state.daftar_pelatihan.append(pelatihan_baru)
                st.success("Pelatihan berhasil dibuat dan disimpan!")

    with tab2:
        st.subheader("Daftar Pendaftar Semua Pelatihan")
        if len(st.session_state.daftar_pendaftar) > 0:
            df = pd.DataFrame(st.session_state.daftar_pendaftar)
            st.dataframe(df, use_container_width=True)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Unduh Data Pendaftar (CSV)",
                data=csv,
                file_name=f"daftar_pendaftar_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        else:
            st.info("Belum ada peserta yang mendaftar.")

# ====================== DASHBOARD PESERTA ======================
elif st.session_state.peran == "peserta":
    st.title("👤 Dashboard Peserta Pelatihan")
    if st.button("🔙 Kembali ke Halaman Utama"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    if len(st.session_state.daftar_pelatihan) == 0:
        st.warning("Belum ada pelatihan yang dibuka oleh pengelola. Silakan cek kembali nanti.")
    else:
        pilihan_pelatihan = st.selectbox("Pilih Pelatihan yang Diikuti", [p["nama"] for p in st.session_state.daftar_pelatihan])
        data_pilih = next(p for p in st.session_state.daftar_pelatihan if p["nama"] == pilihan_pelatihan)
        
        st.subheader("📋 Informasi & Persyaratan Lengkap")
        st.info(f"**Pelatihan:** {data_pilih['nama']}\n**Tanggal:** {data_pilih['tanggal']}\n**Lokasi:** {data_pilih['lokasi']}")
        
        with st.expander("📌 Persyaratan Umum"):
            st.markdown(data_pilih["syarat_umum"])
        with st.expander("📌 Persyaratan Jabatan & Kualifikasi"):
            st.write(f"**Jabatan:** {data_pilih['jabatan']}")
            st.write("**Syarat Pendidikan & Pengalaman:**")
            for s in data_pilih["syarat_kualifikasi"]:
                st.write(f"- {s}")
        
        st.subheader("📝 Isi Data & Unggah Persyaratan")
        nama = st.text_input("Nama Lengkap Sesuai KTP")
        nik = st.text_input("NIK")
        alamat = st.text_area("Alamat Lengkap")
        no_hp = st.text_input("Nomor HP / WhatsApp")
        pendidikan = st.text_input("Pendidikan Terakhir")
        pengalaman = st.number_input("Lama Pengalaman Kerja (Tahun)", min_value=0, step=1)
        
        st.subheader("📎 Unggah Berkas Persyaratan")
        ktp = st.file_uploader("Scan / Foto KTP", type=["jpg","jpeg","png","pdf"])
        ijazah = st.file_uploader("Scan / Foto Ijazah Terakhir", type=["jpg","jpeg","png","pdf"])
        foto = st.file_uploader("Pas Foto Terbaru", type=["jpg","jpeg","png"])
        berkas_lain = st.file_uploader("Berkas Pendukung Lainnya", type=["jpg","jpeg","png","pdf"], accept_multiple_files=True)
        
        setuju = st.checkbox("Saya menyatakan data dan berkas yang diunggah benar dan memenuhi persyaratan di atas")
        
        if st.button("✅ Kirim Pendaftaran", type="primary"):
            if nama == "" or nik == "" or not setuju:
                st.error("Lengkapi data wajib dan centang persetujuan terlebih dahulu!")
            else:
                nomor_daftar = f"REG-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:4].upper()}"
                pendaftar_baru = {
                    "Nomor Pendaftaran": nomor_daftar,
                    "Waktu Daftar": datetime.now().strftime("%d-%m-%Y %H:%M"),
                    "Nama Pelatihan": pilihan_pelatihan,
                    "Nama Lengkap": nama,
                    "NIK": nik,
                    "Alamat": alamat,
                    "No HP": no_hp,
                    "Pendidikan": pendidikan,
                    "Pengalaman (Tahun)": pengalaman,
                    "KTP": "Terunggah" if ktp else "Belum",
                    "Ijazah": "Terunggah" if ijazah else "Belum",
                    "Pas Foto": "Terunggah" if foto else "Belum",
                    "Berkas Lain": "Terunggah" if berkas_lain else "Belum"
                }
                st.session_state.daftar_pendaftar.append(pendaftar_baru)
                st.success(f"🎉 Pendaftaran berhasil! Nomor Anda: **{nomor_daftar}**")
                st.info("Simpan nomor ini untuk mengetahui hasil seleksi selanjutnya.")
