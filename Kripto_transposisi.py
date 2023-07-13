"""
    Judul Program   : Transposisi kolom
    Pembuat         : Hilal Haidar Alimin
    NIM             : A11.2020.12485
    Dekripsi        : Program pembuatan chiper text dengan menggunakan metode transposisi kolom
    Tanggal         : 6 April 2023
"""

def buat_kunci(kunci):
    """
        Fungsi yang digunakan untuk membuat urutan tiap karakter pada kunci

    Args:
        kunci (str): kunci yang didapatkan dari user
    """
    
    urutan = {}
    urut = 1
    print("Urutan Kunci : ")
    
    # Pengurutan karakter dalam kunci
    for huruf in sorted(kunci):
            urutan[huruf] = urut
            urut+=1
            
    # Menampilkan hasil urutan
    for i in kunci:
            print(i," = ",urutan[i])
    
def buat_matrix(kunci,pesan):
    """
        Fungsi yang digunakan untuk Membuat matriks dengan menggunakan kunci dan pesan yang diberikan.
        jumlah kolom berdasarkan panjang kunci.
        jumlah baris disesuaikan dengan panjang pesan. 

    Args:
        kunci (str): kunci yang digunakan untuk membuat matriks
        pesan (str): Plaintext yang akan dienkripsi

    Returns:
        matriks (list): Matriks yang terbentuk dari kunci dan pesan
    """
    
    baris = len(pesan) // len(kunci)
    if len(pesan) % len(kunci) != 0:
        baris += 1

    # membuat matriks dengan len(kunci) kolom dan jumlah baris yang ditentukan oleh pesan
    matrix = []
    print("Matriks Pesan : ")
    for i in range(baris):
        row = []
        for j in range(len(kunci)):
            if i * len(kunci) + j < len(pesan):
                row.append(pesan[i * len(kunci) + j])
            else:
                row.append("")
        matrix.append(row)
    return matrix

def enkripsi(kunci,pesan):
    """
        Fungsi yang digunakan untuk mengenkripsi pesan user.
        enkripsi dilakukan dengan mengambil urutan karakter kunci secara ascending.
        urutan tersebut menentukan kolom pada matriks yang akan diambil terlebih dahulu

    Args:
        kunci (str): Kunci untuk mengenkripsi
        pesan (str): Plaintext yang akan dienkripsi
    """
    
    # pembuatan matriks
    matriks = buat_matrix(kunci, pesan)
    for row in matriks:
        print(row)
        
    print('Chiper Text : ')
    
    for i in kunci:
        ascii_values = [ord(huruf) for huruf in kunci]  # Mengambil nilai ASCII dari setiap karakter di dalam string
        min_ascii = min(ascii_values)  # Mencari nilai ASCII terkecil
        
        #hapus karakter pertama dengan nilai ASCII terkecil
        index_to_remove = ascii_values.index(min_ascii)
        kunci = kunci[:index_to_remove] + kunci[index_to_remove+1:]
        
        # Menampilkan Chipertext
        if type(min_ascii) is not None:
            for row in matriks:
                print(row[index_to_remove], end="")
                del row[index_to_remove]


def main():
    """
        Fungsi yang digunakan untuk deklarasi, inisiasi variabel, dan eksekusi fungsi
    """
    print(" *** PROGRAM TRANSPOSISI KOLOM ***")
    kunci = str(input("Masukkan Kunci : ")).lower().replace(" ", "")
    pesan = str(input("Masukkan Pesan : ")).replace(" ", "")
    
    # Memanggil fungsi 
    
    buat_kunci(kunci)
    enkripsi(kunci, pesan)

if __name__ == '__main__':
    main()
