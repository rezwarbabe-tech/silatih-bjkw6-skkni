import streamlit as st
import pandas as pd
from datetime import datetime

# ====================== KONFIGURASI APLIKASI ======================
st.set_page_config(
    page_title="Pendaftaran Pelatihan",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Gaya tampilan dioptimalkan untuk HP Android & iOS
st.markdown("""
<style>
    .stApp {max-width: 100%; padding: 1rem 1.2rem;}
    h1 {font-size: 1.7rem !important; text-align: center;}
    h2 {font-size: 1.3rem !important; margin-top: 1rem;}
    .stButton>button {width: 100%; padding: 0.8rem; font-size: 1.1rem; border-radius: 10px;}
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>textarea {font-size: 1rem; padding: 0.7rem; border-radius: 8px;}
    div[data-testid="stFileUploader"] {font-size: 0.95rem;}
</style>
""", unsafe_allow_html=True)

# ====================== PENYIMPANAN DATA ======================
if "data_pendaftar" not in st.session_state:
    st.session_state.data_pendaftar = []

# ====================== JUDUL APLIKASI ======================
st.title("🎓 Sistem Pendaftaran Pelatihan")
st.divider()

# ====================== FORM PENDAFTARAN ======================
st.subheader("📝 Isi Data Diri & Pilih Pelatihan")

# Data Pribadi
nama_lengkap = st.text_input("Nama Lengkap", placeholder="Tulis nama sesuai KTP")
nik = st.text_input("NIK / Nomor Identitas", placeholder="16 digit angka")
tempat_lahir = st.text_input("Tempat Lahir")
tanggal_lahir = st.date_input("Tanggal Lahir", min_value=datetime(1950,1,1))
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Pilih...", "Laki-laki", "Perempuan"])
alamat = st.text_area("Alamat Lengkap", placeholder="Jalan, RT/RW, Desa/Kelurahan, Kecamatan")
no_hp = st.text_input("Nomor HP / WhatsApp", placeholder="Contoh: 081234567890")
email = st.text_input("Alamat Email (Jika ada)")

# Pilihan Pelatihan
st.subheader("📚 Pilih Jenis Pelatihan")
jenis_pelatihan = st.selectbox(
    "Pelatihan yang diikuti",
    ["Pilih jenis pelatihan...", "Pelatihan Teknis", "Pelatihan Administrasi", "Pelatihan Keamanan", "Pelatihan Keterampilan Baru"]
)
tanggal_pelatihan = st.date_input("Tanggal Pelaksanaan Pelatihan")

# Catatan Tambahan
catatan = st.text_area("Catatan Khusus (Jika ada)", placeholder="Contoh: kebutuhan khusus, alasan mengikuti pelatihan")

# ====================== TOMBOL KIRIM ======================
if st.button("✅ Kirim Pendaftaran", type="primary"):
    # Validasi isian wajib
    if (nama_lengkap == "" or nik == "" or jenis_kelamin == "Pilih..." or 
        jenis_pelatihan == "Pilih jenis pelatihan..." or no_hp == ""):
        st.error("❌ Mohon lengkapi semua kolom yang wajib diisi terlebih dahulu!")
    else:
        # Simpan data
        data_baru = {
            "Waktu Daftar": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Nama Lengkap": nama_lengkap,
            "NIK": nik,
            "Tempat Lahir": tempat_lahir,
            "Tanggal Lahir": tanggal_lahir.strftime("%d-%m-%Y"),
            "Jenis Kelamin": jenis_kelamin,
            "Alamat": alamat,
            "No HP/WA": no_hp,
            "Email": email,
            "Jenis Pelatihan": jenis_pelatihan,
            "Tanggal Pelatihan": tanggal_pelatihan.strftime("%d-%m-%Y"),
            "Catatan": catatan
        }
        st.session_state.data_pendaftar.append(data_baru)
        
        st.success(f"🎉 Selamat {nama_lengkap}! Pendaftaranmu untuk {jenis_pelatihan} sudah diterima.")
        st.info("📩 Kami akan menghubungimu lewat nomor HP/WhatsApp yang kamu berikan untuk informasi selanjutnya.")

# ====================== TAMPILAN DATA TERDAFTAR (UNTUK ADMIN) ======================
st.divider()
with st.expander("🔍 Lihat Daftar Pendaftar"):
    if len(st.session_state.data_pendaftar) > 0:
        df = pd.DataFrame(st.session_state.data_pendaftar)
        st.dataframe(df, use_container_width=True)
        
        # Tombol unduh data ke Excel
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Unduh Data (CSV)",
            data=csv,
            file_name=f"daftar_pendaftar_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("Belum ada pendaftar yang masuk.")
