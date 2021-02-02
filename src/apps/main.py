import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import date

def content(app):
    layout = dbc.Container(
        [   
            html.Br(),
            html.H1("Users Suscribed"),
            big_box_kpi(app, 'first_plot', 
            [
                'users_suscribed',
                'users_suscribed_perc',
                'growth_suscribed',
                'growth_perc'
            ],
            [
                'Users Subscribed',
                'of our users are subscribed'
            ], 
            [
                'box_up_1_time',
                'box_up_2_time',
                'box_up_3_time'
            ]),
            html.H1("Active Users"),
            big_box_kpi(app, 'first_plot', 
            [
                'users_suscribed',
                'users_suscribed_perc',
                'growth_suscribed',
                'growth_perc'
            ],
            [
                'Users Subscribed',
                'of our users are subscribed'
            ], 
            [
                'box_1_time',
                'box_2_time',
                'box_3_time'
            ])
        ]
    )
    return layout


def big_box_kpi(app, plot_id, values_id, text_list, time_window_id_list):
    """Creates the big box for each KPI.

    Args:
        app (dash.Dash): Dash object
        plot_id (str): plot id
        values_id (list): list of 4 ids.
        text_list (list):  list of two strings.
        time_window_id_list (list): list of 3 ids

    Returns:
        dbc.Row: Big box
    """
    big_box = dbc.Row(
        [
            dbc.Col( #Left Column
                empty_plot(app, plot_id),
                sm=12,
                lg=7
            ),
            dbc.Col( #right Column
                 right_card(app, values_id, text_list, time_window_id_list),
                 align='center'
            )
        ]
    )
    return big_box

def right_card(app, values_id_list, text_list,time_window_id_list):
    """ Creates the right card.

    Args:
        app (dash.Dash): Dash object
        values_id_list (list): list of 4 ids.
        text_list (list):  list of two strings.
        time_window_id_list (list): list of 3 ids

    Returns:
        html.Div: Card
    """
    card = html.Div(
        [
            box_2_lines(app, values_id_list[0], text_list[0], time_window_id_list[0]),
            box_2_lines(app, values_id_list[1], text_list[1], time_window_id_list[1]),
            html.Div(id="h-line"),
            box_1_line(app, values_id_list[2], ' this week',time_window_id_list[2]),
            box_1_line(app, values_id_list[3],' Growth', 'one_line_right')
        ]
    )
    return card

def right_card_bootstrap(app, values_id_list, text_list,time_window_id_list):
    """ Creates the right card.

    Args:
        app (dash.Dash): Dash object
        values_id_list (list): list of 4 ids.
        text_list (list):  list of two strings.
        time_window_id_list (list): list of 3 ids

    Returns:
        html.Div: Card
    """
    card = dbc.Card(
        dbc.CardBody(
            [
                box_2_lines(app, values_id_list[0], text_list[0], time_window_id_list[0]),
                box_2_lines(app, values_id_list[1], text_list[1], time_window_id_list[1]),
                html.Div(id="h-line"),
                box_1_line(app, values_id_list[2], ' this week',time_window_id_list[2]),
                box_1_line(app, values_id_list[3],' Growth', 'one_line_right')                
            ]
        ),
        color='ligth',
        outline=True
    )
    
    return card

    

def box_2_lines(app, value_id, text, time_window_id):
    """ Creates a box with two rows

    Args:
        app (dash.Dash): Dash object
        values_id (list): id for the value.
        text (list):  text for two row.
        time_window_id (list): id of the time window

    Returns:
        html.Div: Box
    """
    box = html.Div(
            [
            html.Span('100000', id=value_id, className='main_value'),
            html.P(
                [
                    html.Span(text, className='text_box'),
                    html.Span(" this week", id=time_window_id)
                ]
            )
        ]
        , className='box-2-lines'
    )
    return box

def box_1_line(app, left_id, text, right_id):
    """ Create 1 line Box.

    Args:
        app (dash.Dash): Dash Object
        left_id (str): id of the value in the left
        right_id (str): id of the value in the left

    Returns:
        html.Div: Box
    """
    box=html.Div(
        [
            html.Span("+ 200", id=left_id),
            html.Span(text, id=right_id, className='one_line_right'),

        ],
        className='box-1-line'
    )
    return box

def empty_plot(app, plot_id):
    """Empty plot just with text

    Args:
        app (dash.Dash): Dash Object
        plot_id (str): id of the plot

    Returns:
        html.Div: plot
    """
    plot = html.Div(
        [
            dcc.Graph(
                id=plot_id,
                figure = {
                    "layout": {
                        "xaxis": {
                            "visible": False
                        },
                        "yaxis": {
                            "visible": False
                        },
                        "annotations": [
                            {
                                "text": "Loading data...",
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
            ),
        ]
    )
    return plot

def cohort(app):
    #https://medium.com/analytics-vidhya/cohort-analysis-95a794b4e58c

    pass