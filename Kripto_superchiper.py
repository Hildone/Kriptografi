"""
    Judul Program   : Supercipher
    Pembuat         : Hilal Haidar Alimin
    NIM             : A11.2020.12485
    Dekripsi        : Program pembuatan chiper text dengan menggunakan metode playfair dan vigenere
    Tanggal         : 12 April 2023
"""

# AWAL PROGRAM SUPERCIPHER
# AWAL PROGRAM PLAYFAIR
def buat_kunci_playfair(kunci):
    """
        fungsi yang digunakan untuk membuat matrix kunci guna enkripsi
        kunci akan diambil 2 huruf terdepan, digabung dengan alpha, dihilangkan duplikat,
            lalu mengganti huruf j dengan i
        matrix ukuran 5x5 yang diisi dengan hasil kunci sebelumnya
    Args:
        kunci (str): kunci yang diinputkan user

    Returns:
        matrix (list): terbentuk dari kunci yang sudah dimodifikasi
    """
    alpha = 'abcdefghiklmnopqrstuvwxyz'
    gabung_kata=""
    # Memotong kunci dengan mengambil 2 huruf terdepan setiap kata
    for i in kunci.split(" "):
        gabung_kata += i[0:2]
    # Menggabungkan kedua string
    kunci_baru = gabung_kata.lower().replace("j", "i").replace(" ", "") + alpha
    # Menghapus karakter duplikat dan mengganti huruf "j" dengan "i"
    kunci_baru = ''.join(sorted(set(kunci_baru), key=kunci_baru.index))
    # Membuat matrix kunci
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            if i * 5 + j < len(kunci_baru):
                row.append(kunci_baru[i * 5 + j])
            else:
                row.append("")
        matrix.append(row)
    return matrix


def cari_huruf(matrix,huruf):
    """
        Fungsi yang digunakan untuk mencari nilai kolom dan baris per huruf pada pesan
    Args:
        matrix (list): matriks kunci untuk enkripsi
        huruf (str): huruf yang berada pada pesan

    Returns:
        row, col (int): baris dan kolom yang dihasilkan dari pencarian
    """
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == huruf:
                return row, col
    return None


def enkripsi_1(kunci, pesan):
    """
        Fungsi yang digunakan untuk mengenkripsi pesan dengan kunci
        Pembuatan matrix untuk mengenkripsi pesan.
        Jika pesan berjumlah ganjil maka ditambahkan huruf 'z'.
        Pembuatan pasangan huruf dengan pesan jika ada duplikasi maka disisipkan huruf 'z'.
        Pembuatan chiper dengan membandingkan antara baris dan kolom setiap pasangan huruf,
            jika pada baris yang sama maka diambil huruf dikanannya
            jika pada kolom yang sama maka diambil huruf dibawahnya
            jika berbeda kolom dan baris maka diambil huruf secara diagonal
    Args:
        kunci (str): kunci untuk mengenkripsi
        pesan (str): pesan yang akan dienkripsi

    Returns:
        ciphertext (str): ciphertext yang dihasilkan dari operasi playfair
    """
    matrix = buat_kunci_playfair(kunci)    
    pesan = pesan.replace(" ", "").replace("j", "i")
    
    # Jika pesan berjumlah ganjil akan ditambahkan "z"
    if len(pesan)%2 ==1:
        pesan += "z"
    
    # Membuat pasangan huruf 
    pesan_baru = []
    for i in range(0, len(pesan), 2):
        # Jika pasangan huruf sama maka disisipkan huruf "z"
        if pesan[i] == pesan[i+1]:
            pesan_baru.append((pesan[i], 'z'))
            pesan = pesan[:i+1] + 'z' + pesan[i+1:]
        else:
            pesan_baru.append((pesan[i], pesan[i+1]))
    
    # Membuat ciphertext
    ciphertext = ''
    for pair in pesan_baru:
        # Mengambil nilai baris dan kolom
        row1, col1 = cari_huruf(matrix,pair[0])
        row2, col2 = cari_huruf(matrix,pair[1])
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    print("Ciphertext Pertama : " + ciphertext)
    return ciphertext

# AKHIR PROGRAM PLAYFAIR

# PERBATASAN ALGORITMA PLAYFAIR DAN VIGENERE

# AWAL PROGRAM VIGENERE

    
def buat_kunci_vigenere(kunci,pesan):
    """
        Fungsi untuk membuat kunci enkripsi.
        Bahan kunci diambil dari huruf tengah tiap kata pada var kunci
        kunci enkrip terbuat dari kunci user yang panjangnya sama dengan pesan
    Args:
        kunci (str): kunci dari user 
        pesan (str): pesan sebagai acuan panjang kunci

    Returns:
        kunci_baru (str): kunci enkrip terbuat dari kunci yang diulang sebanyak panjang pesan
        pisah_pesan (str): menghapus spasi pada pesan
    """
    # Untuk mendapatkan kunci dg mengambil huruf di tengah
    kunci_tmp = ""
    for i in kunci.split(" "):
        if len(i)%2 ==0:
            kunci_tmp += i[len(i)//2-1:len(i)//2+2]
        else:
            kunci_tmp += i[len(i)//2]
    pisah_pesan = "".join(pesan.split()).lower()
    # menentukan berapa kali kunci akan diulang
    if len(kunci_tmp)!= len(pisah_pesan):
        ulang = len(pisah_pesan)//len(kunci_tmp)
    kunci_baru = kunci_tmp * ulang
    # Pengecekan jika masih ada sisa panjang pesan
    if len(pisah_pesan) % len(kunci_tmp) != 0:
        # Menambahkan sisa huruf pada variabel kunci_tmp ke variabel kunci_baru
        kunci_baru += kunci_tmp[:len(pisah_pesan) % len(kunci_tmp)]
    return kunci_baru, pisah_pesan

def  enkripsi_2(kunci,pesan):
    """
        Fungsi digunakan untuk enkripsi pesan dengan kunci.
        inisiasi konv_kunci_baru dengan nilai values berdasarkan dict konversi pada kunci
        inisiasi konv_kunci_pesan dengan nilai values berdasarkan dict konversi pada pesan
        Proses vigenere = (P+K)%26, vigenere akan direverse untuk mendapatkan key pada dict konversi
    Args:
        kunci (str): kunci untuk enkripsi 
        pesan (str): pesan yang akan dienkripsi

    Returns:
        cipher_text (str): hasil dari proses vigenere
    """
    # Inisiasi dict konversi
    konversi = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
            'e': 4, 'f': 5, 'g': 6, 'h': 7, 
            'i': 8, 'j': 9, 'k': 10, 'l': 11, 
            'm': 12, 'n': 13, 'o': 14, 'p': 15, 
            'q': 16, 'r': 17, 's': 18, 't': 19, 
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 
            'y': 24, 'z': 25}
    # pembuatan kunci enkripsi
    kunci_baru,pisah_pesan = buat_kunci_vigenere(kunci, pesan)
    # Konversi kunci dan pesan
    konv_kunci_baru = [konversi[huruf] for huruf in kunci_baru]
    konv_pisah_pesan = [konversi[huruf] for huruf in pisah_pesan]
    # Proses vigenere 
    vigenere = [(konv_pisah_pesan[i]+konv_kunci_baru[i])%26 for i in range (len(pisah_pesan))]
    reverse_konversi = dict((desimal, huruf) for huruf, desimal in konversi.items())

    cipher_text = ''.join([reverse_konversi[desimal] for desimal in vigenere])
    return cipher_text

# AKHIR PROGRAM VIGENERE


def main():
    print(" *** PROGRAM SUPERCIPHER ***")
    kunci = str(input("Masukkan Kunci : ")).lower()
    pesan = str(input("Masukkan Pesan : ")).lower()

    print("CipherText Akhir : "+ enkripsi_2(kunci, enkripsi_1(kunci, pesan)))
if __name__ == '__main__':
    main()