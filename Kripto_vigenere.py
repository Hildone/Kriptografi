"""
    Judul Program   : Vigenere
    Pembuat         : Hilal Haidar Alimin
    NIM             : A11.2020.12485
    Dekripsi        : Program pembuatan chiper text dengan menggunakan metode Vigenere
    Tanggal         : 5 April 2023
"""

def buat_kunci(kunci,pesan):
    """
        Fungsi untuk membuat kunci enkripsi.
        kunci enkrip terbuat dari kunci user yang panjangnya sama dengan pesan
    Args:
        kunci (str): kunci dari user 
        pesan (str): pesan sebagai acuan panjang kunci

    Returns:
        kunci_baru (str): kunci enkrip terbuat dari kunci yang diulang sebanyak panjang pesan
        pisah_pesan (str): menghapus spasi pada pesan
    """
    pisah_pesan = "".join(pesan.split()).lower()
    # menentukan berapa kali kunci akan diulang
    if len(kunci)!= len(pisah_pesan):
        ulang = len(pisah_pesan)//len(kunci)
    kunci_baru = kunci * ulang
    # Pengecekan jika masih ada sisa panjang pesan
    if len(pisah_pesan) % len(kunci) != 0:
        # Menambahkan sisa huruf pada variabel kunci ke variabel kunci_baru
        kunci_baru += kunci[:len(pisah_pesan) % len(kunci)]
    return kunci_baru, pisah_pesan

def enkripsi(kunci,pesan):
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
    kunci_baru,pisah_pesan = buat_kunci(kunci, pesan)
    # Konversi kunci dan pesan
    konv_kunci_baru = [konversi[huruf] for huruf in kunci_baru]
    konv_pisah_pesan = [konversi[huruf] for huruf in pisah_pesan]
    # Proses vigenere 
    vigenere = [(konv_pisah_pesan[i]+konv_kunci_baru[i])%26 for i in range (len(pisah_pesan))]
    reverse_konversi = dict((desimal, huruf) for huruf, desimal in konversi.items())

    cipher_text = ''.join([reverse_konversi[desimal] for desimal in vigenere])
    return cipher_text

def dekripsi(kunci,pesan):
    """
        Fungsi digunakan untuk dekripsi pesan dengan kunci.
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
    # Pembuatan kunci
    kunci_baru,pisah_pesan = buat_kunci(kunci, pesan)
    # konversi kunci dan pesan
    konv_kunci_baru = [konversi[huruf] for huruf in kunci_baru]
    konv_pisah_pesan = [konversi[huruf] for huruf in pisah_pesan]
    # proses vigenere dan dekripsi
    vigenere = [(konv_pisah_pesan[i]+konv_kunci_baru[i])%26 for i in range (len(pisah_pesan))]
    dekripsi = [(vigenere[i]-konv_kunci_baru[i])%26 for i in range (len(pisah_pesan))]
    reverse_konversi = dict((desimal, huruf) for huruf, desimal in konversi.items())
    
    dekripsi_text = ''.join([reverse_konversi[desimal] for desimal in dekripsi])
    return dekripsi_text


def main():
    """
        fungsi untuk deklarasi, inisiasi dan eksekusi
    """
    
    kunci = str(input("Masukkan Kunci : "))
    pesan = str(input("Masukkan Pesan : "))
    
    print(
    "Pesan : " + pesan + "\n" + 
    "Kunci : " + kunci + "\n" + 
    "Chiper text : " + enkripsi(kunci, pesan) + "\n" +
    "Dekripsi text : " + dekripsi(kunci, pesan)
    )   
    
if __name__ == '__main__':
    main()



