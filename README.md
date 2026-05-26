# Algoritma Genetika untuk Knapsack Problem

> **Praktikum Kecerdasan Buatan – Pertemuan 9**  
> Optimasi pemilihan barang menggunakan Algoritma Genetika

---

## Identitas Praktikan

| Nama      | [Nama Lengkap]           |
| ----------| ------------------------ |
| **Nama**  | [Latifani kaNurafwi]     |
| **NIM**   | [H1D024099]              |

---

## Deskripsi Program

Program ini menyelesaikan **Knapsack Problem** (masalah memilih barang dengan keuntungan maksimal dalam kapasitas terbatas) menggunakan **Algoritma Genetika (AG)**.

Data yang digunakan terdiri dari **9 barang** dengan nilai dan bobot tertentu. Kapasitas maksimum tas adalah **50**.

Algoritma Genetika bekerja dengan prinsip evolusi:
1. **Inisialisasi** – membangkitkan populasi awal (kromosom biner acak).
2. **Evaluasi** – menghitung fitness = total nilai barang yang dipilih (0 jika melebihi kapasitas).
3. **Seleksi** – memilih parent menggunakan *Roulette Wheel Selection*.
4. **Crossover** – menggabungkan gen dua parent (*One‑Point Crossover*).
5. **Mutasi** – mengubah gen secara acak (*Swap Mutation*).
6. **Generasi baru** – mengulangi hingga generasi maksimum.

Program ini **modular** – setiap komponen GA dipisah ke file sendiri untuk memudahkan pembelajaran.

---

## Struktur File

```
NIM-PraktikumKB-Pertemuan9/
│
├── InisiasiPopulasi.py      # Membangkitkan populasi awal
├── EvaluasiFitness.py       # Data barang & fungsi fitness
├── selection.py             # Roulette Wheel & Tournament Selection
├── crossover.py             # One-Point, Two-Point, Uniform Crossover
├── mutation.py              # Swap, Inversion, Uniform Mutation
├── ga_knapsack.py           # Versi semua fungsi dalam satu file (opsional)
├── main.py                  # File utama (impor modul-modul di atas)
└── README.md                # File ini
```

> **Catatan:** `main.py` mengimpor fungsi dari file-file modular. `ga_knapsack.py` adalah alternatif jika ingin semua kode dalam satu file.

---

## Instalasi & Persiapan

### 1. Pastikan Python terinstal (versi 3.7+)
```bash
python --version
```

### 2. Install library yang diperlukan
Hanya **matplotlib** yang perlu diinstal (random, numpy sudah bawaan):
```bash
pip install matplotlib
```

### 3. Letakkan semua file dalam satu folder
Pastikan file-file berikut ada:
- `InisiasiPopulasi.py`
- `EvaluasiFitness.py`
- `selection.py`
- `crossover.py`
- `mutation.py`
- `main.py`

---

## Cara Menjalankan

Buka terminal di folder tersebut, lalu jalankan:

```bash
python main.py
```

Atau jika ingin versi satu file:

```bash
python ga_knapsack.py
```

Program akan:
- Menampilkan **progress fitness** setiap generasi di terminal.
- Setelah selesai, menampilkan **grafik perkembangan fitness** (tertinggi, rata-rata, terendah, dan titik semua individu).
- Menampilkan **hasil akhir**: total keuntungan terbaik, total bobot, dan daftar barang terpilih.

---

## Data Barang & Parameter

### Data Barang (9 item)
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

**Kapasitas tas:** 50

### Parameter Algoritma Genetika (di `main.py`)
| Parameter          | Nilai | Keterangan                          |
| ------------------ | ----- | ----------------------------------- |
| Jumlah generasi    | 50    | Iterasi evolusi                     |
| Jumlah populasi    | 20    | Banyak individu per generasi        |
| Probabilitas crossover | 0.5  | 50% pasangan parent melakukan crossover |
| Probabilitas mutasi | 0.1  | 10% anak mengalami mutasi           |

> Parameter dapat diubah di dalam fungsi `run_ga()` di `main.py` atau `ga_knapsack.py`.

---

## Penjelasan Kode Modular

### 1. `InisiasiPopulasi.py`
- Fungsi `inisialisasi_populasi(jumlah_populasi, jumlah_gen)`
- Membangkitkan populasi awal berupa kromosom biner acak (0/1) sepanjang `jumlah_gen`.

### 2. `EvaluasiFitness.py`
- Data barang (nama, nilai, bobot) dan kapasitas tas.
- Fungsi `hitung_fitness(kromosom, barang, kapasitas)`  
  → mengembalikan total nilai jika total bobot ≤ kapasitas, selain itu 0 (penalti).

### 3. `selection.py`
- `roulette_wheel_selection(populasi, fitness_populasi)` – pilih parent berdasarkan probabilitas proporsional terhadap fitness.
- `tournament_selection(populasi, fitness_populasi, k=3)` – pilih k acak, ambil yang fitness tertinggi.
- **Catatan:** `main.py` hanya menggunakan Roulette Wheel.

### 4. `crossover.py`
- `one_point_crossover(p1, p2)` – satu titik potong.
- `two_point_crossover(p1, p2)` – dua titik potong.
- `uniform_crossover(p1, p2)` – setiap gen dipilih acak dari salah satu parent.
- **Catatan:** `main.py` hanya menggunakan One‑Point.

### 5. `mutation.py`
- `swap_mutation(kromosom)` – tukar dua gen acak.
- `inversion_mutation(kromosom)` – balik urutan gen pada segmen acak.
- `uniform_mutation(kromosom, rate=0.1)` – flip setiap gen dengan probabilitas rate.
- **Catatan:** `main.py` hanya menggunakan Swap Mutation.

### 6. `main.py`
- Mengimpor semua fungsi di atas.
- Menjalankan GA dengan parameter yang ditentukan.
- Mencatat statistik setiap generasi.
- Menampilkan grafik dan hasil akhir.

---

## Contoh Output

### Hasil akhir (contoh)
```
=============================================
Nilai Fitness:
Individu 1: Fitness = 0
Individu 2: Fitness = 190
Individu 3: Fitness = 230

Parent Terpilih:
Parent 1: individu3
Parent 2: individu4

Anak Hasil Crossover:
Anak 1: [1, 0, 1, 0, 1]
Anak 2: [0, 1, 0, 1, 0]

Anak Setelah Mutasi:
Anak 1 (Swap Mutation): [0, 1, 1, 0, 1]
Anak 2 (Inversion Mutation): [0, 1, 1, 0, 1]
Anak 3 (Uniform Mutation): [0, 1, 1, 0, 1]
Nilai Fitness Terbaik: 329
Total Bobot: 50
Barang Terpilih:
- Barang2
- Barang5
- Barang6
- Barang8
=============================================
```

### Grafik
Grafik menampilkan:
- **Garis biru** – fitness tertinggi per generasi.
- **Garis merah** – fitness rata-rata.
- **Garis kuning** – fitness terendah.
- **Titik abu-abu** – semua nilai fitness individu per generasi (semakin gelap = semakin banyak individu dengan fitness serupa).

---
