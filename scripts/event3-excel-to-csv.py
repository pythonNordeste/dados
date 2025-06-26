import re

from pathlib import Path
from pandas import read_excel, DataFrame
from typer import Typer
from rich.console import Console


EMPTY_CELL_TEXT = 'Não respondeu'
COLUMNS_TO_REMOVE = [
    r'^id',
    r'^nome.*',
    r'^e.mail',
    r'^cpf',
    r'^cep',
    r'^n.mero.*',
    r'^telefone.*',
    r'^endere.o',
    r'^comprovante.*',
    r'^minibio',
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
    excel_content = read_excel(excel)
    
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