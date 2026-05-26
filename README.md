# Algoritma Genetika untuk Knapsack Problem

> Praktikum Kecerdasan Buatan — Pertemuan 9

---

## Deskripsi

**Knapsack Problem** adalah masalah optimasi klasik: diberikan sejumlah barang yang masing-masing memiliki **nilai** dan **bobot**, tentukan kombinasi barang yang menghasilkan **total nilai maksimum** tanpa melebihi **kapasitas tas**.

**Algoritma Genetika (AG)** menyelesaikan masalah ini dengan meniru proses evolusi biologis:

1. **Inisialisasi** — Bangkitkan populasi awal berupa kromosom biner acak.  
2. **Evaluasi** — Hitung nilai fitness setiap individu (total nilai barang, atau 0 jika melebihi kapasitas).  
3. **Seleksi** — Pilih dua parent menggunakan *Roulette Wheel Selection*.  
4. **Crossover** — Gabungkan gen kedua parent untuk menghasilkan dua anak baru (*One-Point Crossover*).  
5. **Mutasi** — Ubah gen secara acak untuk menjaga keberagaman (*Swap Mutation*).  
6. **Generasi Baru** — Ganti populasi lama dengan populasi baru dan ulangi.

---

## Struktur File

```
NIM-PraktikumKB-Pertemuan9/
│
├── ga_knapsack.py   # Satu file utama berisi semua fungsi + main
└── README.md
```

---

## Library yang Diperlukan

| Library      | Kegunaan                              |
|--------------|---------------------------------------|
| `matplotlib` | Menampilkan grafik perkembangan fitness |
| `random`     | Pembangkitan bilangan acak (built-in) |

Instalasi library eksternal:

```bash
pip install matplotlib
```

---

## Cara Menjalankan Program

```bash
python ga_knapsack.py
```

Program akan menampilkan:
- Progress fitness per generasi di terminal.
- Grafik perkembangan fitness setelah semua generasi selesai.
- Hasil akhir: nilai fitness terbaik, total bobot, dan daftar barang terpilih.

---

## Data Barang

| Barang   | Nilai | Bobot |
|----------|-------|-------|
| Barang1  | 60    | 10    |
| Barang2  | 100   | 20    |
| Barang3  | 120   | 30    |
| Barang4  | 90    | 25    |
| Barang5  | 69    | 11    |
| Barang6  | 70    | 9     |
| Barang7  | 80    | 15    |
| Barang8  | 90    | 10    |
| Barang9  | 25    | 3     |

**Kapasitas Tas:** 50

---

## Parameter Algoritma Genetika

| Parameter          | Nilai  | Penjelasan                                               |
|--------------------|--------|----------------------------------------------------------|
| `jumlah_generasi`  | 50     | Jumlah iterasi evolusi                                   |
| `jumlah_populasi`  | 20     | Jumlah individu (kromosom) per generasi                  |
| `prob_crossover`   | 0.5    | Probabilitas 50% crossover terjadi pada sepasang parent  |
| `prob_mutasi`      | 0.1    | Probabilitas 10% mutasi terjadi pada setiap anak         |
| `kapasitas_tas`    | 50     | Batas bobot maksimum tas                                 |

---

## Fungsi-Fungsi Utama

| Fungsi | Deskripsi |
|--------|-----------|
| `inisialisasi_populasi(n, g)` | Bangkitkan `n` kromosom biner acak sepanjang `g` gen |
| `hitung_fitness(kromosom, barang, kapasitas)` | Hitung total nilai; kembalikan 0 jika bobot melebihi kapasitas |
| `roulette_wheel_selection(pop, fit)` | Pilih satu individu secara probabilistik proporsional terhadap fitness |
| `tournament_selection(pop, fit, k=3)` | Pilih `k` individu acak, ambil yang fitness tertinggi |
| `one_point_crossover(p1, p2)` | Crossover satu titik potong, hasilkan dua anak |
| `two_point_crossover(p1, p2)` | Crossover dua titik potong |
| `uniform_crossover(p1, p2)` | Crossover berbasis mask acak |
| `swap_mutation(kromosom)` | Tukar dua gen acak dalam kromosom |
| `inversion_mutation(kromosom)` | Balik segmen gen acak |
| `uniform_mutation(kromosom, rate)` | Flip setiap gen dengan probabilitas `rate` |
| `run_ga(...)` | Fungsi utama yang menjalankan seluruh proses AG |

---

## Contoh Output

### Terminal
```
Generasi   1 | Terbaik:  219 | Rata-rata:   30.45 | Terburuk:    0
Generasi   2 | Terbaik:  300 | Rata-rata:  205.65 | Terburuk:   90
...
Generasi  50 | Terbaik:  334 | Rata-rata:  284.80 | Terburuk:    0

=============================================
  Nilai Fitness Terbaik : 334
  Total Bobot           : 48
  Barang Terpilih       :
    - Barang5
    - Barang6
    - Barang7
    - Barang8
    - Barang9
=============================================
```

### Grafik Perkembangan Fitness
Grafik menampilkan 3 garis utama:
- 🔵 **Biru** — Fitness tertinggi per generasi
- 🔴 **Merah** — Fitness rata-rata per generasi
- 🟡 **Kuning** — Fitness terendah per generasi
- ⚪ **Abu-abu** (titik) — Nilai fitness semua individu per generasi

> **Catatan:** Fluktuasi nilai yang acak menunjukkan sifat variatif AG yang tinggi — algoritma mengeksplorasi berbagai kemungkinan solusi di setiap generasi.

---

## Cara Upload ke GitHub

```bash
# Inisialisasi repositori
git init
git add .
git commit -m "Praktikum KB Pertemuan 9 - Algoritma Genetika Knapsack"

# Hubungkan ke GitHub (ganti NIM dengan NIM Anda)
git remote add origin https://github.com/username/NIM-PraktikumKB-Pertemuan9.git
git branch -M main
git push -u origin main
```

Nama repositori: **`NIM-PraktikumKB-Pertemuan9`**  
Contoh: `123456789-PraktikumKB-Pertemuan9`

---

## Catatan

Program ini dibuat untuk memenuhi tugas **Praktikum Kecerdasan Buatan Pertemuan 9** dengan topik **Algoritma Genetika** pada studi kasus **Knapsack Problem**.
