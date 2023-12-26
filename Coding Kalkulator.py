print('=======================')
print(' Kalkulator Sederhana')
print('Muhammad Sandi Zakariya')
print('=======================')

num_1 = int(input('Masukkan angka pertama : '))
option = input('Pilih opsi (+, -, *, /): ')
num_2 = int(input('Masukkan angka kedua   : '))

opsi_plus = num_1 + num_2
opsi_min = num_1 - num_2
opsi_kali = num_1 * num_2
opsi_bagi = num_1 / num_2
print('--------------------------')

if option == '+':
    print('Hasilnya adalah : ' + str(opsi_plus))
elif option == '_':
    print('Hasilnya adalah : ' + str(opsi_min))
elif option == '*':
    print('Hasilnya adalah : ' + str(opsi_kali))
elif option == '/':
    print('Hasilnya adalah : ' + str(opsi_bagi))
    print('dan jika dibulatkan, menjadi : ' + str(round(opsi_bagi)))
print('--------------------------')