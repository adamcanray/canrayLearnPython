# ----- header
# file ini akan me-write/menulis ke file output.txt, sesuai perintah yang kita masukan.

# ----- start reading
# Perhatikan:
# * Jika Anda membuka file menggunakan "w" (write) sebagai argumen kedua, file kosong baru akan dibuat. 
# * Perhatikan bahwa jika ada file lain dengan nama yang sama, file lama itu akan dihapus. 
# * Jika Anda ingin menambahkan beberapa konten ke file yang ada, 
# * Anda harus menggunakan pengubah "a" (append).
# ----- end.

# ----- start coding
# Implementasi:

# buat list, kita akan memasukan(menulis) isi dari list ini ke file output.txt
list_buah = ['apel',"jambu","belimbing",'pir','kedongdong']

# cek jika __name__ == "__main__" maka eksekusi kode dibawah
# __name__ adalah variabel spesial, ia akan bernilai "__main__" ketika ini adalah main program.
if __name__ == "__main__":
    # then
    # buat variabel yang menyimpan perintah open sebuah file
    # coba ubah parameter kedua write "w" menjadi append "a" dan perhatikan perbedaannya
    f = open("D:/belajar/belajarPython/latihan_course_pycharm/Introduction to Python/09_file_input_output/1_write_to_file/output.txt","w")

    # perulangan sebanyak list_buah
    for buah in list_buah:
        # tulis setiap element dari list_buah ke dalam file output.txt
        f.write(buah + "\n")

    # close file
    f.close()

# ----- end.

# note: coba ubah parameter kedua dari open() dan perhatikan apa bedanya ketika kita menggunakan "a" atau "w" sebagai parameter kedua.