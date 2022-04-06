from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1('Details', className = 'text-center'),
            className = 'mb-5 mt-5')
        ]),
        dbc.Row([
            dbc.Col(html.H5(children = 'Data was taken from the Carbon Montior website. Their Google Docs illuminates their methods in acquiring their data.'
            + ' Any insights I derive are from the data. Positive effects of the decrease of CO2 can be researched from other sources.'),
            className = 'mb-4')
        ]),
        dbc.Row([
            dbc.Col(html.H5(children = 'One Metic ton (Mt) is equal to 1000 kilograms (2205 lbs)'),
            className = 'mb-4')
        ]),
        dbc.Row([
            dbc.Col(html.H5(children = 'In 2019, China emitted 9536.28 Mt CO2. In 2020, 9465.55 was produced. This is a %0.74 decrease. In the graphs, a decrease in emissions can be seen '
            + ' due to a lockdown period from the 25th of January to the 3rd of March.' + ' Afterwards, the levels of emissions return to their normal levels in every sector except Domestic Aviation.'))
        ])
    ])
])

if __name__ == '__main__':
    print('Inisghts layout.')