# ==============================================
# 1. MUAT PUSTAKA & GAYA KUSTOM KEMENTERIAN PU
# ==============================================
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO
from datetime import datetime

# === GAYA TAMPILAN RESMI KEMENTERIAN PEKERJAAN UMUM ===
st.markdown("""
<style>
:root {
    --pu-biru-utama: #004B87;
    --pu-biru-terang: #0071BC;
    --pu-biru-muda: #E8F3FC;
    --pu-hijau: #059669;
    --pu-kuning: #F59E0B;
    --pu-merah: #DC2626;
    --pu-abu: #F5F7FA;
    --pu-teks: #2C3E50;
}
.stApp {
    background-color: var(--pu-biru-muda);
    font-family: 'Segoe UI', Roboto, sans-serif;
}
h1, h2, h3, h4 { color: var(--pu-biru-utama); font-weight: 700; }
.stButton>button {
    background-color: var(--pu-biru-utama); color: white; border-radius: 6px;
    border: 2px solid var(--pu-biru-utama); padding: 0.5rem 1.2rem;
}
.stButton>button:hover { background-color: var(--pu-biru-terang); border-color: var(--pu-biru-terang); }
.pu-kotak { background: white; border-left: 6px solid var(--pu-biru-utama); padding: 1.2rem; border-radius: 8px; margin-bottom: 1rem; }
.pu-sukses { background: #F0FDF4; border-left: 6px solid var(--pu-hijau); padding: 1rem; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# ==============================================
# 2. KONFIGURASI & JUDUL APLIKASI
# ==============================================
st.set_page_config(
    page_title="Pemantauan Kinerja Anggaran BJKW VI Makassar",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("<hr style='border: 3px solid #004B87; border-radius: 2px; margin-bottom: 1.5rem;'>", unsafe_allow_html=True)
st.title("📊 Pemantauan Indikator Pelaksanaan Anggaran")
st.subheader("Balai Jasa Konstruksi Wilayah VI Makassar")
st.markdown("<h3 style='color:#004B87;'>Kementerian Pekerjaan Umum</h3>", unsafe_allow_html=True)
st.markdown("---")

# ==============================================
# 3. UNGGAH BERKAS DATA
# ==============================================
st.subheader("📂 Unggah Berkas Data Anggaran")
berkas = st.file_uploader("Pilih berkas Excel Indikator Pelaksanaan Anggaran Satker", type=["xlsx", "xls"])

# Data contoh dari berkas yang kamu kirim (jika belum unggah berkas)
data_contoh = pd.DataFrame([
    {
        "Bulan": "Juli",
        "Tahun": 2026,
        "Revisi DIPA": 100.00,
        "Deviasi Halaman III DIPA": 59.50,
        "Kualitas Perencanaan Anggaran": 79.75,
        "Penyerapan Anggaran": 93.06,
        "Belanja Kontraktual": 100.00,
        "Penyelesaian Tagihan": 100.00,
        "Pengelolaan UP dan TUP": 89.53,
        "Kualitas Pelaksanaan Anggaran": 95.65,
        "Capaian Output": 66.49,
        "Nilai Akhir": 66.49
    }
])

if berkas is not None:
    try:
        df = pd.read_excel(berkas)
        st.success("✅ Berkas berhasil dibaca! Menampilkan data dari berkas yang diunggah.")
    except Exception as e:
        st.warning("⚠️ Gagal membaca berkas, menampilkan data contoh dari Juli 2026")
        df = data_contoh
else:
    st.info("ℹ️ Belum ada berkas yang diunggah, menampilkan data contoh dari Juli 2026. Silakan unggah berkas lengkap untuk melihat data satu tahun berjalan.")
    df = data_contoh

# ==============================================
# 4. TAMPILAN DATA RINGKASAN
# ==============================================
st.markdown("---")
st.header("📋 Ringkasan Data Capaian")
st.dataframe(df, use_container_width=True, hide_index=True)

# ==============================================
# 5. GRAFIK & DIAGRAM CAPAIAN PER BULAN
# ==============================================
st.markdown("---")
st.header("📈 Visualisasi Capaian Selama Satu Tahun Berjalan")

# Jika data kurang dari 12 bulan, tambahkan catatan
if len(df) < 12:
    st.info("📝 Saat ini baru tersedia data bulan Juli. Setelah unggah data lengkap 12 bulan, grafik akan menampilkan seluruh periode tahun berjalan.")

# === GRAFIK GARIS: PERKEMBANGAN NILAI UTAMA ===
st.subheader("📊 Perkembangan Nilai Utama Tiap Bulan")
kolom_grafik = ["Kualitas Perencanaan Anggaran", "Kualitas Pelaksanaan Anggaran", "Capaian Output", "Nilai Akhir"]
fig_garis = px.line(
    df,
    x="Bulan",
    y=kolom_grafik,
    markers=True,
    color_discrete_sequence=["#004B87", "#0071BC", "#F59E0B", "#059669"],
    title="Perkembangan Indikator Kinerja Anggaran",
    labels={"value": "Nilai (0-100)", "variable": "Indikator"}
)
fig_garis.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="#2C3E50")
st.plotly_chart(fig_garis, use_container_width=True)

# === DIAGRAM BATANG: PERBANDINGAN INDIKATOR ===
st.subheader("📊 Perbandingan Capaian Tiap Indikator")
kolom_batang = ["Revisi DIPA", "Deviasi Halaman III DIPA", "Penyerapan Anggaran", "Belanja Kontraktual", "Penyelesaian Tagihan", "Pengelolaan UP dan TUP", "Capaian Output"]
fig_batang = px.bar(
    df.melt(id_vars="Bulan", value_vars=kolom_batang),
    x="variable",
    y="value",
    color="Bulan",
    barmode="group",
    color_discrete_sequence=px.colors.qualitative.Set2,
    title="Nilai Capaian Tiap Komponen Indikator",
    labels={"value": "Nilai Capaian", "variable": "Komponen Indikator"}
)
fig_batang.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_color="#2C3E50", xaxis_tickangle=-45)
st.plotly_chart(fig_batang, use_container_width=True)

# === DIAGRAM PIE: KOMPOSISI NILAI ===
st.subheader("🥧 Komposisi Sumber Nilai Akhir")
nilai_komponen = {
    "Komponen": ["Kualitas Perencanaan", "Kualitas Pelaksanaan", "Kualitas Hasil"],
    "Kontribusi": [df["Kualitas Perencanaan Anggaran"].iloc[0] * 0.25, df["Kualitas Pelaksanaan Anggaran"].iloc[0] * 0.40, df["Capaian Output"].iloc[0] * 0.35]
}
df_pie = pd.DataFrame(nilai_komponen)
fig_pie = px.pie(
    df_pie,
    values="Kontribusi",
    names="Komponen",
    color_discrete_sequence=["#004B87", "#0071BC", "#F59E0B"],
    title="Komposisi Pembentukan Nilai Akhir Kinerja"
)
fig_pie.update_layout(paper_bgcolor="white", font_color="#2C3E50")
st.plotly_chart(fig_pie, use_container_width=True)

# ==============================================
# 6. INFORMASI SATUAN KERJA
# ==============================================
st.markdown("---")
st.markdown("""
<div class="pu-kotak">
<h4>🏢 Data Satuan Kerja</h4>
<p><strong>Nama Satker:</strong> Balai Jasa Konstruksi Wilayah VI Makassar<br>
<strong>Kode KPPN:</strong> 054<br>
<strong>Kode BA:</strong> 145<br>
<strong>Kode Satker:</strong> 694413<br>
<strong>Periode Data:</strong> Juli 2026</p>
</div>
""", unsafe_allow_html=True)

# Kaki halaman
st.markdown("<hr style='border: 2px solid #004B87; margin-top: 2rem;'>", unsafe_allow_html=True)
st.caption("© 2026 Balai Jasa Konstruksi Wilayah VI Makassar — Kementerian Pekerjaan Umum | Aplikasi Pemantauan Kinerja Anggaran")
