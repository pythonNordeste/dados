from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc

from dashboard.layout import Navbar, AllCharts

charts = AllCharts()
dash = Dash(
    name=__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title='Estatísticas da Python Nordeste',
)

dash.layout = [
    dcc.Location(id='url', refresh=False),
    Navbar(),
    html.Div(id="page-content")
]

@dash.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render(pathname: str) -> html.Div:
    if pathname == "/":
        return html.Div(
            [dbc.Alert("Selecione um ano para ver as estatísticas.", color="success")],
            className="container my-4"
        )
    
    elif (year := pathname.removeprefix("/")) in charts:
        return html.Div(charts[year], className="container mt-4")
    
    else:
        return html.Div(
            [
                html.H1("404", className="text-danger"),
                html.P("Página não encontrada.")
            ],
            className="container my-5 text-center"
        )
