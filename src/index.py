# Import dash 
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

# Import plotly
import plotly.graph_objects as go

# Import dependencies for callbacks
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_table

# Connect to main app.py file, apps pages and backend
from app import app, create_layout
from apps import main, help
from apps.visual_backend import DashPlotting
import backend


# Describe the layout/UI of the app
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content")
    ]
)

### Callback for page salection
@app.callback(Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname'))
def display_page(pathname):
    if pathname == '/help':
        return create_layout(app, help)
    else:
        return create_layout(app, main)


### Callback for users suscribed
@app.callback(Output(component_id='users_suscribed_plot', component_property='figure'),
    [
        Input(component_id='pick_date_range', component_property='start_date'),
        Input(component_id='pick_date_range', component_property='end_date'),
    ])
def user_suscribed_plot(start, end):
    df = backend.users_suscribed(start, end)
    print(df)
    if df.empty:
        fig = {
            "layout": {
                "xaxis": {
                    "visible": False
                },
                "yaxis": {
                    "visible": False
                },
                "annotations": [
                    {
                        "text": "Empty",
                        "xref": "paper",
                        "yref": "paper",
                        "showarrow": False,
                        "font": {
                            "size": 28
                        }   
                    }
                ]
            }
        }
    else:
        fig = DashPlotting.histogram(df)
    layout = go.Layout(height = 120)
    return go.Figure(data=fig, layout=layout)






if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
