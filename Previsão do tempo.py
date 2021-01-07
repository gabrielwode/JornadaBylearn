horario = 'manhã'
clima = 'ensolarado'
temperatura = 'quente'

if horario == 'manhã' or horario == 'tarde':
  if clima == 'ensolarado' and temperatura == 'quente':
    print('uma piscina cairia bem')

  if (clima == 'ensolarado' or clima == 'nublado') and (temperatura == 'amena' or temperatura == 'frio'):
    print('Seria legal praticar algum esporte')
  
  if clima == 'chuvoso':
    print('Aproveite para treinar seu Python')
else:
  if clima == 'chuvoso':
    print('Que tal um filme, série ou jogatina?')
  else:
    print('Um jantar fora parece interessante...')