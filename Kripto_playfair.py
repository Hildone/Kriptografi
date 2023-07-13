
"""
    Judul Program   : Playfair
    Pembuat         : Hilal Haidar Alimin
    NIM             : A11.2020.12485
    Dekripsi        : Program pembuatan cipher text dengan menggunakan metode playfair
    Tanggal         : 10 April 2023
"""


def buat_kunci(kunci):
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
    potong_kata =[]
    # Memotong kunci dengan mengambil 2 huruf terdepan setiap kata
    for i in kunci.split(" "):
        potong_kata.append(i[0:2])
    gabung_kata = "".join(potong_kata).lower().replace("j", "i")
    # Menggabungkan kedua string
    kunci_baru = gabung_kata + alpha
    # Menghapus karakter duplikat dan mengganti huruf "j" dengan "i"
    kunci_baru = ''.join(sorted(set(kunci_baru), key=kunci_baru.index))
    # Membuat matrix kunci
    matrix = []
    print("Matriks Kunci : ")
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



def enkripsi(kunci, pesan):
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
    matrix = buat_kunci(kunci)
    for i in matrix:
        print(i)
    
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
    return ciphertext


def main():
    print(" *** PROGRAM PLAYFAIR ***")
    kunci = str(input("Masukkan Kunci : ")).lower()
    pesan = str(input("Masukkan Pesan : ")).lower()
    print(enkripsi(kunci, pesan))
if __name__ == '__main__':
    main()




