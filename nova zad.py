def pokaji_smetka(info):
    print('Sobstvenik: ',info['ime'])
    print('Balans: ',info['balans'],'eur')

def vnesi_pari(info,suma):
    info['balans']+= suma
    print('Uspeshno vneseni pari!')

def tegli_pari(info,suma):
    if suma <=info['balans']:
        info['balans']-= suma
        print('Uspeshno iztegli pari!')
    else:
        print('Nedostatuchna nalichnost!')


info = {
    'ime':'Denis',
    'balans':7000000,
}

pokaji_smetka(info)

vnos = float(input('Kolko pari iskash da vnesesh? : '))
vnesi_pari(info,vnos)

teglene = float(input('Kolko pari iskash da izteglish? : '))
tegli_pari(info,teglene)

pokaji_smetka(info)

