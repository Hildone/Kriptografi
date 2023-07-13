import numpy as np

"""
    Judul Program   : Hill Chiper
    Pembuat         : Hilal Haidar Alimin
    NIM             : A11.2020.12485
    Dekripsi        : Program pembuatan chiper text dengan menggunakan metode Hill Chiper
    Tanggal         : 11 April 2023
"""


def enkripsi (kunci,pesan):
    """
        Fungsi yang digunakan untuk enkripsi pesan dengan kunci
        pesan akan dibuat biagram dan konversi ke decimalnya, jika ganjil ditambahkan str "w"
        Operasi hill cipher : (K x P) mod 26
        Reverse konversi untuk mendapatkan ciphertext dalam huruf
        
    Args:
        kunci (str): kunci untuk enkripsi
        pesan (str): pesan yang di enkripsi

    Returns:
        ciphertext (str) : ciphertext hasil dari operasi hill cipher 
    """
    # Deklarasi list
    pesan_baru,konversi_pesan,hasil_kali,dec_pesan=[],[],[],[]
    # Inisiasi dict
    konversi = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
                'e': 5, 'f': 6, 'g': 7, 'h': 8, 
                'i': 9, 'j': 10, 'k': 11, 'l': 12, 
                'm': 13, 'n': 14, 'o': 15, 'p': 16, 
                'q': 17, 'r': 18, 's': 19, 't': 20, 
                'u': 21, 'v': 22, 'w': 23, 'x': 24, 
                'y': 25, 'z': 0}
    # Jika pesan bernilai ganjil
    pesan = pesan.replace(" ", "").lower()
    if len(pesan)%2 ==1:
        pesan += "w"
    # Pembuatan biagram pesan
    for i in range(0, len(pesan), 2):
        pesan_baru.append((pesan[i], pesan[i+1]))
        konversi_pesan.append((konversi[pesan[i]],konversi[pesan[i+1]]))
    # Operasi hill cipher
    for i in range(5):
        hasil_kali.append((np.dot(kunci,konversi_pesan[i]))%26)
    reverse_konversi = dict((desimal, huruf) for huruf, desimal in konversi.items())
    # Mengubah matriks menjadi list dan merubah menjadi huruf
    for i in hasil_kali:
        for y in i :
            dec_pesan.append(y)
    ciphertext = ''.join([reverse_konversi[decimal] for decimal in dec_pesan])
    return ciphertext


def main():

    pesan = str(input("Masukkan Pesan : "))
    kunci = np.array([[5,6],[2,3]])
    print("Cipher text : " + enkripsi(kunci, pesan))

if __name__ == '__main__':
    main()







