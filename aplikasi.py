import streamlit as st
import pandas as pd
from datetime import datetime

# === Konfigurasi Halaman ===
st.set_page_config(page_title="Sertifikat Pelatihan", page_icon="📜", layout="wide")

# === Simulasi Koneksi ke API Base44 ===
# Ganti bagian ini dengan pemanggilan API asli kamu
@st.cache_data(ttl=10)
def muat_sertifikat():
    try:
        # Ganti dengan: return base44.entities.Certificate.list("-created_date", 50)
        return st.session_state.get("sertifikat_data", [])
    except Exception as e:
        st.error(f"Gagal memuat sertifikat: {e}")
        return []

@st.cache_data(ttl=10)
def muat_pelatihan():
    try:
        # Ganti dengan: return base44.entities.Training.list("-created_date", 50)
        return st.session_state.get("pelatihan_data", [])
    except Exception as e:
        st.error(f"Gagal memuat pelatihan: {e}")
        return []

def simpan_sertifikat(data):
    try:
        # Ganti dengan: await base44.entities.Certificate.create(data)
        if "sertifikat_data" not in st.session_state:
            st.session_state["sertifikat_data"] = []
        data["id"] = len(st.session_state["sertifikat_data"]) + 1
        st.session_state["sertifikat_data"].append(data)
        st.cache_data.clear()
        return True
    except Exception as e:
        st.error(f"Gagal menyimpan: {e}")
        return False

def ubah_status(id_sertifikat, status_baru):
    try:
        # Ganti dengan: await base44.entities.Certificate.update(id_sertifikat, {"status": status_baru})
        for sertif in st.session_state["sertifikat_data"]:
            if sertif["id"] == id_sertifikat:
                sertif["status"] = status_baru
                break
        st.cache_data.clear()
        return True
    except Exception as e:
        st.error(f"Gagal mengubah status: {e}")
        return False

# === Inisialisasi Data Contoh ===
if "pelatihan_data" not in st.session_state:
    st.session_state["pelatihan_data"] = [
        {"id": "1", "title": "Pelatihan Dasar Keselamatan Kerja"},
        {"id": "2", "title": "Pelatihan Manajemen Proyek"},
        {"id": "3", "title": "Pelatihan Pengolahan Data"}
    ]
if "sertifikat_data" not in st.session_state:
    st.session_state["sertifikat_data"] = [
        {
            "id": 1,
            "training_id": "1",
            "participant_name": "Budi Santoso",
            "certificate_number": "SERT-2026-001",
            "issue_date": "2026-07-20",
            "training_title": "Pelatihan Dasar Keselamatan Kerja",
            "status": "Draft"
        }
    ]

# === Tampilan Utama ===
st.title("📜 Sertifikat Terbit")
st.subheader("Kelola penerbitan sertifikat pelatihan")

# Tombol Tambah & Pencarian
col_tombol, col_cari = st.columns([1, 2])
with col_tombol:
    tombol_tambah = st.button("➕ Terbitkan Sertifikat Baru", type="primary")
with col_cari:
    kata_kunci = st.text_input("🔍 Cari nama peserta", placeholder="Ketik nama peserta...")

# === Form Tambah Sertifikat ===
if tombol_tambah:
    with st.expander("Formulir Penerbitan Sertifikat", expanded=True):
        pelatihan_list = muat_pelatihan()
        if not pelatihan_list:
            st.warning("Data pelatihan belum tersedia!")
        else:
            with st.form("form_sertifikat"):
                pilihan_pelatihan = st.selectbox(
                    "Pilih Pelatihan *",
                    options=[p["id"] for p in pelatihan_list],
                    format_func=lambda x: next((p["title"] for p in pelatihan_list if p["id"] == x), x)
                )
                nama_peserta = st.text_input("Nama Lengkap Peserta *")
                nomor_sertifikat = st.text_input("Nomor Sertifikat *")
                tanggal_terbit = st.date_input("Tanggal Terbit *", value=datetime.today())

                if st.form_submit_button("💾 Simpan & Terbitkan"):
                    if not all([pilihan_pelatihan, nama_peserta.strip(), nomor_sertifikat.strip(), tanggal_terbit]):
                        st.error("Semua kolom bertanda * wajib diisi!")
                    else:
                        pelatihan_terpilih = next((p for p in pelatihan_list if p["id"] == pilihan_pelatihan), None)
                        data_baru = {
                            "training_id": pilihan_pelatihan,
                            "participant_name": nama_peserta.strip(),
                            "certificate_number": nomor_sertifikat.strip(),
                            "issue_date": tanggal_terbit.strftime("%Y-%m-%d"),
                            "training_title": pelatihan_terpilih["title"] if pelatihan_terpilih else "",
                            "status": "Draft"
                        }
                        if simpan_sertifikat(data_baru):
                            st.success("✅ Sertifikat berhasil ditambahkan!")
                            st.rerun()

# === Tampilan Daftar Sertifikat ===
st.divider()
data_sertifikat = muat_sertifikat()

# Filter data
if kata_kunci:
    data_terfilter = [
        s for s in data_sertifikat
        if kata_kunci.lower() in str(s.get("participant_name", "")).lower()
    ]
else:
    data_terfilter = data_sertifikat

if not data_terfilter:
    st.info("ℹ️ " + ("Tidak ada sertifikat yang cocok dengan pencarian" if kata_kunci else "Belum ada sertifikat yang diterbitkan"))
else:
    st.subheader(f"Ditemukan {len(data_terfilter)} sertifikat")
    for sertif in data_terfilter:
        with st.container(border=True):
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                st.markdown(f"**{sertif.get('participant_name', 'Peserta Tidak Diketahui')}**")
                st.caption(f"No: {sertif.get('certificate_number', '-')} | {sertif.get('training_title', '-')}")
                st.caption(f"Terbit: {sertif.get('issue_date', '-')}")
            with col2:
                status = sertif.get("status", "Draft")
                warna_status = {"Draft": "🟤 Draft", "Terbit": "🟢 Terbit", "Dikirim": "🔵 Dikirim"}.get(status, status)
                st.info(warna_status)
            with col3:
                if status == "Draft":
                    if st.button(f"Terbitkan", key=f"terbit_{sertif['id']}", type="primary"):
                        if ubah_status(sertif["id"], "Terbit"):
                            st.success("Status diubah menjadi Terbit")
                            st.rerun()
                elif status == "Terbit":
                    if st.button(f"Kirim", key=f"kirim_{sertif['id']}", type="primary"):
                        if ubah_status(sertif["id"], "Dikirim"):
                            st.success("Status diubah menjadi Dikirim")
                            st.rerun()
            with col4:
                st.empty()
