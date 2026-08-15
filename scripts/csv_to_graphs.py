from pathlib import Path
from pandas import read_csv, DataFrame
from typer import Typer
from rich.console import Console


cli = Typer()
console = Console()

@cli.command()
def main(csv: Path):
    console.print(f'Reading the file [bold]{csv}[/bold]...')
    csv_content = read_csv(csv)

    for column in csv_content.columns:
        count = csv_content[column].value_counts()
        plot = count.plot(kind='bar', title=column)
        plot.get_figure().savefig(f'graphs/{column}.png')


if __name__ == '__main__':
    cli()