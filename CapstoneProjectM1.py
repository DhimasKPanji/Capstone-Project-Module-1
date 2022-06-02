Buku = [
    {'Kode Buku': 'HJN001','Judul Buku': 'Hujan','Tahun Terbit': '2018','Penulis': 'Tere Liye','Ketersediaan': 'Dipinjam','Waktu Pinjam': '10 hari','Tanggal Pinjam': '2022-05-25','Tanggal Kembali': '2022-06-04'},
    {'Kode Buku': 'SCR002','Judul Buku': 'Secrets','Tahun Terbit': '2022','Penulis': 'A.Helwa','Ketersediaan': 'Dipinjam','Waktu Pinjam': '12 hari','Tanggal Pinjam': '2022-05-26','Tanggal Kembali': '2022-06-07'},
    {'Kode Buku': 'ATH003','Judul Buku': 'Atomic Habit','Tahun Terbit': '2018','Penulis': 'James Clear','Ketersediaan': 'Tersedia','Waktu Pinjam': '-------','Tanggal Pinjam': '----------','Tanggal Kembali': '----------'},
    {'Kode Buku': 'DEW004','Judul Buku': 'Deep Work','Tahun Terbit': '2016','Penulis': 'Cal Newport','Ketersediaan': 'Tersedia','Waktu Pinjam': '-------','Tanggal Pinjam': '----------','Tanggal Kembali': '----------' },
    {'Kode Buku': 'LAM005','Judul Buku': 'Like a Monk','Tahun Terbit': '2020','Penulis': 'Jay Shetty','Ketersediaan': 'Tersedia','Waktu Pinjam': '-------','Tanggal Pinjam': '----------','Tanggal Kembali': '----------'}
]

from datetime import timedelta, date
now_date = date.today()

# Sub Menu untuk buku yang tersedia (Read)
def daftarbuku() :
    while True :
        menuDaftar = input('''
        ========================================
        1. Tampilkan Seluruh List Buku 
        2. Cari Buku berdasarkan kode buku
        3. Kembali ke Menu Awal
        
    \tPilih Menu yang ingin anda jalankan (1-3): ''')

        if menuDaftar == '1' :
            daftarbukuall()
        elif menuDaftar == '2' :
            daftarbukukode()
        elif menuDaftar == '3' :
            break

# Melihat list buku seluruhnya
def daftarbukuall() :
    print('\n\tDaftar Buku Perpustakaan JCDS: \n')
    print('Kode Buku\t| Judul Buku \t\t| Tahun Terbit\t| Penulis \t| Ketersediaan \t| Waktu Pinjam \t| Tanggal Pinjam \t| Tanggal Kembali \t|' )
    for i in range(len(Buku)) :
        print('{}\t\t| {} \t\t| {}\t\t| {}\t| {}\t| {}\t| {}\t\t| {} \t\t|'.format(Buku[i]['Kode Buku'],Buku[i]['Judul Buku'],Buku[i]['Tahun Terbit'],Buku[i]['Penulis'],Buku[i]['Ketersediaan'],Buku[i]['Waktu Pinjam'],Buku[i]['Tanggal Pinjam'],Buku[i]['Tanggal Kembali']))

# Melihat list buku sesuai pencarian kode buku
def daftarbukukode() :
    kodeBuku = input('\tMasukan kode item: ').upper()
    for i in range(len(Buku)) :
        if kodeBuku == Buku[i]['Kode Buku'] :
            print('\nKode Buku\t| Judul Buku \t\t| Tahun Terbit\t| Penulis \t| Ketersediaan \t| Waktu Pinjam \t| Tanggal Pinjam \t| Tanggal Kembali |\t' )
            print('{}\t\t| {} \t\t| {}\t\t| {}\t| {}\t| {}\t| {}\t\t| {}\t  |'.format(Buku[i]['Kode Buku'],Buku[i]['Judul Buku'],Buku[i]['Tahun Terbit'],Buku[i]['Penulis'],Buku[i]['Ketersediaan'],Buku[i]['Waktu Pinjam'],Buku[i]['Tanggal Pinjam'],Buku[i]['Tanggal Kembali']))
            break
    else:
        print('\n \t======Buku Tidak Ditemukan======')
        
# Sub Menu menambah buku kedalam list perpusatakaan (Create)
def tambahBuku() :
    while True:
        tambahbuku1 = input('''
        ==========================================
        1. Menambahkan buku kedalam Perpustakaan
        2. Kembali Ke Menu Awal    
        
        Pilih Menu yang ingin anda jalankan (1-2): ''')

        if tambahbuku1 == '1':
            tambahbuku2()
        elif tambahbuku1 == '2':
            break

# Menambah buku kedalam list perpusatakaan
def tambahbuku2():
    daftarbukuall()
    print('\n\tPASTIKAN KODE BUKU YANG ANDA MASUKAN BELUM DI INPUT!!!\n')
    newKode = input('\tMasukan Kode Buku (format 3 huruf dan 3 angka): ').upper()
    
    for i in range(len(Buku)) :
        if newKode == Buku[i]['Kode Buku']:
            print('\n\t======Kode Buku Telah di Input Sebelumnya======')
            break
        else :
            while True:  
                simpanData = input('\tApakah Anda Yakin Untuk Menambahkan Buku Kedalam List Perpustakaan?(YA/TIDAK): ').upper()
                if simpanData == 'YA' :
                    newBuku = input('\tMasukan Judul Buku Yang Ingin Ditambahkan: ').capitalize()
                    newTahun = input('\tMasukan Tahun Terbit: ')
                    newPenulis = input('\tMasukan Nama Penulis: ').capitalize()
                    Buku.append({
                        'Kode Buku'     : newKode,
                        'Judul Buku'    : newBuku,
                        'Tahun Terbit'  : newTahun,
                        'Penulis'       : newPenulis,
                        'Ketersediaan'  : 'Tersedia',
                        'Waktu Pinjam'  : '-------',
                        'Tanggal Pinjam' : '----------',
                        'Tanggal Kembali': '----------'
                    })
                    print('\n\t======Buku Telah Ditambahkan Kedalam List Perpustakaan======')
                    break
                elif simpanData == 'TIDAK' :
                    print('\n\t======Buku Tidak Jadi Ditambahkan kedalam List Perpustakaan======\n')
                    break
                else:
                    print('\n\t======Anda Salah Memasukan Input======\n')
        daftarbukuall()
        break

# Sub Menu untuk Pinjam dan Kembalikan Buku (Update)
def updateBuku():
    while True:
        updatebuku1 = input('''
        ==========================================
        1. Pinjam Buku Dari Perpustakaan
        2. Kembalikan Buku ke Perpustakaan
        3. Kembali Ke Menu Awal    
        
        Pilih Menu yang ingin anda jalankan (1-3): ''')

        if updatebuku1 == '1':
            pinjambuku()
        elif updatebuku1 == '2':
            kembalibuku()
        elif updatebuku1 == '3':
            break

# Update peminjaman buku
def pinjambuku() :
    daftarbukuall()
    print('\n\tPASTIKAN KODE BUKU YANG ANDA MASUKAN TERSEDIA!!!')
    kodebukupinjam = input('\n\tMasukan Kode Buku Yang Akan Anda Pinjam: ').upper()
    for i in range(len(Buku)):
        if(kodebukupinjam == Buku[i]['Kode Buku']):
            print('\nKode Buku\t| Judul Buku \t\t| Tahun Terbit\t| Penulis \t| Ketersediaan \t| Waktu Pinjam \t| Tanggal Pinjam \t| Tanggal Kembali |\t' )
            print('{}\t\t| {} \t\t| {}\t\t| {}\t| {}\t| {}\t| {}\t\t| {}\t  |'.format(Buku[i]['Kode Buku'],Buku[i]['Judul Buku'],Buku[i]['Tahun Terbit'],Buku[i]['Penulis'],Buku[i]['Ketersediaan'],Buku[i]['Waktu Pinjam'],Buku[i]['Tanggal Pinjam'],Buku[i]['Tanggal Kembali']))
            bukutersedia = input('\n\tApakah Buku Tersedia?(YA/TIDAK) : ').upper()
            if bukutersedia == 'YA' :
                waktupinjam = int(input('\n\tBerapa Lama Akan Meminjam Buku?(hari): '))
                Buku[i]['Ketersediaan'] = 'Dipinjam'
                Buku[i]['Waktu Pinjam'] = ('{} hari'.format(waktupinjam))
                Buku[i]['Tanggal Pinjam'] = ('{}'.format(now_date))
                Buku[i]['Tanggal Kembali'] = now_date + timedelta(days=waktupinjam)
                print('\n\tTerima Kasih Telah Melakukan Peminjaman Buku')
                break
            elif bukutersedia =='TIDAK' :
                print('\n\tMaaf Buku Telah Dipinjam, Silahkan Menunggu Atau Meminjam Buku Yang Lain\n')
                break
            else:
                print('\n\t======Anda Salah Memasukan Input======\n')
                break
    else:
        print('\n\t======Buku Tidak Tersedia======')

# Update kembalikan Buku            
def kembalibuku():
    daftarbukuall()
    print('\n\tPASTIKAN KODE BUKU YANG ANDA MASUKAN TERSEDIA DENGAN KETERSEDIAAN DIPINJAM!!!')
    kodebukukembali = input('\n\tMasukan Kode Buku Yang Akan Anda Kembalikan: ').upper()
    for i in range(len(Buku)):
        if(kodebukukembali == Buku[i]['Kode Buku']):
            kembalikanbuku = input('\n\tApakah Anda Yakin Untuk Mengembalikan Buku?(YA/TIDAK): ').upper()
            if kembalikanbuku == 'YA':
                Buku[i]['Ketersediaan'] = 'Tersedia'
                Buku[i]['Waktu Pinjam'] = '-------'
                Buku[i]['Tanggal Pinjam'] = '----------'
                Buku[i]['Tanggal Kembali'] = '----------'
                print('\n\tTerima Kasih Telah Mengembalikan Buku Yang Anda Pinjam')
                break
            elif kembalikanbuku == 'TIDAK':
                print('\n\tAnda Tidak Jadi Mengembalikan Buku, Terima Kasih')
                break
            else:
                print('\n\t======Anda Salah Memasukan Input======\n')
                break
    else:
        print('\n\t======Buku Tidak Tersedia======')

# Sub Menu Delete Buku (Delete)
def hapusBuku():
    while True:
        hapusbuku1 = input('''
        ==========================================
        1. Hapus Buku dari List Perpustakaan
        2. Kembali Ke Menu Awal    
        
        Pilih Menu yang ingin anda jalankan (1-2): ''')

        if hapusbuku1 == '1':
            menghapusbuku()
        elif hapusbuku1 == '2':
            break

# Menhapus Buku Dari Perpustakaan        
def menghapusbuku():
    daftarbukuall()
    print('\n\tPASTIKAN KODE BUKU YANG ANDA INGIN HAPUS TERSEDIA!!!')
    newkodehapus = input('\n\tMasukan Kode Buku (format 3 huruf dan 3 angka): ').upper()
    for i in range(len(Buku)) :
        if(newkodehapus == Buku[i]['Kode Buku']) :
            kodehapus = input('\n\tApakah Anda Yakin Untuk Menghapus Buku dari Perpustakaan?(YA/TIDAK): ').upper()
            if kodehapus == 'YA':
                del Buku[i]
                print('\n\tBuku Telah Dihapus Dari List Perpustakaan')
                break
            elif kodehapus == 'TIDAK':
                print('\n\tAnda Tidak Jadi Menghapus Buku Dari List Perputakaan')
                break
            else:
                print('\n\t======Anda Salah Memasukan Input======\n')
                break
    else:
        print('\n\t======Kode Buku Tidak Tersedia======')
    
    daftarbukuall()
    

while True:
    pilihMenu = input('''
    \t===============================================
    \t++++++Selamat Datang Di Perpustakaan JCDS++++++
    \t===============================================


    \tPilihan Menu Tersedia:

    \t1. Tampilkan List Buku Perpustakaan
    \t2. Tambah Buku Ke Perpustakaan
    \t3. Peminjaman dan Pengembalian Buku
    \t4. Hapus Buku dari Perpustakaan
    \t5. Keluar Dari Perpustakaan JCDS
    
    
    \tSilahkan Pilih Menu Yang Tersedia (1-5): ''')

    if pilihMenu == '1' :
        daftarbuku()
    elif pilihMenu == '2' :
        tambahBuku()
    elif pilihMenu == '3' :
        updateBuku()
    elif pilihMenu == '4' :
        hapusBuku()
    elif pilihMenu == '5' :
        print('\n========Terima Kasih Telah Mengunjungi Perpustakaan JCDS========\n')
        break
    else:
        print('\n Pilihan yang anda masukan salah, silahkan masukan kembali pilihan yang benar')