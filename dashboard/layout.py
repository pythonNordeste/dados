import dash_bootstrap_components as dbc
import plotly.express as px

from dash import html
from dash.dcc import Graph
from pandas import DataFrame

from dashboard.assets import datasets, years


def ChartCard(title: str, chart: Graph) -> dbc.Card:
    return dbc.Card(
        [
            dbc.CardHeader(title),
            dbc.CardBody([chart])
        ],
        class_name="mb-4"
    )


def DataFrameCharts(year: str, df: DataFrame) -> list[dbc.Card]:
    cards = []

    for column in df.columns:
        if 'hora' in column.lower() or 'data' in column.lower():
            continue

        graph_df = df[column].value_counts().reset_index()
        graph_df.columns = [column, 'Contagem']

        cards.append(
            ChartCard(
                title=f'{year} / {column}',
                chart=Graph(
                    figure=px.bar(graph_df, x=column, y='Contagem'),
                    id=f'{year}-{column.replace(" ", "-")}'
                )
            ) 
        )
    
    return cards


def AllCharts() -> dict[str, list[Graph]]:
    content = {}

    for year, df in datasets():
        if year not in content:
            content[year] = [
                dbc.Button(
                    'Abrir CSV',
                    color='primary',
                    href=f'https://github.com/pythonNordeste/dados/tree/main/data/{year}/inscritos.csv',
                    className='mb-3',
                    external_link=True
                ),
            ]

        content[year].extend(DataFrameCharts(year, df))
        
    return content


def Navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(year, href=f"/{year}"))
            for year in years()
        ],
        brand="Python Nordeste",
        brand_href="/",
        color="dark",
        dark=True,
    )
