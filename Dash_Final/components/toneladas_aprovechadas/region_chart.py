#Import libraries
from dash import html , dcc
import dash_bootstrap_components as dbc
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly.offline as pyo

#from components.table.table import table


class region_chart:
    """A class to get the horizontal bar chart of region participation by tons effectively used"""
    def __init__(self, barchart_title:str, ID:str, year:int):
        """__init__
        Construct all the attributes for the bar chart
     
        Args:
            barchart_title (str): _Title for the bar chart_
            ID (str): _div id to specify unique #id with callbacks and css_
        
        Methods:

        display()
            Function to show a bar chart with no arguments, uses plotly express data.
            
            Arguments:
                None

            Returns:
                html.Div : A Div container with a dash core component dcc.Graph() inside
        """
        self.barchart_title = barchart_title
        self.year = year
        self.id = ID
        
    @staticmethod
    def figura(self):
        
        #Call database
        Union3 = pd.read_csv("./data/toneladas_aprovechadas/final_data_year.csv",sep='|',index_col=0)
        #Rename variable "TONELADAS APROVECHADAS" to "TONELADAS_APROVECHADAS", for complete the table
        Union3.rename(columns = {'TONELADAS APROVECHADAS':'TONELADAS_APROVECHADAS'}, inplace = True)   
        #Create a pivot table to aggreagte data by "Department" and "Period" variables
        table3 = pd.pivot_table(Union3, values='TONELADAS_APROVECHADAS', index=['AÑO', 'REGION'],aggfunc=np.sum).reset_index()
        
        
        #Define rank of time 
        x = self.year
        table3_seg = table3[(table3["AÑO"] == x)].sort_values(by="TONELADAS_APROVECHADAS").head()
        
        #Get percentage
        total = sum(table3_seg["TONELADAS_APROVECHADAS"].values)
        table3_seg["percentage"] = table3_seg["TONELADAS_APROVECHADAS"].apply(lambda x: "{:.2f}%".format((x/total)*100))
        
        #Set the chart (horizontal bar chart)

        fig = px.bar(table3_seg, x="percentage", y="REGION", color='REGION', orientation='h',
                     hover_data=["REGION", "percentage"],
                     width=700)
        fig.update_layout(showlegend=False) 
        fig.update_layout(
            xaxis_title="Percentage", yaxis_title="Region"
        )
        
        #Set two decimals for the Tons effectively used   
        table3_seg['TONELADAS_APROVECHADAS'] = table3_seg['TONELADAS_APROVECHADAS'].apply(lambda x: round(x, 2))
        
        #table of tons by year 
        table1 = go.Figure(data=[go.Table(header=dict(values=['Region', 'Tons effectively used']),
                 cells=dict(values=[table3_seg.REGION, table3_seg.TONELADAS_APROVECHADAS]))
                     ])
        
        return fig, table1
    
    
    def display(self):   
        layout = html.Div(
            [
                    dbc.Row([
                        
                        dbc.Col([
                        dcc.Graph(figure=region_chart.figura(self)[0], id=self.id)
                        ]),
                        dbc.Col([
                        dcc.Graph(figure=region_chart.figura(self)[1], id="table1"),
                        ])
                   ]) 
                
            ]
        )
        return layout