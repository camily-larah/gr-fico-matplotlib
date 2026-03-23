import matplotlib.pyplot as plt
meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho']
vendas = [200, 300, 340, 305, 360, 400]
plt.plot(meses, vendas)
plt.title('Vendas no primeiro semestre')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.savefig("grafico_barras.png")
