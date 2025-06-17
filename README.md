# 🏋️‍♀️ Projeto de Big Data — Atitudy Fitness

Este repositório contém o projeto de análise de dados realizado para a disciplina de Big Data, com foco nos dados coletados de alunos da academia **Atitudy Fitness**.

O objetivo principal foi entender o perfil dos alunos, seus hábitos de treino e simular cenários críticos baseados em dados reais e simulados.

---

## 📄 Arquivos do repositório

![Arquivos do projeto](tabela_arquivos_projeto.png)

---

## 🧠 Etapas do Projeto — Big Data na Atitudy Fitness

### 1️⃣ Coleta de Dados
- 📋 **Formulário aplicado** com 15 perguntas sobre:
  - Treinos  
  - Horários e frequência  
  - Planos contratados  
  - Aulas coletivas e objetivos  
- 📊 **Total de 107 respostas simuladas**, baseadas em um cenário realista da academia.

### 2️⃣ Tratamento e Preparação dos Dados
- 🧹 Remoção de campos vazios e dados inconsistentes  
- 🔄 Padronização de nomes de colunas e categorias  
- 🔢 Conversão de tipos: datas, idades e frequência semanal  
- ✅ Garantia de qualidade para análise estatística

### 3️⃣ Análise Exploratória dos Dados (EDA)
- 📈 Gênero, idade e turnos preferidos (manhã, tarde, noite)  
- 🎯 Objetivos de treino: emagrecimento, hipertrofia, condicionamento  
- 🗓️ Frequência semanal média  
- 🧘 Aulas coletivas mais frequentadas  
- 🏋️‍♀️ Tipos de treino realizados por conta própria  
- 📊 Gráficos de pizza, histograma e barras horizontais

### 4️⃣ Interpretação e Simulação de Cenários Críticos
Com base nos dados, foram simulados **impactos reais** em situações de falha operacional:

| Cenário | Critério adotado | Impacto estimado |
|---------|------------------|------------------|
| ❄️ Falha no ar-condicionado | Redução de 40 % na frequência em tarde/noite | −40 % frequência |
| 👨‍🏫 Ausência de professor | 30 % faltam, 10 % desistem das aulas | −30 % presença, −10 % adesão |
| ⚠️ Superlotação no pico | 20 % encurtam ou evitam o treino | −20 % duração/comparecimento |
| 🛠️ Quebra de aparelho popular | 20 % faltam, 5 % cancelam o plano | −20 % presença, −5 % churn |

---

## 💡 Conclusão
A análise permitiu identificar padrões importantes sobre o comportamento dos alunos e gargalos operacionais. As simulações mostraram como problemas técnicos simples podem impactar a retenção e a frequência, evidenciando a importância da manutenção preventiva e do conforto térmico.

---

## 👩‍💻 Desenvolvido por
**Isabela Gouveia** — Estudante de Análise e Desenvolvimento de Sistemas  
GitHub: [@euaisabela](https://github.com/euaisabela)
