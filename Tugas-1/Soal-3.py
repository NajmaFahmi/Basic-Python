nilai_teori = float(input('Nilai Ujian Teori: '))
nilai_praktek = float(input('Nilai Ujian Praktek: '))

if (nilai_teori>= 70) & (nilai_praktek >= 70):
    print('Selamat, anda lulus!')
elif (nilai_teori >= 70) & (nilai_praktek < 70):
    print('Anda harus mengulang ujian praktek.')
elif (nilai_teori < 70) & (nilai_praktek >= 70):
    print('Anda harus mengulang ujian teori.')
else:
    print('Anda harus mengulang ujian teori dan praktek.')