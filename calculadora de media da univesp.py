while True:

    materia = input('digite o nome da matéria que deseja saber a média ') 
    nota_at = float(input('digite a nota que tirou nas atividades semanais '))
    nota_prova = float(input('digite a nota que tirou na prova '))

    c = (nota_at * 0.40) + (nota_prova * 0.60)



    if c >= 5:
        print(f'sua média é: {c:.2f}, em {materia}. parabéns você atingiu a média!')
    else:
        print(f'sua média é: {c:.2f}, em {materia}. Infelizmente, você precisará fazer o exame!')
        if c < 5:
            e = float(input('digite a nota do exame'))
            d = ( c + e)/ 2
            if d >= 5:
                print(f'sua média final é: {d}. vc passou!')
            else:
                print(f'sua média final é: {d}. estude mais!')

        else:
            print('você está de exame.')
