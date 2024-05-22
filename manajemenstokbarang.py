def tampilkan_data(stok):
    if not stok:
        print("Data Barang Kosong")
    else:
        for idx, barang in enumerate(stok):
            print(f"{idx}. Nama: {barang['nama']}, Jumlah: {barang['jumlah']}")

def hitung_jumlah_data(stok):
    return len(stok)

def cari_data(stok, nama_barang):
    hasil = [barang for barang in stok if barang['nama'].lower() == nama_barang.lower()]
    if hasil:
        return hasil[0]
    else:
        return None

def edit_data(stok, indeks, nama_baru, jumlah_baru):
    if 0 <= indeks < len(stok):
        stok[indeks]['nama'] = nama_baru
        stok[indeks]['jumlah'] = jumlah_baru
        return True
    else:
        return False

def hapus_data(stok, indeks):
    if 0 <= indeks <len(stok):
        del stok[indeks]
        return True
    else :
        return False

def tambah_data_barang(stok, nama_benda, jumlah_benda):
    stok.append({'nama': nama_benda, 'jumlah': jumlah_benda})