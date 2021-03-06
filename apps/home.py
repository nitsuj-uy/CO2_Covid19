#import dash
from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("COVID-19's Effect on CO2 Emissions Dashboard", className="text-center"), 
                    className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='The goal of this app is to demonstrate the effect of the Covid-19 pandemic on CO2 emissions in China.'), 
                    className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='The Graphs page showcases the difference in the amount of CO2 emitted in 2019 and 2020. '
                                     'There are a total of six graphs. Five of them are paritioned into a sector: Power, Ground Transporation, Industry, Residential, and Domestic Aviation.'), 
                    className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H6(children='The original data is from this site. The owners have displayed CO2 emissions from different countries.',
                                               className="text-center"),
                                       dbc.Button("Carbon Monitor",
                                                  href="https://carbonmonitor.org/",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True), 
                    width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H6(children='The owners have a google doc to describe how the data was gathered and other important details. ',
                                               className="text-center"),
                                       dbc.Button("Google Doc",
                                                  href="https://docs.google.com/document/d/1_q4QSUeSbwToR5ePTJnCxUzjsZFN-DbO/edit",
                                                  color="primary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True), 
                    width=4, className="mb-4"),
            
            dbc.Col(dbc.Card(children=[html.H6(children='Here are the graphs. Here are some analysis. ', 
                                                className = 'text-center'),
                                        dbc.Button('Graphs',
                                                   href = '/graphs',
                                                   color = 'primary',
                                                   className = 'mt-3'),
                                        dbc.Button('Inisights',
                                                   href = '/insight',
                                                   color = 'primary',
                                                   className = 'mt-3')
                                                   ],
                                                   
                                body = True, color = 'dark', outline = True),
                                
                                
                    width = 4, className = 'mb-4')

        ], className="mb-5"),

    ])

])