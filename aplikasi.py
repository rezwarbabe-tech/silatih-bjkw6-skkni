# Tampilkan data otomatis sesuai master data (judul sudah diganti)
    st.markdown("### 📋 Data Jabatan Kerja Sesuai SKKNI")
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Kode & Klasifikasi**: {data_jabatan['kode_klasifikasi']} - {data_jabatan['klasifikasi']}")
        st.info(f"**Sub Klasifikasi**: {data_jabatan['sub_klasifikasi']}")
        st.info(f"**Kualifikasi**: {data_jabatan['kualifikasi']}")
    with col2:
        st.info(f"**ID Jabatan**: {data_jabatan['id_jabatan']}")
        st.info(f"**Jenjang Jabatan**: {data_jabatan['jenjang']}")
        st.info(f"**Acuan SKKNI**: {data_jabatan['acuan']}")
    
    st.markdown(f"**Keterangan**: {data_jabatan['keterangan']}")

    # Form detail pelatihan
    st.markdown("### 📝 Isi Detail Pelatihan")
    with st.form("form_pelatihan_jabatan"):
        nama_pelatihan = st.text_input("Nama Pelatihan", value=f"Pelatihan Sertifikasi {data_jabatan['jabatan_kerja']}")
        deskripsi = st.text_area("Deskripsi & Tujuan Pelatihan")
        tanggal_pelaksanaan = st.date_input("Tanggal Pelaksanaan")
        lokasi = st.text_input("Lokasi Pelatihan")
        kuota = st.number_input("Kuota Peserta", min_value=1, value=30)
        tombol_simpan = st.form_submit_button("💾 Simpan Pelatihan")

        if tombol_simpan:
            berhasil = simpan_pelatihan({
                "id_jabatan": data_jabatan["id_jabatan"],
                "jabatan_kerja": data_jabatan["jabatan_kerja"],
                "nama_pelatihan": nama_pelatihan,
                "deskripsi": deskripsi,
                "tanggal_pelaksanaan": tanggal_pelaksanaan.strftime("%Y-%m-%d"),
                "lokasi": lokasi,
                "kuota": kuota,
                "kualifikasi": data_jabatan["kualifikasi"],
                "jenjang": data_jabatan["jenjang"],
                "acuan_skkni": data_jabatan["acuan"]
            })
            if berhasil:
                st.success("✅ Data pelatihan berhasil disimpan!")
            else:
                st.error("❌ Gagal menyimpan data pelatihan!")

# ==============================================================
# MENU PESERTA (BONUS AGAR TIDAK ERROR)
# ==============================================================
else:
    st.markdown("""
    <div class="menu-peserta">
        <h3>👤 Menu Peserta</h3>
        <p>Lihat daftar pelatihan yang tersedia dan daftarkan diri Anda.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📚 Daftar Pelatihan Tersedia")
    if len(st.session_state.daftar_pelatihan) == 0:
        st.info("Belum ada pelatihan yang dibuat. Silakan kembali nanti!")
    else:
        for pelatihan in st.session_state.daftar_pelatihan:
            with st.expander(f"{pelatihan['nama_pelatihan']} — {pelatihan['status']}"):
                st.write(f"**Jabatan Kerja**: {pelatihan['jabatan_kerja']}")
                st.write(f"**Tanggal Pelaksanaan**: {pelatihan['tanggal_pelaksanaan']}")
                st.write(f"**Lokasi**: {pelatihan['lokasi']}")
                st.write(f"**Kuota**: {pelatihan['kuota']} peserta")
                st.write(f"**Acuan SKKNI**: {pelatihan['acuan_skkni']}")

# ==============================================================
# TAMPILAN FOOTER
# ==============================================================
st.markdown("""
<div class="footer-box">
    © 2026 Balai Jasa Konstruksi Wilayah VI Makassar | siLATIH - Sistem Informasi Pelatihan Terintegrasi
</div>
""", unsafe_allow_html=True)
