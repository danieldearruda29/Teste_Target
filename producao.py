#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado
# teve dentro do valor total mensal da distribuidora.  

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros
percentual = 0

estado_desejado = input("Digite o Estado que deseja analisar: ")

if estado_desejado in 'spSPSp':
    percentual = (sp/total) * 100
elif estado_desejado in 'mgMgMG':
    percentual = (mg/total) * 100
elif estado_desejado in 'rjRJRj':
    percentual = (rj/total) * 100
elif estado_desejado in 'esESEs':
    percentual = (es/total) * 100
elif estado_desejado in 'outrosOutros':
    percentual = (outros/total) * 100

print(f'{percentual:.2f}%')