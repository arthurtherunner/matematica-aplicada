"""
nossa função Afim = C(x) = 15x + 50

x = quantidade de gb de espaço utilizado
C(x) = custo total da hospedagem
"""

import matplotlib.pyplot as plt
 
def custo_hospedagem(x):
    return 15 * x + 50
 
# tabela de valores
gb_utilizados = [0, 5, 10, 20, 30, 50]
custos = [custo_hospedagem(x) for x in gb_utilizados]
 
print("GB utilizados | Custo Total (R$)")
for x, c in zip(gb_utilizados, custos):
    print(f"{x:>13} | {c:>16.2f}")
 
# -gráfico da nossa função
plt.figure(figsize=(7, 5))
plt.plot(gb_utilizados, custos, marker='o', color='#1C7293', linewidth=2)
plt.title("Custo Total x GB Utilizados no Site")
plt.xlabel("Espaço utilizado (GB)")
plt.ylabel("Custo total C(x) em R$")
plt.grid(True, linestyle='--', alpha=0.5)
 
# simulação
entrada = float(input("\nDigite a quantidade de GB utilizados: "))
resultado = custo_hospedagem(entrada)
print(f"Custo total para {entrada} GB: R$ {resultado:.2f}")
 
#  ponto digitado pelo usuário no gráfico
plt.scatter(entrada, resultado, color='red', s=100, zorder=5,
            label=f"Seu valor: {entrada} GB → R$ {resultado:.2f}")
plt.legend()
 
plt.tight_layout()
plt.savefig("grafico_hospedagem.png", dpi=150)
plt.show()