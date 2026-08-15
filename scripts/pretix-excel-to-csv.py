import re

from pathlib import Path
from pandas import read_excel, DataFrame
from typer import Typer
from rich.console import Console


EMPTY_CELL_TEXT = 'Não respondeu'
SHEET_NAME = 'Posição dos pedidos'
COLUMNS_TO_REMOVE = [
    r'.*do.evento',
    r'.*do.pedido',
    r'.*id\s.*',
    r'status',
    r'email',
    r'.*telefone.*',
    r'varia.*o',
    r'taxa.*',
    r'regra.*',
    r'valor.*',
    r'nome.do.*',
    r'zona.do.*',
    r'fileira.do.*',
    r'n.mero.do.*',
    r'empresa.*',
    r'endere.o',
    r'c.digo.*',
    r'voucher.*',
    r'segredo.*',
    r'bloqueado',
    r'v.lido.*',
    r'coment.rio.*',
    r'.*fatura.*',
    r'.*acompanhamento',
    r'.*vendas',
    r'.*check-in',
    r'.*link.*',
]


cli = Typer()
console = Console()


def get_columns_to_remove(excel_content: DataFrame):
    for column_to_remove in COLUMNS_TO_REMOVE:
        for column_name in excel_content.columns:
            if re.match(column_to_remove, column_name, re.IGNORECASE):
                yield column_name


@cli.command()
def convert(excel: Path):
    # Reading the Excel file
    console.print(f'Reading the file [bold]{excel}[/bold]...')
    excel_content = read_excel(excel, sheet_name=SHEET_NAME)
    
    # Removing columns with sensive data
    columns_to_remove = list(get_columns_to_remove(excel_content))
    console.print(f'Removing columns [bold]{", ".join(columns_to_remove)}[/bold]...')
    excel_content.drop(columns=columns_to_remove, inplace=True)

    # Filling empty cells with a default text
    console.print(f'Filling empty cells...')
    excel_content.fillna(EMPTY_CELL_TEXT, inplace=True)

    # Writting the output CSV file
    output_path = excel.with_suffix('.csv')
    console.print(f'Saving data to [bold]{output_path}[/bold]...')
    excel_content.to_csv(output_path, index=False)


if __name__ == '__main__':
    cli()