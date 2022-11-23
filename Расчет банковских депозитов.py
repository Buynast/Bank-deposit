money = int(input('Введите сумму, которую хотите положить под депозит:'))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

procent = list(per_cent.values())

deposit = [(money*procent[0]/100), (money*procent[1]/100), (money*procent[2]/100), (money*procent[3])/100]

deposit_i = max(deposit)

print('Максимальная сумма, которую вы можете заработать:', deposit_i)


