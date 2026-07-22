import streamlit as st

# ====================== KONFIGURASI UTAMA (WAJIB UNTUK HP) ======================
st.set_page_config(
    page_title="Aplikasi Saya",
    page_icon="📱",
    layout="centered",          # Tampilan pas di layar HP
    initial_sidebar_state="collapsed", # Sembunyikan menu samping di awal
    menu_items={
        'About': "Aplikasi ini berjalan di Android & iOS",
        'Report a bug': None,
        'Get Help': None
    }
)

# Hilangkan margin berlebih & sesuaikan ukuran font untuk HP
st.markdown("""
<style>
    .stApp {
        max-width: 100%;
        padding: 1rem 1.2rem;
    }
    h1 { font-size: 1.8rem !important; }
    h2 { font-size: 1.4rem !important; }
    h3 { font-size: 1.2rem !important; }
    .stButton>button {
        width: 100%;
        padding: 0.8rem;
        font-size: 1.1rem;
        border-radius: 12px;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>select {
        font-size: 1rem;
        padding: 0.7rem;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ====================== ISI APLIKASI ======================
st.title("👋 Selamat Datang di Aplikasi Saya")
st.subheader("Kompatibel dengan Android & iOS")
st.divider()

# Bagian Input Data
st.subheader("📝 Isi Data Diri")
nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama kamu")
umur = st.number_input("Umur", min_value=1, max_value=120, value=17)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Pilih...", "Laki-laki", "Perempuan"])

# Tombol Kirim
if st.button("✅ Kirim Data", type="primary"):
    if nama == "" or jenis_kelamin == "Pilih...":
        st.error("❌ Silakan lengkapi semua data terlebih dahulu!")
    else:
        st.success(f"🎉 Terima kasih {nama}! Data kamu sudah tersimpan.")
        st.info(f"📋 Ringkasan: Umur {umur} tahun, {jenis_kelamin}")

# Informasi Tambahan
st.divider()
st.caption("💡 Aplikasi ini bisa dibuka di browser HP maupun dibungkus menjadi aplikasi di Play Store/App Store")
st.caption("🔄 Setiap perubahan kode akan otomatis terupdate tanpa perlu instal ulang aplikasi")
