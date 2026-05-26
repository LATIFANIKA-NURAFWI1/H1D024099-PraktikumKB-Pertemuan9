"""
====================================================
  Algoritma Genetika untuk Knapsack Problem
  Praktikum Kecerdasan Buatan - Pertemuan 9
====================================================
"""

import random
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────
# DATA BARANG
# ──────────────────────────────────────────────────
# Format: (nama, nilai, bobot)
barang = [
    ("Barang1", 60,  10),
    ("Barang2", 100, 20),
    ("Barang3", 120, 30),
    ("Barang4", 90,  25),
    ("Barang5", 69,  11),
    ("Barang6", 70,   9),
    ("Barang7", 80,  15),
    ("Barang8", 90,  10),
    ("Barang9", 25,   3),
]

# ──────────────────────────────────────────────────
# 1. INISIALISASI POPULASI
# ──────────────────────────────────────────────────
def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    """
    Membangkitkan populasi awal secara acak.
    Setiap individu (kromosom) adalah list biner sepanjang jumlah_gen.
    Gen bernilai 1 = barang dipilih, 0 = tidak dipilih.
    """
    populasi = []
    for _ in range(jumlah_populasi):
        kromosom = [random.randint(0, 1) for _ in range(jumlah_gen)]
        populasi.append(kromosom)
    return populasi


# ──────────────────────────────────────────────────
# 2. EVALUASI FITNESS
# ──────────────────────────────────────────────────
def hitung_fitness(kromosom, barang, kapasitas_tas):
    """
    Menghitung nilai fitness satu kromosom.
    Fitness = total nilai barang yang dipilih, asalkan total bobot <= kapasitas.
    Jika melebihi kapasitas, fitness = 0 (penalti).
    """
    total_nilai = 0
    total_bobot = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_nilai  += barang[i][1]
            total_bobot  += barang[i][2]
    if total_bobot > kapasitas_tas:
        return 0  # Penalti: melebihi kapasitas
    return total_nilai


# ──────────────────────────────────────────────────
# 3. SELEKSI
# ──────────────────────────────────────────────────
def roulette_wheel_selection(populasi, fitness_populasi):
    """
    Roulette Wheel Selection: memilih satu individu secara probabilistik
    berdasarkan proporsi nilai fitness-nya terhadap total fitness populasi.
    Mengembalikan (individu, indeks).
    """
    total_fitness = sum(fitness_populasi)
    if total_fitness == 0:
        # Semua fitness nol → pilih acak
        idx = random.randrange(len(populasi))
        return populasi[idx], idx

    # Hitung probabilitas kumulatif
    kumulatif = 0.0
    kumulatif_prob = []
    for f in fitness_populasi:
        kumulatif += f / total_fitness
        kumulatif_prob.append(kumulatif)

    r = random.random()
    for i, kp in enumerate(kumulatif_prob):
        if r <= kp:
            return populasi[i], i

    # Fallback: kembalikan individu terakhir
    return populasi[-1], len(populasi) - 1


def tournament_selection(populasi, fitness_populasi, k=3):
    """
    Tournament Selection: pilih k individu acak, ambil yang fitness-nya tertinggi.
    Mengembalikan (individu, indeks).
    """
    k = min(k, len(populasi))
    peserta_indices = random.sample(range(len(populasi)), k)
    best_idx = max(peserta_indices, key=lambda i: fitness_populasi[i])
    return populasi[best_idx], best_idx


# ──────────────────────────────────────────────────
# 4. CROSSOVER
# ──────────────────────────────────────────────────
def one_point_crossover(parent1, parent2):
    """
    One-Point Crossover: pilih satu titik potong acak, tukar bagian setelah
    titik tersebut antara kedua parent untuk menghasilkan dua anak.
    """
    titik_potong = random.randint(1, len(parent1) - 1)
    anak1 = parent1[:titik_potong] + parent2[titik_potong:]
    anak2 = parent2[:titik_potong] + parent1[titik_potong:]
    return anak1, anak2


def two_point_crossover(parent1, parent2):
    """
    Two-Point Crossover: tukar segmen gen antara dua titik potong acak.
    """
    titik1 = random.randint(1, len(parent1) - 2)
    titik2 = random.randint(titik1 + 1, len(parent1) - 1)
    anak1 = parent1[:titik1] + parent2[titik1:titik2] + parent1[titik2:]
    anak2 = parent2[:titik1] + parent1[titik1:titik2] + parent2[titik2:]
    return anak1, anak2


def uniform_crossover(parent1, parent2):
    """
    Uniform Crossover: setiap gen pada anak ditentukan oleh mask acak.
    mask=0 → ambil dari parent masing-masing; mask=1 → tukar.
    """
    mask  = [random.randint(0, 1) for _ in range(len(parent1))]
    anak1, anak2 = [], []
    for i in range(len(parent1)):
        if mask[i] == 0:
            anak1.append(parent1[i])
            anak2.append(parent2[i])
        else:
            anak1.append(parent2[i])
            anak2.append(parent1[i])
    return anak1, anak2


# ──────────────────────────────────────────────────
# 5. MUTASI
# ──────────────────────────────────────────────────
def swap_mutation(kromosom):
    """
    Swap Mutation: tukar posisi dua gen yang dipilih secara acak.
    """
    kromosom = list(kromosom)
    pos1, pos2 = random.sample(range(len(kromosom)), 2)
    kromosom[pos1], kromosom[pos2] = kromosom[pos2], kromosom[pos1]
    return kromosom


def inversion_mutation(kromosom):
    """
    Inversion Mutation: balik urutan gen dalam segmen acak.
    """
    kromosom = list(kromosom)
    pos1 = random.randint(0, len(kromosom) - 2)
    pos2 = random.randint(pos1 + 1, len(kromosom) - 1)
    kromosom[pos1:pos2] = list(reversed(kromosom[pos1:pos2]))
    return kromosom


def uniform_mutation(kromosom, mutation_rate=0.1):
    """
    Uniform Mutation: setiap gen dibalik (flip) dengan probabilitas mutation_rate.
    """
    kromosom = list(kromosom)
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]
    return kromosom


# ──────────────────────────────────────────────────
# 6. FUNGSI UTAMA: RUN GA
# ──────────────────────────────────────────────────
def run_ga(jumlah_generasi=50, jumlah_populasi=20,
           prob_crossover=0.5, prob_mutasi=0.1, kapasitas_tas=50):
    """
    Menjalankan Algoritma Genetika untuk Knapsack Problem.

    Parameter:
        jumlah_generasi : jumlah iterasi evolusi
        jumlah_populasi : ukuran populasi per generasi
        prob_crossover  : probabilitas crossover terjadi (0–1)
        prob_mutasi     : probabilitas mutasi terjadi (0–1)
        kapasitas_tas   : batas bobot maksimum tas
    """
    jumlah_gen = len(barang)

    # ── Inisialisasi populasi awal ──────────────────
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)

    # ── Hitung fitness awal ─────────────────────────
    fitness_populasi = [hitung_fitness(ind, barang, kapasitas_tas)
                        for ind in populasi]

    # ── List pencatatan untuk plotting ─────────────
    best_fitness_list  = []
    worst_fitness_list = []
    avg_fitness_list   = []
    all_fitness        = []   # semua nilai fitness per generasi

    # ── Individu terbaik sepanjang evolusi ──────────
    best_individu        = None
    best_fitness_overall = 0

    # ── Loop generasi ───────────────────────────────
    for generasi in range(jumlah_generasi):

        # Evaluasi fitness populasi saat ini
        fitness_populasi = [hitung_fitness(ind, barang, kapasitas_tas)
                            for ind in populasi]

        # Catat statistik generasi ini
        best_fitness  = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness   = sum(fitness_populasi) / len(fitness_populasi)

        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())

        # Simpan individu terbaik secara keseluruhan
        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            idx_best             = fitness_populasi.index(best_fitness)
            best_individu        = populasi[idx_best][:]

        # (Opsional) Tampilkan progress tiap generasi
        print(f"Generasi {generasi+1:3d} | "
              f"Terbaik: {best_fitness:4d} | "
              f"Rata-rata: {avg_fitness:7.2f} | "
              f"Terburuk: {worst_fitness:4d}")

        # ── Bentuk populasi baru ────────────────────
        new_populasi = []

        while len(new_populasi) < jumlah_populasi:
            # Seleksi parent 1 dengan Roulette Wheel
            parent1, idx1 = roulette_wheel_selection(populasi, fitness_populasi)

            # Seleksi parent 2 dari sisa populasi (pastikan berbeda)
            available_indices = [i for i in range(len(populasi)) if i != idx1]
            if not available_indices:
                available_indices = list(range(len(populasi)))

            avail_pop     = [populasi[i]         for i in available_indices]
            avail_fitness = [fitness_populasi[i]  for i in available_indices]

            parent2, local_idx = roulette_wheel_selection(avail_pop, avail_fitness)

            # Crossover
            if random.random() < prob_crossover:
                anak1, anak2 = one_point_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]

            # Mutasi
            if random.random() < prob_mutasi:
                anak1 = swap_mutation(anak1)
            if random.random() < prob_mutasi:
                anak2 = swap_mutation(anak2)

            new_populasi.extend([anak1, anak2])

        # Potong agar tepat sesuai jumlah_populasi
        populasi = new_populasi[:jumlah_populasi]

    # ── Tampilkan Grafik Fitness ────────────────────
    plt.figure(figsize=(13, 7))

    # Scatter semua individu per generasi (abu-abu transparan)
    for i in range(jumlah_generasi):
        x_vals = [i + 1] * len(all_fitness[i])
        plt.scatter(x_vals, all_fitness[i], color='gray', alpha=0.15, s=18)

    # Garis tren
    generasi_x = range(1, jumlah_generasi + 1)
    plt.plot(generasi_x, best_fitness_list,  color='blue',   linewidth=2,
             label='Fitness Tertinggi')
    plt.plot(generasi_x, avg_fitness_list,   color='red',    linewidth=2,
             label='Fitness Rata-rata')
    plt.plot(generasi_x, worst_fitness_list, color='#FFD700', linewidth=2,
             label='Fitness Terendah')

    plt.title('Perkembangan Nilai Fitness', fontsize=14, fontweight='bold')
    plt.xlabel('Generasi', fontsize=12)
    plt.ylabel('Nilai Fitness', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.show()

    # ── Tampilkan Hasil Terbaik ─────────────────────
    selected_items  = [barang[i][0] for i in range(len(best_individu))
                       if best_individu[i] == 1]
    selected_value  = hitung_fitness(best_individu, barang, kapasitas_tas)
    selected_weight = sum(barang[i][2] for i in range(len(best_individu))
                          if best_individu[i] == 1)

    print("\n" + "=" * 45)
    print(f"  Nilai Fitness Terbaik : {selected_value}")
    print(f"  Total Bobot           : {selected_weight}")
    print("  Barang Terpilih       :")
    for item in selected_items:
        print(f"    - {item}")
    print("=" * 45)


# ──────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────
if __name__ == "__main__":
    run_ga(
        jumlah_generasi=50,
        jumlah_populasi=20,
        prob_crossover=0.5,
        prob_mutasi=0.1,
        kapasitas_tas=50
    )
