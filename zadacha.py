def dobavi(produkt):
    ime = input('Vuvedi ime na nov product: ')
    cena = float(input('Vuvedi cena nov product: '))
    produkt[ime] = cena

def pokaji(produkt):
    for ime,cena in produkt.items():
        print(ime,'-',cena,'eur')

def nai_skup_product(produkt):
   return max(produkt.values())

produkt = {
    'hlqb':1.20,
    'kola':1.50,
    'meso':6.70,
    'sirence':2.30,
}

dobavi(produkt)
pokaji(produkt)
nai_skup_product(produkt)

print('Nai visokata cena na product v magazina e: ',nai_skup_product(produkt), 'eur')


