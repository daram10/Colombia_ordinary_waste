#libraries
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


# dash-labs plugin call, menu name and route
register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Row([
                
                html.H1(['Analyzing Waste Recovery Rate Effects in Colombia']),
            html.Div([dcc.Markdown([open('./data/Home/p1.md').read()])],style={'textAlign': 'justify'}),

            ]),
        
        dbc.Row([
            
             dbc.Col([
            
                html.Img(src='/assets/Home/IMG1.png', style={'width':'50%'}),
                 
             ], style={'textAlign': 'center'}, className='card-image')
            
        ]),
                
        dbc.Row([
            html.Div([dcc.Markdown([open('./data/Home/p2.md').read()])],style={'textAlign': 'justify'}),            
            dbc.Col([
            
                html.Img(src='/assets/Home/IMG2.jpg', style={'width':'50%'}),   
            
            ], style={'textAlign': 'center'}, className='card-image')
        ]),
        
        dbc.Row([
            html.Div([dcc.Markdown([open('./data/Home/p3.md').read()])],style={'textAlign': 'justify'}),   
        ], className='card-image'),


    ]
) 



