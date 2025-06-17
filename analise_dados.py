import pandas as pd
import matplotlib.pyplot as plt

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


plt.figure(figsize=(6, 6))
df['Objetivo'].value_counts().plot.pie(
    autopct='%1.1f%%', startangle=90, ylabel='')
plt.title('Distribuição dos Objetivos dos Alunos')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df['Idade'], bins=10, edgecolor='black')
plt.title('Distribuição das Idades dos Alunos')
plt.xlabel('Idade'); plt.ylabel('Quantidade')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
df['Plano'].value_counts().plot.barh()
plt.title('Distribuição dos Tipos de Plano')
plt.xlabel('Quantidade'); plt.ylabel('Plano')
plt.tight_layout()
plt.show()

turno_freq = df.groupby('Turno')['FrequenciaSemanal'].mean()
sim_ar = turno_freq.copy()
sim_ar[['Tarde (12h às 17h)', 'Noite (17h às 22h)']] *= 0.6  # –40 %

plt.figure(figsize=(8, 6))
x = range(len(turno_freq))
plt.bar(x, turno_freq, width=0.35, label='Original')
plt.bar([i + 0.35 for i in x], sim_ar, width=0.35, label='Falha no ar')
plt.xticks([i + 0.175 for i in x], turno_freq.index, rotation=30)
plt.title('Frequência Semanal – Impacto Falha no Ar-condicionado')
plt.ylabel('Frequência Média'); plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


total_aula_col = df['AulasColetivas'].notnull().sum()
faltas_prof = int(total_aula_col * 0.30)
desist_prof = int(total_aula_col * 0.10)

print(f"⛔ Ausência de professor:\n"
      f"   • {faltas_prof} alunos faltariam no dia\n"
      f"   • {desist_prof} podem desistir das aulas coletivas\n")


plt.figure(figsize=(5, 4))
plt.bar(['Faltas', 'Desistências'],
        [faltas_prof, desist_prof])
plt.title('Impacto – Ausência de Professor')
plt.ylabel('Número de alunos')
plt.tight_layout()
plt.show()

turnos_count = df['Turno'].value_counts()
turno_pico = turnos_count.idxmax()
pico_original = turnos_count.max()
pico_sim = int(pico_original * 0.80)

print(f"⚠️ Superlotação no turno {turno_pico}: "
      f"{pico_original - pico_sim} alunos (20 %) impactados.\n")

plt.figure(figsize=(5, 4))
plt.bar(['Original', 'Com superlotação'],
        [pico_original, pico_sim])
plt.title(f'Impacto – Superlotação ({turno_pico})')
plt.ylabel('Alunos no turno pico')
plt.tight_layout()
plt.show()


mask_cardio = df['TreinoProprio'].str.contains(
    'cardio|esteira|musculação|leg press', case=False, na=False)
usuarios_aparelho = mask_cardio.sum()

faltas_app = int(usuarios_aparelho * 0.20)
cancel_app = int(usuarios_aparelho * 0.05)

print(f"💥 Quebra de aparelho popular:\n"
      f"   • {faltas_app} alunos faltariam\n"
      f"   • {cancel_app} poderiam cancelar o plano\n")

plt.figure(figsize=(5, 4))
plt.bar(['Faltas', 'Cancelamentos'],
        [faltas_app, cancel_app])
plt.title('Impacto – Quebra de Aparelho')
plt.ylabel('Número de alunos')
plt.tight_layout()
plt.show()
