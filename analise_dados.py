import pandas as pd
import matplotlib.pyplot as plt

# Lendo e limpando os dados
df = pd.read_csv("dados_atitudy.csv", encoding="utf-8")
df.columns = [col.strip() for col in df.columns]
df = df.rename(columns={
    'Nome completo': 'Nome',
    'Idade': 'Idade',
    'Gênero': 'Genero',
    'E-mail': 'Email',
    'Avaliação física realizada?': 'AvaliacaoFisica',
    'Qual seu principal objetivo com os treinos?': 'Objetivo',
    'Qual seu plano atual?': 'Plano',
    'Data de início do plano:': 'InicioPlano',
    'Frequência semanal estimada (vezes por semana)': 'FrequenciaSemanal',
    'Em qual turno você costuma treinar?': 'Turno',
    'Quais aulas coletivas você costuma frequentar?': 'AulasColetivas',
    'Você gostaria de receber uma sugestão de treino orientado com base nas suas respostas?': 'DesejaSugestao',
    'Que tipo de treino você costuma fazer por conta própria?': 'TreinoProprio',
    'Status de envio': 'StatusEnvio'
})
df = df.dropna(subset=['Nome', 'Email'])
df['Idade'] = df['Idade'].astype(int)
df['InicioPlano'] = pd.to_datetime(df['InicioPlano'], errors='coerce')
df['FrequenciaSemanal'] = pd.to_numeric(df['FrequenciaSemanal'], errors='coerce')

# Gráfico 1: Pizza dos Objetivos
objetivos = df['Objetivo'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(objetivos, labels=objetivos.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição dos Objetivos dos Alunos')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Gráfico 2: Histograma de Idade
plt.figure(figsize=(8, 5))
plt.hist(df['Idade'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribuição das Idades dos Alunos')
plt.xlabel('Idade')
plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Gráfico 3: Barras horizontais para Planos
planos = df['Plano'].value_counts()
plt.figure(figsize=(8, 5))
plt.barh(planos.index, planos.values, color='lightgreen')
plt.title('Distribuição dos Tipos de Plano')
plt.xlabel('Quantidade')
plt.ylabel('Plano')
plt.tight_layout()
plt.show()

# Gráfico 4: Frequência média por turno com simulação
turno_freq = df.groupby('Turno')['FrequenciaSemanal'].mean()
simulado = turno_freq.copy()
simulado[['Tarde (12h às 17h)', 'Noite (17h às 22h)']] *= 0.6

plt.figure(figsize=(8, 6))
x = range(len(turno_freq))
plt.bar(x, turno_freq, width=0.4, label='Original', align='center')
plt.bar([i + 0.4 for i in x], simulado, width=0.4, label='Com falha no ar', align='center')
plt.xticks([i + 0.2 for i in x], turno_freq.index, rotation=30)
plt.title('Frequência Média Semanal por Turno\nImpacto da Falha no Ar-condicionado')
plt.ylabel('Frequência Semanal Média')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
