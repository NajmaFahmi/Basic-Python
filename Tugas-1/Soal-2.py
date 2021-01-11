import math

jari2 = int(input('Jari-jari lingkaran (cm): '))
luas_lingkaran = (math.pi)*(jari2**2)
luas_lingkaran = "{:.2f}".format(luas_lingkaran)

display = print(f'Luas lingkaran dengan jari-jari {jari2} cm adalah {luas_lingkaran} cm\u00b2.')
display