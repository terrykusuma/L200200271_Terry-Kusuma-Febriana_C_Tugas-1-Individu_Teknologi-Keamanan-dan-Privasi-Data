#==============================[ FUNGSI UNTUK PROSES ENKRIPSI VIGENERE CHIPER]=====================================
def enkripsi(pesan, kunci):
    pesan_enkripsi= ''  
    for i in range(len(pesan)):
        char = pesan[i]  
        kunci_char = kunci[i % len(kunci)] 
        if char.isalpha():
            no_char = ord(char.upper()) - 65  
            no_kunci = ord(kunci_char.upper()) - 65 
            no_enkripsi = (no_char + no_kunci) % 26 
            char_enkripsi = chr(no_enkripsi + 65)
            if char.isupper(): 
                pesan_enkripsi += char_enkripsi  
            else:
                pesan_enkripsi += char_enkripsi.lower() 
        else:
            pesan_enkripsi += char 
    return pesan_enkripsi 

#==============================[ FUNGSI UNTUK PROSES DEKRIPSI VIGENERE CHIPER]=====================================
def dekripsi(teks_chiper, kunci):
    pesan_dekripsi = ''  
    for i in range(len(teks_chiper)):
        char = teks_chiper[i]  
        kunci_char = kunci[i % len(kunci)]  

        if char.isalpha():  
            no_char = ord(char.upper()) - 65  
            no_kunci = ord(kunci_char.upper()) - 65  

            no_dekripsi = (no_char - no_kunci) % 26  
            char_dekripsi = chr(no_dekripsi + 65)  

            if char.isupper():  
                pesan_dekripsi += char_dekripsi  
            else:
                pesan_dekripsi += char_dekripsi.lower()  
        else:
            pesan_dekripsi += char  
    return pesan_dekripsi  

#====================[ FUNGSI UNTUK MENJALANKAN PROSES ENKRIPSI DEKRIPSI VIGENERE CHIPER ]======================
def main():
    print("-----------------------------------------------------")
    print("=== [ PROSES ENKRIPSI DEKRIPSI VIGENERE CHIPER ] ====")
    print("-----------------------------------------------------")
    pesan = input('Isi Pesan      : ')  
    kunci = ('271') #menggunakan kunci 271 karena NIM saya L200200271 (3 angka terakhir adalah 271)
    teks_chiper = enkripsi(pesan, kunci)
    print('Hasil enkripsi :', teks_chiper)
    print('Hasil dekripsi :', dekripsi(teks_chiper, kunci))
    print("======================================================")
   
if __name__ == '__main__':
    main()