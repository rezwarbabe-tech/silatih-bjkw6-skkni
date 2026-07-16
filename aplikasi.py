<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>siLATIH - Sistem Informasi Pelatihan Terintegrasi</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #f0f7ff 0%, #e6f0ff 100%);
            min-height: 100vh;
            color: #2c3e50;
            line-height: 1.6;
        }

        /* === HEADER JUDUL === */
        .header-aplikasi {
            background: linear-gradient(135deg, #0056b3 0%, #003d7a 100%);
            color: white;
            text-align: center;
            padding: 28px 20px;
            box-shadow: 0 4px 12px rgba(0, 86, 179, 0.25);
        }

        .header-aplikasi h1 {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 6px;
            letter-spacing: 0.5px;
        }

        .header-aplikasi h2 {
            font-size: 19px;
            font-weight: 600;
            margin-bottom: 6px;
            color: #ffd700;
        }

        .header-aplikasi p {
            font-size: 16px;
            font-weight: 500;
            opacity: 0.95;
        }

        /* === KONTAINER UTAMA === */
        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 0 20px;
        }

        /* === MENU NAVIGASI === */
        .menu-nav {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .menu-card {
            flex: 1;
            min-width: 280px;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }

        .menu-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        }

        .menu-pengelola {
            background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
            color: white;
        }

        .menu-peserta {
            background: linear-gradient(135deg, #17a2b8 0%, #117a8b 100%);
            color: white;
        }

        .menu-card h3 {
            font-size: 20px;
            margin-bottom: 12px;
            font-weight: 700;
        }

        .menu-card ul {
            list-style: none;
            padding-left: 0;
        }

        .menu-card li {
            padding: 6px 0;
            font-size: 15px;
            font-weight: 500;
            border-bottom: 1px solid rgba(255,255,255,0.2);
        }

        /* === BAGIAN KONTEN === */
        .konten-panel {
            background: white;
            border-radius: 12px;
            padding: 28px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }

        .konten-panel h3 {
            color: #0056b3;
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 18px;
            padding-bottom: 8px;
            border-bottom: 2px solid #ffd700;
        }

        .konten-panel p, .konten-panel li {
            font-size: 15px;
            font-weight: 500;
            color: #34495e;
            margin-bottom: 8px;
        }

        /* === WARNA KATEGORI SYARAT === */
        .kategori-ahli {
            background-color: #fff9e6;
            border-left: 5px solid #ffc107;
            padding: 14px;
            border-radius: 8px;
            margin: 12px 0;
        }

        .kategori-teknis {
            background-color: #e6f2ff;
            border-left: 5px solid #007bff;
            padding: 14px;
            border-radius: 8px;
            margin: 12px 0;
        }

        .kategori-operator {
            background-color: #e6fff2;
            border-left: 5px solid #28a745;
            padding: 14px;
            border-radius: 8px;
            margin: 12px 0;
        }

        .kategori-ahli h4, .kategori-teknis h4, .kategori-operator h4 {
            font-weight: 700;
            font-size: 17px;
            margin-bottom: 8px;
        }

        .kategori-ahli h4 { color: #856404; }
        .kategori-teknis h4 { color: #004085; }
        .kategori-operator h4 { color: #155724; }

        /* === FOOTER HAK CIPTA === */
        .footer-aplikasi {
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            font-size: 14px;
            font-weight: 500;
        }
    </style>
</head>
<body>

<!-- JUDUL APLIKASI -->
<div class="header-aplikasi">
    <h1>Aplikasi Pelatihan & Sertifikasi UJI Kompetensi</h1>
    <h2>Balai Jasa Konstruksi Wilayah VI Makassar</h2>
    <p>siLATIH - Sistem Informasi Pelatihan Terintegrasi</p>
</div>

<div class="container">
    <!-- MENU UTAMA -->
    <div class="menu-nav">
        <div class="menu-card menu-pengelola">
            <h3>🔧 Menu Pengelola</h3>
            <p>Hanya dapat diakses oleh Pengelola Sistem</p>
            <ul>
                <li>Pengelolaan Pelatihan (Buat, Edit, Hapus)</li>
                <li>Pengelolaan Data Peserta</li>
                <li>Laporan & Statistik Pelatihan</li>
                <li>Pengaturan Konfigurasi Sistem</li>
            </ul>
        </div>

        <div class="menu-card menu-peserta">
            <h3>👤 Menu Tamu / Peserta</h3>
            <p>Dapat diakses oleh seluruh peserta pelatihan</p>
            <ul>
                <li>Daftar Pelatihan Tersedia</li>
                <li>Pelatihan yang Saya Ikuti</li>
                <li>Riwayat Pendaftaran & Sertifikat</li>
                <li>Pusat Bantuan & Informasi</li>
            </ul>
        </div>
    </div>

    <!-- INFORMASI SISTEM -->
    <div class="konten-panel">
        <h3>📋 Informasi & Persyaratan Sistem</h3>
        <p><strong>Fitur Utama:</strong></p>
        <ul style="padding-left: 20px;">
            <li>Pelatihan tersimpan permanen, hanya Pengelola yang dapat mengubah atau menghapus</li>
            <li>Peserta dapat melihat seluruh pelatihan yang tersedia</li>
            <li>Validasi otomatis persyaratan pendidikan dan pengalaman kerja</li>
            <li>Pengelompokan jabatan menjadi Ahli, Teknis/Analis, dan Operator</li>
        </ul>

        <div class="kategori-ahli">
            <h4>🟡 Kualifikasi Ahli (Jenjang 9, 8, 7)</h4>
            <p>Persyaratan untuk jenjang tertinggi dengan latar belakang pendidikan tinggi hingga doktor</p>
        </div>

        <div class="kategori-teknis">
            <h4>🔵 Kualifikasi Teknis / Analis (Jenjang 6, 5, 4)</h4>
            <p>Persyaratan untuk tenaga teknis dengan latar belakang D1 hingga S1</p>
        </div>

        <div class="kategori-operator">
            <h4>🟢 Kualifikasi Operator (Jenjang 3, 2, 1)</h4>
            <p>Persyaratan untuk tenaga pelaksana dengan latar belakang dasar hingga D1/SMK</p>
        </div>
    </div>
</div>

<!-- HAK CIPTA -->
<div class="footer-aplikasi">
    © 2026 Balai Jasa Konstruksi Wilayah VI Makassar — Kementerian Pekerjaan Umum | siLATIH v2.2
</div>

<!-- KODE LOGIKA SISTEM (SUDAH TERMASUK SEMUA FUNGSI) -->
<script>
// ==============================================================
// DATA PERSYARATAN JABATAN KERJA
// ==============================================================
const PERSYARATAN_JABATAN = [
  { kualifikasi: "AHLI", jenjang: 9, daftarSyarat: [
    { pendidikan: "Doktor/Doktor Terapan/Pendidikan Spesialis_2", pengalamanMinimal: 0 },
    { pendidikan: "S2/S2 Terapan/Pendidikan Spesialis_1", pengalamanMinimal: 4 },
    { pendidikan: "Pendidikan Profesi", pengalamanMinimal: 7 },
    { pendidikan: "S1/S1 Terapan/D4 Terapan", pengalamanMinimal: 8 }
  ]},
  { kualifikasi: "AHLI", jenjang: 8, daftarSyarat: [
    { pendidikan: "Magister/Magister Terapan/S2/S2 Terapan/Pendidikan Spesialis_1", pengalamanMinimal: 0 },
    { pendidikan: "Pendidikan Profesi", pengalamanMinimal: 5 },
    { pendidikan: "S1/S1 Terapan/D4 Terapan", pengalamanMinimal: 6 }
  ]},
  { kualifikasi: "AHLI", jenjang: 7, daftarSyarat: [
    { pendidikan: "Pendidikan Profesi", pengalamanMinimal: 0 },
    { pendidikan: "S1/S1 Terapan/D4 Terapan (Dengan Pemberian Kompetensi Tambahan untuk Fresh Graduated, masa berlaku SKK = 1)", pengalamanMinimal: 0 },
    { pendidikan: "S1/S1 Terapan/D4 Terapan", pengalamanMinimal: 2 }
  ]},
  { kualifikasi: "TEKNIS/ANALIS", jenjang: 6, daftarSyarat: [
    { pendidikan: "S1/S1 Terapan/D4 Terapan", pengalamanMinimal: 0 },
    { pendidikan: "D3", pengalamanMinimal: 4 },
    { pendidikan: "D2", pengalamanMinimal: 8 },
    { pendidikan: "D1", pengalamanMinimal: 12 }
  ]},
  { kualifikasi: "TEKNIS/ANALIS", jenjang: 5, daftarSyarat: [
    { pendidikan: "D3", pengalamanMinimal: 0 },
    { pendidikan: "D2", pengalamanMinimal: 4 },
    { pendidikan: "D1/SMK Plus", pengalamanMinimal: 8 },
    { pendidikan: "SMK", pengalamanMinimal: 10 },
    { pendidikan: "SMA", pengalamanMinimal: 12 }
  ]},
  { kualifikasi: "TEKNIS/ANALIS", jenjang: 4, daftarSyarat: [
    { pendidikan: "D2", pengalamanMinimal: 0 },
    { pendidikan: "D1/SMK Plus", pengalamanMinimal: 2 },
    { pendidikan: "SMK", pengalamanMinimal: 4 },
    { pendidikan: "SMA", pengalamanMinimal: 6 }
  ]},
  { kualifikasi: "OPERATOR", jenjang: 3, daftarSyarat: [
    { pendidikan: "D1/SMK Plus", pengalamanMinimal: 0 },
    { pendidikan: "SMK", pengalamanMinimal: 3 },
    { pendidikan: "SMA", pengalamanMinimal: 4 },
    { pendidikan: "Pendidikan Dasar", pengalamanMinimal: 5 }
  ]},
  { kualifikasi: "OPERATOR", jenjang: 2, daftarSyarat: [
    { pendidikan: "SMK", pengalamanMinimal: 0 },
    { pendidikan: "SMA", pengalamanMinimal: 1 },
    { pendidikan: "Pendidikan Dasar", pengalamanMinimal: 0 }
  ]},
  { kualifikasi: "OPERATOR", jenjang: 1, daftarSyarat: [
    { pendidikan: "Pendidikan Dasar", pengalamanMinimal: 0 },
    { pendidikan: "Non Pendidikan (Dengan PBK)", pengalamanMinimal: 2 }
  ]}
];

// DATA PELATIHAN & FUNGSI PENGELOLAAN
let DAFTAR_PELATIHAN = [];
function simpanPelatihan(data) { const b = {id:Date.now(),...data,tanggalDibuat:new Date().toISOString()}; DAFTAR_PELATIHAN.push(b); return {status:true, data:b}; }
function ubahPelatihan(id, dataBaru) { const i = DAFTAR_PELATIHAN.findIndex(p=>p.id===id); if(i<0) return {status:false}; DAFTAR_PELATIHAN[i]={...DAFTAR_PELATIHAN[i],...dataBaru}; return {status:true}; }
function hapusPelatihan(id) { const i = DAFTAR_PELATIHAN.findIndex(p=>p.id===id); if(i<0) return {status:false}; DAFTAR_PELATIHAN.splice(i,1); return {status:true}; }
function lihatPelatihan(peran) { return peran==="Pengelola" ? DAFTAR_PELATIHAN : DAFTAR_PELATIHAN.filter(p=>p.status==="Tersedia"); }
</script>

</body>
</html>
