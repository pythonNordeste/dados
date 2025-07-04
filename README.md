# Dados da Python Nordeste

**Pessoas > Tecnologia**

Repositório de dados das edições da Python Nordeste.

## Datasets

| Arquivo | Ano | Descrição | Formato |
|-|-|-|-|
| [2019/inscritos.csv](./data/2019/inscritos.csv) | 2019 | Pessoas inscritas na PyNE 2019 | `csv` |
| [2024/inscritos.csv](./data/2024/inscritos.csv) | 2024 | Pessoas inscritas na PyNE 2024 | `csv` |
| [2025/inscritos.csv](./data/2025/inscritos.csv) | 2025 | Pessoas inscritas na PyNE 2025 | `csv` |

## Veja também

- [Dados da Python Brasil](https://github.com/pythonbrasil/dados)
- [Projeto Dados Abertos da Python Brasil](https://github.com/pybropendata/pythonbrasil-opendata)

## Adicionando novos dados

### Limpando os dados

Caso o evento use a plataforma da Even3, já existe um script em `scripts/even3-excel-to-csv.py` que lê o arquivo bruto de credenciamento da Even3 e gera um CSV sem colunas de dados sensíveis e com células vazias preenchidas com o texto `Não respondeu`.

```shell
scripts/even3-excel-to-csv.py "Python Nordeste 2019.xlsx"
```

```
Reading the file Python Nordeste 2019.xlsx...
Removing columns ID, Nome, Nome Crachá, E-mail, CPF, CEP, Número, Número de Inscrição, Telefone Primário, Telefone Secundário, Endereço, Comprovante de Meia-entrada...
Filling empty cells...
Saving data to Python Nordeste 2019.csv...
```

Após limpar os dados, você pode mover o csv gerado para a pasta `data/{ano do evento}/inscritos.csv`.