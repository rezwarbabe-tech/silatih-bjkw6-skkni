<!DOCTYPE html>
<html lang="id">
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
      background:rgba(218,165,32,0.05);
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
      gap:24px;
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
    input:read-only{
      background-color:#E2E8F0;
      color:#64748B;
      cursor:not-allowed;
    }
    input[type="file"] {
      padding: 8px 12px;
      background: #FAFBFF;
      cursor: pointer;
    }

    .box-pilihan {
      max-height: 160px;
      overflow-y: auto;
      border: 2px solid var(--abu-batas);
      border-radius: 10px;
      padding: 12px;
      background: var(--putih);
    }
    .item-pilihan {
      display: flex !important;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
      font-size: 0.9rem;
      cursor: pointer;
      color: #334155;
      font-weight: 400;
    }
    .item-pilihan input[type="checkbox"] {
      width: auto;
      margin: 0;
      cursor: pointer;
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
    .gagal{
      padding:16px;
      background:linear-gradient(135deg, rgba(196,58,49,0.05) 0%, rgba(196,58,49,0.08) 100%);
      border-left:5px solid var(--merah-bata);
      border-radius:12px;
      margin:12px 0;
      font-size:0.95rem;
      color:var(--merah-bata);
    }
    
    .sembunyi{display:none !important;}
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
    .box-login {
      padding: 24px;
      border: 2px solid var(--abu-batas);
      border-radius: 16px;
      background: #FAFBFF;
      box-shadow: 0 4px 10px rgba(0,0,0,0.02);
      transition: border-color 0.3s ease;
    }
    .box-login:hover {
      border-color: var(--biru-tengah);
    }
    .box-login.peserta:hover {
      border-color: var(--emas);
    }
    @media(max-width:768px){
      .dua-kolom{grid-template-columns:1fr;}
    }
  </style>
</head>
<body>
  <div class="wadah">
    <!-- HALAMAN UTAMA: DUA LOGIN -->
    <div id="halaman-utama">
      <h1>🎓 <span>si</span>LATI</h1>
      <p class="sub-judul">Sistem Pelatihan Terintegrasi<br>
        <span class="tag-pupr">Kementerian Pekerjaan Umum<br>Direktorat Jenderal Bina Konstruksi<br>Balai Jasa Konstruksi Wilayah VI Makassar</span>
      </p>
      <hr>
      
      <!-- Box Notifikasi Login -->
      <div id="status-login" class="sembunyi"></div>

      <div class="dua-kolom">
        <div class="box-login">
          <h3 style="text-align:center; margin-bottom: 15px; color: var(--biru-tua);">💼 Login Pengelola</h3>
          <p style="font-size:0.85rem; color:#64748B; text-align:center; margin-bottom:15px;">Khusus untuk Admin/Pengelola Balai</p>
          <div class="grup">
            <label>Username Pengelola *</label>
            <input type="text" id="admin-user" placeholder="Masukkan User Pengelola">
          </div>
          <div class="grup">
            <label>Password *</label>
            <input type="password" id="admin-pass" placeholder="Masukkan Password">
          </div>
          <button type="button" class="tombol tombol-utama" onclick="loginPengelola()">Masuk Sebagai Pengelola</button>
        </div>

        <div class="box-login peserta">
          <h3 style="text-align:center; margin-bottom: 15px; color: var(--emas);">👤 Login Peserta</h3>
          <p style="font-size:0.85rem; color:#64748B; text-align:center; margin-bottom:15px;">Gunakan NIK KTP Anda yang terdaftar di Dukcapil</p>
          <div class="grup">
            <label>NIK (16 Digit Angka) *</label>
            <input type="text" id="peserta-user" placeholder="Contoh: 7371xxxxxxxxxxxx" maxlength="16">
          </div>
          <div class="grup">
            <label>Password *</label>
            <input type="password" id="peserta-pass" placeholder="Masukkan Password">
          </div>
          <button type="button" class="tombol tombol-utama" style="background: linear-gradient(135deg, var(--emas) 0%, #B8860B 100%); box-shadow:0 4px 12px rgba(218,165,32,0.3);" onclick="loginPeserta()">Masuk Sebagai Peserta</button>
        </div>
      </div>
    </div>

    <!-- HALAMAN ADMIN -->
    <div id="halaman-admin" class="sembunyi">
      <button type="button" class="tombol tombol-biasa" onclick="logout()" style="width: auto; display: inline-flex;">🚪 Keluar (Logout)</button>
      <h2>Dashboard Pengelola Pelatihan</h2>
      
      <h3>📝 Buat Pelatihan Baru</h3>
      <div class="grup">
        <label>Nama Pelatihan *</label>
        <input type="text" id="nama-pelatihan" placeholder="Contoh: Pelatihan Gabungan Kualifikasi Ahli Wilayah VI">
      </div>

      <h4 style="margin:16px 0 8px; color:var(--biru-tengah); font-weight:600;">📅 Periode Pendaftaran</h4>
      <div class="dua-kolom" style="grid-template-columns: 1fr 1fr;">
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
      <div class="dua-kolom" style="grid-template-columns: 1fr 1fr;">
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

      <h3>📌 Pilih Jabatan & Kualifikasi Berkelompok (Bisa Pilih Banyak)</h3>
      <div class="grup">
        <label>Klasifikasi Bidang * (Centang beberapa)</label>
        <div id="klasifikasi-wadah" class="box-pilihan"></div>
      </div>
      <div class="grup">
        <label>Subklasifikasi * (Centang beberapa)</label>
        <div id="subklasifikasi-wadah" class="box-pilihan"></div>
      </div>
      <div class="grup">
        <label>Nama Jabatan & Jenjang * (Centang beberapa jabatan yang dibuka)</label>
        <div id="jabatan-wadah" class="box-pilihan"></div>
      </div>
      
      <div id="syarat-kualifikasi" class="info sembunyi"></div>
      
      <!-- BOX NOTIFIKASI SIMPAN PELATIHAN (Bypass Iframe Alert Blocking) -->
      <div id="status-admin-box" class="sembunyi"></div>

      <button type="button" class="tombol tombol-utama" onclick="simpanPelatihan()">✅ Simpan Pelatihan</button>

      <hr>
      <!-- DAFTAR PELATIHAN BARU AGAR ADMIN TAHU DATANYA TERSIMPAN -->
      <h3>📚 Daftar Pelatihan yang Telah Dibuat</h3>
      <div id="daftar-pelatihan-admin" class="peringatan">Belum ada pelatihan yang dibuat.</div>
      <hr>

      <h2>👥 Daftar Pendaftar Masuk</h2>
      <button type="button" class="tombol tombol-hijau" onclick="unduhCSV()">📥 Unduh Daftar ke Excel (.CSV)</button>
      <div id="daftar-pendaftar" class="peringatan">Belum ada data pendaftar.</div>
    </div>

    <!-- HALAMAN PESERTA -->
    <div id="halaman-peserta" class="sembunyi">
      <button type="button" class="tombol tombol-biasa" onclick="logout()" style="width: auto; display: inline-flex;">🚪 Keluar (Logout)</button>
      <h2>Pendaftaran Pelatihan</h2>
      
      <div class="grup">
        <label>Pilih Pelatihan yang Tersedia *</label>
        <select id="pilih-pelatihan" onchange="tampilkanDetailPelatihan()"></select>
      </div>
      <div id="detail-pelatihan" class="peringatan">Silakan pilih pelatihan terlebih dahulu.</div>

      <h3>📝 Isi Data Diri & Unggah Berkas</h3>
      <div class="grup">
        <label>Pilih Skema Jabatan & Jenjang yang Ingin Anda Ikuti *</label>
        <select id="pilih-jabatan">
          <option value="">-- Pilih Jabatan Terlebih Dahulu --</option>
        </select>
      </div>
      <div class="grup">
        <label>Nama Lengkap Sesuai KTP *</label>
        <input type="text" id="nama-peserta" placeholder="Contoh: Andi Pratama">
      </div>
      <div class="grup">
        <label>NIK / Nomor KTP *</label>
        <input type="text" id="nik" placeholder="16 digit angka otomatis terkunci dari login">
      </div>
      <div class="grup">
        <label>Nomor WhatsApp Aktif *</label>
        <input type="text" id="no-hp" placeholder="0812xxxxxxxxx">
      </div>
      
      <div class="grup">
        <label>Pendidikan Terakhir Anda *</label>
        <select id="pendidikan">
          <option value="">-- Pilih Pendidikan Terakhir --</option>
          <option value="S3">Doktor (S3) / Doktor Terapan / Spesialis 2</option>
          <option value="S2">Magister (S2) / Spesialis 1</option>
          <option value="Profesi">Pendidikan Profesi</option>
          <option value="S1">Sarjana (S1) / Diploma 4 (D4) Terapan</option>
          <option value="D3">Diploma 3 (D3)</option>
          <option value="D2">Diploma 2 (D2)</option>
          <option value="D1">Diploma 1 (D1) / SMK Plus</option>
          <option value="SMK">SMK (Sekolah Menengah Kejuruan)</option>
          <option value="SMA">SMA (Sekolah Menengah Atas)</option>
          <option value="Dasar">Pendidikan Dasar (SD/SMP)</option>
          <option value="Non-Edu">Non Pendidikan (Dengan Sertifikat PBK)</option>
        </select>
      </div>
      
      <div class="grup">
        <label>Lama Pengalaman Kerja di Bidang Terkait (Tahun) *</label>
        <input type="number" id="pengalaman" min="0" value="0">
      </div>
      
      <div class="dua-kolom">
        <div class="grup">
          <label>Lampirkan Ijazah (Semua Format File) *</label>
          <input type="file" id="berkas-ijazah">
        </div>
        <div class="grup">
          <label>Lampirkan Bukti Kerja (Semua Format File) *</label>
          <input type="file" id="berkas-kerja">
        </div>
      </div>

      <!-- BOX NOTIFIKASI PENDAFTARAN -->
      <div id="status-registrasi-box" class="sembunyi"></div>

      <button type="button" class="tombol tombol-utama" onclick="kirimPendaftaran()">✅ Kirim Pendaftaran</button>
    </div>
  </div>

  <script>
    const syaratKualifikasi = {
      "9": { nama: "Jenjang 9 - Ahli Utama", aturan: ["Doktor/Doktor Terapan/Spesialis 2: Minimal 0 Tahun", "S2/Spesialis 1: Minimal 4 Tahun", "Pendidikan Profesi: Minimal 7 Tahun", "S1/D4 Terapan: Minimal 8 Tahun"] },
      "8": { nama: "Jenjang 8 - Ahli Madya", aturan: ["S2/Spesialis 1: Minimal 0 Tahun", "Pendidikan Profesi: Minimal 5 Tahun", "S1/D4 Terapan: Minimal 6 Tahun"] },
      "7": { nama: "Jenjang 7 - Ahli Muda", aturan: ["Pendidikan Profesi: Minimal 0 Tahun", "S1/D4 Terapan: Minimal 0 Tahun"] },
      "6": { nama: "Jenjang 6 - Teknisi/Analis Tingkat Ahli", aturan: ["S1/D4 Terapan: Minimal 0 Tahun", "D3: Minimal 4 Tahun", "D2: Minimal 8 Tahun", "D1: Minimal 12 Tahun"] },
      "5": { nama: "Jenjang 5 - Teknisi/Analis Tingkat Menengah", aturan: ["D3: Minimal 0 Tahun", "D2: Minimal 4 Tahun", "D1/SMK Plus: Minimal 8 Tahun", "SMK: Minimal 10 Tahun", "SMA: Minimal 12 Tahun"] },
      "4": { nama: "Jenjang 4 - Teknisi/Analis Tingkat Dasar", aturan: ["D2: Minimal 0 Tahun", "D1/SMK Plus: Minimal 2 Tahun", "SMK: Minimal 4 Tahun", "SMA: Minimal 6 Tahun"] },
      "3": { nama: "Jenjang 3 - Operator/Pelaksana Tingkat Ahli", aturan: ["D1/SMK Plus: Minimal 0 Tahun", "SMK: Minimal 3 Tahun", "SMA: Minimal 4 Tahun", "Pendidikan Dasar: Minimal 5 Tahun"] },
      "2": { nama: "Jenjang 2 - Operator/Pelaksana Tingkat Menengah", aturan: ["SMK: Minimal 0 Tahun", "SMA: Minimal 1 Tahun", "Pendidikan Dasar: Minimal 0 Tahun"] },
      "1": { nama: "Jenjang 1 - Operator/Pelaksana Tingkat Dasar", aturan: ["Pendidikan Dasar: Minimal 0 Tahun", "Non Pendidikan (Dengan PBK): Minimal 2 Tahun"] }
    };

    const matriksValidasi = {
      "9": { "S3": 0, "S2": 4, "Profesi": 7, "S1": 8 },
      "8": { "S2": 0, "Profesi": 5, "S1": 6 },
      "7": { "Profesi": 0, "S1": 0 },
      "6": { "S1": 0, "D3": 4, "D2": 8, "D1": 12 },
      "5": { "D3": 0, "D2": 4, "D1": 8, "SMK": 10, "SMA": 12 },
      "4": { "D2": 0, "D1": 2, "SMK": 4, "SMA": 6 },
      "3": { "D1": 0, "SMK": 3, "SMA": 4, "Dasar": 5 },
      "2": { "SMK": 0, "SMA": 1, "Dasar": 0 },
      "1": { "Dasar": 0, "Non-Edu": 2 }
    };

    const teksPendidikan = {
      "S3": "Doktor (S3) / Spesialis 2", "S2": "Magister (S2) / Spesialis 1", "Profesi": "Pendidikan Profesi",
      "S1": "Sarjana (S1) / D4 Terapan", "D3": "Diploma 3 (D3)", "D2": "Diploma 2 (D2)",
      "D1": "Diploma 1 (D1) / SMK Plus", "SMK": "SMK", "SMA": "SMA",
      "Dasar": "Pendidikan Dasar (SD/SMP)", "Non-Edu": "Non Pendidikan (Dengan PBK)"
    };

    // DATABASE JABATAN KERJA LENGKAP SKKNI
    const dataJabatan = [
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Bidang Keahlian Teknik Sumber Daya Air (SI101015)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Bidang Keahlian Teknik Sumber Daya Air (SI101014)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (SI101013)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bidang Keahlian Teknik Sumber Daya Air (Freshgraduate) (SI101019)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Hidrologi (SI101003)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Hidrologi (SI101002)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Hidrologi (SI101001)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Hidrolika (SI101018)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Hidrolika (SI101021)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Hidrolika (SI101020)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pengeboran Air Tanah (Level 6) (SI102005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pengeboran Air Tanah (Level 5) (SI102006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pengeboran Air Tanah (Level 5) (SI102007)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sumber Daya Air","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pengeboran Air Tanah (Level 4) (SI102008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Jalan (SI031022)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Jalan (SI031023)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Jalan (SI031024)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Jalan (Freshgraduate) (SI031029)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Keselamatan Jalan (SI031025)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Keselamatan Jalan (SI031026)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Keselamatan Jalan (SI031027)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Auditor Keselamatan Jalan (SI031031)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Auditor Keselamatan Jalan (SI031030)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"7","kualifikasi":"Pengendali","nama_jabatan":"Pengendali Pelaksanaan Pekerjaan Jalan (SI031028)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Jalan (Level 6) (SI032023)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Jalan (Level 5) (SI032024)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Jalan (Level 4) (SI032025)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Uji Laik Fungsi Jalan (Level 6) (SI032026)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan dan Jembatan","jenjang":"3","kualifikasi":"Mandor","nama_jabatan":"Mandor Pemeliharaan Jalan (SI033016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Jembatan (SI041023)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Jembatan (SI041024)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Jembatan (SI041025)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Jembatan (Freshgraduate) (SI041028)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencanaan Jembatan Rangka Baja (SI041026)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencanaan Jembatan Rangka Baja (SI041030)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencanaan Jembatan Rangka Baja (SI041029)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"7","kualifikasi":"Pengendali","nama_jabatan":"Pengendali Pelaksanaan Pekerjaan Jembatan (SI041013)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pemeriksaan Jembatan (SI041027)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pemeliharaan Jembatan (Level 6) (SI042014)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pemeliharaan Jembatan (Level 5) (SI042015)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pemeliharaan Jembatan (Level 4) (SI042016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lapangan Pekerjaan Jembatan Rangka Baja Panel Darurat (SI042017)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja Panel Darurat (SI042018)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja (Level 6) (SI042019)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Jembatan Rangka Baja (Level 5) (SI042020)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"2","kualifikasi":"Kepala Tukang","nama_jabatan":"Kepala Tukang Pasang/Perakit Jembatan Rangka Baja Panel Darurat (SI043003)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jembatan","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Pasang/Perakit Jembatan Rangka Baja Panel Darurat (SI043004)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Bangunan Gedung (SI011031)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Bangunan Gedung (SI011032)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Bangunan Gedung (SI011033)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Bangunan Gedung (Freshgraduate) (SI011039)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"7","kualifikasi":"Manajer","nama_jabatan":"Manajer Pengelolaan Bangunan Gedung (SI011034)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Penilai Laik Fungsi Bangunan Gedung (SI011035)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencana Beton Pracetak Untuk Struktur Bangunan Gedung (SI011036)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Bangunan Gedung Hijau (SI011042)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Bangunan Gedung Hijau (SI011041)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bangunan Gedung Hijau (SI011040)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"6","kualifikasi":"Analis","nama_jabatan":"Analis Struktur Bangunan RISHA (SI012028)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Bangunan Gedung (Level 6) (SI012029)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Bangunan Gedung (Level 5) (SI012030)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Gedung (Level 6) (SI012031)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Gedung (Level 5) (SI012032)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Gedung (Level 4) (SI012033)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"4","kualifikasi":"Juru Gambar","nama_jabatan":"Juru Gambar Kepala Bidang Konstruksi (SI012034)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"3","kualifikasi":"Juru Gambar","nama_jabatan":"Juru Gambar Konstruksi (SI013060)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"2","kualifikasi":"Juru Gambar","nama_jabatan":"Juru Gambar Pemula Konstruksi (SI013061)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"3","kualifikasi":"Mandor","nama_jabatan":"Mandor Konstruksi Bangunan Gedung (SI013062)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"3","kualifikasi":"Aplikator","nama_jabatan":"Aplikator Bangunan RISHA (Level 3) (SI013063)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"2","kualifikasi":"Aplikator","nama_jabatan":"Aplikator Bangunan RISHA (Level 2) (SI013064)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"2","kualifikasi":"Kepala Tukang","nama_jabatan":"Kepala Tukang Bangunan Gedung (SI013065)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"2","kualifikasi":"Kepala Tukang","nama_jabatan":"Kepala Tukang Pasang Perancah dan Acuan/Cetakan Beton (SI013066)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Pasang Perancah dan Acuan/Cetakan Beton (SI013067)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Pasang Bata dan Plesteran (SI013068)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Pasang Ubin/Keramik (SI013069)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Besi Beton (SI013070)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Kayu Konstruksi (SI013071)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Cat Bangunan Gedung (SI013072)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Pasang Water Proofing (SI013073)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Pasang Rangka Baja Ringan (SI013074)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"1","kualifikasi":"Tukang","nama_jabatan":"Tukang Pasang Penutup Atap (SI013075)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"7","kualifikasi":"Pengelola","nama_jabatan":"Pengelola Teknis Pembangunan Bangunan Gedung Negara (SI011037)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Gedung","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pengelola Rumah Susun (SI011038)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Material Jalan (SI021007)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Material Jalan (SI021008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Material Jalan (SI021009)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Konstruksi, Fabrikasi, Sipil dan Struktur (SI022016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"6","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Beton Aspal (Level 6) (SI022017)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Beton Aspal (Level 5) (SI022018)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Beton Aspal (Level 4) (SI022019)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"6","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Tanah (Level 6) (SI022020)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Tanah (Level 5) (SI022021)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Tanah (Level 4) (SI022022)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"6","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Beton (Level 6) (SI022025)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Beton (Level 5) (SI022026)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Laboratorium Beton (Level 4) (SI022027)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Produksi Campuran Aspal Panas (Level 5) (SI022023)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Material dan Laboratorium","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Produksi Campuran Aspal Panas (Level 4) (SI022024)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Geologi Pekerjaan Konstruksi (SI151012)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Geologi Pekerjaan Konstruksi (SI151017)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Geoteknik (SI151013)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Geoteknik (SI151014)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Geoteknik (SI151015)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Geoteknik (Freshgraduate) (SI151016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"6","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Geoteknik (Level 6) (SI152005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Geoteknik (Level 5) (SI152006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Sondir (Level 5) (SI152007)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Sondir (Level 4) (SI152008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Pengeboran Pengujian Tanah (Level 5) (SI152009)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Pengeboran Pengujian Tanah (Level 4) (SI152010)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Alat Penyelidikan Tanah (SI153003)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Geoteknik dan Geologi","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Alat Penyelidikan Tanah (SI153004)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Survei Terestris (SI161015)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Survei Terestris (SI161016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Survei Terestris (SI161017)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Hidrografi Lepas Pantai (SI161011)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Hidrografi Pesisir (SI161023)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Survei Pemetaan Udara (SI161008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Sistem Informasi Geografis (SI161018)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"7","kualifikasi":"Spesialis","nama_jabatan":"Spesialis SIG (SI161019)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Kewilayahan (SI161020)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Kewilayahan (SI161021)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"7","kualifikasi":"Manager","nama_jabatan":"Manager Proyek Survei dan Pemetaan Wilayah (SI161022)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"6","kualifikasi":"Surveyor","nama_jabatan":"Surveyor Terestris (SI162006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"6","kualifikasi":"Surveyor","nama_jabatan":"Surveyor Rekayasa (SI162005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Survei Terestris (SI162007)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"4","kualifikasi":"Operator Utama","nama_jabatan":"Operator Utama Survei Terestris (SI162003)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"3","kualifikasi":"Operator Madya","nama_jabatan":"Operator Madya Survei Terestris (SI163010)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"2","kualifikasi":"Operator Muda","nama_jabatan":"Operator Muda Survei Terestris (SI163009)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Survei dan Pemetaan","jenjang":"2","kualifikasi":"Juru Ukur","nama_jabatan":"Juru Ukur Konstruksi (SI163008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Irigasi (SI081014)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Irigasi (SI081015)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Irigasi (SI081016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Perencanaan Irigasi Rawa (SI081017)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Perencanaan Irigasi Rawa (SI081019)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Rawa (SI081018)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Rawa (SI081021)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Rawa (SI081020)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Saluran Irigasi (Level 5) (SI082014)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Saluran Irigasi (Level 4) (SI082015)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"6","kualifikasi":"Pengamat","nama_jabatan":"Pengamat Irigasi (SI082013)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pemasangan Pintu Air (Level 6) (SI082016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pemasangan Pintu Air (Level 5) (SI082017)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Irigasi dan Rawa","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Pengairan (SI082018)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Pantai (SI091011)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Pantai (SI091012)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Pantai (SI091013)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencanaan Operasi & Pemeliharaan Prasarana Sungai (SI091014)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencanaan OP Prasarana Sungai (SI091016)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencanaan OP Prasarana Sungai (SI091015)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pekerjaan Pemeliharaan Sungai (Level 5) (SI092006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pekerjaan Pemeliharaan Sungai (Level 4) (SI092007)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai (Level 5) (SI092008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai (Level 4) (SI092009)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Sungai dan Pantai","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Pengerukan (SI092010)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Dermaga dan Pelabuhan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Dermaga (SI191004)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Dermaga dan Pelabuhan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Dermaga (SI191006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Dermaga dan Pelabuhan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Dermaga (SI191005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Dermaga dan Pelabuhan","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Perawatan Fasilitas Pelabuhan (Level 6) (SI192004)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Dermaga dan Pelabuhan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Perawatan Fasilitas Pelabuhan (Level 5) (SI192005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan Rel","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Jalan Rel (SI171008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan Rel","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Jalan Rel (SI171009)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan Rel","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Jalan Rel (SI171010)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan Rel","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Pengelasan Rel Kereta Api (Level 6) (SI172006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan Rel","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Pengelasan Rel Kereta Api (Level 5) (SI172007)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan Rel","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel (Level 5) (SI172008)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Jalan Rel","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel (Level 4) (SI172009)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Terowongan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Terowongan (SI061009)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Terowongan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Terowongan (SI061010)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Terowongan","jenjang":"6","kualifikasi":"Inspektur","nama_jabatan":"Inspektur Terowongan (SI062005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Grouting","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Grouting (SI231003)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Grouting","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Grouting (SI231002)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Grouting","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Grouting (Level 5) (SI232003)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Grouting","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Grouting (SI233003)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Pembongkaran Bangunan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Pelaksanaan Pembongkaran Bangunan (SI221004)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Pembongkaran Bangunan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Pelaksanaan Pembongkaran Bangunan (SI221006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Pembongkaran Bangunan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pelaksanaan Pembongkaran Bangunan (SI221005)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Tata Udara dan Refrigerasi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencanaan Sistem Tata Udara (ME011004)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Tata Udara dan Refrigerasi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencanaan Sistem Tata Udara (ME011005)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Tata Udara dan Refrigerasi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencanaan Sistem Tata Udara (ME011006)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Plambing dan Pompa Mekanik (ME021004)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Plambing dan Pompa Mekanik (ME021005)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Plambing dan Pompa Mekanik (ME021006)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Plambing (Level 6) (ME022006)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Plambing (Level 5) (ME022007)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Teknik Plambing (Level 5) (ME022008)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Teknik Plambing (Level 4) (ME022009)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"3","kualifikasi":"Mandor","nama_jabatan":"Mandor Plambing (ME023006)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"3","kualifikasi":"Asisten Pelaksana","nama_jabatan":"Asisten Pelaksana Plambing dan Pompa Mekanik (ME023007)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Plambing dan Pompa Mekanik","jenjang":"2","kualifikasi":"Asisten Pemula","nama_jabatan":"Asisten Pemula Pelaksana Plambing dan Pompa Mekanik (ME023008)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Proteksi Kebakaran","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Pengkaji Teknis Proteksi Kebakaran (ME031005)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Proteksi Kebakaran","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Pengkaji Teknis Proteksi Kebakaran (ME031006)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Proteksi Kebakaran","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pengkaji Teknis Proteksi Kebakaran (ME031007)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Proteksi Kebakaran","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Fire Alarm (ME032002)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Pesawat Lift dan Eskalator","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Pesawat Lift dan Eskalator (ME041004)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Pesawat Lift dan Eskalator","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Pesawat Lift dan Eskalator (ME041005)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Pesawat Lift dan Eskalator","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pesawat Lift dan Eskalator (ME041006)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Pesawat Lift dan Eskalator","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Pesawat Lift dan Eskalator (Freshgraduate) (ME041007)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Bidang Keahlian Teknik Mekanikal (ME051011)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Bidang Keahlian Teknik Mekanikal (ME051012)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bidang Keahlian Teknik Mekanikal (ME051013)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bidang Keahlian Teknik Mekanikal (Freshgraduate) (ME051017)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Mekanikal Bangunan Gedung (Level 6) (ME052009)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Mekanikal Bangunan Gedung (Level 5) (ME052010)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Mekanikal (Level 6) (ME052011)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Mekanikal (Level 5) (ME052012)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Prestressing Equipment (ME052014)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Penyambung Pipa Polietilena Dengan Fusi Panas (ME052013)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"3","kualifikasi":"Juru Las","nama_jabatan":"Juru Las (ME053018)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"2","kualifikasi":"Juru Las Pemula","nama_jabatan":"Juru Las Pemula (ME053019)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Teknik Mekanikal Umum","jenjang":"3","kualifikasi":"Asisten Mekanik","nama_jabatan":"Asisten Mekanik HVAC (ME053020)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Manajer Alat Berat (ME061001)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Scaffolding (ME062011)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi Scaffolding (ME062009)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Scaffolding (ME063094)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Scaffolding (ME063095)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Bulldozer (ME063096)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Bulldozer (ME063097)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Motor Grader (ME063098)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Motor Grader (ME063099)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Wheel Excavator (ME063100)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Wheel Excavator (ME063101)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Tandem Roller (ME063102)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Tandem Roller (ME063103)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Vibrator Roller (ME063104)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Vibrator Roller (ME063105)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Pneumatic Tire Roller (ME063106)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Pneumatic Tire Roller (ME063107)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Wheel Loader (ME063014)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Wheel Loader (ME063108)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Mobile Crane (ME063109)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Mobile Crane (ME063110)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Tower Crane (ME063028)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Tower Crane (ME063111)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Truck Mounted Crane (ME063112)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Truck Mounted Crane (ME063113)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Backhoe Loader (ME063114)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Backhoe Loader (ME063115)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Pile Drive Hammer (ME063116)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Pile Drive Hammer (ME063117)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Pompa Beton (ME063142)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Pompa Beton (ME063118)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Bore Pile (ME063119)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Bore Pile (ME063120)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Mesin Pencampur Aspal (ME063121)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Mesin Pencampur Aspal (ME063122)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Mesin Penggelar Aspal (ME063123)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Mesin Penggelar Aspal (ME063124)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Mesin Pemecah Batu (ME063125)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Mesin Pemecah Batu (ME063126)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Mesin Penghampar Beton Semen (ME063127)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Mesin Penghampar Beton Semen (ME063128)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Cold Milling Machine (ME063012)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Cold Milling Machine (ME063129)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Batching Plant (ME063029)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Batching Plant (ME063130)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Hydraulic Hammer Breaker (ME063131)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Hydraulic Hammer Breaker (ME063132)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Ripper Tractor (ME063133)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Ripper Tractor (ME063134)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Mekanik","nama_jabatan":"Mekanik Tower Crane (ME063135)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Mekanik","nama_jabatan":"Mekanik Asphalt Mixing Plant (ME063005)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Mekanik","nama_jabatan":"Mekanik Kapal Keruk (ME063002)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Mekanik","nama_jabatan":"Mekanik Engine Tingkat Dasar (ME063141)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Mekanik Pemula","nama_jabatan":"Mekanik Engine Pemula Tingkat Dasar (ME063136)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Mekanik","nama_jabatan":"Mekanik Hidrolik Alat Berat (ME063137)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Mekanik Pemula","nama_jabatan":"Mekanik Hidrolik Alat Berat Pemula (ME063138)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Mekanik","nama_jabatan":"Mekanik Engine Alat Berat (ME063140)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Mekanik Pemula","nama_jabatan":"Mekanik Engine Alat Berat Pemula (ME063139)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator","nama_jabatan":"Operator Dump Truck (ME063027)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Launching Girder (ME071004)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Launching Girder (ME071003)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"7","kualifikasi":"Lifting Engineer","nama_jabatan":"Lifting Engineer (ME071002)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"6","kualifikasi":"Supervisor","nama_jabatan":"Lifting Supervisor (ME072006)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Launching Gantry (ME072003)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Launching Gantry (ME072002)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"6","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Erection Girder (ME072005)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Erection Girder (ME072004)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Gondola pada Bangunan Gedung (ME073007)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Gondola pada Bangunan Gedung (ME073008)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"3","kualifikasi":"Operator","nama_jabatan":"Operator Launching Gantry (ME073003)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Slinging and Rigging (ME073009)"},
      {"klasifikasi":"TEKNIK MEKANIKAL","subklasifikasi":"Alat Berat dan Erection","jenjang":"2","kualifikasi":"Operator Pemula","nama_jabatan":"Operator Pemula Forklift (ME073010)"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Elektrikal Bangunan Gedung","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Elektrikal Konstruksi Bangunan Gedung (ME051014)"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Elektrikal Bangunan Gedung","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Elektrikal Konstruksi Bangunan Gedung (ME051015)"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Elektrikal Bangunan Gedung","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Elektrikal Konstruksi Bangunan Gedung (ME051016)"},
      {"klasifikasi":"TEKNIK ELEKTRIKAL","subklasifikasi":"Elektrikal Bangunan Gedung","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Elektrikal Konstruksi Bangunan Gedung (Freshgraduate) (ME051018)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Arsitek Utama (AR011001)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Arsitek Madya (AR011002)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Asisten Arsitek (AR011004)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Asisten Arsitek (Freshgraduate) (AR011005)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"6","kualifikasi":"Asisten Pemula","nama_jabatan":"Asisten Pemula Arsitek (AR012001)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lapangan Bidang Arsitektur (Level 6) (AR012003)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lapangan Bidang Arsitektur (Level 5) (AR012004)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"4","kualifikasi":"Juru Gambar","nama_jabatan":"Juru Gambar Kepala Bidang Arsitektur (AR012005)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"3","kualifikasi":"Juru Gambar","nama_jabatan":"Juru Gambar Arsitektur (AR013003)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur","jenjang":"2","kualifikasi":"Juru Gambar Pemula","nama_jabatan":"Juru Gambar Pemula Arsitektur (AR013004)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Arsitek Lanskap Utama (AL011009)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Arsitek Lanskap Madya (AL011010)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Arsitek Lanskap Muda (AL011011)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Arsitek Lanskap Muda (Freshgraduate) (AL011008)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"8","kualifikasi":"Manajer Madya","nama_jabatan":"Manajer Lanskap Madya (AL011012)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"7","kualifikasi":"Manajer Muda","nama_jabatan":"Manajer Lanskap Muda (AL011013)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lanskap (Level 6) (AL012006)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lanskap (Level 5) (AL012007)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lanskap (Level 5) (AL012008)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lanskap (Level 4) (AL012009)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"3","kualifikasi":"Juru Tanam","nama_jabatan":"Juru Tanam (AL013004)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"2","kualifikasi":"Juru Tanam Pemula","nama_jabatan":"Juru Tanam Pemula (AL013005)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Arsitektur Lanskap","jenjang":"1","kualifikasi":"Tukang Taman","nama_jabatan":"Tukang Taman (AL013006)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencanaan Iluminasi (AL021005)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencanaan Iluminasi (AL021004)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencanaan Iluminasi (AL021007)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencanaan Iluminasi (Freshgraduate) (AL021006)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Iluminasi (Level 6) (AL022003)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Iluminasi (Level 5) (AL022004)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pekerjaan Iluminasi (Level 4) (AL022005)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Iluminasi dan Pencahayaan","jenjang":"3","kualifikasi":"Asisten Pelaksana","nama_jabatan":"Asisten Pelaksana Iluminasi (AL023004)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Desainer Interior Utama (AL031005)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Desainer Interior Madya (AL031006)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Desainer Interior Muda (AL031007)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Desainer Interior Muda (Freshgraduate) (AL031010)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Manajemen Interior (AL031008)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Manajemen Interior (AL031009)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Manajemen Interior (Freshgraduate) (AL031011)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Interior (Level 6) (AL032005)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Interior (Level 5) (AL032006)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pekerjaan Interior (Level 5) (AL032007)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pekerjaan Interior (Level 4) (AL032008)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"4","kualifikasi":"Ilustrator","nama_jabatan":"Ilustrator Desain Interior (AL032009)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"4","kualifikasi":"Spesifikator","nama_jabatan":"Spesifikator Desain Interior (AL032010)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"3","kualifikasi":"Juru Gambar","nama_jabatan":"Juru Gambar Desain Interior (AL033001)"},
      {"klasifikasi":"ARSITEKTUR","subklasifikasi":"Desain Interior","jenjang":"2","kualifikasi":"Juru Gambar Pemula","nama_jabatan":"Juru Gambar Pemula Desain Interior (AL033002)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Bidang Keahlian Manajemen Konstruksi (MP021008)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Bidang Keahlian Manajemen Konstruksi (MP021007)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bidang Keahlian Manajemen Konstruksi (MP021006)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bidang Manajemen Konstruksi (Freshgraduate) (MP021013)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Manajemen Proyek (MP021012)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Manajemen Proyek (MP021011)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Manajemen Proyek (MP021010)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"7","kualifikasi":"Manajer Logistik","nama_jabatan":"Manajer Logistik Proyek (MP021002)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"6","kualifikasi":"Fasilitator","nama_jabatan":"Fasilitator Teknis Pembangunan Infrastruktur Berbasis Masyarakat (Level 6) (MP022007)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Konstruksi","jenjang":"5","kualifikasi":"Fasilitator","nama_jabatan":"Fasilitator Teknis Pembangunan Infrastruktur Berbasis Masyarakat (Level 5) (MP022008)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Kontrak dan Hukum Konstruksi","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Kontrak Kerja Konstruksi (MP031003)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Kontrak dan Hukum Konstruksi","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Kontrak Kerja Konstruksi (MP031002)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Sistem Manajemen Mutu Konstruksi (MP041014)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Sistem Manajemen Mutu Konstruksi (MP041016)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Sistem Manajemen Mutu Konstruksi (MP041015)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"6","kualifikasi":"Quality Engineer","nama_jabatan":"Quality Engineer (Level 6) (MP042007)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"5","kualifikasi":"Quality Engineer","nama_jabatan":"Quality Engineer (Level 5) (MP042008)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pengendali Mutu Jalan dan Jembatan (MP042009)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"6","kualifikasi":"QA Engineer","nama_jabatan":"Quality Assurance Engineer (Level 6) (MP042010)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"5","kualifikasi":"QA Engineer","nama_jabatan":"Quality Assurance Engineer (Level 5) (MP042011)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Manajemen Mutu","jenjang":"6","kualifikasi":"Asesor","nama_jabatan":"Asesor Badan Usaha Jasa Konstruksi (MP042004)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Estimasi Biaya & Quantity Surveyor","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Quantity Surveyor (MP051005)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Estimasi Biaya & Quantity Surveyor","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Quantity Surveyor (MP051004)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Estimasi Biaya & Quantity Surveyor","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Quantity Surveyor (MP051003)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Estimasi Biaya & Quantity Surveyor","jenjang":"6","kualifikasi":"Estimator","nama_jabatan":"Estimator Biaya Bidang Konstruksi (Level 6) (MP052010)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Estimasi Biaya & Quantity Surveyor","jenjang":"5","kualifikasi":"Estimator","nama_jabatan":"Estimator Biaya Bidang Konstruksi (Level 5) (MP052011)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Estimasi Biaya & Quantity Surveyor","jenjang":"6","kualifikasi":"Quantity Surveyor","nama_jabatan":"Quantity Surveyor (Level 6) (MP052012)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Estimasi Biaya & Quantity Surveyor","jenjang":"5","kualifikasi":"Quantity Surveyor","nama_jabatan":"Quantity Surveyor (Level 5) (MP052013)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Keselamatan Konstruksi (MP011006)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Keselamatan Konstruksi (MP011005)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Keselamatan Konstruksi (MP011004)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Keselamatan Konstruksi (Freshgraduate) (MP011008)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama K3 Konstruksi (MP011003)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya K3 Konstruksi (MP011002)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda K3 Konstruksi (MP011001)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda K3 Konstruksi (Freshgraduate) (MP011007)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"7","kualifikasi":"Manajer","nama_jabatan":"Manajer Keselamatan Kebakaran Bangunan Gedung (MP011009)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"6","kualifikasi":"Supervisor","nama_jabatan":"Supervisor K3 Konstruksi (Level 6) (MP012004)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"5","kualifikasi":"Supervisor","nama_jabatan":"Supervisor K3 Konstruksi (Level 5) (MP012005)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"4","kualifikasi":"Personil K3","nama_jabatan":"Personil Keselamatan dan Kesehatan Kerja (MP012001)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"3","kualifikasi":"Petugas","nama_jabatan":"Petugas Keselamatan Konstruksi (MP013002)"},
      {"klasifikasi":"MANAJEMEN PELAKSANAAN","subklasifikasi":"Keselamatan dan Kesehatan Kerja","jenjang":"3","kualifikasi":"Petugas K3","nama_jabatan":"Petugas K3 Konstruksi (MP013003)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Lingkungan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Lingkungan (TL01)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Lingkungan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Lingkungan (TL01)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Lingkungan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Lingkungan (TL01)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Lingkungan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Lingkungan Bidang Jasa Konstruksi (TL021004)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Lingkungan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Lingkungan Bidang Jasa Konstruksi (TL021005)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Lingkungan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Lingkungan Bidang Jasa Konstruksi (TL021006)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Lingkungan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Lingkungan Bidang Jasa Konstruksi (Freshgraduate) (TL021007)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Teknik Air Minum (TL011011)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Air Minum (TL011012)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Air Minum (TL011013)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Air Minum (Freshgraduate) (TL011014)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Penanggulangan Kehilangan Air (TL011008)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Penanggulangan Kehilangan Air (TL011009)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Deteksi Kebocoran Jaringan Perpipaan SPAM (TL011010)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"6","kualifikasi":"Analis","nama_jabatan":"Analis Commissioning IPA (Level 6) (TL012014)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"5","kualifikasi":"Analis","nama_jabatan":"Analis Commissioning IPA (Level 5) (TL012015)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"5","kualifikasi":"Teknisi","nama_jabatan":"Teknisi OP Unit Pelayanan Air Minum (Level 5) (TL012016)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"4","kualifikasi":"Teknisi","nama_jabatan":"Teknisi OP Unit Pelayanan Air Minum (Level 4) (TL012017)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"5","kualifikasi":"Kepala Lab","nama_jabatan":"Kepala Laboratorium Air Minum (TL012018)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"5","kualifikasi":"Analis Lab","nama_jabatan":"Analis Laboratorium Air Minum (Level 5) (TL012019)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"4","kualifikasi":"Analis Lab","nama_jabatan":"Analis Laboratorium Air Minum (Level 4) (TL012020)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"4","kualifikasi":"Supervisor","nama_jabatan":"Supervisor Mekanikal Elektrikal Air Minum (TL012021)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lapangan Konstruksi SPAM (TL012022)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Konstruksi SPAM (TL012023)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"3","kualifikasi":"Asisten Pelaksana","nama_jabatan":"Asisten Pelaksana Instalatur Unit Pelayanan Air Minum (TL013005)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"2","kualifikasi":"Asisten Pemula","nama_jabatan":"Asisten Pemula Pelaksana Instalatur Air Minum (TL013006)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sistem Penyediaan Air Minum","jenjang":"2","kualifikasi":"Operator","nama_jabatan":"Operator Instalasi Pengolahan Air Minum (TL013007)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Bangunan Air Limbah / SPALD (SI121102)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Bangunan Air Limbah / SPALD (SI121001)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Bangunan Air Limbah Permukiman (Level 5) (SI122003)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Bangunan Air Limbah Permukiman (Level 4) (SI122004)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencana Sistem Sanitasi Lingkungan (TL031006)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencana Sistem Sanitasi Lingkungan (TL031007)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencana Sistem Sanitasi Lingkungan (TL031008)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"6","kualifikasi":"Fasilitator","nama_jabatan":"Fasilitator Teknis Pembangunan Sarana Sanitasi Berbasis Masyarakat (Level 6) (TL032004)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"5","kualifikasi":"Fasilitator","nama_jabatan":"Fasilitator Teknis Pembangunan Sarana Sanitasi Berbasis Masyarakat (Level 5) (TL032005)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas OP Instalasi Pengolahan Lumpur Tinja (Level 5) (TL032006)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas OP Perpipaan Air Limbah Domestik (Level 5) (TL032007)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas OP IPAL Domestik (Level 5) (TL032008)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana OP Instalasi Pengolahan Lumpur Tinja (Level 4) (TL032009)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana OP Perpipaan Air Limbah Domestik (Level 4) (TL032010)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana OP IPAL Domestik (Level 4) (TL032011)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"3","kualifikasi":"Asisten Pelaksana","nama_jabatan":"Asisten Pelaksana IPLT (TL033003)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"3","kualifikasi":"Asisten Pelaksana","nama_jabatan":"Asisten Pelaksana Perpipaan Air Limbah Domestik (TL033004)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Sanitasi dan Air Limbah","jenjang":"3","kualifikasi":"Asisten Pelaksana","nama_jabatan":"Asisten Pelaksana IPAL Domestik (TL033005)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Teknik Bangunan Persampahan / TPA (SI131004)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Teknik Bangunan Persampahan / TPA (SI131003)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 5) (SI132008)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pembuatan Fasilitas Sampah dan Limbah (Level 4) (SI132009)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencana Pengelolaan Sampah (TL051005)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencana Pengelolaan Sampah (TL051006)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencana Pengelolaan Sampah (TL051007)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pengelolaan TPA Sampah (Level 6) (TL052009)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pengelolaan TPA Sampah (Level 5) (TL052010)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Persampahan","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Pengelolaan TPA Sampah (TL052011)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Perpipaan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Bidang Teknik Perpipaan (TL041003)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Perpipaan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Bidang Teknik Perpipaan (TL041002)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Perpipaan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Bidang Teknik Perpipaan (TL041001)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Perpipaan","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Teknik Perpipaan (Level 6) (TL042014)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Perpipaan","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Pekerjaan Teknik Perpipaan (Level 5) (TL042015)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Perpipaan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Perpipaan (Level 5) (TL042016)"},
      {"klasifikasi":"TATA LINGKUNGAN","subklasifikasi":"Teknik Perpipaan","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Perpipaan (Level 4) (TL042017)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencana Wilayah Pesisir dan Pulau Kecil (PW011004)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Penyusunan Peraturan Zonasi (PW011010)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Penyusunan Peraturan Zonasi (PW011015)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencana Tata Bangunan dan Lingkungan (PW011011)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencana Tata Bangunan dan Lingkungan (PW011012)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencana Tata Ruang Wilayah dan Kota (PW011003)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencana Tata Ruang Wilayah dan Kota (PW011002)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencana Tata Ruang Wilayah dan Kota (PW011001)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"7","kualifikasi":"Penyusun Rencana","nama_jabatan":"Penyusun Rencana Pengembangan Infrastruktur Wilayah (PW011013)"},
      {"klasifikasi":"PERENCANAAN WILAYAH","subklasifikasi":"Perencanaan Wilayah dan Kota","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencana Tata Ruang Wilayah dan Kota (Freshgraduate) (PW011014)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Building Information Modeling (BIM)","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Manager BIM Madya (SR021005)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Building Information Modeling (BIM)","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Manager BIM Muda (SR021004)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Building Information Modeling (BIM)","jenjang":"6","kualifikasi":"Koordinator","nama_jabatan":"Koordinator BIM (SR022004)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Building Information Modeling (BIM)","jenjang":"5","kualifikasi":"Modeler","nama_jabatan":"Modeler BIM (Level 5) (SR022005)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Building Information Modeling (BIM)","jenjang":"4","kualifikasi":"Modeler","nama_jabatan":"Modeler BIM (Level 4) (SR022006)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Building Information Modeling (BIM)","jenjang":"3","kualifikasi":"Juru Gambar","nama_jabatan":"Juru Gambar BIM (SR023002)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Building Information Modeling (BIM)","jenjang":"2","kualifikasi":"Juru Gambar Pemula","nama_jabatan":"Juru Gambar Pemula BIM (SR023003)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Perencanaan Proyek","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencanaan Proyek Infrastruktur (SR011006)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Perencanaan Proyek","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencanaan Proyek Infrastruktur (SR011007)"},
      {"klasifikasi":"SIPIL REKAYASA","subklasifikasi":"Perencanaan Proyek","jenjang":"9","kualifikasi":"Ahli Rekayasa Nilai","nama_jabatan":"Ahli Rekayasa Nilai / Value Engineering (SR011002)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Drainase Perkotaan","jenjang":"9","kualifikasi":"Ahli Utama","nama_jabatan":"Ahli Utama Perencanaan Jaringan Drainase (SI141004)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Drainase Perkotaan","jenjang":"8","kualifikasi":"Ahli Madya","nama_jabatan":"Ahli Madya Perencanaan Jaringan Drainase (SI141006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Drainase Perkotaan","jenjang":"7","kualifikasi":"Ahli Muda","nama_jabatan":"Ahli Muda Perencanaan Jaringan Drainase (SI141005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Drainase Perkotaan","jenjang":"6","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lapangan Pekerjaan Drainase Perkotaan (Level 6) (SI142004)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Drainase Perkotaan","jenjang":"5","kualifikasi":"Pengawas","nama_jabatan":"Pengawas Lapangan Pekerjaan Drainase Perkotaan (Level 5) (SI142005)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Drainase Perkotaan","jenjang":"5","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Drainase Perkotaan (Level 5) (SI142006)"},
      {"klasifikasi":"TEKNIK SIPIL","subklasifikasi":"Drainase Perkotaan","jenjang":"4","kualifikasi":"Pelaksana","nama_jabatan":"Pelaksana Lapangan Pekerjaan Drainase Perkotaan (Level 4) (SI142007)"}
    ];

    let daftarPelatihan = [];
    let daftarPendaftar = [];
    let sesiNikPeserta = "";

    try {
      daftarPelatihan = JSON.parse(localStorage.getItem("daftarPelatihan") || "[]");
      daftarPendaftar = JSON.parse(localStorage.getItem("daftarPendaftar") || "[]");
    } catch (e) {
      console.warn("Storage diblokir, menggunakan memori sementara.");
    }

    function simpanKeStorage(kunci, data) {
      try { localStorage.setItem(kunci, JSON.stringify(data)); } catch (e) {}
    }

    function loginPengelola() {
      const user = document.getElementById("admin-user").value.trim();
      const pass = document.getElementById("admin-pass").value.trim();
      const statusBox = document.getElementById("status-login");
      
      if(user === "bjkw2026" && pass === "pelatihan2026") {
        statusBox.classList.add("sembunyi");
        bukaHalaman("admin");
      } else {
        statusBox.className = "gagal";
        statusBox.innerHTML = "❌ <strong>Login Pengelola Gagal!</strong> Username atau Password salah.";
        statusBox.classList.remove("sembunyi");
      }
    }

    function loginPeserta() {
      const nik = document.getElementById("peserta-user").value.trim();
      const pass = document.getElementById("peserta-pass").value.trim();
      const statusBox = document.getElementById("status-login");

      if(!/^\d{16}$/.test(nik)) {
        statusBox.className = "gagal";
        statusBox.innerHTML = "❌ <strong>Validasi Dukcapil Gagal!</strong> NIK harus terdiri dari 16 digit angka.";
        statusBox.classList.remove("sembunyi");
        return;
      }
      
      if(pass === "pelatihan2026") {
        statusBox.classList.add("sembunyi");
        sesiNikPeserta = nik;
        bukaHalaman("peserta");
        document.getElementById("nik").value = sesiNikPeserta;
        document.getElementById("nik").readOnly = true;
      } else {
        statusBox.className = "gagal";
        statusBox.innerHTML = "❌ <strong>Login Peserta Gagal!</strong> Password salah.";
        statusBox.classList.remove("sembunyi");
      }
    }

    function logout() {
      sesiNikPeserta = "";
      document.getElementById("status-login").classList.add("sembunyi");
      bukaHalaman("utama");
    }

    function bukaHalaman(namaHalaman) {
      document.querySelectorAll("[id^='halaman-']").forEach(el => el.classList.add("sembunyi"));
      document.getElementById(`halaman-${namaHalaman}`).classList.remove("sembunyi");
      
      if(namaHalaman === "admin") { 
        inisialisasiPilihan(); 
        tampilkanDaftarPelatihanAdmin();
        tampilkanPendaftar(); 
      }
      if(namaHalaman === "peserta") { 
        muatPilihanPelatihan(); 
      }
    }

    function inisialisasiPilihan() {
      const daftarKlasifikasi = [...new Set(dataJabatan.map(item => item.klasifikasi))].sort();
      const wadah = document.getElementById("klasifikasi-wadah");
      wadah.innerHTML = "";
      daftarKlasifikasi.forEach(klas => {
        wadah.innerHTML += `<label class="item-pilihan"><input type="checkbox" value="${klas}" onchange="updateSubklasifikasi()"> ${klas}</label>`;
      });
      document.getElementById("subklasifikasi-wadah").innerHTML = "<span>Pilih klasifikasi dahulu</span>";
      document.getElementById("jabatan-wadah").innerHTML = "<span>Pilih subklasifikasi dahulu</span>";
      
      const boxSyarat = document.getElementById("syarat-kualifikasi");
      if(boxSyarat) { boxSyarat.innerHTML = ""; boxSyarat.classList.add("sembunyi"); }
    }

    function updateSubklasifikasi() {
      const klasTerpilih = Array.from(document.querySelectorAll('#klasifikasi-wadah input:checked')).map(cb => cb.value);
      const wadahSub = document.getElementById("subklasifikasi-wadah");
      const subTerpilihSebelumnya = Array.from(wadahSub.querySelectorAll('input:checked')).map(cb => cb.value);

      wadahSub.innerHTML = "";
      if(klasTerpilih.length === 0) { 
        wadahSub.innerHTML = "<span>Pilih klasifikasi dahulu</span>"; 
        updateJabatan();
        return; 
      }
      
      const daftarSub = [...new Set(dataJabatan.filter(item => klasTerpilih.includes(item.klasifikasi)).map(item => item.subklasifikasi))].sort();
      daftarSub.forEach(sub => {
        const isChecked = subTerpilihSebelumnya.includes(sub) ? "checked" : "";
        wadahSub.innerHTML += `<label class="item-pilihan"><input type="checkbox" value="${sub}" ${isChecked} onchange="updateJabatan()"> ${sub}</label>`;
      });
      updateJabatan();
    }

    function updateJabatan() {
      const klasTerpilih = Array.from(document.querySelectorAll('#klasifikasi-wadah input:checked')).map(cb => cb.value);
      const subTerpilih = Array.from(document.querySelectorAll('#subklasifikasi-wadah input:checked')).map(cb => cb.value);
      const wadahJab = document.getElementById("jabatan-wadah");
      const jabTerpilihSebelumnya = Array.from(wadahJab.querySelectorAll('input:checked')).map(cb => cb.getAttribute('data-full'));

      wadahJab.innerHTML = "";
      if(subTerpilih.length === 0) { 
        wadahJab.innerHTML = "<span>Pilih subklasifikasi dahulu</span>"; 
        tampilkanSyarat();
        return; 
      }

      const filterJab = dataJabatan.filter(item => klasTerpilih.includes(item.klasifikasi) && subTerpilih.includes(item.subklasifikasi));
      filterJab.forEach((jab, i) => {
        const labelFull = `${jab.nama_jabatan} (Jenjang ${jab.jenjang})`;
        const isChecked = jabTerpilihSebelumnya.includes(labelFull) ? "checked" : "";
        wadahJab.innerHTML += `
          <label class="item-pilihan">
            <input type="checkbox" value="${jab.jenjang}" data-nama="${jab.nama_jabatan}" data-full="${labelFull}" ${isChecked} onchange="tampilkanSyarat()"> 
            ${jab.nama_jabatan} | Jenjang ${jab.jenjang}
          </label>`;
      });
      tampilkanSyarat();
    }

    function tampilkanSyarat() {
      const jenjangTerpilih = [...new Set(Array.from(document.querySelectorAll('#jabatan-wadah input:checked')).map(cb => cb.value))];
      const elemenSyarat = document.getElementById("syarat-kualifikasi");
      
      if(jenjangTerpilih.length === 0) { 
        elemenSyarat.innerHTML = ""; 
        elemenSyarat.classList.add("sembunyi"); 
        return; 
      }
      
      elemenSyarat.classList.remove("sembunyi");
      let html = "<strong>📋 Aturan Pengalaman Kerja (Sesuai Jenjang Terpilih):</strong><br>";
      jenjangTerpilih.sort((a,b) => b - a).forEach(j => {
        if(syaratKualifikasi[j]) html += `<div style="margin-top:8px;"><strong>${syaratKualifikasi[j].nama}:</strong><br>- ${syaratKualifikasi[j].aturan.join("<br>- ")}</div>`;
      });
      elemenSyarat.innerHTML = html;
    }

    function simpanPelatihan() {
      const elNama = document.getElementById("nama-pelatihan");
      const elBuka = document.getElementById("buka-pendaftaran");
      const elTutup = document.getElementById("tutup-pendaftaran");
      const elMulai = document.getElementById("mulai-pelatihan");
      const elSelesai = document.getElementById("selesai-pelatihan");
      const elLokasi = document.getElementById("lokasi");
      const elSyarat = document.getElementById("syarat-umum");
      
      const boxStatus = document.getElementById("status-admin-box");

      const nama = elNama.value.trim();
      const buka = elBuka.value;
      const tutup = elTutup.value;
      const mulai = elMulai.value;
      const selesai = elSelesai.value;
      const lokasi = elLokasi.value.trim();
      const syaratUmum = elSyarat.value.trim();
      
      const jabCheckboxes = document.querySelectorAll('#jabatan-wadah input:checked');
      
      // SISTEM VALIDASI BARU DENGAN IDENTIFIKASI KOLOM YANG KURANG
      let pesanError = [];
      if(!nama) pesanError.push("Nama Pelatihan");
      if(!buka || !tutup) pesanError.push("Tanggal Buka & Tutup Pendaftaran");
      if(!mulai || !selesai) pesanError.push("Tanggal Mulai & Selesai Pelaksanaan");
      if(!lokasi) pesanError.push("Lokasi / Tautan");
      if(jabCheckboxes.length === 0) pesanError.push("Minimal centang satu Skema Jabatan");

      if(pesanError.length > 0) {
        boxStatus.className = "gagal";
        boxStatus.innerHTML = `<strong>⚠️ Gagal Menyimpan!</strong><br>Data belum lengkap, mohon isi bagian berikut:<br><ul style="margin-left: 20px; margin-top:5px;"><li>${pesanError.join("</li><li>")}</li></ul>`;
        boxStatus.classList.remove("sembunyi");
        window.scrollTo({ top: boxStatus.offsetTop - 50, behavior: 'smooth' });
        return;
      }

      let skemaList = [];
      jabCheckboxes.forEach(cb => {
        skemaList.push({
          jenjang: cb.value,
          namaJabatan: cb.getAttribute('data-nama'),
          labelLengkap: cb.getAttribute('data-full')
        });
      });

      const klasifikasi = Array.from(document.querySelectorAll('#klasifikasi-wadah input:checked')).map(cb => cb.value).join(", ");
      const subklasifikasi = Array.from(document.querySelectorAll('#subklasifikasi-wadah input:checked')).map(cb => cb.value).join(", ");
      const labelJabatan = skemaList.map(s => s.labelLengkap).join(" | ");

      daftarPelatihan.push({ nama, bukaPendaftaran: buka, tutupPendaftaran: tutup, mulaiPelatihan: mulai, selesaiPelatihan: selesai, lokasi, syaratUmum, klasifikasi, subklasifikasi, jabatanTerpilih: labelJabatan, skemaList });
      simpanKeStorage("daftarPelatihan", daftarPelatihan);
      
      // Mengosongkan form sebagai respons visual untuk user
      elNama.value = "";
      elBuka.value = "";
      elTutup.value = "";
      elMulai.value = "";
      elSelesai.value = "";
      elLokasi.value = "";
      elSyarat.value = "1. Fotokopi KTP masih berlaku\n2. Fotokopi Ijazah Terakhir dilegalisir\n3. Pas foto 4x6 cm sebanyak 2 lembar\n4. Surat keterangan sehat dari dokter\n5. Surat tugas instansi (jika diperlukan)";
      
      // Reset pilihan checkbox secara otomatis
      inisialisasiPilihan();

      // Notifikasi Sukses
      boxStatus.className = "berhasil";
      boxStatus.innerHTML = `<strong>✅ Program Pelatihan Berhasil Disimpan!</strong><br>Pelatihan "${nama}" telah ditambahkan ke sistem.`;
      boxStatus.classList.remove("sembunyi");
      
      // Menggulung ke atas sedikit agar notifikasi terlihat
      window.scrollTo({ top: boxStatus.offsetTop - 50, behavior: 'smooth' });
      
      // Perbarui Tampilan Daftar Pelatihan
      tampilkanDaftarPelatihanAdmin();
      
      // Sembunyikan notifikasi setelah 5 detik
      setTimeout(() => {
        boxStatus.classList.add("sembunyi");
      }, 5000);
    }

    function tampilkanDaftarPelatihanAdmin() {
      const wadah = document.getElementById("daftar-pelatihan-admin");
      if(daftarPelatihan.length === 0) { 
        wadah.innerHTML = "Belum ada pelatihan yang dibuat."; 
        wadah.className = "peringatan"; 
        return; 
      }
      
      wadah.className = "";
      let html = "";
      daftarPelatihan.forEach((p, idx) => {
        html += `
          <div class="daftar-item" style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; margin-bottom:8px; border-radius:8px;">
            <strong style="color:var(--biru-tua); font-size:1rem;">${idx + 1}. ${p.nama}</strong><br>
            📅 <strong>Pendaftaran:</strong> ${p.bukaPendaftaran} s.d ${p.tutupPendaftaran}<br>
            📍 <strong>Lokasi:</strong> ${p.lokasi}<br>
            💼 <strong>Kualifikasi Skema:</strong> <span style="color:#475569;">${p.jabatanTerpilih}</span>
          </div>`;
      });
      wadah.innerHTML = html;
    }

    function tampilkanPendaftar() {
      const wadah = document.getElementById("daftar-pendaftar");
      if(daftarPendaftar.length === 0) { wadah.innerHTML = "Belum ada data pendaftar."; wadah.className = "peringatan"; return; }
      wadah.className = "";
      let html = "";
      daftarPendaftar.forEach((p, idx) => {
        html += `
          <div class="daftar-item" style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px; margin-bottom:8px; border-radius:8px;">
            <strong>${idx + 1}. ${p.namaPeserta}</strong> (${p.nik}) - <span style="color:${p.status === 'Ditolak' ? 'var(--merah-bata)':'var(--hijau-daun)'}; font-weight:600;">${p.status}</span><br>
            Pelatihan & Jabatan: ${p.namaPelatihan} (${p.jabatanDiikuti})<br>
            Profil: ${p.pendidikanText} | Kerja: ${p.pengalaman} Tahun<br>
            ${p.keterangan ? `<em style="color:var(--merah-bata)">Alasan: ${p.keterangan}</em>`: `📁 Berkas: ${p.fileIjazah}, ${p.fileKerja}`}
          </div>`;
      });
      wadah.innerHTML = html;
    }

    function muatPilihanPelatihan() {
      const select = document.getElementById("pilih-pelatihan");
      select.innerHTML = '<option value="">-- Pilih Pelatihan --</option>';
      daftarPelatihan.forEach((p, idx) => { select.innerHTML += `<option value="${idx}">${p.nama}</option>`; });
      tampilkanDetailPelatihan();
    }

    function tampilkanDetailPelatihan() {
      const idx = document.getElementById("pilih-pelatihan").value;
      const detail = document.getElementById("detail-pelatihan");
      const selectJabatan = document.getElementById("pilih-jabatan");
      
      selectJabatan.innerHTML = '<option value="">-- Pilih Jabatan Terlebih Dahulu --</option>';
      if (idx === "") { detail.innerHTML = "Silakan pilih pelatihan terlebih dahulu."; detail.className = "peringatan"; return; }
      
      const p = daftarPelatihan[idx];
      detail.className = "info";
      detail.innerHTML = `
        <strong>📌 Informasi Program:</strong> ${p.nama}<br>
        <strong>Kualifikasi Dibuka:</strong> ${p.jabatanTerpilih}<br>
        <strong>Lokasi:</strong> ${p.lokasi}<br>
        <strong>Syarat Umum Dokumen:</strong> <pre style="white-space:pre-wrap; font-family:inherit;">${p.syaratUmum}</pre>`;
      
      p.skemaList.forEach((skema, i) => {
        selectJabatan.innerHTML += `<option value="${i}" data-jenjang="${skema.jenjang}" data-nama="${skema.namaJabatan}">${skema.labelLengkap}</option>`;
      });
    }

    function kirimPendaftaran() {
      const idxPelatihan = document.getElementById("pilih-pelatihan").value;
      const idxJabatan = document.getElementById("pilih-jabatan").value;
      const namaPeserta = document.getElementById("nama-peserta").value.trim();
      const nik = document.getElementById("nik").value.trim();
      const noHp = document.getElementById("no-hp").value.trim();
      const pendidikanValue = document.getElementById("pendidikan").value;
      const pengalamanInput = document.getElementById("pengalaman").value;
      
      const inputIjazah = document.getElementById("berkas-ijazah").files[0];
      const inputKerja = document.getElementById("berkas-kerja").files[0];
      
      const boxStatus = document.getElementById("status-registrasi-box");

      if(idxPelatihan === "" || idxJabatan === "" || !namaPeserta || !nik || !noHp || !pendidikanValue || pengalamanInput === "" || !inputIjazah || !inputKerja) {
        boxStatus.className = "gagal";
        boxStatus.innerHTML = `<strong>⚠️ Pendaftaran Gagal!</strong><br>Harap lengkapi seluruh isian formulir dan pastikan berkas persyaratan (Ijazah & Bukti Kerja) sudah dilampirkan.`;
        boxStatus.classList.remove("sembunyi");
        window.scrollTo({ top: boxStatus.offsetTop - 50, behavior: 'smooth' });
        return;
      }

      const pelatihan = daftarPelatihan[idxPelatihan];
      const optTerpilih = document.getElementById("pilih-jabatan").options[document.getElementById("pilih-jabatan").selectedIndex];
      const jenjangTujuan = optTerpilih.getAttribute("data-jenjang");
      const namaJabatanTujuan = optTerpilih.getAttribute("data-nama");
      
      const thnPengalaman = parseInt(pengalamanInput);
      const textEdu = teksPendidikan[pendidikanValue];

      const aturanJenjang = matriksValidasi[jenjangTujuan];
      let lulusScreening = true;
      let alasanTolak = "";

      if (!(pendidikanValue in aturanJenjang)) {
        lulusScreening = false;
        alasanTolak = `Tingkat pendidikan terakhir Anda (${textEdu}) tidak memenuhi syarat kualifikasi regulasi untuk Jabatan ${namaJabatanTujuan} (Jenjang ${jenjangTujuan}).`;
      } else {
        const minTahun = aturanJenjang[pendidikanValue];
        if (thnPengalaman < minTahun) {
          lulusScreening = false;
          alasanTolak = `Pengalaman kerja Anda kurang. Untuk lulus kualifikasi Jenjang ${jenjangTujuan} dengan latar belakang ${textEdu}, dibutuhkan pengalaman minimal ${minTahun} tahun (Pengalaman Anda saat ini: ${thnPengalaman} tahun).`;
        }
      }

      if (!lulusScreening) {
        boxStatus.className = "gagal";
        boxStatus.innerHTML = `<strong>⛔ PENDAFTARAN OTOMATIS DITOLAK (SISTEM SCREENING V.2026)</strong><br>${alasanTolak}<br><br><small>Berkas Anda masuk ke data penolakan sistem evaluasi Balai Jasa Konstruksi Wilayah VI Makassar.</small>`;
        boxStatus.classList.remove("sembunyi");

        daftarPendaftar.push({
          namaPelatihan: pelatihan.nama, jabatanDiikuti: namaJabatanTujuan + ` (Jenjang ${jenjangTujuan})`,
          namaPeserta, nik, noHp, pendidikanText: textEdu, pengalaman: thnPengalaman,
          fileIjazah: inputIjazah.name, fileKerja: inputKerja.name, status: "Ditolak", keterangan: alasanTolak
        });
        simpanKeStorage("daftarPendaftar", daftarPendaftar);
        window.scrollTo({ top: boxStatus.offsetTop - 50, behavior: 'smooth' });
        return;
      }

      boxStatus.className = "berhasil";
      boxStatus.innerHTML = `<strong>🎉 SELAMAT! PENDAFTARAN BERHASIL DITERIMA</strong><br>Data Anda untuk skema <strong>${namaJabatanTujuan} (Jenjang ${jenjangTujuan})</strong> telah lolos verifikasi persyaratan kualifikasi awal sistem siLATI.`;
      boxStatus.classList.remove("sembunyi");

      daftarPendaftar.push({
        namaPelatihan: pelatihan.nama, jabatanDiikuti: namaJabatanTujuan + ` (Jenjang ${jenjangTujuan})`,
        namaPeserta, nik, noHp, pendidikanText: textEdu, pengalaman: thnPengalaman,
        fileIjazah: inputIjazah.name, fileKerja: inputKerja.name, status: "Diterima (Lolos)", keterangan: ""
      });
      
      simpanKeStorage("daftarPendaftar", daftarPendaftar);

      document.getElementById("nama-peserta").value = "";
      document.getElementById("no-hp").value = "";
      document.getElementById("pendidikan").value = "";
      document.getElementById("pengalaman").value = "0";
      document.getElementById("berkas-ijazah").value = "";
      document.getElementById("berkas-kerja").value = "";
      
      window.scrollTo({ top: boxStatus.offsetTop - 50, behavior: 'smooth' });
    }

    function unduhCSV() {
      if(daftarPendaftar.length === 0) { alert("Data kosong!"); return; }
      let csv = "No,Nama Pelatihan,Skema Jabatan,Nama Pendaftar,NIK,No WA,Pendidikan,Pengalaman(Tahun),Status,Keterangan\n";
      daftarPendaftar.forEach((p, idx) => {
        csv += `${idx + 1},"${p.namaPelatihan}","${p.jabatanDiikuti}","${p.namaPeserta}","${p.nik}","${p.noHp}","${p.pendidikanText}",${p.pengalaman},"${p.status}","${p.keterangan}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.setAttribute("download", "Data_Screening_siLATI.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  </script>
</body>
</html>
