#libraries
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


# dash-labs plugin call, menu name and route
register_page(__name__, path="/waste_effectively_used")

from components.toneladas_aprovechadas.region_chart import region_chart
from components.toneladas_aprovechadas.recovery_rate import recovery_rate
from components.toneladas_aprovechadas.usable_waste import usable_waste


hbarchart = region_chart('habarchart', 'div_barchart',2016)
lineplot = recovery_rate('lineplot', 'div_lineplot')
barplot = usable_waste ('barplot', 'div_barplot')

# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
                html.H1(['Effectively used waste'])
        ], style={'textAlign': 'center'}),
        dbc.Row([
            html.H3(['Kilograms per capita of waste effectively used']),
              dbc.Col([
                  
                dcc.Dropdown(['2016', '2017', '2018',"2019","2020","2021"], '2016', id='mapa-dropdown',style = {"width" : 600}),
                html.Iframe(style = {"height" : 500, "width" : 600}, id = "Mapa"),                

             ]),
            
            dbc.Col([
                 dcc.Markdown([open('./data/toneladas_aprovechadas/map.md').read()])     
             ],style={'textAlign': 'justify'}),

        ]),

        dbc.Row([
            html.H3(['Waste recovery rate']),
            html.Div([dcc.Markdown([open('./data/toneladas_aprovechadas/recovery_rate.md').read()])],style={'textAlign': 'justify'}),
            lineplot.display()
        ], className='card'),
        
        dbc.Row([
            html.H3(['Tons effectively used']),
            html.Div([dcc.Markdown([open('./data/toneladas_aprovechadas/tons_used.md').read()])],style={'textAlign': 'justify'}),
            barplot.display()
        ], className='card'),
        
        dbc.Row([
            
                       
        ]),
        
       dbc.Row([
           
           html.H3(['Region participation by tons effectively used']),
           html.Div([dcc.Markdown([open('./data/toneladas_aprovechadas/region.md').read()])],style={'textAlign': 'justify'}), 
           html.P("Year:"),
           dcc.Dropdown([{"label": "2016", "value": 2016},
                        {"label": "2017", "value": 2017},
                        {"label": "2018", "value": 2018},
                        {"label": "2019", "value": 2019},
                        {"label": "2020", "value": 2020},
                        {"label": "2021", "value": 2021},], 2016, id='year-label', style = {"width" : 600}),
            html.Div([hbarchart.display()], id = "row_hbarchart")
                       
        ], className='card'),
        

        ]#, className='container-fluid', style={'margin': 'auto', 'width':'100%'}
)


# Callbacks
@callback(
    Output("row_hbarchart", "children"), 
    Input("year-label", "value"))
def update_hbarchart(year):
    hbarchart.year = year
    new_hbarchart =  hbarchart.display()
    return [new_hbarchart]

@callback(
    Output('Mapa', 'src'),
    Input('mapa-dropdown', 'value')
)
def update_output(value):
    if value == "2016":
        return 'assets/Toneladas_aprovechadas/mapa_kg_per_capita_2016.html'
    elif value == "2017":
        return 'assets/Toneladas_aprovechadas/mapa_kg_per_capita_2017.html'
    elif value == "2018":
        return 'assets/Toneladas_aprovechadas/mapa_kg_per_capita_2018.html'
    elif value == "2019":
        return 'assets/Toneladas_aprovechadas/mapa_kg_per_capita_2019.html'
    elif value == "2020":
        return 'assets/Toneladas_aprovechadas/mapa_kg_per_capita_2020.html'
    elif value == "2021":
        return 'assets/Toneladas_aprovechadas/mapa_kg_per_capita_2021.html'