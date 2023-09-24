import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([
    html.H1('MyBudget', classname = 'text_primary)'),
    html.P('By Davi Rezende', classname = 'text_info'),
    html.Hr(),


    dbc.Button(id ="Botao_avatar", children = [html.Img(src = "assets/avatar.png", style = {"width": "100px", "height": "100px"})], color = "primary", className = "mr-1", style = {"width": "100px", "height": "100px"}),

                
            ])
# ========= Callbacks ========= #
dbc.Row([
    dbc.Col([
        dbc.Button(color = "danger", id ='open-novo-despesa', children = 'Nova Despesa', className = 'mr-1', style = {'width': '100%'}),
    ], md = 4),
    dbc.Col([
        dbc.Button(color = "success", id ='open-novo-receita', children = 'Nova Receita', className = 'mr-1', style = {'width': '100%'}),
    ], md = 4),

])
html.Hr(),
dbc.Nav(
    [dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
     dbc.NavLink("Extratos", href="/extratos", active="exact"),
     ], vertical = True, pills = True, id = "Nav_Buttons", style = {'margin-botton': '50px'}),


dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Nova Receita")),
    dbc.ModalBody([
    ])
], id = "modal-novo-receita")
#modal despesa
dbc.Modal([
    dbc.ModalHeader(dbc.ModalTitle("Despesa")),
    dbc.ModalBody([
    ])
], id = "modal-novo-despesa"), 
	







# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),	
    input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open'),

)

def toggle_modal(n1,is_open):
    if n1:
        return not is_open
    return is_open

@app.callback(
    Output('modal-novo-despesa', 'is_open'),	
    input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open'),

)

def toggle_modal(n1,is_open):
    if n1:
        return not is_open
    return is_open