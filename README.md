# Simulação e Análise de Multiplicidade em Reator CSTR (ENG07042)

Este repositório contém a solução para o **Exercício Computacional 2** da disciplina de **Modelagem e Controle de Processos Industriais (ENG07042)**.

O projeto consiste na simulação computacional de um Reator Tanque Agitado Contínuo (CSTR) não-adiabático, focado na análise de não-linearidades e multiplicidade de estados estacionários.

## 📋 Objetivos

1.  **Diagrama de Bifurcação:** Mapear a variação da concentração estacionária ($C_{A,ss}$) em função da temperatura da camisa ($T_j$), identificando regiões de histerese e multiplicidade de soluções.
2.  **Análise de Plano de Fase:** Para uma temperatura crítica ($T_j$) onde coexistem 3 estados estacionários, simular o comportamento dinâmico e visualizar as bacias de atração e a estabilidade dos pontos de equilíbrio.

## ⚙️ Parâmetros do Sistema

Os parâmetros utilizados nesta simulação são específicos para este caso de estudo:

| Parâmetro | Descrição | Valor | Unidade |
| :--- | :--- | :--- | :--- |
| **F** | Vazão de alimentação | 1.1 | $m^3/h$ |
| **Tf** | Temperatura de alimentação | 315.0 | $K$ |
| **V** | Volume do reator | 1.0 | $m^3$ |
| **Caf** | Concentração de entrada | 10.0 | $kmol/m^3$ |

> **Nota:** Devido à alta temperatura de alimentação ($T_f = 315 K$), a região de multiplicidade ocorre em temperaturas de camisa ($T_j$) significativamente mais baixas (aprox. 240 K).

## 🚀 Estrutura do Código

O projeto é dividido em módulos para organizar as Equações Diferenciais Ordinárias (EDOs) e as equações algébricas:

* `main.ipynb` (ou `.py`): Script principal que executa a varredura de bifurcação e a integração dinâmica.
* `cstr_dyn.py`: Contém o modelo dinâmico do CSTR (EDOs) usado pelo `odeint`.
* `cstr_dyn_ss.py`: Contém o modelo estacionário (Algébrico) usado pelo `scipy.optimize.root`.

## 📊 Metodologia Numérica

### Tarefa 1: Bifurcação
Utilizou-se o método `scipy.optimize.root` (algoritmo híbrido de Powell) com uma grade de estimativas iniciais (Grid Search) para garantir a convergência para todas as raízes possíveis.
* **Filtro de Resíduos:** Foi implementada uma verificação pós-cálculo para descartar "falsos positivos" numéricos, aceitando apenas soluções com erro residual $< 10^{-5}$.
* **Range de $T_j$:** 200 K a 340 K.

### Tarefa 2: Plano de Fase
O script identifica automaticamente o $T_j$ central da região de multiplicidade.
* **$T_j$ Crítico Encontrado:** $240.80 \, K$
* **Pontos de Equilíbrio Detectados:**
    1.  Estado de alta conversão (Estável): $C_A \approx 2.24$, $T \approx 371.7 K$
    2.  Estado intermediário (Instável/Sela): $C_A \approx 5.60$, $T \approx 340.2 K$
    3.  Estado de baixa conversão (Estável): $C_A \approx 8.60$, $T \approx 312.1 K$

A estabilidade é visualizada através da integração de 400 trajetórias distintas no espaço de estados.

## 🛠️ Requisitos

* Python 3.x
* Numpy
* Scipy
* Matplotlib
