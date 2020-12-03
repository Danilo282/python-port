segundos = int(input("Segundos: "))
segundos_duracao = int(input('Segundos de duração: '))

dias = segundos // 86400
segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

dias1 = segundos_duracao // 86400
segundos_rest1 = segundos_duracao % 86400
horas1 = segundos_rest1 // 3600
segundos_rest1 = segundos_rest1 % 3600
minutos1 = segundos_rest1 // 60
segundos_rest1 = segundos_rest1 % 60

total_duracao = segundos_duracao - segundos
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")
print(dias1,"dias,",horas1,"horas,",minutos1,"minutos e",segundos_rest1,"segundos.")
print('A nova duracao será de: {}' .format(total_duracao))
