print('~~~ Selamat Datang di Kalkulator Sederhana ~~~')
p = input('Masukkan operator matematika yang ingin Anda hitung: ')
while True:
    if p == '+':
        aa = int(input('Mau penjumlahan berapa: '))
        bb = int(input('Print berapa banyak: '))
        for i in range(bb):
            print(f'{i+1} + {bb-i} = {(i+1)+(bb-i)}')
    elif p == '-':
        aa = int(input('Mau pengurangan berapa: '))
        bb = int(input('Print berapa banyak: '))
        for i in range(bb):
            print(f'{i+1} + {bb-i} = {(i+1)-(bb-i)}')
    elif p in ('x', 'X'):
        aa = int(input('Mau perkalian berapa: '))
        bb = int(input('Print berapa banyak: '))
        for i in range(bb):
            print(f'{i+1} X {bb-i} = {(i+1)*(bb-i)}')
    elif p == ':':
        aa = int(input('Mau pembagian berapa: '))
        bb = int(input('Print berapa banyak: '))
        for i in range(bb):
            print(f'{i+1} : {bb-i} = {(i+1)/(bb-i)}')
    else:
        print('Maaf, Operator Matematika yang Anda cari  belum tersedia.')
        break
    pernyataan = input('Apakah Anda Ingin Menghitung Lagi? (Y/T): ')
    if pernyataan in ('T', 't'):
        print('Terima Kasih dan Sampai Jumpa Lagi!')
        break
    elif pernyataan in ('Y', 'y'):
        continue
    
        