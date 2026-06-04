# 📊 Análise Exploratória de Dados - Vendas

Projeto de análise exploratória de dados utilizando uma base real de vendas.

## 🚀 Objetivo
Explorar os dados para identificar:
- Produtos mais vendidos
- Produtos mais lucrativos
- Comportamento de vendas ao longo do tempo
- Padrões de clientes

## 🛠️ Tecnologias
- Python
- Pandas
- Matplotlib
- SQLite

## 📂 Estrutura
- `data/` → base de dados
- `src/` → código modularizado
- `dashboard/` → páginas de gráficos e resultados

## 📊 Principais análises
- Top produtos por quantidade
- Top produtos por lucro
- Vendas mensais
- Análise de clientes

## ▶️ Como rodar

```bash
# 1 crie um ambiente para dev python
python3 -m venv .venv
# 2 ative o ambiente virtual
source .venv/bin/activate
# 3 instale as dependências
pip install -r requirements.txt
# 4 crie o diretório /data na raiz no projeto
# 5 inclua o banco de dados com o nome banco_de_dados.db
# 6 rode o projeto
export PYTHONPATH=$PWD && streamlit run dashboard/home.py
