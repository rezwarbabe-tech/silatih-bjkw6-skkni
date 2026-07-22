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

# ====================== PERSYARATAN KUALIFIKASI LENGKAP JENJANG 1-9 ======================
syarat_kualifikasi = {
    "9": [
        "Doktor/Doktor Terapan/Pendidikan Spesialis 2: Minimal 0 Tahun",
        "S2/S2 Terapan/Pendidikan Spesialis 1: Minimal 4 Tahun",
        "Pendidikan Profesi: Minimal 7 Tahun",
        "S1/S1 Terapan/D4 Terapan: Minimal 8 Tahun"
    ],
    "8": [
        "S2/S2 Terapan/Pendidikan Spesialis 1: Minimal 0 Tahun",
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

# ====================== DATA JABATAN LENGKAP DARI FILE MASTER ======================
data_jabatan = [
    # === SIPIL ===
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101015", "nama_jabatan": "Ahli Utama Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101014", "nama_jabatan": "Ahli Madya Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101013", "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101003", "nama_jabatan": "Ahli Utama Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101002", "nama_jabatan": "Ahli Madya Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101001", "nama_jabatan": "Ahli Muda Hidrologi", "acuan": "SKKNI 32-2014"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI101018", "nama_jabatan": "Ahli Utama Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI101021", "nama_jabatan": "Ahli Madya Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101020", "nama_jabatan": "Ahli Muda Hidrolika", "acuan": "SKKNI 151-2019"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "SI102005", "nama_jabatan": "Pengawas Pengeboran Air Tanah (Level 6)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI102006", "nama_jabatan": "Pengawas Pengeboran Air Tanah (Level 5)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI102007", "nama_jabatan": "Pelaksana Pengeboran Air Tanah (Level 5)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI102008", "nama_jabatan": "Pelaksana Pengeboran Air Tanah (Level 4)", "acuan": "SKKNI 128-2024; SKKNI 17-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI101019", "nama_jabatan": "Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate)", "acuan": "SKKNI 124-2021"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI121102", "nama_jabatan": "Ahli Madya Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI121001", "nama_jabatan": "Ahli Muda Teknik Bangunan Air Limbah (SPALD)", "acuan": "SKKNI 29-2023"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "SI122003", "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Level 5)", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Air Limbah", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "SI122004", "nama_jabatan": "Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Level 4)", "acuan": "SKKNI 312-2009"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "SI191004", "nama_jabatan": "Ahli Utama Teknik Dermaga", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "SI191006", "nama_jabatan": "Ahli Madya Teknik Dermaga", "acuan": "SKKNI 320–2016"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Bangunan Pelabuhan", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "SI191005", "nama_jabatan": "Ahli Muda Teknik Dermaga", "acuan": "SKKNI 320–2016"},

    # === MEKANIKAL ===
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "ME061001", "nama_jabatan": "Manajer Alat Berat", "acuan": "SKKNI 206-2013"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "ME062011", "nama_jabatan": "Pengawas Scaffolding", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 4, "kode_jabatan": "ME062009", "nama_jabatan": "Teknisi Scaffolding", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063094", "nama_jabatan": "Operator Scaffolding", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063095", "nama_jabatan": "Operator Pemula Scaffolding", "acuan": "SKKNI 46-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063096", "nama_jabatan": "Operator Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063097", "nama_jabatan": "Operator Pemula Bulldozer", "acuan": "SKK Khusus Reg.27-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063098", "nama_jabatan": "Operator Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063099", "nama_jabatan": "Operator Pemula Motor Grader", "acuan": "SKK Khusus Reg.30-2022"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "kode_jabatan": "ME063100", "nama_jabatan": "Operator Wheel Excavator", "acuan": "SKKNI 91-2010"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "kode_jabatan": "ME063101", "nama_jabatan": "Operator Pemula Wheel Excavator", "acuan": "SKKNI 91-2010"},

    # === ARSITEKTUR LANSKAP ===
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AL011009", "nama_jabatan": "Arsitek Lanskap Utama", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AL011010", "nama_jabatan": "Arsitek Lanskap Madya", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AL011011", "nama_jabatan": "Arsitek Lanskap Muda", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AL012006", "nama_jabatan": "Pengawas Lanskap (Level 6)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AL012007", "nama_jabatan": "Pengawas Lanskap (Level 5)", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 1, "kode_jabatan": "AL013006", "nama_jabatan": "Tukang Taman", "acuan": "SKKNI 31-2025; SKKNI 29-2023; SKKNI 17-2023"},

    # === ARSITEKTUR ===
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 9, "kode_jabatan": "AR011001", "nama_jabatan": "Arsitek Utama", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 8, "kode_jabatan": "AR011002", "nama_jabatan": "Arsitek Madya", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 7, "kode_jabatan": "AR011004", "nama_jabatan": "Asisten Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 6, "kode_jabatan": "AR012001", "nama_jabatan": "Asisten Pemula Arsitek", "acuan": "SKKNI 196-2021"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI/ANALIS", "jenjang": 5, "kode_jabatan": "AR012004", "nama_jabatan": "Pengawas Lapangan Bidang Arsitektur (Level 5)", "acuan": "SKKNI 196-2021"},
]

# ====================== HALAMAN UTAMA LOGIN ======================
if st.session_state.peran is None:
    st.title("🎓 siLATIH - Sistem Pelatihan Terintegrasi")
    st.divider()
    st.subheader("Pilih Akses Masuk:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔧 Pengelola / Admin", use_container_width=True):
            st.session_state.peran = "admin"
            st.rerun()
    with col2:
        if st.button("👤 Peserta", use_container_width=True):
            st.session_state.peran = "peserta"
            st.rerun()

# ====================== DASHBOARD ADMIN ======================
elif st.session_state.peran == "admin":
    st.title("🔧 Dashboard Pengelola Pelatihan")
    if st.button("🔙 Kembali ke Halaman Utama"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    tab1, tab2 = st.tabs(["📝 Buat Pelatihan Baru", "📋 Daftar Pendaftar"])

    with tab1:
        st.subheader("Data Umum Pelatihan")
        nama_pelatihan = st.text_input("Nama Pelatihan")
        tanggal_pelatihan = st.date_input("Tanggal Pelaksanaan")
        lokasi = st.text_input("Lokasi / Tautan Pelatihan")

        st.subheader("📌 Persyaratan Umum (Wajib Semua Peserta)")
        syarat_umum = st.text_area(
            "Daftar Persyaratan Umum",
            value="1. Fotokopi KTP yang masih berlaku\n2. Fotokopi Ijazah Terakhir yang dilegalisir\n3. Pas foto berwarna ukuran 4x6 cm latar belakang merah/biru\n4. Surat keterangan sehat\n5. Surat tugas dari instansi (jika diperlukan)",
            height=150
        )

        st.subheader("📌 Pilih Jabatan & Persyaratan Kualifikasi")
        klasifikasi_list = sorted({j["klasifikasi"] for j in data_jabatan})
        klasifikasi_pilih = st.selectbox("Pilih Klasifikasi Lengkap", klasifikasi_list)
        
        subklasifikasi_list = sorted({j["subklasifikasi"] for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih})
        subklasifikasi_pilih = st.selectbox("Pilih Subklasifikasi Lengkap", subklasifikasi_list)
        
        jabatan_list = [f"{j['nama_jabatan']} | Jenjang {j['jenjang']} | {j['kode_jabatan']}" 
                       for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih and j["subklasifikasi"] == subklasifikasi_pilih]
        jabatan_pilih = st.selectbox("Pilih Nama Jabatan", jabatan_list)
        
        jenjang_terpilih = next(j["jenjang"] for j in data_jabatan if f"{j['nama_jabatan']} | Jenjang {j['jenjang']} | {j['kode_jabatan']}" == jabatan_pilih)
        st.info(f"✅ Persyaratan Kualifikasi Lengkap Jenjang {jenjang_terpilih}:")
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
                    "syarat_khusus": syarat_kualifikasi[str(jenjang_terpilih)]
                }
                st.session_state.daftar_pelatihan.append(pelatihan_baru)
                st.success("✅ Pelatihan berhasil dibuat dengan persyaratan lengkap!")

    with tab2:
        st.subheader("Daftar Seluruh Pendaftar")
        if len(st.session_state.daftar_pendaftar) > 0:
            df = pd.DataFrame(st.session_state.daftar_pendaftar)
            st.dataframe(df, use_container_width=True)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Unduh Data (CSV)", csv, "daftar_pendaftar_lengkap.csv")
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
        st.warning("⚠️ Belum ada pelatihan yang dibuka oleh pengelola. Silakan cek kembali nanti.")
    else:
        pilihan = st.selectbox("Pilih Pelatihan yang Akan Diikuti", [p["nama"] for p in st.session_state.daftar_pelatihan])
        data_pilih = next(p for p in st.session_state.daftar_pelatihan if p["nama"] == pilihan)

        st.subheader("📋 Informasi & Persyaratan Lengkap")
        st.info(f"**Pelatihan:** {data_pilih['nama']}\n**Tanggal:** {data_pilih['tanggal']}\n**Lokasi:** {data_pilih['lokasi']}")
        
        with st.expander("📌 Persyaratan Umum"):
            st.markdown(data_pilih["syarat_umum"])
        with st.expander("📌 Persyaratan Jabatan & Kualifikasi Lengkap"):
            st.write(f"**Jabatan:** {data_pilih['jabatan']}")
            st.write(f"**Jenjang:** {data_pilih['jenjang']}")
            st.write("**Syarat Pendidikan & Pengalaman:**")
            for s in data_pilih["syarat_khusus"]:
                st.write(f"- {s}")

        st.subheader("📝 Isi Data Diri")
        nama = st.text_input("Nama Lengkap Sesuai KTP")
        nik = st.text_input("NIK / Nomor Identitas")
        alamat = st.text_area("Alamat Lengkap")
        no_hp = st.text_input("Nomor HP / WhatsApp")
        pendidikan = st.text_input("Pendidikan Terakhir")
        pengalaman = st.number_input("Lama Pengalaman Kerja (Tahun)", min_value=0, step=1)

        st.subheader("📎 Unggah Berkas Persyaratan")
        ktp = st.file_uploader("Scan / Foto KTP Asli", type=["jpg","jpeg","png","pdf"])
        ijazah = st.file_uploader("Scan / Foto Ijazah Terakhir Dilegalisir", type=["jpg","jpeg","png","pdf"])
        foto = st.file_uploader("Pas Foto Terbaru", type=["jpg","jpeg","png"])
        berkas_lain = st.file_uploader("Berkas Pendukung Lainnya", type=["jpg","jpeg","png","pdf"], accept_multiple_files=True)

        setuju = st.checkbox("Saya menyatakan data dan berkas yang diunggah benar dan memenuhi seluruh persyaratan di atas")
        
        if st.button("✅ Kirim Pendaftaran", type="primary") and setuju:
            if nama == "" or nik == "" or no_hp == "":
                st.error("❌ Lengkapi semua data wajib terlebih dahulu!")
            else:
                nomor_daftar = f"REG-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:4].upper()}"
                pendaftar = {
                    "Nomor Pendaftaran": nomor_daftar,
                    "Pelatihan": pilihan,
                    "Nama Lengkap": nama,
                    "NIK": nik,
                    "Alamat": alamat,
                    "No HP": no_hp,
                    "Pendidikan": pendidikan,
                    "Pengalaman (Tahun)": pengalaman,
                    "KTP": "Terunggah" if ktp else "Belum",
                    "Ijazah": "Terunggah" if ijazah else "Belum",
                    "Pas Foto": "Terunggah" if foto else "Belum"
                }
                st.session_state.daftar_pendaftar.append(pendaftar)
                st.success(f"🎉 Pendaftaran Berhasil! Nomor Anda: **{nomor_daftar}**")
                st.info("Simpan nomor pendaftaran ini untuk mengetahui hasil seleksi selanjutnya.")
