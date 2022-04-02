from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app 
from apps import home, graphs

dropdown = dbc.DropdownMenu(
    children = [
        dbc.DropdownMenuItem('Home', href = '/home'),
        dbc.DropdownMenuItem('Grahps', href = '/graphs')
    ],
    nav = True,
    in_navbar = True,
    label = 'Explore',
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand('COVID-19 and CO2 Emissions', className = 'ml-2'))
                    ],
                    align = 'center',

                ),
                href = '/home'
            ),
            dbc.NavbarToggler(id = 'navbar-toggler2'),

            dbc.Collapse(
                dbc.Nav(
                    children = [dropdown
                    ],
                    className = 'ml-auto',
                    navbar = True
                ),
                id = 'navbar-collapse2',
                navbar = True
            )
        ],
    ),
    color = 'dark',
    dark = True,
)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname)              :
    if pathname == '/graphs':
        return graphs.layout
    else:
        return home.layout

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    navbar,
    html.Div(id = 'page-content')
])

if __name__ == '__main__':
    app.run_server(debug = True)