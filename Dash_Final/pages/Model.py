#libraries
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page


# dash-labs plugin call, menu name and route
register_page(__name__, path="/Model")

layout = dbc.Container(
    [
        
        html.H1(['Model']),
        dbc.Row([
            html.Iframe(src  = 'assets/Model/model.html',style = {"height" : 530}, id = "model"),
            html.Div([dcc.Markdown([open('./data/Model/modeltext.md').read()])],style={'textAlign': 'justify'}), 
      ], className = 'card'),

    ]
) 



