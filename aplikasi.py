<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sistem Pengelolaan Pelatihan & Jabatan Kerja</title>
<style>
* {box-sizing:border-box; font-family:'Segoe UI', Arial, sans-serif; margin:0; padding:0;}
.container {max-width:1200px; margin:0 auto; padding:20px;}
h1, h2, h3, h4 {margin:20px 0 10px 0; color:#2c3e50;}
p {line-height:1.6; margin-bottom:10px;}
hr {border:1px solid #eee; margin:30px 0;}
table {border-collapse:collapse; width:100%; margin:15px 0;}
th, td {border:1px solid #ddd; padding:12px; text-align:left; vertical-align:top;}
th {background:#f8f9fa; font-weight:bold;}
.ahli {background:#fff9cc;}
.teknis {background:#d7e3f5;}
.operator {background:#d9ead3;}
.form-group {margin:15px 0;}
label {display:block; margin-bottom:6px; font-weight:500;}
input, select, textarea {width:100%; padding:10px; border:1px solid #ccc; border-radius:4px; font-size:14px;}
input[type="checkbox"] {width:auto; margin-right:6px;}
.box-pilih {padding:12px; border-radius:4px; margin:8px 0;}
.btn {padding:10px 20px; border:none; border-radius:4px; cursor:pointer; margin-right:8px; font-size:14px; font-weight:500;}
.btn-simpan {background:#27ae60; color:white;}
.btn-ubah {background:#f39c12; color:white;}
.btn-hapus {background:#e74c3c; color:white;}
.btn-daftar {background:#2980b9; color:white; width:100%; margin-top:10px;}
.info-box {background:#e8f4fd; padding:15px; border-radius:4px; margin:15px 0; border-left:4px solid #2980b9;}
.catatan {background:#fff3cd; padding:15px; border-radius:4px; margin-top:30px; border-left:4px solid #ffc107;}
ul {margin-left:20px; line-height:1.7;}
pre {background:#f8f9fa; padding:15px; border-radius:4px; overflow-x:auto; font-size:13px;}
</style>
</head>
<body>
<div class="container">

<!-- ==============================================
BAGIAN 1: DAFTAR PUSTAKA & KETENTUAN UMUM
============================================== -->
<h1>DOKUMEN SISTEM PENGELOLAAN PELATIHAN & JABATAN KERJA</h1>
<p><strong>Versi:</strong> 1.0 | <strong>Tanggal:</strong> 16 Juli 2026 | <strong>Status:</strong> Final Siap Terapkan</p>

<h2>1. DAFTAR PUSTAKA</h2>
<ul>
  <li>Peraturan Menteri Ketenagakerjaan RI Nomor 1 Tahun 2021 tentang Pelatihan Kerja & Sertifikasi Kompetensi</li>
  <li>Standar Kompetensi Kerja Nasional Indonesia (SKKNI)</li>
  <li>Pedoman Klasifikasi Jabatan Kerja Nasional Tahun 2025</li>
  <li>Pedoman Pengelolaan Sistem Informasi Pelatihan Nomor 04/SJ/2024</li>
  <li>Panduan Teknis Pelatihan Berbasis Kompetensi (PBK)</li>
</ul>

<h2>2. KETENTUAN UMUM</h2>
<ul>
  <li><strong>Jabatan Kerja (Jabker):</strong> Tingkatan pekerjaan dengan syarat pendidikan & pengalaman jelas sesuai standar.</li>
  <li><strong>Pengelola:</strong> Pihak berwenang mengelola data, membuat pelatihan, menautkan jabatan kerja, dan verifikasi.</li>
  <li><strong>Peserta:</strong> Orang yang mengikuti pelatihan, hanya melihat jabatan kerja yang ditautkan ke pelatihannya.</li>
  <li><strong>PBK:</strong> Pelatihan Berbasis Kompetensi disesuaikan syarat jabatan tujuan.</li>
</ul>

<h2>3. PERSYARATAN JABATAN KERJA LENGKAP</h2>
<h3 class="ahli" style="padding:8px; border-radius:4px;">KLASIFIKASI: AHLI</h3>
<table>
<tr><th>Jenjang</th><th>Persyaratan Pendidikan</th><th>Pengalaman Minimal</th></tr>
<tr><td rowspan="4">9</td><td>Doktor / Doktor Terapan / Pendidikan Spesialis_2</td><td>0 Tahun</td></tr>
<tr><td>S2 / S2 Terapan / Pendidikan Spesialis_1</td><td>4 Tahun</td></tr>
<tr><td>Pendidikan Profesi</td><td>7 Tahun</td></tr>
<tr><td>S1 / S1 Terapan / D4 Terapan</td><td>8 Tahun</td></tr>
<tr><td rowspan="3">8</td><td>Magister / Magister Terapan / S2 / S2 Terapan / Pendidikan Spesialis_1</td><td>0 Tahun</td></tr>
<tr><td>Pendidikan Profesi</td><td>5 Tahun</td></tr>
<tr><td>S1 / S1 Terapan / D4 Terapan</td><td>6 Tahun</td></tr>
<tr><td rowspan="3">7</td><td>Pendidikan Profesi</td><td>0 Tahun</td></tr>
<tr><td>S1/S1 Terapan/D4 Terapan (Fresh Graduate dengan SKK Khusus)</td><td>0 Tahun</td></tr>
<tr><td>S1 / S1 Terapan / D4 Terapan</td><td>2 Tahun</td></tr>
</table>

<h3 class="teknis" style="padding:8px; border-radius:4px;">KLASIFIKASI: TEKNIS / ANALIS</h3>
<table>
<tr><th>Jenjang</th><th>Persyaratan Pendidikan</th><th>Pengalaman Minimal</th></tr>
<tr><td rowspan="4">6</td><td>S1 / S1 Terapan / D4 Terapan</td><td>0 Tahun</td></tr>
<tr><td>D3</td><td>4 Tahun</td></tr>
<tr><td>D2</td><td>8 Tahun</td></tr>
<tr><td>D1</td><td>12 Tahun</td></tr>
<tr><td rowspan="5">5</td><td>D3</td><td>0 Tahun</td></tr>
<tr><td>D2</td><td>4 Tahun</td></tr>
<tr><td>D1 / SMK Plus</td><td>8 Tahun</td></tr>
<tr><td>SMK</td><td>10 Tahun</td></tr>
<tr><td>SMA</td><td>12 Tahun</td></tr>
<tr><td rowspan="4">4</td><td>D2</td><td>0 Tahun</td></tr>
<tr><td>D1 / SMK Plus</td><td>2 Tahun</td></tr>
<tr><td>SMK</td><td>4 Tahun</td></tr>
<tr><td>SMA</td><td>6 Tahun</td></tr>
</table>

<h3 class="operator" style="padding:8px; border-radius:4px;">KLASIFIKASI: OPERATOR</h3>
<table>
<tr><th>Jenjang</th><th>Persyaratan Pendidikan</th><th>Pengalaman Minimal</th></tr>
<tr><td rowspan="4">3</td><td>D1 / SMK Plus</td><td>0 Tahun</td></tr>
<tr><td>SMK</td><td>3 Tahun</td></tr>
<tr><td>SMA</td><td>4 Tahun</td></tr>
<tr><td>Pendidikan Dasar</td><td>5 Tahun</td></tr>
<tr><td rowspan="3">2</td><td>SMK</td><td>0 Tahun</td></tr>
<tr><td>SMA</td><td>1 Tahun</td></tr>
<tr><td>Pendidikan Dasar</td><td>0 Tahun</td></tr>
<tr><td rowspan="2">1</td><td>Pendidikan Dasar</td><td>0 Tahun</td></tr>
<tr><td>Non Pendidikan (Dengan PBK)</td><td>2 Tahun</td></tr>
</table>

<h2>4. ATURAN HAK AKSES</h2>
<h3>Pengelola</h3>
<ul>
  <li>Melihat seluruh data jabatan kerja & pelatihan</li>
  <li>Membuat, menyimpan, mengedit, menghapus pelatihan</li>
  <li>Menautkan/mengubah tautan jabatan kerja ke pelatihan</li>
  <li>Memverifikasi pendaftaran peserta</li>
</ul>
<h3>Peserta</h3>
<ul>
  <li>Tidak melihat jabatan kerja di luar pelatihan yang diikuti</li>
  <li>Hanya melihat jabatan kerja yang ditautkan pengelola</li>
  <li>Mendaftar jika memenuhi syarat & mengunggah dokumen</li>
  <li>Tidak dapat mengubah data sistem</li>
</ul>

<hr>

<!-- ==============================================
BAGIAN 2: HALAMAN PENGELOLA (SIMPAN/UBAH/HAPUS)
============================================== -->
<h2>HALAMAN PENGELOLA: KELOLA PELATIHAN</h2>
<form method="post">
  <div class="form-group">
    <label>ID Pelatihan (Isi jika ingin mengubah)</label>
    <input type="text" name="id_pelatihan" placeholder="Kosongkan untuk pelatihan baru">
  </div>
  <div class="form-group">
    <label>Nama Pelatihan</label>
    <input type="text" name="nama_pelatihan" required placeholder="Contoh: Pelatihan Teknis Analisis Data">
  </div>
  <div class="form-group">
    <label>Deskripsi Pelatihan</label>
    <textarea name="deskripsi" rows="3" required placeholder="Tujuan & isi materi pelatihan"></textarea>
  </div>
  <div class="form-group">
    <h4>Pilih Jabatan Kerja yang Berlaku</h4>
    <div class="box-pilih ahli">
      <p><strong>Klasifikasi AHLI</strong></p>
      <label><input type="checkbox" name="jabker[]" value="AHLI-9"> Jenjang 9</label>
      <label style="margin-left:15px;"><input type="checkbox" name="jabker[]" value="AHLI-8"> Jenjang 8</label>
      <label style="margin-left:15px;"><input type="checkbox" name="jabker[]" value="AHLI-7"> Jenjang 7</label>
    </div>
    <div class="box-pilih teknis">
      <p><strong>Klasifikasi TEKNIS / ANALIS</strong></p>
      <label><input type="checkbox" name="jabker[]" value="TEKNIS-6"> Jenjang 6</label>
      <label style="margin-left:15px;"><input type="checkbox" name="jabker[]" value="TEKNIS-5"> Jenjang 5</label>
      <label style="margin-left:15px;"><input type="checkbox" name="jabker[]" value="TEKNIS-4"> Jenjang 4</label>
    </div>
    <div class="box-pilih operator">
      <p><strong>Klasifikasi OPERATOR</strong></p>
      <label><input type="checkbox" name="jabker[]" value="OPERATOR-3"> Jenjang 3</label>
      <label style="margin-left:15px;"><input type="checkbox" name="jabker[]" value="OPERATOR-2"> Jenjang 2</label>
      <label style="margin-left:15px;"><input type="checkbox" name="jabker[]" value="OPERATOR-1"> Jenjang 1</label>
    </div>
  </div>
  <button type="submit" name="aksi" value="simpan" class="btn btn-simpan">Simpan Baru</button>
  <button type="submit" name="aksi" value="ubah" class="btn btn-ubah">Simpan Perubahan</button>
  <button type="submit" name="aksi" value="hapus" class="btn btn-hapus">Hapus Pelatihan</button>
</form>

<hr>

<!-- ==============================================
BAGIAN 3: HALAMAN PESERTA (FORMULIR SESUAI JABKER)
============================================== -->
<h2>HALAMAN PESERTA: FORMULIR PENDAFTARAN</h2>
<div class="info-box">
  <h4>Jabatan Kerja Sesuai Pelatihan Anda</h4>
  <p>Berikut syarat yang berlaku untuk pelatihan <strong>Pelatihan Teknis Analisis Data</strong>:</p>
  <table>
    <tr><th>Klasifikasi</th><th>Jenjang</th><th>Persyaratan Pendidikan</th><th>Pengalaman Minimal</th></tr>
    <tr><td rowspan="4">TEKNIS / ANALIS</td><td rowspan="4">6</td><td>S1 / S1 Terapan / D4 Terapan</td><td>0 Tahun</td></tr>
    <tr><td>D3</td><td>4 Tahun</td></tr>
    <tr><td>D2</td><td>8 Tahun</td></tr>
    <tr><td>D1</td><td>12 Tahun</td></tr>
  </table>
</div>

<form method="post" enctype="multipart/form-data">
  <div class="form-group">
    <label>Nama Lengkap Sesuai Dokumen</label>
    <input type="text" name="nama_lengkap" required>
  </div>
  <div class="form-group">
    <label>Nomor Induk Peserta / NIK</label>
    <input type="text" name="nomor_id" required>
  </div>
  <div class="form-group">
    <label>Jenjang Pendidikan Terakhir</label>
    <select name="pendidikan" required>
      <option value="">-- Pilih --</option>
      <option value="S1">S1 / S1 Terapan / D4 Terapan</option>
      <option value="D3">D3</option>
      <option value="D2">D2</option>
      <option value="D1">D1</option>
      <option value="SMK">SMK / SMK Plus</option>
      <option value="SMA">SMA</option>
      <option value="DASAR">Pendidikan Dasar</option>
    </select>
  </div>
  <div class="form-group">
    <label>Lama Pengalaman Kerja (Tahun)</label>
    <input type="number" name="pengalaman" min="0" required placeholder="Contoh: 4">
  </div>
  <div class="form-group">
    <label>Unggah Dokumen (Ijazah, SK Kerja, Sertifikat)</label>
    <input type="file" name="dokumen" accept=".pdf,.jpg,.png" required>
  </div>
  <button type="submit" class="btn btn-daftar">Kirim Pendaftaran</button>
</form>

<hr>

<!-- ==============================================
BAGIAN 4: STRUKTUR DATA JSON & LOGIKA SISTEM
============================================== -->
<h2>STRUKTUR DATA & LOGIKA SISTEM</h2>
<pre>
{
  "versi": "1.0",
  "hak_akses": {
    "pengelola": {"lihat_semua":true, "simpan":true, "ubah":true, "hapus":true},
    "peserta": {"lihat_semua":false, "lihat_tertaut":true, "daftar":true}
  },
  "aturan_tampilan": "Peserta hanya melihat jabker yang ditautkan ke pelatihannya",
  "syarat_jabker": "Sesuai tabel persyaratan di atas"
}
</pre>

<h3>Logika Pemrosesan (Inti Sistem)</h3>
<pre>
// 1. Cek Akses
JIKA pengguna = PENGELOLA:
   Tampilkan SEMUA jabatan kerja & fitur kelola
JIKA pengguna = PESERTA:
   Ambil pelatihan yang diikuti
   Tampilkan HANYA jabatan kerja yang DITAUTKAN ke pelatihan tersebut
   Sembunyikan yang lain

// 2. Kelola Pelatihan
- Simpan Baru: Masukkan data pelatihan + daftar jabker terpilih ke database
- Ubah: Perbarui data pelatihan + hapus tautan lama, masukkan tautan baru
- Hapus: Hapus pelatihan & tautan jabker (tidak bisa dikembalikan)

// 3. Formulir Peserta
- Tampilkan syarat sesuai jabker pelatihan
- Validasi: Pendidikan & pengalaman minimal sesuai syarat
- Terima dokumen & simpan pendaftaran
</pre>

<hr>

<!-- ==============================================
BAGIAN 5: CATATAN KHUSUS & KAKU
============================================== -->
<div class="catatan">
  <h3>CATATAN KHUSUS & CATATAN KAKU</h3>
  <ul>
    <li>Perubahan data pelatihan/jabatan kerja HANYA boleh dilakukan pengelola berwenang.</li>
    <li>Persyaratan jabatan kerja tidak boleh diubah tanpa mengikuti standar nasional resmi.</li>
    <li>Sistem otomatis menyembunyikan jabatan kerja lain dari peserta — tidak ada akses lain.</li>
    <li>Data yang dihapus tidak dapat dipulihkan; pastikan cadangan sebelum menghapus.</li>
    <li>Setiap perubahan tercatat waktu, nama pengelola, dan jenis perubahan untuk audit.</li>
    <li>Dokumen palsu menyebabkan pembatalan pendaftaran & pemblokiran permanen.</li>
    <li>Formulir peserta menyesuaikan syarat secara otomatis sesuai jabatan kerja yang ditautkan.</li>
  </ul>
</div>

</div>
</body>
</html>
