# testing-QA
Untuk memenuhi UTS Mata Kuliah Testing dan QA Perangkat Lunak<br><br>

File Power Point : /UTS/Ahmad Bajuri_201011400106_UTS_Testing Dan QA Perangkat Lunak.pptx<br>
File Contoh Konfigurasi CI CD : /.github/workflows/python-ci-cd.yml<br>
File Contoh Unit Testing dan Whitebox Testing : my_unit_test.py


## PENJELASAN my_unit_test.py
![image](https://github.com/ahmadbj11/testing-QA/assets/19506380/251b7474-fa1c-43f9-8e2e-c7bd5e81ab72)
### Keterangan : 

kita memiliki fungsi *tambah* yang menerima dua angka dan mengembalikan hasil penjumlahannya.<br>
fungsi *test_tambah_string* sebagai contoh Whitebox Testing. Fungsi ini mencoba menjumlahkan string dan angka, yang seharusnya menimbulkan TypeError.<br>
Dengan *with self.assertRaises(TypeError)*, kita memastikan bahwa operasi ini benar-benar memunculkan pengecualian TypeError.<br><br>


Dengan demikian, contoh ini mencakup Unit Testing (menguji fungsionalitas) dan Whitebox Testing (menguji kode internal) dalam Python.<br>
Kedua jenis pengujian ini saling melengkapi dan merupakan bagian penting dari praktik pengujian perangkat lunak.
