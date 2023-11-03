import unittest

# Fungsi sederhana yang akan kita uji
def tambah(a, b):
    return a + b

# Kelas turunan dari unittest.TestCase untuk membuat test case
class TestTambah(unittest.TestCase):

    # Fungsi test case pertama
    def test_tambah_positif(self):
        hasil = tambah(3, 5)
        self.assertEqual(hasil, 8)  # Memastikan hasilnya benar

    # Fungsi test case kedua
    def test_tambah_negatif(self):
        hasil = tambah(-2, 1)
        self.assertEqual(hasil, -1)  # Memastikan hasilnya benar

    # Whitebox Testing: Melakukan pengecekan pada kode
    def test_tambah_string(self):
        with self.assertRaises(TypeError):
            tambah("hello", 1)

if __name__ == '__main__':
    unittest.main()