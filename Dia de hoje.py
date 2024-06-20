import time

hora_atual = time.localtime()

def dia_semana(num):
	if num == 0: return 'Segunda-feira'
	if num == 1: return 'Terça-feira'
	if num == 2: return 'Quarta-feira'
	if num == 3: return 'Quinta-feira'
	if num == 4: return 'Sexta-feira'
	if num == 5: return 'Sábado'
	if num == 6: return 'Domingo'

dia = hora_atual.tm_mday
mes = hora_atual.tm_mon
ano = hora_atual.tm_year
dia_da_semana = dia_semana(hora_atual.tm_wday)

print(f'Dia: {dia:02}/{mes:02}/{ano} - {dia_da_semana}')
input('\nAperte ENTER para sair...')
'''
print(time.localtime()) -> Para imprimir a estrutura completa de localtime

Dados da estrutura:

tm_year: ano, ex. 2023
tm_mon: mês, de 1 a 12
tm_mday: dia do mês, de 1 a 31
tm_hour: hora, de 0 a 23
tm_min: minuto, de 0 a 59
tm_sec: segundo, de 0 a 61 (60 ou 61 são valores para segundos bissextos)
tm_wday: dia da semana, de 0 (segunda-feira) a 6 (domingo)
tm_yday: dia do ano, de 1 a 366
tm_isdst: flag de horário de verão, 1 se o horário de verão está em vigor, 0 se não está, e -1 se a informação não está disponível
'''