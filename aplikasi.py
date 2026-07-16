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
# DATA PEMETAAN JABATAN KERJA (LENGKAP DENGAN KLASIFIKASI & SUBKLASIFIKASI)
# ==============================================================
DATA_JABATAN_KERJA = [
    {
        "namaJabatan": "Ahli Perencanaan Konstruksi",
        "kualifikasi": "AHLI",
        "subKlasifikasi": "Perencanaan & Rekayasa",
        "jenjang": 9,
        "syaratPendidikan": "Doktor/Doktor Terapan/Pendidikan Spesialis_2",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Ahli Pengawas Konstruksi Utama",
        "kualifikasi": "AHLI",
        "subKlasifikasi": "Pengawasan & Pengendalian",
        "jenjang": 8,
        "syaratPendidikan": "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Ahli Manajemen Proyek Konstruksi",
        "kualifikasi": "AHLI",
        "subKlasifikasi": "Manajemen Proyek",
        "jenjang": 7,
        "syaratPendidikan": "Pendidikan Profesi / S1/S1 Terapan/D4 Terapan",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Analis Biaya & Rencana Anggaran",
        "kualifikasi": "TEKNIS/ANALIS",
        "subKlasifikasi": "Perencanaan Biaya",
        "jenjang": 6,
        "syaratPendidikan": "S1/S1 Terapan/D4 Terapan",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Teknisi Pengujian Bahan Konstruksi",
        "kualifikasi": "TEKNIS/ANALIS",
        "subKlasifikasi": "Pengujian & Kualitas",
        "jenjang": 5,
        "syaratPendidikan": "D3",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Teknisi Gambar Kerja & Desain",
        "kualifikasi": "TEKNIS/ANALIS",
        "subKlasifikasi": "Desain & Dokumentasi",
        "jenjang": 4,
        "syaratPendidikan": "D2",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Operator Alat Berat Ekskavator",
        "kualifikasi": "OPERATOR",
        "subKlasifikasi": "Pengoperasian Alat Berat",
        "jenjang": 3,
        "syaratPendidikan": "D1/SMK Plus",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Operator Pekerjaan Beton",
        "kualifikasi": "OPERATOR",
        "subKlasifikasi": "Pelaksanaan Lapangan",
        "jenjang": 2,
        "syaratPendidikan": "SMK",
        "pengalamanMinimal": 0
    },
    {
        "namaJabatan": "Pekerja Umum Konstruksi",
        "kualifikasi": "OPERATOR",
        "subKlasifikasi": "Pelaksanaan Dasar",
        "jenjang": 1,
        "syaratPendidikan": "Pendidikan Dasar / Non Pendidikan (Dengan PBK)",
        "pengalamanMinimal": 0
    }
]

# ==============================================================
# PENYIMPANAN DATA
# ==============================================================
if "daftar_pelatihan" not in st.session_state:
    st.session_state.daftar_pelatihan = []

# ==============================================================
# FUNGSI PENGELOLAAN
# ==============================================================
def simpan_pelatihan(data):
    data["id"] = datetime.now().timestamp()
    data["tanggal_dibuat"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["status"] = "Tersedia"
    st.session_state.daftar_pelatihan.append(data)
    return True

def ubah_pelatihan(id_pelatihan, data_baru):
    for idx, pelatihan in enumerate(st.session_state.daftar_pelatihan):
        if pelatihan["id"] == id_pelatihan:
            st.session_state.daftar_pelatihan[idx].update(data_baru)
            st.session_state.daftar_pelatihan[idx]["tanggal_diubah"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    return False

def hapus_pelatihan(id_pelatihan):
    st.session_state.daftar_pelatihan = [p for p in st.session_state.daftar_pelatihan if p["id"] != id_pelatihan]
    return True

# ==============================================================
# TAMPILAN JUDUL UTAMA
# ==============================================================
st.markdown("""
<div class="header-box">
    <h1>Aplikasi Pelatihan & Sertifikasi UJI Kompetensi</h1>
    <h2>Balai Jasa Konstruksi Wilayah VI Makassar</h2>
    <p>siLATIH - Sistem Informasi Pelatihan Terintegrasi</p>
</div>
""", unsafe_allow_html=True)

# ==============================================================
# PILIH PERAN
# ==============================================================
peran = st.sidebar.selectbox("Pilih Peran Anda", ["Pengelola", "Peserta"])

# ==============================================================
# MENU PENGELOLA
# ==============================================================
if peran == "Pengelola":
    st.markdown("""
    <div class="menu-pengelola">
        <h3>🔧 Menu Pengelola</h3>
        <p>Pilih langsung Jabatan Kerja — klasifikasi, subklasifikasi, dan persyaratan terisi otomatis sesuai pemetaan resmi</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📝 Buat Pelatihan Berdasarkan Jabatan Kerja")
    
    # PILIH JABATAN KERJA (OTOMATIS MEMETA)
    pilihan_jabatan = [jab["namaJabatan"] for jab in DATA_JABATAN_KERJA]
    jabatan_terpilih = st.selectbox("Pilih Nama Jabatan Kerja", pilihan_jabatan)
    
    # AMBIL DATA OTOMATIS BERDASARKAN JABATAN YANG DIPILIH
    data_jabatan = next(jab for jab in DATA_JABATAN_KERJA if jab["namaJabatan"] == jabatan_terpilih)

    # TAMPILKAN DATA YANG SUDAH TERPETAKAN (TIDAK BISA DIUBAH)
    st.markdown("### 📋 Data Jabatan (Terpetakan Otomatis)")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Klasifikasi**: {data_jabatan['kualifikasi']}")
        st.info(f"**Sub Klasifikasi**: {data_jabatan['subKlasifikasi']}")
    with col2:
        st.info(f"**Jenjang Jabatan**: {data_jabatan['jenjang']}")
    
    st.markdown('<div class="syarat-box">', unsafe_allow_html=True)
    st.markdown(f"**Persyaratan Pendidikan**: {data_jabatan['syaratPendidikan']}")
    st.markdown(f"**Pengalaman Minimal**: {data_jabatan['pengalamanMinimal']} tahun")
    st.markdown('</div>', unsafe_allow_html=True)

    # FORM TAMBAHAN PELATIHAN
    st.markdown("### 📝 Isi Detail Pelatihan")
    with st.form("form_pelatihan_jabatan"):
        nama_pelatihan = st.text_input("Nama Pelatihan", value=f"Pelatihan Sertifikasi {jabatan_terpilih}")
        deskripsi = st.text_area("Deskripsi & Tujuan Pelatihan")
        tanggal_pelaksanaan = st.date_input("Tanggal Pelaksanaan")
        lokasi = st.text_input("Lokasi Pelatihan")
        tombol_simpan = st.form_submit_button("💾 Simpan Pelatihan")

        if tombol_simpan:
            simpan_pelatihan({
                "namaJabatan": jabatan_terpilih,
                "kualifikasi": data_jabatan["kualifikasi"],
                "subKlasifikasi": data_jabatan["subKlasifikasi"],
                "jenjang": data_jabatan["jenjang"],
                "syaratPendidikan": data_jabatan["syaratPendidikan"],
                "pengalamanMinimal": data_jabatan["pengalamanMinimal"],
                "namaPelatihan": nama_pelatihan,
                "deskripsi": deskripsi,
                "tanggalPelaksanaan": tanggal_pelaksanaan.strftime("%d-%m-%Y"),
                "lokasi": lokasi
            })
            st.success("✅ Pelatihan berhasil disimpan! Semua data jabatan sudah sesuai pemetaan resmi.")

    # DAFTAR PELATIHAN & PENGELOLAAN
    st.subheader("📋 Daftar Semua Pelatihan yang Telah Dibuat")
    if st.session_state.daftar_pelatihan:
        df = pd.DataFrame(st.session_state.daftar_pelatihan)
        tampil_kolom = ["namaPelatihan", "namaJabatan", "kualifikasi", "jenjang", "tanggalPelaksanaan", "lokasi", "status"]
        st.dataframe(df[tampil_kolom])

        id_pilih = st.selectbox("Pilih Pelatihan untuk diubah/dihapus",
                                options=[p["id"] for p in st.session_state.daftar_pelatihan],
                                format_func=lambda x: f"{next(p['namaPelatihan'] for p in st.session_state.daftar_pelatihan if p['id']==x)}")
        
        col_e, col_h = st.columns(2)
        with col_e:
            if st.button("✏️ Ubah Status"):
                ubah_pelatihan(id_pilih, {"status": "Ditutup" if next(p["status"] for p in st.session_state.daftar_pelatihan if p["id"]==id_pilih) == "Tersedia" else "Tersedia"})
                st.rerun()
        with col_h:
            if st.button("🗑️ Hapus Pelatihan", type="secondary"):
                hapus_pelatihan(id_pilih)
                st.rerun()
    else:
        st.info("Belum ada pelatihan yang dibuat. Silakan pilih jabatan di atas.")

# ==============================================================
# MENU PESERTA
# ==============================================================
elif peran == "Peserta":
    st.markdown("""
    <div class="menu-peserta">
        <h3>👤 Menu Tamu / Peserta</h3>
        <p>Lihat pelatihan yang tersedia beserta persyaratan jabatan kerjanya</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📚 Daftar Pelatihan Tersedia")
    pelatihan_tersedia = [p for p in st.session_state.daftar_pelatihan if p["status"] == "Tersedia"]
    
    if pelatihan_tersedia:
        for pelatihan in pelatihan_tersedia:
            with st.expander(f"📌 {pelatihan['namaPelatihan']} — {pelatihan['namaJabatan']}"):
                st.write(f"**Klasifikasi**: {pelatihan['kualifikasi']}")
                st.write(f"**Sub Klasifikasi**: {pelatihan['subKlasifikasi']}")
                st.write(f"**Jenjang**: {pelatihan['jenjang']}")
                st.write(f"**Syarat Pendidikan**: {pelatihan['syaratPendidikan']}")
                st.write(f"**Pengalaman Minimal**: {pelatihan['pengalamanMinimal']} tahun")
                st.write(f"**Tanggal**: {pelatihan['tanggalPelaksanaan']}")
                st.write(f"**Lokasi**: {pelatihan['lokasi']}")
                st.write(f"**Deskripsi**: {pelatihan['deskripsi']}")
    else:
        st.info("Saat ini belum ada pelatihan yang tersedia untuk pendaftaran.")

# ==============================================================
# INFORMASI PEMETAAN JABATAN
# ==============================================================
st.subheader("📋 Ringkasan Pemetaan Jabatan Kerja")
st.markdown("""
<div class="kategori-ahli">
    <h4>🟡 Kualifikasi Ahli (Jenjang 9, 8, 7)</h4>
    <p>Untuk jabatan yang membutuhkan keahlian tingkat tinggi, perencanaan, dan pengambilan keputusan strategis.</p>
</div>
<div class="kategori-teknis">
    <h4>🔵 Kualifikasi Teknis / Analis (Jenjang 6, 5, 4)</h4>
    <p>Untuk jabatan teknis, pengujian, analisis, dan dukungan pelaksanaan pekerjaan.</p>
</div>
<div class="kategori-operator">
    <h4>🟢 Kualifikasi Operator (Jenjang 3, 2, 1)</h4>
    <p>Untuk jabatan pelaksana lapangan, pengoperasian alat, dan pekerjaan dasar konstruksi.</p>
</div>
""", unsafe_allow_html=True)

# ==============================================================
# HAK CIPTA
# ==============================================================
st.markdown("""
<div class="footer-box">
    © 2026 Balai Jasa Konstruksi Wilayah VI Makassar — Kementerian Pekerjaan Umum | siLATIH v2.2
</div>
""", unsafe_allow_html=True)
