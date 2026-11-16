from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)
df_iris = iris.frame
df_iris["species"] = df_iris["target"].map(dict(enumerate(iris.target_names)))
df_iris = df_iris.drop(columns="target")


# Usei para ver dados inicialmente
#print(df_iris.groupby('species').agg(Comprimento_sep=('sepal length (cm)', 'mean'), largura_sep=('sepal width (cm)', 'mean'), Comprimento_pet=('petal length (cm)', 'mean'), Largura_pet=('petal width (cm)', 'mean')))
#print(df_iris.groupby('species')['sepal length (cm)'].mean())
#print(df_iris.groupby("species")[["sepal length (cm)", "petal length (cm)"]].agg(["min", "max", 'mean', 'median']))

# Ver a quantidade de flores por espécies
#print(df_iris.groupby('species')['species'].count())

# Gráfico de barras com a quantidade de flores
sns.countplot(data=df_iris, x="species")
plt.title("Flores por espécie")
plt.xlabel("Espécie")
plt.ylabel("Quantidade de flores")
plt.tight_layout()
plt.show()

# Ver os dados das medidas
#print(df_iris.groupby('species').agg(['min', 'max', 'mean']))

# Gráfico boxplot para para comparar as larguras
sns.boxplot(data=df_iris, y="petal width (cm)", x='species')
plt.title("Largura das pétalas")
plt.tight_layout()
plt.show()

# Gráfico boxplot para comparar os comprimentos
sns.boxplot(data=df_iris, y="petal length (cm)", x='species')
plt.title("Comprimento das pétalas")
plt.tight_layout()
plt.show()

# Gráfico Scatter para tentar observar uma relação
sns.scatterplot(data=df_iris, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Comparação do comprimento de sépalas e pétalas')
plt.xlabel('Comprimento da sépala')
plt.ylabel('Comprimento da pétala')
plt.tight_layout()
plt.show()

# Tabela com a correlação
numerico = df_iris.groupby('species')[['sepal length (cm)', 'petal length (cm)']]
correlacao = numerico.corr()
sns.heatmap(correlacao, annot=True, cmap='vlag', center=0, fmt=".2f")
plt.title('Comparação do comprimento de sépalas e pétalas')
plt.tight_layout()
plt.show()