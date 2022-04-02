import pandas as pd
from datetime import datetime

import dash
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(
    'Graphs',
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)

# -------------------------------------------------------------
# Import and clean data 

dat = pd.read_excel('carbon-monitor-maingraphdatas.xlsx')
dat.tail(10)
dat.drop(dat.index[46830:46835], inplace = True)

leap_index = dat.index[dat['date'] == '29/02/2020'].tolist()
dat_leap = dat.iloc[leap_index]

dat = dat.drop(dat.index[dat['date'] == '29/02/2020'].tolist()).reset_index(drop = True)

china = dat[dat['country / group of countries'] == 'China']
china['date'] = pd.to_datetime(china['date'], format = '%d/%m/%Y')


china_combined = china.groupby(['date']).sum().reset_index()
china_combined['date'] = china_combined['date'].astype(str)
china_combined['date'] = china_combined['date'].str[8:10] + '/' + china_combined['date'].str[5:7] + '/' +china_combined['date'].str[:4]

china_combined_2019 = china_combined[china_combined['date'].str.contains('2019')]
china_combined_2019 = china_combined_2019.reset_index(drop = True)
china_combined_2019['day_month'] = china_combined_2019['date'].str[:5] 

china_combined_2020 = china_combined[china_combined['date'].str.contains('2020')]
china_combined_2020 = china_combined_2020.reset_index(drop = True)
china_combined_2020['day_month'] = china_combined_2020['date'].str[:5] 

china['date'] = china['date'].astype(str)
china['date'] = china['date'].str[8:10] + '/' + china['date'].str[5:7] + '/' + china['date'].str[:4]

#Power 
china_2019 = china[china['date'].str.contains('2019')]
china_2019_power = china_2019[china_2019['sector'] == 'Power']
china_2019_power['day_month'] = china_2019_power['date'].str[:5]

#print(china_combined_2019)

china_2020 = china[china['date'].str.contains('2020')]
china_2020_power = china_2020[china_2020['sector'] == 'Power']
china_2020_power = china_2020_power.reset_index(drop = True)
china_2020_power['day_month'] = china_2020_power['date'].str[:5]

#Ground Transportation
china_2019_groundtrans = china_2019[china_2019['sector'] == 'Ground Transport']
china_2019_groundtrans = china_2019_groundtrans.reset_index(drop = True)
china_2019_groundtrans['day_month'] = china_2019_groundtrans['date'].str[:5]

china_2020_groundtrans = china_2020[china_2020['sector'] == 'Ground Transport']
china_2020_groundtrans = china_2020_groundtrans.reset_index(drop = True)
china_2020_groundtrans['day_month'] = china_2020_groundtrans['date'].str[:5]

#Industry
china_2019_industry = china_2019[china_2019['sector'] == 'Industry']
china_2019_industry = china_2019_industry.reset_index(drop = True)
china_2019_industry['day_month'] = china_2019_industry['date'].str[:5]

china_2020_industry = china_2020[china_2020['sector'] == 'Industry']
china_2020_industry = china_2020_industry.reset_index(drop = True)
china_2020_industry['day_month'] = china_2020_industry['date'].str[:5]

#Residential
china_2019_residential = china_2019[china_2019['sector'] == 'Residential']
china_2019_residential = china_2019_residential.reset_index(drop = True)
china_2019_residential['day_month'] = china_2019_residential['date'].str[:5]

china_2020_residential = china_2020[china_2020['sector'] == 'Residential']
china_2020_residential = china_2020_residential.reset_index(drop = True)
china_2020_residential['day_month'] = china_2020_residential['date'].str[:5]

#Domestic Aviation
china_2019_domaviate = china_2019[china_2019['sector'] == 'Domestic Aviation']
china_2019_domaviate = china_2019_domaviate.reset_index(drop = True)
china_2019_domaviate['day_month'] = china_2019_domaviate['date'].str[:5]

china_2020_domaviate = china_2020[china_2020['sector'] == 'Domestic Aviation']
china_2020_domaviate = china_2020_domaviate.reset_index(drop = True)
china_2020_domaviate['day_month'] = china_2020_domaviate['date'].str[:5]

china_combined_2019 = china_combined_2019.rename(columns = {'MtCO2 per day' : 'totalco2'})
china_2019_power = china_2019_power.rename(columns = {'MtCO2 per day' : 'power'})
china_2019_groundtrans = china_2019_groundtrans.rename(columns = {'MtCO2 per day' : 'groundtrans'})
china_2019_industry = china_2019_industry.rename(columns = {'MtCO2 per day' : 'industry'})
china_2019_residential = china_2019_residential.rename(columns = {'MtCO2 per day' : 'residential'})
china_2019_domaviate = china_2019_domaviate.rename(columns = {'MtCO2 per day' : 'domaviate'})

sectors_2019 = china_combined_2019.join([china_2019_power['power'], china_2019_groundtrans['groundtrans'],china_2019_industry['industry'], china_2019_residential['residential'], china_2019_domaviate['domaviate']])
print(list(sectors_2019))

china_combined_2020 = china_combined_2020.rename(columns = {'MtCO2 per day' : 'totalco2'})
china_2020_power = china_2020_power.rename(columns = {'MtCO2 per day' : 'power'})
china_2020_groundtrans = china_2020_groundtrans.rename(columns = {'MtCO2 per day' : 'groundtrans'})
china_2020_industry = china_2020_industry.rename(columns = {'MtCO2 per day' : 'industry'})
china_2020_residential = china_2020_residential.rename(columns = {'MtCO2 per day' : 'residential'})
china_2020_domaviate = china_2020_domaviate.rename(columns = {'MtCO2 per day' : 'domaviate'})

sectors_2020 = china_combined_2020.join([china_2020_power['power'], china_2020_groundtrans['groundtrans'],china_2020_industry['industry'], china_2020_residential['residential'], china_2020_domaviate['domaviate']])

fig_total = go.Figure(
    layout = go.Layout(
        title = go.layout.Title(text = 'Total CO2 Emitted')
    )
)
fig_total.add_scatter(x = sectors_2019['day_month'], y = sectors_2019['totalco2'], mode = 'markers+lines', name ='2019')
fig_total.add_scatter(x = sectors_2020['day_month'], y = sectors_2020['totalco2'], mode = 'markers+lines', name = '2020')

total_co2 = dcc.Graph(
    figure = fig_total
)

fig_power = go.Figure(
     layout = go.Layout(
        title = go.layout.Title(text = 'Power Sector')
    )
)
fig_power.add_scatter(x = sectors_2019['day_month'], y = sectors_2019['power'], mode = 'markers+lines', name ='2019')
fig_power.add_scatter(x = sectors_2020['day_month'], y = sectors_2020['power'], mode = 'markers+lines', name ='2020')

power = dcc.Graph(
    figure = fig_power
)

fig_ground = go.Figure(
     layout = go.Layout(
        title = go.layout.Title(text = 'Ground Transportation')
    )
)
fig_ground.add_scatter(x = sectors_2019['day_month'], y = sectors_2019['groundtrans'], mode = 'markers+lines', name ='2019')
fig_ground.add_scatter(x = sectors_2020['day_month'], y = sectors_2020['groundtrans'], mode = 'markers+lines', name ='2019')

ground = dcc.Graph(
    figure = fig_ground
)

fig_industry = go.Figure(
     layout = go.Layout(
        title = go.layout.Title(text = 'Industry')
    )
)
fig_industry.add_scatter(x = sectors_2019['day_month'], y = sectors_2019['industry'], mode = 'markers+lines', name ='2019')
fig_industry.add_scatter(x = sectors_2020['day_month'], y = sectors_2020['industry'], mode = 'markers+lines', name ='2020')

industry = dcc.Graph(
    figure = fig_industry
)

fig_resident = go.Figure(
     layout = go.Layout(
        title = go.layout.Title(text = 'Residential')
    )
)
fig_resident.add_scatter(x = sectors_2019['day_month'], y = sectors_2019['residential'], mode = 'markers+lines', name ='2019')
fig_resident.add_scatter(x = sectors_2020['day_month'], y = sectors_2020['residential'], mode = 'markers+lines', name ='2020')

resident = dcc.Graph(
    figure = fig_resident
)

fig_aviate = go.Figure(
     layout = go.Layout(
        title = go.layout.Title(text = 'Domestic Aviation')
    )
)
fig_aviate.add_scatter(x = sectors_2019['day_month'], y = sectors_2019['domaviate'], mode = 'markers+lines', name ='2019')
fig_aviate.add_scatter(x = sectors_2020['day_month'], y = sectors_2020['domaviate'], mode = 'markers+lines', name ='2020')

aviate = dcc.Graph(
    figure = fig_aviate
)


# page_content2 = dbc.Row(
#     children = [

#         dbc.Col(
#             power,
#             lg = 6
#         ),

#         dbc.Col(
#             ground,
#             lg = 6
#         )
#     ]
# )

#app.layout = html.Div(
layout = html.Div(
    children = [

        dbc.Row(
            className = "bg-dark text-light text-center",
            children = [
                dbc.Col(
                    html.H1('Carbon Emissions in China'),
                    lg = 16
                )
            ]
        ),


        dbc.Row(
            children = [
                dbc.Col(
                    total_co2
                )
             ]
        ),

        dbc.Row(
            children = [

                dbc.Col(
                    power,
                    lg = 6
                ),

                dbc.Col(
                    ground,
                    lg = 6
                )
            ]   
        ),

        dbc.Row(
            children = [
                dbc.Col(
                    industry
                ),

                dbc.Col(
                    resident
                )
            ]
        ),

        dbc.Row(
            dbc.Col(
                aviate
            )
        )
        # page_content2,
        # page_content2
    ]
)
# ---------------------------------------------------------------
# App Layout

# app.layout = html.Div([
#     html.H1('Carbom Emissions', style = {'text-align': 'center'}),

#     dcc.Dropdown(
#         id = 'slct_sectors',
#         options = [
#             {'lable': 'Total', 'value': 'totalco2'},
#             {'lable': 'Power', 'value': 'power'},
#             {'lable': 'Ground Transportation', 'value': 'groundtrans'},
#             {'lable': 'Industry', 'value': 'industry'},
#             {'lable': 'Residential', 'value': 'residential'},
#             {'lable': 'Domestic Aviation', 'value': 'domaviate'}
#         ],
#         value = 'totalco2',
#         style = {'width': '40%'}
#     ),

#     html.Div(id = 'output_container', children = []),
#     html.Br(),

#     dcc.Graph(id = 'my_graphs', figure = {})
# ])

# #Connect graphs to Dash Components

# @app.callback(
#     [Output(component_id = 'output_container', component_property = 'children'),
#      Output(component_id = 'my_graphs', component_property = 'figure')],
#     [Input(component_id = 'slct_sectors', component_property = 'value')]
# )
# def update_graph(option_slctd):

#     container = "The option selected was : {}".format(option_slctd)
#     fig = go.Figure()
#     #fig = px.line(data_frame = sectors_2019, x = sectors_2019.day_month, y = option_slctd)
#     fig.add_scatter(x = sectors_2019['day_month'], y = sectors_2019[option_slctd], name = '2019')
#     fig.add_scatter(x = sectors_2020['day_month'], y = sectors_2020[option_slctd], name = '2020')

#     return container, fig

if __name__ == '__main__':
    app.run_server(debug = True)