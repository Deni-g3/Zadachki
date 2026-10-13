kucheshka_hrana = 4
koteshka_hrana = 2.50

broi_kuche = int(input('Vuvedete kolichestvo kucheshka hrana:'))
broi_kotka = int(input('Vuvedete kolichestvo koteshka hrana: '))

cena_kuche = kucheshka_hrana * broi_kuche 
cena_kotka = koteshka_hrana * broi_kotka 
cena_obshto = cena_kotka + cena_kuche

print(f'Cena na kucheshka hrana:{cena_kuche}')
print(f'Cena na koteshka hrana{cena_kotka}')
print(f'Obshta cena za dvete hrani:{cena_obshto}')