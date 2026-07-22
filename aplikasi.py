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

# ====================== INISIALISASI DATA ======================
if "peran" not in st.session_state:
    st.session_state.peran = None
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []
if "daftar_pendaftar" not in st.session_state:
    st.session_state.daftar_pendaftar = []

# ====================== PERSYARATAN KUALIFIKASI LENGKAP JENJANG 1-9 ======================
syarat_kualifikasi = {
    "9": [
        "Doktor/Doktor Terapan: Minimal 0 Tahun",
        "S2/S2 Terapan: Minimal 4 Tahun",
        "Pendidikan Profesi: Minimal 7 Tahun",
        "S1/S1 Terapan/D4: Minimal 8 Tahun"
    ],
    "8": [
        "S2/S2 Terapan: Minimal 0 Tahun",
        "Pendidikan Profesi: Minimal 5 Tahun",
        "S1/S1 Terapan/D4: Minimal 6 Tahun"
    ],
    "7": [
        "Pendidikan Profesi: Minimal 0 Tahun",
        "S1/S1 Terapan/D4 (Fresh Graduate): Minimal 0 Tahun",
        "S1/S1 Terapan/D4: Minimal 2 Tahun"
    ],
    "6": [
        "S1/S1 Terapan/D4: Minimal 0 Tahun",
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

# ====================== DATA JABATAN LENGKAP ======================
data_jabatan = [
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 9, "nama_jabatan": "Ahli Utama Teknik Sumber Daya Air"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 8, "nama_jabatan": "Ahli Madya Teknik Sumber Daya Air"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "AHLI", "jenjang": 7, "nama_jabatan": "Ahli Muda Teknik Sumber Daya Air"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI", "jenjang": 6, "nama_jabatan": "Pengawas Pengeboran Air Tanah"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI", "jenjang": 5, "nama_jabatan": "Pelaksana Pengeboran Air Tanah"},
    {"klasifikasi": "SIPIL", "subklasifikasi": "Air Tanah dan Air Baku", "kualifikasi": "TEKNISI", "jenjang": 4, "nama_jabatan": "Asisten Pelaksana Pengeboran"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 3, "nama_jabatan": "Operator Bulldozer"},
    {"klasifikasi": "MEKANIKAL", "subklasifikasi": "Alat Berat", "kualifikasi": "OPERATOR", "jenjang": 2, "nama_jabatan": "Operator Pemula Bulldozer"},
    {"klasifikasi": "ARSITEKTUR LANSKAP", "subklasifikasi": "Arsitektur Lanskap", "kualifikasi": "OPERATOR", "jenjang": 1, "nama_jabatan": "Tukang Taman"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "AHLI", "jenjang": 9, "nama_jabatan": "Arsitek Utama"},
    {"klasifikasi": "ARSITEKTUR", "subklasifikasi": "Arsitektural", "kualifikasi": "TEKNISI", "jenjang": 6, "nama_jabatan": "Pengawas Lapangan Arsitektur"}
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
    st.title("🔧 Dashboard Pengelola")
    if st.button("🔙 Kembali"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    tab1, tab2 = st.tabs(["📝 Buat Pelatihan", "📋 Pendaftar"])

    with tab1:
        st.subheader("Data Pelatihan")
        nama_pelatihan = st.text_input("Nama Pelatihan")
        tanggal = st.date_input("Tanggal Pelaksanaan")
        lokasi = st.text_input("Lokasi/Tautan")

        st.subheader("📌 Persyaratan Umum")
        syarat_umum = st.text_area(
            "Daftar Persyaratan",
            value="1. KTP Asli & Fotokopi\n2. Ijazah Terakhir Dilegalisir\n3. Pas Foto 4x6\n4. Surat Keterangan Sehat",
            height=120
        )

        st.subheader("📌 Persyaratan Jabatan")
        klasifikasi_pilih = st.selectbox("Klasifikasi", sorted({j["klasifikasi"] for j in data_jabatan}))
        subklasifikasi_pilih = st.selectbox("Subklasifikasi", sorted({j["subklasifikasi"] for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih}))
        jabatan_list = [f"{j['nama_jabatan']} (Jenjang {j['jenjang']})" for j in data_jabatan if j["klasifikasi"] == klasifikasi_pilih and j["subklasifikasi"] == subklasifikasi_pilih]
        jabatan_pilih = st.selectbox("Jabatan", jabatan_list)
        jenjang = next(j["jenjang"] for j in data_jabatan if f"{j['nama_jabatan']} (Jenjang {j['jenjang']})" == jabatan_pilih)
        
        st.info(f"✅ Syarat Kualifikasi Jenjang {jenjang}:")
        for s in syarat_kualifikasi[str(jenjang)]:
            st.write(f"- {s}")

        if st.button("✅ Simpan Pelatihan", type="primary"):
            if nama_pelatihan:
                pelatihan = {
                    "id": str(uuid.uuid4())[:8].upper(),
                    "nama": nama_pelatihan,
                    "tanggal": tanggal.strftime("%d-%m-%Y"),
                    "lokasi": lokasi,
                    "syarat_umum": syarat_umum,
                    "jabatan": jabatan_pilih,
                    "jenjang": jenjang,
                    "syarat_khusus": syarat_kualifikasi[str(jenjang)]
                }
                st.session_state.daftar_pelatihan.append(pelatihan)
                st.success("Pelatihan berhasil disimpan!")
            else:
                st.error("Nama pelatihan wajib diisi!")

    with tab2:
        st.subheader("Daftar Pendaftar")
        if st.session_state.daftar_pendaftar:
            st.dataframe(pd.DataFrame(st.session_state.daftar_pendaftar), use_container_width=True)
            st.download_button("📥 Unduh CSV", pd.DataFrame(st.session_state.daftar_pendaftar).to_csv(index=False).encode("utf-8"), "daftar_pendaftar.csv")
        else:
            st.info("Belum ada pendaftar.")

# ====================== DASHBOARD PESERTA ======================
elif st.session_state.peran == "peserta":
    st.title("👤 Dashboard Peserta")
    if st.button("🔙 Kembali"):
        st.session_state.peran = None
        st.rerun()
    st.divider()

    if not st.session_state.daftar_pelatihan:
        st.warning("Belum ada pelatihan dibuka.")
    else:
        pilih = st.selectbox("Pilih Pelatihan", [p["nama"] for p in st.session_state.daftar_pelatihan])
        data = next(p for p in st.session_state.daftar_pelatihan if p["nama"] == pilih)

        st.subheader("📋 Informasi & Syarat Lengkap")
        st.info(f"**Tanggal:** {data['tanggal']} | **Lokasi:** {data['lokasi']}")
        with st.expander("Persyaratan Umum"):
            st.markdown(data["syarat_umum"])
        with st.expander("Persyaratan Jabatan & Kualifikasi"):
            st.write(f"**Jabatan:** {data['jabatan']}")
            for s in data["syarat_khusus"]:
                st.write(f"- {s}")

        st.subheader("📝 Isi Pendaftaran")
        nama = st.text_input("Nama Lengkap")
        nik = st.text_input("NIK")
        hp = st.text_input("No. HP/WA")
        pendidikan = st.text_input("Pendidikan Terakhir")
        pengalaman = st.number_input("Lama Pengalaman (Tahun)", min_value=0)

        st.subheader("📎 Unggah Berkas")
        ktp = st.file_uploader("KTP", type=["jpg","png","pdf"])
        ijazah = st.file_uploader("Ijazah", type=["jpg","png","pdf"])
        foto = st.file_uploader("Pas Foto", type=["jpg","png"])

        if st.checkbox("Data yang saya kirim sudah benar") and st.button("✅ Kirim Pendaftaran", type="primary"):
            nomor = f"REG-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:4].upper()}"
            st.session_state.daftar_pendaftar.append({
                "No Daftar": nomor,
                "Pelatihan": pilih,
                "Nama": nama,
                "NIK": nik,
                "HP": hp,
                "Pendidikan": pendidikan,
                "Pengalaman": pengalaman,
                "Berkas Lengkap": "Ya" if ktp and ijazah and foto else "Tidak"
            })
            st.success(f"🎉 Pendaftaran Berhasil! Nomor: {nomor}")
