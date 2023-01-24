#Import libraries
from dash import html , dcc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np


class recovery_rate:
    """A class to get line plot of recovery rate"""
    def __init__(self, title:str, ID:str):
        """__init__
        Construct all the attributes for the bar chart
     
        Args:
            title (str): _Title for the line plot_
            ID (str): _div id to specify unique #id with callbacks and css_
        
        Methods:

        display()
            Function to show a line plot with no arguments, uses plotly express data.
            
            Arguments:
                None

            Returns:
                html.Div : A Div container with a dash core component dcc.Graph() inside
        """
        self.title = title
        self.id = ID
        
    @staticmethod
    def figura(self):
        
        #Call database
        Union4 = pd.read_csv("./data/toneladas_aprovechadas/final_data_month.csv",sep='|',index_col=0)
        Union4["Departamento"].replace({'ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA':'SAN ANDRES'}, inplace = True)
        
        #Create a pivot table to aggreagte data by "Department" and "Period" variables
        table2 = pd.pivot_table(Union4, values='Tasa_apro', index=['PERIODO_NUEVO', 'Departamento'], aggfunc='mean').reset_index()
        
        
        #Create figure from arguments
        fig = go.Figure()

        #Define the list of deparment to dropdown list
        departamento_list = list(table2['Departamento'].unique())

        #Create the chart layout related to the "Departamento" selection list
        for department in departamento_list:
            fig.add_trace(
                go.Scatter(
                    x = table2['PERIODO_NUEVO'][table2['Departamento']==department],
                    y = table2['Tasa_apro'][table2['Departamento']==department],
                    name = department, visible = True,

                )
            )

        #Create the display of time fraction    
        fig.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                         dict(count=1,
                             label="1m",
                             step="month",
                             stepmode="backward"),
                        dict(count=6,
                             label="6m",
                             step="month",
                             stepmode="backward"),
                        dict(count=1,
                             label="YTD",
                             step="year",
                             stepmode="todate"),
                        dict(count=1,
                             label="1y",
                             step="year",
                             stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
            )
        ) 

        

        fig.update_layout(
            autosize=False,
            width=1200,
            height=800
        )

        #style layout
        fig.update_layout(
                         xaxis=dict(
                title="Period"
            ),
            yaxis=dict(
                title="Rate (%)"
            ))

        
        return fig
    
    
    def display(self):   
        layout = html.Div(
            [

                    dcc.Graph(figure=recovery_rate.figura(self), id=self.id)
                
            ]
        )
        return layout