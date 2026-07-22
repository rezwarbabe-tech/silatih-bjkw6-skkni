import streamlit as st

# === KONFIGURASI HALAMAN ===
st.set_page_config(
    page_title="siLATI - Sistem Pelatihan Terintegrasi",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === KODE LENGKAP: HTML + CSS + JAVASCRIPT ===
kode_lengkap = """
<html>
<head>
  <meta charset="UTF-8">
  <title>siLATI - Sistem Pelatihan Terintegrasi</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *{box-sizing:border-box; font-family:'Poppins', sans-serif; margin:0; padding:0;}
    :root{
      --biru-tua:#0A2463;
      --biru-tengah:#1E3A8A;
      --emas:#DAA520;
      --kuning-terang:#FFD700;
      --hijau-daun:#2E8B57;
      --merah-bata:#C43A31;
      --putih:#FFFFFF;
      --abu-lembut:#F8FAFC;
      --abu-batas:#E2E8F0;
    }
    body{
      background:linear-gradient(135deg, #F0F4FF 0%, #F8FBFF 100%);
      min-height:100vh;
      padding:20px 10px;
      position:relative;
      overflow-x:hidden;
    }
    
    body::before{
      content:"";
      position:fixed;
      top:-120px;
      right:-120px;
      width:450px;
      height:450px;
      background:radial-gradient(circle, rgba(218,165,32,0.08) 0%, transparent 70%);
      z-index:-1;
    }
    body::after{
      content:"";
      position:fixed;
      bottom:-100px;
      left:-100px;
      width:400px;
      height:400px;
      background:radial-gradient(circle, rgba(46,139,87,0.07) 0%, transparent 70%);
      z-index:-1;
    }
    
    .wadah{
      max-width:1000px;
      margin:0 auto;
      padding:32px;
      background:var(--putih);
      border-radius:20px;
      box-shadow:0 8px 32px rgba(10,36,99,0.12);
      position:relative;
      overflow:hidden;
      border-top:6px solid var(--emas);
    }
    .wadah::before{
      content:"";
      position:absolute;
      top:0;
      left:0;
      width:100%;
      height:5px;
      background:linear-gradient(90deg, var(--biru-tua) 0%, var(--emas) 50%, var(--hijau-daun) 100%);
    }
    
    h1{
      font-size:2rem;
      text-align:center;
      color:var(--biru-tua);
      margin-bottom:8px;
      font-weight:700;
      letter-spacing:0.5px;
    }
    h1 span{color:var(--emas);}
    h2{
      font-size:1.4rem;
      margin:1.5rem 0 1rem;
      color:var(--biru-tengah);
      font-weight:600;
      display:flex;
      align-items:center;
      gap:8px;
    }
    h2::before{
      content:"";
      width:6px;
      height:24px;
      background:linear-gradient(180deg, var(--emas) 0%, var(--hijau-daun) 100%);
      border-radius:3px;
    }
    h3{
      font-size:1.15rem;
      margin:1.2rem 0 0.7rem;
      color:#1E293B;
      font-weight:600;
    }
    
    .tombol{
      width:100%;
      padding:14px 20px;
      border:none;
      border-radius:12px;
      font-size:1rem;
      font-weight:500;
      cursor:pointer;
      transition:all 0.3s ease;
      margin:8px 0;
      display:flex;
      align-items:center;
      justify-content:center;
      gap:8px;
      position:relative;
      overflow:hidden;
    }
    .tombol::after{
      content:"";
      position:absolute;
      top:0;
      left:-100%;
      width:100%;
      height:100%;
      background:linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
      transition:left 0.5s ease;
    }
    .tombol:hover::after{left:100%;}
    .tombol-utama{
      background:linear-gradient(135deg, var(--biru-tua) 0%, var(--biru-tengah) 100%);
      color:white;
      box-shadow:0 4px 12px rgba(10,36,99,0.3);
    }
    .tombol-utama:hover{
      transform:translateY(-2px);
      box-shadow:0 6px 20px rgba(10,36,99,0.4);
    }
    .tombol-biasa{
      background:var(--abu-lembut);
      color:var(--biru-tengah);
      border:2px solid var(--abu-batas);
      font-weight:500;
    }
    .tombol-biasa:hover{
      background:rgba(218,165,32,0.08);
      border-color:var(--emas);
      transform:translateY(-1px);
    }
    .tombol-hijau{
      background:linear-gradient(135deg, var(--hijau-daun) 0%, #227048 100%);
      color:white;
      box-shadow:0 4px 12px rgba(46,139,87,0.3);
      margin-bottom:16px;
    }
    .tombol-hijau:hover{
      transform:translateY(-2px);
      box-shadow:0 6px 20px rgba(46,139,87,0.4);
    }
    
    .grup{margin-bottom:18px;}
    .dua-kolom{
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:16px;
    }
    label{
      display:block;
      margin-bottom:8px;
      font-weight:500;
      color:#334155;
      font-size:0.95rem;
    }
    input, select, textarea{
      width:100%;
      padding:12px 16px;
      border:2px solid var(--abu-batas);
      border-radius:10px;
      font-size:0.95rem;
      transition:all 0.3s ease;
      background:var(--putih);
    }
    input:focus, select:focus, textarea:focus{
      outline:none;
      border-color:var(--emas);
      box-shadow:0 0 0 4px rgba(218,165,32,0.15);
    }
    
    .info{
      padding:16px;
      background:linear-gradient(135deg, rgba(10,36,99,0.05) 0%, rgba(30,58,138,0.08) 100%);
      border-left:5px solid var(--biru-tua);
      border-radius:12px;
      margin:12px 0;
      font-size:0.95rem;
      color:var(--biru-tengah);
    }
    .peringatan{
      padding:16px;
      background:linear-gradient(135deg, rgba(218,165,32,0.08) 0%, rgba(255,215,0,0.1) 100%);
      border-left:5px solid var(--emas);
      border-radius:12px;
      margin:12px 0;
      font-size:0.95rem;
      color:#92400E;
    }
    .berhasil{
      padding:16px;
      background:linear-gradient(135deg, rgba(46,139,87,0.05) 0%, rgba(34,112,72,0.08) 100%);
      border-left:5px solid var(--hijau-daun);
      border-radius:12px;
      margin:12px 0;
      font-size:0.95rem;
      color:#166534;
    }
    
    .sembunyi{display:none;}
    .grid{
      display:grid;
      grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));
      gap:16px;
      margin:24px 0;
    }
    hr{
      border:none;
      border-top:2px solid var(--abu-batas);
      margin:24px 0;
      position:relative;
    }
    hr::after{
      content:"";
      position:absolute;
      top:-1px;
      left:50%;
      transform:translateX(-50%);
      width:120px;
      height:3px;
      background:linear-gradient(90deg, var(--biru-tua), var(--emas), var(--hijau-daun));
      border-radius:2px;
    }
    
    .daftar-item{
      padding:14px;
      border-bottom:1px solid var(--abu-batas);
      font-size:0.9rem;
      transition:all 0.2s ease;
      border-radius:8px;
      margin-bottom:8px;
    }
    .daftar-item:hover{
      background:rgba(218,165,32,0.05);
      padding-left:18px;
    }
    .daftar-item:last-child{border-bottom:none; margin-bottom:0;}
    
    .sub-judul{
      text-align:center;
      color:#475569;
      margin-bottom:20px;
      font-size:1rem;
      line-height:1.6;
    }
    .tag-pupr{
      display:inline-block;
      padding:6px 14px;
      background:linear-gradient(135deg, var(--biru-tua) 0%, var(--biru-tengah) 100%);
      color:var(--putih);
      border-radius:24px;
      font-size:0.8rem;
      font-weight:500;
      margin-top:6px;
      box-shadow:0 2px 8px rgba(10,36,99,0.2);
    }
    @media(max-width:600px){
      .dua-kolom{grid-template-columns:1fr;}
    }
  </style>
</head>
<body>
  <div class="wadah">
    <div id="halaman-utama">
      <h1>🎓 <span>si</span>LATI</h1>
      <p class="sub-judul">Sistem Pelatihan Terintegrasi</p>
      <hr>
      <h3 style="text-align:center">Silakan Pilih Akses Masuk:</h3>
      <div class="grid">
        <button class="tombol tombol-utama" onclick="bukaHalaman('admin')">🔧 Pengelola / Admin</button>
        <button class="tombol tombol-utama" onclick="bukaHalaman('peserta')">👤 Peserta Pelatihan</button>
      </div>
    </div>

    <div id="halaman-admin" class="sembunyi">
      <button class="tombol tombol-biasa" onclick="bukaHalaman('utama')">🔙 Kembali ke Halaman Utama</button>
      <h2>Dashboard Pengelola Pelatihan</h2>
      
      <h3>📝 Buat Pelatihan Baru</h3>
      <div class="grup">
        <label>Nama Pelatihan *</label>
        <input type="text" id="nama-pelatihan" placeholder="Contoh: Pelatihan Ahli Muda Hidrologi 2026">
      </div>

      <h4 style="margin:16px 0 8px; color:var(--biru-tengah); font-weight:600;">📅 Periode Pendaftaran</h4>
      <div class="dua-kolom">
        <div class="grup">
          <label>Tanggal Buka Pendaftaran *</label>
          <input type="date" id="buka-pendaftaran">
        </div>
        <div class="grup">
          <label>Tanggal Tutup Pendaftaran *</label>
          <input type="date" id="tutup-pendaftaran">
        </div>
      </div>

      <h4 style="margin:16px 0 8px; color:var(--biru-tengah); font-weight:600;">📅 Periode Pelaksanaan</h4>
      <div class="dua-kolom">
        <div class="grup">
          <label>Tanggal Mulai Pelaksanaan *</label>
          <input type="date" id="mulai-pelatihan">
        </div>
        <div class="grup">
          <label>Tanggal Selesai Pelaksanaan *</label>
          <input type="date" id="selesai-pelatihan">
        </div>
      </div>

      <div class="grup">
        <label>Lokasi / Tautan *</label>
        <input type="text" id="lokasi" placeholder="Alamat tempat atau tautan Zoom/Google Meet">
      </div>
      <div class="grup">
        <label>Daftar Persyaratan Umum</label>
        <textarea id="syarat-umum" rows="4">1. Fotokopi KTP masih berlaku
2. Fotokopi Ijazah Terakhir dilegalisir
3. Pas foto 4x6 cm sebanyak 2 lembar
4. Surat keterangan sehat dari dokter
5. Surat tugas instansi (jika diperlukan)</textarea>
      </div>

      <h3>📌 Pilih Jabatan & Kualifikasi (Jenjang 1–9 Lengkap Semua Bidang)</h3>
      <div class="grup">
        <label>Klasifikasi Bidang *</label>
        <select id="klasifikasi" onchange="updateSubklasifikasi()"></select>
      </div>
      <div class="grup">
        <label>Subklasifikasi *</label>
        <select id="subklasifikasi" onchange="updateJabatan()"></select>
      </div>
      <div class="grup">
        <label>Nama Jabatan (Tertera Jenjang Lengkap) *</label>
        <select id="jabatan" onchange="tampilkanSyarat()"></select>
      </div>
      <div id="syarat-kualifikasi" class="info"></div>
      <button class="tombol tombol-utama" onclick="simpanPelatihan()">✅ Simpan Pelatihan</button>

      <h2>Daftar Pendaftar</h2>
      <button class="tombol tombol-hijau" onclick="unduhCSV()">📥 Unduh Daftar ke Excel (.CSV)</button>
      <div id="daftar-pendaftar" class="peringatan">Belum ada data pendaftar.</div>
    </div>

    <div id="halaman-peserta" class="sembunyi">
      <button class="tombol tombol-biasa" onclick="bukaHalaman('utama')">🔙 Kembali ke Halaman Utama</button>
      <h2>Pendaftaran Pelatihan</h2>
      
      <div class="grup">
        <label>Pilih Pelatihan yang Tersedia *</label>
        <select id="pilih-pelatihan" onchange="tampilkanDetailPelatihan()"></select>
      </div>
      <div id="detail-pelatihan" class="peringatan">Silakan pilih pelatihan terlebih dahulu.</div>

      <h3>📝 Isi Data Diri</h3>
      <div class="grup">
        <label>Nama Lengkap Sesuai KTP *</label>
        <input type="text" id="nama-peserta" placeholder="Contoh: Andi Pratama">
      </div>
      <div class="grup">
        <label>NIK / Nomor KTP *</label>
        <input type="text" id="nik" placeholder="16 digit angka">
      </div>
      <div class="grup">
        <label>Nomor WhatsApp Aktif *</label>
        <input type="text" id="no-hp" placeholder="0812xxxxxxxxx">
      </div>
      <div class="grup">
        <label>Pendidikan Terakhir *</label>
        <input type="text" id="pendidikan" placeholder="Contoh: S1 Teknik Sipil">
      </div>
      <div class="grup">
        <label>Lama Pengalaman Kerja (Tahun) *</label>
        <input type="number" id="pengalaman" min="0" value="0">
      </div>
      <button class="tombol tombol-utama" onclick="kirimPendaftaran()">✅ Kirim Pendaftaran</button>
      <div id="pesan-konfirmasi" class="sembunyi berhasil"></div>
    </div>
  </div>

  <script>
    // === PERSYARATAN JENJANG 1–9 LENGKAP ===
    const syaratKualifikasi = {
      "9": {nama: "Jenjang 9 - Ahli Utama", aturan: ["Doktor/Doktor Terapan/Spesialis 2: Minimal 0 Tahun", "S2/Spesialis 1: Minimal 4 Tahun", "Pendidikan Profesi: Minimal 7 Tahun", "S1/D4 Terapan: Minimal 8 Tahun"]},
      "8": {nama: "Jenjang 8 - Ahli Madya", aturan: ["S2/Spesialis 1: Minimal 0 Tahun", "Pendidikan Profesi: Minimal 5 Tahun", "S1/D4 Terapan: Minimal 6 Tahun"]},
      "7": {nama: "Jenjang 7 - Ahli Muda", aturan: ["Pendidikan Profesi: Minimal 0 Tahun", "S1/D4 Terapan: Minimal 0–2 Tahun"]},
      "6": {nama: "Jenjang 6 - Teknisi/Analis Tingkat Ahli", aturan: ["S1/D4 Terapan: Minimal 0 Tahun", "D3: Minimal 4 Tahun", "D2: Minimal 8 Tahun", "D1: Minimal 12 Tahun"]},
      "5": {nama: "Jenjang 5 - Teknisi/Analis Tingkat Menengah", aturan: ["D3: Minimal 0 Tahun", "D2: Minimal 4 Tahun", "D1/SMK Plus: Minimal 8 Tahun", "SMK: Minimal 10 Tahun", "SMA: Minimal 12 Tahun"]},
      "4": {nama: "Jenjang 4 - Teknisi/Analis Tingkat Dasar", aturan: ["D2: Minimal 0 Tahun", "D1/SMK Plus: Minimal 2 Tahun", "SMK: Minimal 4 Tahun", "SMA: Minimal 6 Tahun"]},
      "3": {nama: "Jenjang 3 - Operator/Pelaksana Tingkat Ahli", aturan: ["D1/SMK Plus: Minimal 0 Tahun", "SMK: Minimal 3 Tahun", "SMA: Minimal 4 Tahun", "Pendidikan Dasar: Minimal 5 Tahun"]},
      "2": {nama: "Jenjang 2 - Operator/Pelaksana Tingkat Menengah", aturan: ["SMK: Minimal 0 Tahun", "SMA: Minimal 1 Tahun", "Pendidikan Dasar: Minimal 0 Tahun"]},
      "1": {nama: "Jenjang 1 - Operator/Pelaksana Tingkat Dasar", aturan: ["Pendidikan Dasar: Minimal 0 Tahun", "Non Pendidikan (Dengan PBK): Minimal 2 Tahun"]}
    };

    // === DATA JABATAN LENGKAP ===
    const dataJabatan = [
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Hidrologi"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Hidrologi"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Hidrologi"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Pengawas Pengeboran Air Tanah"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Teknisi Pengujian Air Tanah"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Pengawas Pengeboran"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Pelaksana Pengeboran Air Tanah"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Operator Alat Pengeboran"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Air Tanah dan Air Baku","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Operator Pengeboran"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perkerasan Jalan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencanaan Jembatan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pengawasan Jalan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Inspektur Jembatan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Teknisi Pengujian Beton Jalan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Inspeksi Jalan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Pelaksana Pekerjaan Perkerasan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Operator Alat Berat Jalan"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Bangunan Jalan dan Jembatan","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Pekerjaan Jalan"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Alat Berat"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perawatan Mesin"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Inspeksi Alat Berat"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Teknisi Ahli Perbaikan Hidrolik"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Teknisi Perawatan Berkala"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Teknisi Mesin"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Operator Ahli Ekskavator"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Operator Alat Berat Umum"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat Konstruksi","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Perawatan Alat Berat"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Sistem Kelistrikan"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Keamanan Listrik"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencanaan Instalasi"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Pengawas Instalasi Listrik"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Teknisi Pengujian Kelistrikan"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Pengawas Listrik"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Ahli Pemasangan Kabel"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Teknisi Pemasangan Listrik"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Instalasi Listrik Konstruksi","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Pemasangan Listrik"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Arsitek Utama"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Arsitek Madya"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Arsitek Muda"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Penyusun Gambar Teknis Ahli"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Penyusun Gambar Kerja"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Penyusun Gambar"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Pelaksana Tata Letak Bangunan"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Pembuat Model Sederhana"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Perencanaan Arsitektur","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Persiapan Gambar"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Lanskap"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Taman Kota"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Penghijauan"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Pengawas Pembuatan Taman"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Teknisi Pemilihan Tanaman"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Perancangan Taman"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Pelaksana Penanaman Pohon"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Perawat Taman Menengah"},
      {"klasifikasi":"ARSITEKTUR LANSKAP","subklasifikasi":"Perancangan Lanskap","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Penanaman Tanaman"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama AMDAL"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Pengelolaan Lingkungan"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pemantauan Lingkungan"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Pengawas Pemantauan Lingkungan"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Teknisi Pengujian Limbah"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Pengambilan Sampel"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Pelaksana Pengolahan Limbah"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Pemantau Lapangan Lingkungan"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Analisis Dampak Lingkungan","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Lapangan Lingkungan"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Manajer Proyek Utama"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Manajer Proyek Madya"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Manajer Proyek Muda"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Pengawas Lapangan Ahli"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Penyusun Laporan Proyek"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Administrasi Proyek"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Pelaksana Jadwal Proyek"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Petugas Administrasi Lapangan"},
      {"klasifikasi":"MANAJEMEN KONSTRUKSI","subklasifikasi":"Manajemen Proyek Konstruksi","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Dokumen Proyek"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Mutu Konstruksi"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Jaminan Mutu"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pengujian Mutu"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"6","kualifikasi":"Teknisi Ahli","nama_jabatan":"Pengawas Mutu Lapangan"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"5","kualifikasi":"Teknisi Menengah","nama_jabatan":"Teknisi Pengujian Bahan"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"4","kualifikasi":"Teknisi Dasar","nama_jabatan":"Asisten Pengujian Mutu"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"3","kualifikasi":"Pelaksana Ahli","nama_jabatan":"Pelaksana Pemeriksaan Bahan"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"2","kualifikasi":"Pelaksana Menengah","nama_jabatan":"Pemeriksa Bahan Menengah"},
      {"klasifikasi":"TEKNIK INDUSTRI","subklasifikasi":"Pengendalian Mutu Konstruksi","jenjang":"1","kualifikasi":"Pelaksana Dasar","nama_jabatan":"Pembantu Pemeriksaan Mutu"}
    ];

    // === FUNGSI PENYIMPANAN DATA ===
    let daftarPelatihan = JSON.parse(localStorage.getItem("daftarPelatihan") || "[]");
    let daftarPendaftar = JSON.parse(localStorage.getItem("daftarPendaftar") || "[]");

    // === FUNGSI NAVIGASI ===
    function bukaHalaman(namaHalaman) {
      document.querySelectorAll("[id^='halaman-']").forEach(el => el.classList.add("sembunyi"));
      document.getElementById(`halaman-${namaHalaman}`).classList.remove("sembunyi");
      if(namaHalaman === "admin") { inisialisasiPilihan(); tampilkanDaftarPendaftar(); }
      if(namaHalaman === "peserta") muatPilihanPelatihan();
    }

    // === INISIALISASI PILIHAN ===
    function inisialisasiPilihan() {
      const daftarKlasifikasi = [...new Set(dataJabatan.map(item => item.klasifikasi))].sort();
      const elemenKlasifikasi = document.getElementById("klasifikasi");
      elemenKlasifikasi.innerHTML = `<option value="">-- Pilih Klasifikasi --</option>`;
      daftarKlasifikasi.forEach(klas => elemenKlasifikasi.innerHTML += `<option value="${klas}">${klas}</option>`);
    }

    function updateSubklasifikasi() {
      const klas = document.getElementById("klasifikasi").value;
      const subEl = document.getElementById("subklasifikasi");
      const jabEl = document.getElementById("jabatan");
      subEl.innerHTML = `<option value="">-- Pilih Subklasifikasi --</option>`;
      jabEl.innerHTML = `<option value="">-- Pilih Jabatan Dulu --</option>`;
      document.getElementById("syarat-kualifikasi").innerHTML = "";
      if(!klas) return;
      const daftarSub = [...new Set(dataJabatan.filter(i => i.klasifikasi === klas).map(i => i.subklasifikasi))].sort();
      daftarSub.forEach(sub => subEl.innerHTML += `<option value="${sub}">${sub}</option>`);
    }

    function updateJabatan() {
      const klas = document.getElementById("klasifikasi").value;
      const sub = document.getElementById("subklasifikasi").value;
      const jabEl = document.getElementById("jabatan");
      jabEl.innerHTML = `<option value="">-- Pilih Jabatan --</option>`;
      document.getElementById("syarat-kualifikasi").innerHTML = "";
      if(!klas || !sub) return;
      dataJabatan.filter(i => i.klasifikasi === klas && i.subklasifikasi === sub).forEach(jab => {
        jabEl.innerHTML += `<option value="${jab.jenjang}">${jab.nama_jabatan} | ${jab.kualifikasi} (Jenjang ${jab.jenjang})</option>`;
      });
    }

    function tampilkanSyarat() {
      const jenjang = document.getElementById("jabatan").value;
      const el = document.getElementById("syarat-kualifikasi");
      if(!jenjang) { el.innerHTML = ""; return; }
      const data = syaratKualifikasi[jenjang];
      el.innerHTML = `<strong>${data.nama}</strong><br>Persyaratan Pendidikan & Pengalaman:<br>${data.aturan.map(a => `• ${a}`).join("<br>")}`;
    }

    function simpanPelatihan() {
      const nama = document.getElementById("nama-pelatihan").value.trim();
      const buka = document.getElementById("buka-pendaftaran").value;
      const tutup = document.getElementById("tutup-pendaftaran").value;
      const mulai = document.getElementById("mulai-pelatihan").value;
      const selesai = document.getElementById("selesai-pelatihan").value;
      const lokasi = document.getElementById("lokasi").value.trim();
      const syarat = document.getElementById("syarat-umum").value.trim();
      const jenjang = document.getElementById("jabatan").value;
      const jabatan = document.getElementById("jabatan").selectedOptions[0]?.text || "";
      
      if(!nama || !buka || !tutup || !mulai || !selesai || !lokasi || !jenjang) {
        alert("Lengkapi semua data bertanda *!"); return;
      }
      if(new Date(tutup) < new Date(buka)) { alert("Tanggal tutup tidak boleh lebih awal dari buka!"); return; }
      if(new Date(selesai) < new Date(mulai)) { alert("Tanggal selesai tidak boleh lebih awal dari mulai!"); return; }
      
      daftarPelatihan.push({nama, bukaPendaftaran: buka, tutupPendaftaran: tutup, mulaiPelatihan: mulai, selesaiPelatihan: selesai, lokasi, syaratUmum: syarat, jenjang, jabatanTerpilih: jabatan});
      localStorage.setItem("daftarPelatihan", JSON.stringify(daftarPelatihan));
      alert("✅ Pelatihan berhasil disimpan!");
      
      // Reset form
      document.getElementById("nama-pelatihan").value = "";
      document.getElementById("buka-pendaftaran").value = "";
      document.getElementById("tutup-pendaftaran").value = "";
      document.getElementById("mulai-pelatihan").value = "";
      document.getElementById("selesai-pelatihan").value = "";
      document.getElementById("lokasi").value = "";
      document.getElementById("syarat-umum").value = "1. Fotokopi KTP masih berlaku\\n2. Fotokopi Ijazah Terakhir dilegalisir\\n3. Pas foto 4x6 cm sebanyak 2 lembar\\n4. Surat keterangan sehat dari dokter\\n5. Surat tugas instansi (jika diperlukan)";
      document.getElementById("klasifikasi").value = "";
      document.getElementById("subklasifikasi").innerHTML = `<option value="">-- Pilih Subklasifikasi --</option>`;
      document.getElementById("jabatan").innerHTML = `<option value="">-- Pilih Jabatan --</option>`;
      document.getElementById("syarat-kualifikasi").innerHTML = "";
    }

    function tampilkanDaftarPendaftar() {
      const el = document.getElementById("daftar-pendaftar");
      if(daftarPendaftar.length === 0) { el.innerHTML = "Belum ada data pendaftar."; return; }
      el.innerHTML = daftarPendaftar.map((p, i) => `
        <div class="daftar-item">
          <strong>${i+1}. ${p.nama}</strong> (${p.nik})<br>
          Pelatihan: ${p.pelatihan}<br>
          HP: ${p.noHp} | Pendidikan: ${p.pendidikan} | Pengalaman: ${p.pengalaman} tahun
        </div>
      `).join("");
    }

    function unduhCSV() {
      if(daftarPendaftar.length === 0) { alert("Belum ada data untuk diunduh!"); return; }
      const header = "No,Nama Lengkap,NIK,No HP,Pendidikan,Pengalaman (Tahun),Pelatihan Pilihan\\n";
      const isi = daftarPendaftar.map((p,i) => `${i+1},"${p.nama}","${p.nik}","${p.noHp}","${p.pendidikan}",${p.pengalaman},"${p.pelatihan}"`).join("\\n");
      const blob = new Blob([header + isi], {type: "text/csv;charset=utf-8"});
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url; a.download = "daftar_pendaftar_silati.csv"; a.click(); URL.revokeObjectURL(url);
    }

    function muatPilihanPelatihan() {
      const el = document.getElementById("pilih-pelatihan");
      el.innerHTML = `<option value="">-- Pilih Pelatihan --</option>`;
      daftarPelatihan.forEach((p, i) => el.innerHTML += `<option value="${i}">${p.nama}</option>`);
    }

    function tampilkanDetailPelatihan() {
      const idx = document.getElementById("pilih-pelatihan").value;
      const el = document.getElementById("detail-pelatihan");
      if(idx === "") { el.innerHTML = "Silakan pilih pelatihan terlebih dahulu."; return; }
      const p = daftarPelatihan[idx];
      el.className = "info";
      el.innerHTML = `
        <strong>${p.nama}</strong><br>
        📅 Daftar: ${p.bukaPendaftaran} s.d ${p.tutupPendaftaran}<br>
        📅 Pelaksanaan: ${p.mulaiPelatihan} s.d ${p.selesaiPelatihan}<br>
        📍 Lokasi: ${p.lokasi}<br>
        📌 Jabatan: ${p.jabatanTerpilih}<br>

       
