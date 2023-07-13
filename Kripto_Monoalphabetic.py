"""
    Judul Program   : Chiper Monoalphabetic
    Pembuat         : Hilal Haidar Alimin
    NIM             : A11.2020.12485
    Dekripsi        : Program pembuatan chiper text dengan menggunakan metode chiper monoalpha
    Tanggal         : 19 Maret 2023
"""


def buat_kunci(kunci):
    """
        Fungsi ini digunakan untuk membuat kunci enkripsi.
        kunci dari user akan diambil 2 huruf terdepan setiap kata.
        kunci akan ditambahkan huruf alphabet yang belum ada sebelumnya.
    Args:
        kunci (str): kunci inputan user
    Returns:
        kunci_enkrip (str): kunci_enkrip yang terbentuk dari kunci dan alpha
    """
    
    gabung_kata = ""
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # Memotong kunci dengan mengambil 2 huruf terdepan setiap kata
    for i in kunci.split(" "):
        gabung_kata += i[0:2]
    # Menggabungkan kedua string
    kunci_enkrip = gabung_kata.lower()+ alpha
    # Menghapus karakter duplikat
    kunci_enkrip = ''.join(sorted(set(kunci_enkrip), key=kunci_enkrip.index))
    return kunci_enkrip

def enkripsi(pesan,kunci):
    """
        Fungsi untuk mengenkripsi pesan menggunakan kunci dengan proses substitusi
    Args:
        pesan (str): pesan untuk dienkripsi
        kunci (str): kunci untuk mengenkripsi pesan

    Returns:
        ciphertext (str): ciphertext merupakan enkripsi dari substitusi pesan dan kunci
    """
    kunci = buat_kunci(kunci)
    ciphertext = ''
    # Proses enkripsi dengan substitusi
    for char in pesan.lower():
        if char.isalpha():
            index = ord(char) - ord('a')
            ciphertext += kunci[index]
        else:
            ciphertext += char
    return ciphertext


def dekripsi(cipher_text, kunci):
    """
        Fungsi untuk mengdekripsi pesan menggunakan kunci dengan proses substitusi
    Args:
        cipher_text (str): pesan rahasia untuk dekripsi
        key (str): kunci untuk dekripsi pesan

    Returns:
        plaintext (str): plaintext merupakan dekripsi dari substitusi cipher_text dan kunci
    """
    kunci = buat_kunci(kunci)
    plaintext = ''
    # Proses dekripsi dengan substitusi
    for char in cipher_text:
        if char.isalpha():
            index = kunci.index(char)
            plaintext += chr(index + ord('a'))
        else:
            plaintext += char
    return plaintext

def main():
    print(" *** PROGRAM MONOALPHABETIC ***")
    
    kunci = str(input("Masukkan Kunci : "))
    pesan = str(input("Masukkan Pesan : "))
    print("Enkripsi : " + enkripsi(pesan,kunci))
    print("Dekripsi : " + dekripsi(enkripsi(pesan, kunci),kunci))
    
if __name__ == '__main__':
    main()


