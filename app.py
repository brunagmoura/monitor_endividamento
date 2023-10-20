from flask import Flask, render_template
from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px

# Inicializa a aplicação Flask
server = Flask(__name__)

# Inicializa a aplicação Dash
app = Dash(__name__, server=server, routes_pathname_prefix='/dash/')

# Carrega os dados
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Layout da aplicação Dash
app.layout = html.Div([
    html.H1(children='Dash App embedded in Flask'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10, id='table'),
    dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'), id='graph')
])

# Rota da página inicial da aplicação Flask
@server.route('/')
def index():
    return render_template('index_git.html')

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=5000)
