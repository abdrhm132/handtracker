print("="*8,'WARUNG MAKAN','='*8,'\n')

print('''|  KODE  |  MAKANAN  |    HARGA  |
|   AB   |   NASGOR  | Rp.15.000 |
|   BC   |   PECEL   | Rp.20.000 | \n''')

kode = input('Masukan Kode : ')
uang = int(input('Masukan Uang : '))
pesanan = int(input('Masukan Jumlah Pesanan : '))

if kode == "AB":
    nasgor = 15000
    total = nasgor * pesanan
    kembalian = nasgor * pesanan - uang
    print(f' Nasi goreng = {nasgor}\n pesanan = {pesanan}\n total = {total}\n kembalian = {kembalian}')

if kode == "BC":
    soto = 20000
    total = soto * pesanan
    kembalian = soto * pesanan - uang
    print(f' Soto Ayam = {soto}\n pesanan = {pesanan}\n total = {total}\n kembalian = {kembalian}')
