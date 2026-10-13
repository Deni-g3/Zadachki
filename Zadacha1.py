broi = int(input('Vuvedi broi povtoreniq:'))
sbor = 0

for i in range (broi):
    chislo = int(input('Vuvedi chislo: '))
    sbor +=  chislo

print(f'Obshtiyat sbor e:{sbor}')