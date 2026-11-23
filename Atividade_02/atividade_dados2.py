from sklearn.datasets import load_iris
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)
df_iris = iris.frame
df_iris["species"] = df_iris["target"].map(dict(enumerate(iris.target_names)))
df_iris = df_iris.drop(columns="target")

# Gráfico1 com melt para mostrar as 3 espécies, uma ao lado da outra no mesmo gráfico. As 4 variáveis.
medias = df_iris.groupby("species").mean()
melt = df_iris.melt(id_vars="species", var_name="medida", value_name="valor")
sns.barplot(data=melt, x="medida", y="valor", hue="species", errorbar=None)
plt.xticks(ticks=[0, 1, 2, 3], labels=["Comp. sépala", "Larg. sépala", "Comp. pétala", "Larg. pétala"])
plt.title("Média das variáveis de cada flor")
plt.xlabel("Variáveis")
plt.ylabel("Média (cm)")
plt.tight_layout()
plt.show()

# Gráfico Scatter para tentar observar uma relação
sns.scatterplot(data=df_iris, x='sepal length (cm)', y='petal length (cm)', hue='species')
sns.regplot(data=df_iris, x="sepal length (cm)", y="petal length (cm)", scatter=False, ci=None, color="black")
plt.title('Comparação do comprimento de sépalas e pétalas')
plt.legend(title='Espécies')
plt.xlabel('Comprimento da sépala')
plt.ylabel('Comprimento da pétala')
plt.tight_layout()
plt.show()