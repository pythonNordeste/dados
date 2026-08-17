import re
import textwrap

from datetime import date
from pathlib import Path
from matplotlib import pyplot as plt
from pandas import read_csv, DataFrame
from typer import Typer
from rich.console import Console


COLUMNS_TO_EXPORT = [
    r'.*UF(\s?).*',
    r'.*python.*',
    r'.*identi.*',
    r'.*define.*',
    r'.*defici.ncia.*',
]

cli = Typer()
console = Console()


def get_columns_to_export(csv: DataFrame):
    for column_to_remove in COLUMNS_TO_EXPORT:
        for column_name in csv.columns:
            if re.match(column_to_remove, column_name, re.IGNORECASE):
                yield column_name


@cli.command()
def main(csv: Path, year: int):
    # Reading the CSV file
    console.print(f'Reading the file [bold]{csv}[/bold]...')
    csv_content = read_csv(csv)

    # Creating the export folder
    export_path = Path(f'graphs/{year}')
    export_path.mkdir(parents=True, exist_ok=True)

    # Get only the interesting columns to export
    columns_to_plot = list(get_columns_to_export(csv_content))
    console.print(f'Exporting the columns [bold]{", ".join(columns_to_plot)}[/bold]...')

    for column in columns_to_plot:
        file = export_path / f'{column.replace("?", "")}.png'
        console.print(f'Exporting [bold]{file}[/bold]...')

        # Counting the column values
        count = csv_content[column].value_counts()

        # Formatting the labels to fit in the graph
        labels = [
            textwrap.fill(str(label), width=13)
            for label in count.index
        ]

        plot = count.plot(
            kind='bar',
            xlabel='',
            figsize=(len(count) * 2, 9),
            fontsize=16,
            color="#0C23F7",
        )
        plot.set_title(
            label=column,
            pad=15,
            fontdict={
                'fontsize': 16,
                'fontweight': 'bold',
            }
        )
        plot.bar_label(
            plot.containers[0],
            labels=count,
            fontsize=16,
        )

        # Adding the formatted labels
        plot.set_xticklabels(labels)

        # Keep the x-axis labels horizontal
        plot.tick_params(
            axis='x',
            labelrotation=0
        )

        # Saving the graph to a file
        figure = plot.get_figure()
        figure.tight_layout()
        figure.savefig(file)
        plt.close(figure)


if __name__ == '__main__':
    cli()