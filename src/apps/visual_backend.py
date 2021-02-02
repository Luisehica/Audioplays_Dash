import plotly.express as px
import plotly.graph_objects as go
from itertools import cycle
import pandas as pd


pd.options.plotting.backend = "plotly"
# Tal vez abría que hacer pequeñas modificaciones para que los graficos interactuan con los callbacks de dash

class DashPlotting:
    
    ptp_palette = ['#F16C1F', '#bbbfca', '#9ad3bc']
    template    = "plotly_white"
    
    def __init__(self):
        pass
    

    @classmethod
    def monthly_plot():
        pass

    @classmethod
    def weekly_plot():
        pass
    


    @classmethod
    def histogram(cls, df, x_data=None, title=None):
        
        figure = px.histogram(df,
                         x=x_data,
                         color_discrete_sequence=DashPlotting.ptp_palette, 
                         template = DashPlotting.template,
                         title=title)
        return figure

    @classmethod
    def time_series_plot(cls, y_data, x_data=None, title=None):
        
        figure = px.line(y=y_data,
                         x=x_data,
                         color_discrete_sequence=DashPlotting.ptp_palette, 
                         template = DashPlotting.template,
                         title=title)
        return figure
        
    
    @classmethod
    def bar_plot(cls, data, groups, values, color, func='mean',  **kwargs):
        
        palette = cycle(DashPlotting.ptp_palette)
        
        if func=='mean':
            fig = go.Figure(
                data = [go.Bar(
                    y=data[data[groups] == group].groupby(color)[values].mean(), 
                    x=data[color].unique()
                ) for group in data[groups].unique()],
                marker=dict(color=next(palette))
            )
        else:
            fig = go.Figure(
                data = [go.Bar(
                    y=data[data[groups] == group].groupby(color)[values].count(), 
                    x=data[color].unique(),
                    marker=dict(color=next(palette))
                ) for group in data[groups].unique()]
                
            )
        fig.update_layout(template= DashPlotting.template,height=300)
        
        return fig
        
    
    @classmethod
    def scatter_plot(cls, data, x, y, **kwargs):
        figure = px.scatter(data,x=x, y=y,
                            color_discrete_sequence=DashPlotting.ptp_palette,
                            template= DashPlotting.template,
                            **kwargs)
        return figure
    