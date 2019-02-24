import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask
import pandas as pd
import time
import os

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

app = dash.Dash('app', server=server)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

def set_data(data_frame,data_name):
    app.layout = html.Div([
        html.H1(data_name),
        dcc.Graph(
            id='my-graph',
            figure={
                'data': [{
                    'x': data_frame.timestamp,
                    'y': data_frame.close,
                    'line': {
                        'width': 3,
                        'shape': 'linear'
                    }
                }],
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 20,
                        'b': 30,
                        't': 20
                    }
                }
            })
    ], className="container")
    return

def run():
    app.run_server()
