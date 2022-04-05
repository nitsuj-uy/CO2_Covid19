from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1('Insights', className = 'text-center'),
            className = 'mb-5 mt-5')
        ]),
        dbc.Row([
            dbc.Col(html.H5(children = 'details of the insights, lock down periods, numbers numbers nubmers'),
             className = 'mb-4')
        ])
    ])
])

if __name__ == '__main__':
    print('Inisghts layout.')