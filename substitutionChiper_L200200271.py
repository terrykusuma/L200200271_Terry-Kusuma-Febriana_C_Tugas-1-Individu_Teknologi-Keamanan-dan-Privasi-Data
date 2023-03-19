import string, random

#===========================[ FUNGSI UNTUK PROSES ENKRIPSI SUBSTITATION CHIPER]=====================================
def enkripsi(plaintext):
    huruf = list(string.ascii_uppercase)
    random.shuffle(huruf)
    peta_subtitution = {}
    for i in range(26):
        peta_subtitution[huruf[i]] = string.ascii_uppercase[i]
    teks_chiper = ''
    for char in plaintext:
        if char.isalpha(): 
            teks_chiper += peta_subtitution[char.upper()] 
        else: 
           teks_chiper += char
    return teks_chiper, peta_subtitution

#=========================[ FUNGSI UNTUK PROSES DEKRIPSI SUBSTITUTION CHIPER]=====================================
def dekripsi(teks_chiper, peta_substitusi):
    pesan_dekripsi = ''
    for char in teks_chiper:
        if char.isalpha(): 
            for kunci, value in peta_substitusi.items(): 
                if char.upper() == value: 
                    pesan_dekripsi += kunci
        else: 
            pesan_dekripsi += char 
    return pesan_dekripsi
#=================[ FUNGSI UNTUK MENJALANKAN PROSES ENKRIPSI DEKRIPSI SUBSTITUTION CHIPER ]======================
def main():
    print("-----------------------------------------------------")
    print("==[ PROSES ENKRIPSI DEKRIPSI SUBSTITUTION CHIPER ] ==")
    print("-----------------------------------------------------")
    plaintext = input('Isi Pesan      : ')
    teks_chiper,peta_substitusi = enkripsi(plaintext)  
    print('Hasil enkripsi: ', teks_chiper)  
    print('Hasil dekripsi: ', dekripsi(teks_chiper, peta_substitusi)) 
    print("======================================================") 

if __name__ == '__main__':
    main()