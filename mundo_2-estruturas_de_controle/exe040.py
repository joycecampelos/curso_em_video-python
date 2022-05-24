'''
DESAFIO 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO
'''

primeiranota = float(input('Primeira nota: '))
segundanota = float(input('Segunda nota: '))
média = (primeiranota + segundanota) / 2

print(f'Tirando {primeiranota:.1f} e {segundanota:.1f}, a média do aluno é {média:.1f}.')

if média < 5:
    print('O aluno está REPROVADO.')
elif média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')
