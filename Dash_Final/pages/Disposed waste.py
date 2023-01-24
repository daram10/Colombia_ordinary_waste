#libraries
import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path='/waste_disposed')

# specific layout for this page
layout = dbc.Container(
    [

        dbc.Row([
            html.H1(['Disposed Waste']),
        ], style={'textAlign': 'center'}),
        
        dbc.Row([
              dbc.Col([
                html.H3(['Kilograms per capita of waste disposed by year'],id="div_title_maps"),
                dcc.Dropdown(['2016', '2017', '2018',"2019","2020","2021"], '2016', id='demo-dropdown',style = {"width" : 500}),
                 html.Iframe(style = {"height" : 500, "width" : 500},id = "Figura1"),
                  dcc.Markdown([open('./data/Toneladas_dispuestas/Maps1.md').read()]),

             ], className='card'),
        dbc.Col([
                 html.H3(['Kilograms per capita of total waste disposed'],id="div_title_maps10"),
                             html.Iframe(src  = 'assets/Toneladas_dipuestas/mapatoneladas_percapita_total.html',style = {"height" : 530, "width" : 500},id = "Figura2"),
            html.Div([dcc.Markdown([open('./data/Toneladas_dispuestas/Maps2.md').read()])],style={'textAlign': 'justify'}),

             ], className='card'),            

           
        ]),

         dbc.Row([
             dbc.Col([
             html.H3(['Lifespan'],id="Vida_util",style={'textAlign': 'center'}),
             html.Iframe(src  = 'assets/Toneladas_dipuestas/vid_util.html',style = {"height" : 600, "width" : 1220},id = "Figura5"),
                 dcc.Markdown([open('./data/Toneladas_dispuestas/Lifespan.md').read()]), 

           ]),
             

         ], className='card'),
        
        dbc.Row([
            html.H3([' '],id="espacio2",style={'textAlign': 'center'}),
            html.H3(['Total tons of disposed waste'],id="div_title_maps6",style={'textAlign': 'center'}),
            html.Iframe(src  = 'assets/Toneladas_dipuestas/Total_tons_of_disposed_waste.html',style = {"height" : 900, "width" : 1400},id = "Figura8"),
            dcc.Markdown([open('./data/Toneladas_dispuestas/Bar_Chart.md').read()]), 
            ], className='card'),

#         dbc.Row([
#             html.H3(['Disposed waste in Bogota and other departments'],id="Disposed",style={'textAlign': 'center'}),
#             html.Iframe(src  = 'assets/Toneladas_dipuestas/Disposed_waste Bogota _other_departments.html',style = {"height" : 500, "width" : 1200},id = "Figura9") 
#             ], className='card'),

        ]
)  

@callback(
    Output('Figura1', 'src'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    if value == "2016":
        return 'assets/Toneladas_dipuestas/mapatoneladas_percapita_2016.html'
    elif value == "2017":
        return 'assets/Toneladas_dipuestas/mapatoneladas_percapita_2017.html'
    elif value == "2018":
        return 'assets/Toneladas_dipuestas/mapatoneladas_percapita_2018.html'
    elif value == "2019":
        return 'assets/Toneladas_dipuestas/mapatoneladas_percapita_2019.html'
    elif value == "2020":
        return 'assets/Toneladas_dipuestas/mapatoneladas_percapita_2020.html'
    elif value == "2021":
        return 'assets/Toneladas_dipuestas/mapatoneladas_percapita_2021.html'