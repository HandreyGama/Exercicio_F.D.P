PI = 3.14

ExercicioSelecionado = input('''Digite o numero do exercicio que deseja selecionar:\n
    1.Pi para radianos\n
    2.Area do trapezio\n
    3.Comprimento do arco da circunferencia\n
    4.Distancia entre dois pontos\n:''')

match(ExercicioSelecionado):
    case '1':
        grau = int(input('Digite o número em graus para converte-lo para radiano:'))
        rad = (grau*PI)/180
        print(f'O valor em radiano do grau digitado é:{rad}')
    case '2':
        b1 = int(input('Digite a base menor do trapezio:'))
        b2 = int(input('Digite a base maior do trapezio:'))
        altura = int(input('Digite a altura do trapezio:'))
        area = (b1 + b2)*altura/2
        print(f'A area do trapezio é:{area}')
    case '3':
        raio = int(input('Digite o raio da circunferencia:'))
        angulo = int(input('Digite o angulo em graus da circunferencia:'))
        comprimento = PI*angulo*raio/180
        print(f'O valor do comprimento do arco da circunferencia é:{comprimento}')
    case '4':
        x1 = int(input('Digite o x do primeiro ponto:'))
        y1 = int(input('Digite o y do primeiro ponto:'))
        x2 = int(input('Digite o x do segundo ponto:'))
        y2 = int(input('Digite o y do segundo ponto:'))
        distancia = ((x1 - x2)**2 + (y1 - y2)**2)**1/2
        print(f'A distancia entre os pontos é:{distancia}')

