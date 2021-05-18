pembatas = ("=") * 20

def cek_konvergen(x_now, x_past, konvergen=False):
    print('\nPengecekan Konvergen dimulai..')
    # Mencari nilai error absolut    
    print('\nPengecekan Error Absolut')
    error_absolut = x_now - x_past
    if error_absolut < 0:
        error_absolut = -error_absolut
    print("|{:.4f} - {:.4f}| : {:.4f}".format(x_now, x_past, error_absolut))
    # Mencari nilai error relatif
    print('Pengecekan Error Relatif')
    error_relatif = (x_now - x_past) / x_now
    if error_relatif < 0:
        error_relatif = -error_relatif
    print("|({:.4f} - {:.4f}) / {:.4f}| = {:.4f}".format(x_now, x_past, x_now, error_relatif))
    # Menampilkan nilai error absolut dan nilai error relatif
    print("\nBerdasarkan hitungan tersebut didapat:\n\
        - Error absolut : {:.4f}\n\
        - Error relatif : {:.4f}\n\
        {}".format(error_absolut, error_relatif, pembatas*2))
    # Menentukan apakah konvergen berdasarkan error absolut
    if error_absolut < pow(10, -4):
        konvergen = True
        print('\tSudah konvergen berdasarkan error absolut')
    # Menentukan apakah konvergen berdasarkan error relatif
    if error_relatif < pow(10, -5):
        konvergen = True
        print('\tSudah konvergen berdasarkan error relatif')
    else:
        print('\tTidak terjadi Konvergen')
    # Menghentikan program
    if konvergen:
        quit(0)

count = 0
def newton_raphson(x):
    global count
    count+=1
    ## Menghitung nilai f(x) dan f'(x)
    print("==== Menghitung nilai f(x) dan f'(x) dari x ====")
    ## f(x) = x^3 +  4x^2 - 10 
    f_x_awal = pow(x, 3) + 4*pow(x, 2) - 10
    ## f'(x) = 3x^2 + 8x
    f_x_awal_aksen = 3 * pow(x, 2) + (8 * x)
    print('====================== ', f_x_awal_aksen)
    ## Menampilkan f(x) dan f'(x)
    print("f({:.4f}) = {:.4f}^3 + 4({:.4f})^2 - 10 = {:.4f}".format(x, x, x, f_x_awal))
    print("f'({:.4f}) = 3({:.4f})^2 + 8({:.4f})= {:.4f}".format(x, x, x, f_x_awal_aksen))
    ## Menghitung x selanjutnya dengan rumus x saat ini
    print("==== Menghitung x selanjutnya dengan rumus x saat ini ====")
    x_selanjutnya = x - (f_x_awal / f_x_awal_aksen)
    print("x({}) = {:.4f} - ({:.4f} / {:.4f}) = {:.4f}".format(count, x, f_x_awal, f_x_awal_aksen, x_selanjutnya))

    cek_konvergen(x_selanjutnya, x)
    return x_selanjutnya

########## AWAL PROGRAM ########## 
x = 1
i = 0


print('mengambil sembarang nilai sebagai titik awal, misal x0 = ', x)
while True:
    i += 1
    print('\n{} Newton Raphson ke-{} {}'.format(pembatas, i, pembatas))
    print('nilai x: {:.4f}'.format(x))
    x = newton_raphson(x)
    

