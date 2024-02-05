"""
This app examplifies how to create an app with simple fixed sidebar (on left side) layout using
dbc.Nav component including multiple pages and its contents.

Just Updating: dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0 or as per your updates.

It is a good practice to document import stuffs such as version of libraries needed for your project or business problem use case and 
a clear and mindful documentation provides emphasis on your work and helps others understand very well.
"""

import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State
from dash_iconify import DashIconify
import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt 
import dash_mantine_components as dmc
from inspect import getfullargspec
import seaborn as sns 



# Create app objects and start
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP, ], 
                assets_url_path="assets", # never forget to add this arguement when you have assets folder inside of your app root directory
                assets_folder ="assets", 
                suppress_callback_exceptions=True,
                meta_tags=[
                    {
                        "name": "viewport", 
                        "content": "width=device-width, initial-scale=1"
                    }
                ],
)

# create server object needed for render.com
server = app.server

# Change the app name 
app.title = """My First Plotly Dash App"""


# # you can use this data as well
# data_canada = px.data.gapminder().query("country == 'Canada'")
# fig = px.bar(data_canada, x='year', y='pop')


usa_pop_df = pd.read_csv(r'D:\github_shared_dash_app_repo\plotly-dash-app\sample_app\assets\data\usa_final_app_data.csv') 
# usa_pop_df = pd.read_csv('assets/data/usa_final_app_data.csv') 
print(f"Prints some of columns and some rows: {usa_pop_df[['statecode', 'state', 'countycode', 'county', 'year', 'total_population']].head()}")

national_level_df = usa_pop_df[['statecode', 'state', 'countycode', 'county', 'year', 'total_population']].query("countycode==0 & state=='US'")

fig = px.bar(national_level_df, x='year', y='total_population')



# -------------------------------------------------------------------------------------

# Three horizontal bars 
three_horizontal_bars = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "1vh", # you can increase the height of this line using 'vh' which can be '1/2/3/4/n/vh'
                            "width": "100%",
                            "borderColor": "#dc20df",
                            "opacity": "unset",
                            #"border-radius": "4px",
                        },
                    ), 
                    width={"size": 3},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "1vh",
                            "width": "100%",
                            "borderColor": "#e7e9eb", # "#F3DE8A",
                            "opacity": "unset",
                            #"border-radius": "4px",
                        }
                    ),
                    width={"size": 3},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "1vh",
                            "width": "100%",
                            "borderColor": "#4f3bd0",
                            "opacity": "unset",
                            #"border-radius": "4px",
                        }
                    ),
                    width={"size": 3},
                ),
            ],
        ),
    ],
    style={
        "margin-left":'60rem',
    }
)



three_horizontal_bars_part2 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "0.7vh", # you can increase the height of this line using 'vh' which can be '1/2/3/4/n/vh'
                            "width": "100%",
                            "borderColor": "#dc20df",
                            "opacity": "unset",
                            #"border-radius": "4px",
                        }
                    ),
                    width={"size": 3},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "0.7vh",
                            "width": "100%",
                            "borderColor": "#e7e9eb", # "#F3DE8A",
                            "opacity": "unset",
                            #"border-radius": "4px",
                        }
                    ),
                    width={"size": 3},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "0.7vh",
                            "width": "100%",
                            "borderColor": "#4f3bd0",
                            "opacity": "unset",
                            #"border-radius": "4px",
                        }
                    ),
                    width={"size": 3},
                ),
            ],
        ),
    ],
    style={
        "margin-left":'60rem',
    }
)

# ----------------------------------------------------SIDE BAR Contents--------------------------------------------------------



# the style objects for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "26rem",
    "padding": "5rem 3rem",
    'border-radius': '12px',
    'background-image': 'linear-gradient(17deg,  rgb(79, 59, 208), rgb(79, 59, 208), rgb(220, 32, 223))',
}


# side navigation bar object
sidebar = html.Div(
    [
            html.Div(
                html.Img(
                    src=app.get_asset_url("images/sidebar_logo.gif"), #here you can either use dash.get_asset_url("filename") or app.get_asset_url("filename")
                    style={
                        'width': '60%',
                        "height": '60%',
                    },
                ),
                style={'textAlign':'center', 
                    'marginBottom':'1em',
                },
            ),
            html.H2(
                "PLOTLY DASH", 
                className="display-5 fw-bold", 
                style={
                    'color':'white','textAlign':'center'
                    }
            ),
            html.Hr(
                style={
                    'borderWidth': "0.5vh", 
                    "width": "100%", 
                    "borderColor": "white",
                    "opacity": "unset", 
                }
            ), # "transform": "rotate(90deg)" used for rotating the html objects
            html.Br(),
            html.Br(), 
            dcc.Markdown(
                f"""
                    **__Dash__** is an open-source framework for building data visualization interfaces, released in 2017 as a Python library. 
                    Dash helps data scientists build analytical web applications 
                    without requiring advanced web development knowledge. It is built on the top of three technologies: Flask, React.js, and Plotly.js.
                """, 
                className="lead fs-6 text-white text-center"
            ),
            html.Br(),
            html.Br(),
            dbc.Nav(
                [
                    dbc.NavLink(
                        "DS - Introduction", 
                        href="/", 
                        active="exact", 
                        style={
                            'color':'white', 
                            'textAlign':'center', 
                            "border":"1px solid rgba(255, 255, 255, .5)"
                        }, 
                        className='m-3 fw-bold'
                    ),
                    dbc.NavLink(
                        "DS - Projects", 
                        href="/ds-projects", 
                        active="exact", 
                        style={
                            'color':'white', 
                            'textAlign':'center', 
                            "border":"1px solid rgba(255, 255, 255, .5)"
                        }, 
                        className='m-3 fw-bold'
                    ),
                    dbc.NavLink(
                        "Help Me Improve", 
                        href="/help-me-improve", 
                        active="exact", 
                        style={
                            'color':'white', 
                            'textAlign':'center', 
                            "border":"1px solid rgba(255, 255, 255, .5)"
                        }, 
                        className='m-3 fw-bold'
                    ),
                ],
                vertical=True,
                pills=True,
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div(
                [
                    html.A(  
                        html.Span(
                            [
                                html.Img(
                                    src="assets/images/author.png",
                                    style={'display': 'inline-block', 'width': '6%', 'height': '6%'}
                                ),
                                html.P(
                                    "Satyndra Kumar Gautam",
                                    style={'display': 'inline-block', 'font-size': 13, 'margin-left': '0.5rem'}, className="lead link",
                                ),
                            ],
                        ), 
                        href="https://sites.google.com/view/satyndrakgautam/home", 
                        target="_blank", 
                    ),    
                    html.Br(),
                    html.A(    
                        html.Span(
                            [
                                html.Img(
                                    src="assets/images/email_1.png",
                                    style={'display': 'inline-block', 'width': '7.5%', 'height': '7.5%', }
                                ),
                                html.P(
                                    "Email Me",
                                    style={'display': 'inline-block', 'font-size': 13, 'margin-left': '0.4rem' }, className="lead link",
                                ),
                            ], style={'margin-right': '5.3rem',}
                        ), 
                        href = "mailto:gautam.ishu5@gmail.com", 
                        target="_blank",
                    ),
                    html.Br(),
                    html.A(    
                        html.Span(
                            [
                                html.Img(
                                    src="assets/images/phonecall.png",
                                    style={'display': 'inline-block', 'width': '5.2%', 'height': '5.2%'}
                                ),
                                html.P(
                                    "Hello?",
                                    style={'display': 'inline-block', 'font-size': 13, 'margin-right': '2.5rem', 'padding-left': '0.6em' }, className="lead link", #it was 0.7 rem back
                                ),
                            ], style={'margin-right': '3.6rem',}
                        ), 
                        href = "tel:+1-503-616-0690", 
                        target="_blank",
                    ),
                    html.Br(),
                    html.A(   
                        html.Span(
                            [
                                html.Img(
                                    src="assets/images/website.png",
                                    style={
                                        'display': 'inline-block', 
                                        'width': '5.0%', 'height': '5.0%'
                                    },
                                ),
                                html.P(
                                    "Portfolio",
                                    style={
                                        'display': 'inline-block', 
                                        'font-size': 13, 
                                        'margin-left': '0.7rem'
                                    }, 
                                    className="lead link",
                                ),
                            ], style={'margin-right': '5.0rem',}
                        ), 
                        href="https://sites.google.com/view/satyndrakgautam/home", 
                        target="_blank",
                    ),
                    html.Br(),
                    html.A(    
                        html.Span(
                            [
                                html.Img(
                                    src="assets/images/linkedin_icon.png",
                                    style={
                                        'display': 'inline-block', 
                                        'width': '7.3%', 
                                        'height': '7.3%'
                                    },
                                ),
                                html.P(
                                    "Linkedin",
                                    style={
                                        'display': 'inline-block', 
                                        'font-size': 13, 
                                        'margin-left': '0.5rem'
                                    }, 
                                    className="lead link",
                                ),
                            ], style={'margin-right': '5.3rem',}, 
                        ), 
                        href="https://www.linkedin.com/in/satyndra-gautam-79315552/", 
                        target="_blank",
                    ),
                ], style={
                    'textAlign': 'center', 
                    'marginTop': '8rem', 
                    "border": "1px solid rgba(255, 255, 255, .5)", 
                    'border-radius': '10px', 
                    'width': '',
                }, className='m-3'
            ),
    ], style=SIDEBAR_STYLE, 
)


# CONTENT PAGE STYLE
CONTENT_STYLE = {
    "backgroundColor": "#fefeff",
  }



# Create the objects for contents of pages
content = html.Div(
    id="page-content",className='fw-bold', style=CONTENT_STYLE,
)




# CREATE APP LAYOUT  
app.layout = html.Div(
    [
        dcc.Location(id="url"), 
        sidebar, 
        content, 
    ], 
    style={
        "height":'100%', 
        "position":'',
    },
) 


# ------------------------------------------------------------PAGE 1 CONTENTS--------------------------------------------------


page1_layout_and_contents=html.Div(children=
    [
        html.Div(    
            [    
                html.P("INTRODUCTION TO DATA SCIENCE", 
                    style={
                        "margin-left": "30rem",
                        "margin-right": "2rem",
                        "padding": "1rem 1rem",
                        'font-size': 40,
                        "color": '#33374b',
                        "textAlign":'center',
                        'marginTop':'2em', 
                    },
                ),
                html.P(
                    f"""
                        Data Science is an interdisciplinary academic field that uses statistics, scientific 
                        computing, scientific methods, processes, algorithms and systems to extract or extrapolate
                        knowledge and insights from noisy, structured, and unstructured data.
                        Data Science is an interdisciplinary academic field that uses statistics, scientific 
                        computing, scientific methods, processes, algorithms and systems to extract or extrapolate
                        knowledge and insights from noisy, structured, and unstructured data.
                    """,
                    style={
                        'textAlign':'center',
                        "margin-left": "50rem",
                        "margin-right": "25rem",
                        "marginBottom":'4em',
                        #"marginTop": '7em',
                        "font-size":15,
                        "font-family":"montserrat thin",
                        "color":'#33374b',
                    },
                ),
                three_horizontal_bars,
            ],
        ),
        html.Div(
            dbc.Tabs(
                [
                    dbc.Tab(
                        id="tab_1",
                        label="About",
                        tab_id="intro",
                        label_style={"color": "#414147", },
                        tab_style={"background-color": "", "width": "12.64vw", "textAlign":'center', "border":""}, # "background-color": "#ededef"
                        active_label_style={"background-color": "#e7e9eb", 'color':'#4f3bd0', "border": ""},
                    ),
                ],
                id="tabs",
                active_tab="intro",  
                style={
                    "margin-left": "31.5em",
                    "margin-right": "0em",
                    "marginTop":'3em',
                    "position":'fixed',
                    'box-shadow': 'rgba(33, 35, 38, 0.1) 0px 10px 10px -10px', 
                },
            ),
        ),
        html.Br(),    
        html.Div(
            id='tab-content', 
            className='p-5', 
            style={ 
                'marginTop':'3.3rem', 
                "margin-left":'28.54em',
                "margin-right":'3.65em',
                "height": "66.9vh",
                "width": "79.95vw",
            },
        ), 
    ],
)


# ----------------------------------------------------------------PAGE 1 TABS Contents------------------------------------------------------------

# TAB 1 Layout and Contents : ABOUT


tab_1_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col( 
                    dbc.Card(
                        [ # card_1
                            dbc.CardHeader(
                                "Business Problem Statement", 
                                className="d-flex align-items-center",
                                style={
                                    'background-color':'#33374b',
                                    'height':'9vh', 
                                    "color":'white', 
                                    "font-size": 23,
                                    "border-radius": "10px 10px 0px 0px",
                                    #'border-radius': 'unset', it(unset) removes the border from the object
                                },
                            ),
                            dbc.CardBody(
                                [
                                    dcc.Markdown(
                                            """
                                            A business problem statement is a concise description of an issue or challenge that a company faces, 
                                            framed in a way that highlights the impact on business goals or objectives. It serves as a clear and 
                                            specific statement of the problem that needs to be addressed for the business to succeed or improve.

                                            Once the business problem has been clearly stated, the analytic approach needs to be taken into consideration
                                            to solve the problem. Analytical Approaches are descriptive, diagnostic, predictive, and prescriptive. 
                                    
                                            """,
                                        className="m-2 p-2",
                                        style={"font-size":13,
                                                "font-family":"montserrat thin",
                                                #'text-align': 'justify' # we can use this text-align:justify to eliminate the space or fill the divison from both sides left and right
                                        },
                                    ),
                                    dbc.Button( 
                                        "More Details",
                                        id="click_button",
                                        n_clicks=0, 
                                        className="d-grid mx-auto",
                                        style={
                                            "marginTop": '2rem',
                                            "width":'12vb',
                                            "height":"2.9vh",
                                            "backgroundColor":'white',
                                            "color":'#dc20df',
                                            "border":"1px solid #4f3bd0",
                                        },
                                    ),
                                ], style={'height':'34vh', }
                            ),
                        ], style={
                            'box-shadow': 'rgba(149, 157, 165, 0.2) 0px 8px 24px', 
                            "border-radius": "10px"
                        }, 
                    ), 
                ),
                dbc.Col(
                    dbc.Card(
                        [ #card_2
                            dbc.CardHeader(
                                "Data Requirements and Data Collection", 
                                className="d-flex align-items-center",
                                style={
                                'background-color':'#33374b',
                                'height':'9vh', 
                                "color":'white', 
                                "font-size": 23,
                                "border-radius": "10px 10px 0px 0px", 
                                },
                            ),
                            dbc.CardBody(
                                [
                                    dcc.Markdown(
                                        """
                                            Data collection is a systematic process of gathering observations or measurements. Whether it is to perform research for business, 
                                            governmental or academic purposes, data collection allows us to gain first-hand knowledge and original insights into the business problem.
                                            Before begin to collecting data, we need to consider:

                                            * The objectives of the business problem
                                            * The type of data that you will collect
                                            * The methods and procedures you will use to collect, store, and process the data

                                        """,
                                        className="m-2 p-2",
                                        style={"font-size":13,
                                                "font-family":"montserrat thin",
                                        },
                                    ),
                                    dbc.Button( 
                                        "More Details",
                                        id="click_button_2",
                                        n_clicks=0, 
                                        className="d-grid mx-auto",
                                        style={
                                            "marginTop": '2rem',
                                            "width":'12vb',
                                            "height":"2.9vh",
                                            "backgroundColor":'white',
                                            "color":'#dc20df',
                                            "border":"1px solid #4f3bd0",
                                        },
                                    ),
                                ], style={'height':'34vh'}
                            ),
                        ], style={
                            'box-shadow': 'rgba(149, 157, 165, 0.2) 0px 8px 24px',
                            "border-radius": "10px",
                        },
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        [ #card_3
                            dbc.CardHeader(
                                "Data Processing and Transformation", 
                                className="d-flex align-items-center",
                                style={
                                    'background-color':'#33374b',
                                    'height':'9vh', 
                                    "color":'white', 
                                    "font-size": 23, 
                                    "border-radius": "10px 10px 0px 0px", 
                                },
                            ),
                            dbc.CardBody(
                                [
                                    dcc.Markdown(
                                        """
                                            Data wrangling, also known as data munging or data cleaning, refers to the process of cleaning, transforming, 
                                            and preparing raw data into a format suitable for analysis or modeling. This process involves various tasks, 
                                            including handling missing or erroneous data, converting data types, aggregating, filtering, and merging datasets. 
                                            
                                            Data wrangling is a crucial step in the data preprocessing pipeline and plays a significant role in ensuring the 
                                            quality and reliability of the data used for analysis or machine learning.
                                        """,
                                        className="m-2 p-2",
                                        style={"font-size":13,
                                                "font-family":"montserrat thin",
                                                #'text-align': 'justify',  
                                        },
                                    ),
                                    dbc.Button( 
                                        "More Details",
                                        id="click_button_3", 
                                        n_clicks=0,
                                        className="d-grid mx-auto",
                                        style={
                                            "marginTop": '2rem',
                                            "width":'12vb',
                                            "height":"2.9vh",
                                            "backgroundColor":'white',
                                            "color":'#dc20df',
                                            "border":"1px solid #4f3bd0",
                                        },
                                    ),
                                ], style={'height':'34vh'}
                            ),
                        ], 
                        style={
                            'box-shadow': 'rgba(149, 157, 165, 0.2) 0px 8px 24px',
                            "border-radius": "10px", 
                        },
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        [ #card_4
                            dbc.CardHeader(
                                "Exploratory Data Analysis", 
                                className="d-flex align-items-center",
                                style={'background-color':'#33374b',
                                    'height':'9vh', 
                                    "color":'white', 
                                    "font-size": 23,
                                    "border-radius": "10px 10px 0px 0px",  
                                },
                            ),
                            dbc.CardBody(
                                [
                                    dcc.Markdown(
                                        """
                                            Exploratory Data Analysis (EDA) is an approach to analyzing datasets to summarize their main characteristics, 
                                            often with visual methods. It helps to uncover patterns, relationships, anomalies, and gain insights into the 
                                            underlying structure of the data. 
                                            
                                            EDA involves generating summary statistics, visualizations, and sometimes 
                                            employing statistical techniques to understand the data and guide further analysis. It is an essential step in
                                            the data analysis process as it helps in formulating hypotheses and guiding subsequent modeling or decision-making.

                                        """,
                                        className="m-2 p-2",
                                        style={"font-size":13,
                                                "font-family":"montserrat thin",
                                        },
                                    ),
                                    dbc.Button( 
                                        "More Details",
                                        id="click_button_4",
                                        n_clicks=0, 
                                        className="d-grid mx-auto",
                                        style={
                                            "marginTop": '1rem',
                                            "width":'12vb',
                                            "height":"2.9vh",
                                            "backgroundColor":'white',
                                            "color":'#dc20df',
                                            "border":"1px solid #4f3bd0",
                                        },
                                    ),
                                ], style={'height':'34vh'}
                            ),
                        ], 
                        style={
                            'box-shadow': 'rgba(149, 157, 165, 0.2) 0px 8px 24px',
                            "border-radius": "10px", 
                        },
                    ),
                ),
                dbc.Col(
                    dbc.Card(
                        [ #card_5
                            dbc.CardHeader(
                                "Model Development and Deployment", 
                            className="d-flex align-items-center",
                            style={'background-color':'#33374b',
                                    'height':'9vh', 
                                    "color":'white', 
                                    "font-size": 23,
                                    "border-radius": "10px 10px 0px 0px",  
                                },
                            ),
                        dbc.CardBody(
                            [
                                dcc.Markdown(
                                    """
                                        Model development is the process of creating, training, and refining a statistical 
                                        or machine learning model using a dataset. It involves selecting and fine-tuning algorithms, feature 
                                        engineering, and parameter tuning to build a predictive or analytical model.

                                        Model deployment is the process of making a trained machine learning model available for real-world use. 
                                        Key points include infrastructure selection, scalability, input/output interfaces, monitoring, security, 
                                        versioning, and continuous integration.
                                    """,
                                    className="m-2 p-2",
                                        style={"font-size":13,
                                                "font-family":"montserrat thin", 
                                        },
                                ),
                                dbc.Button( 
                                    "More Details",
                                    id="click_button_5", 
                                    n_clicks=0,
                                    className="d-grid mx-auto",
                                    style={
                                        "marginTop": '2rem',
                                        "width":'12vb',
                                        "height":"2.9vh",
                                        "backgroundColor":'white',
                                        "color":'#dc20df',
                                        "border":"1px solid #4f3bd0",
                                    },
                                ),
                            ], style={'height':'34vh'}
                        ),
                    ], style={
                        'box-shadow': 'rgba(149, 157, 165, 0.2) 0px 8px 24px',
                        "border-radius": "10px", 
                        },
                    ),
                ),
            ],
            className="mb-4", style={'marginTop': '2rem'}
        ),
        dbc.Row(
            html.Div(
                [    
                    dcc.Markdown(
                        """
                            Hello! this DS - Introduction page exemplifies key Data Science Processes and their pivotal focal areas. 
                            The inspiration behind this project is to showcase how to use Dash, Plotly, HTML, CSS, Bootstrap, and more for advanced web-based data analysis applications. 
                            I believe there is always room for improvements so your feedback is invaluable in my pursuit of excellence. Thank you! 

                        """,
                        style={
                            "font-size":13,
                            "font-family":"montserrat thin", 
                        },
                    ),
                    html.Hr(
                        style={
                            "width": '60%',
                            'borderWidth': "0.5vh",
                            "margin-left": '12rem',
                            "marginTop": '2.4rem',
                            "borderColor": '#33374B',
                            "opacity": '1.0',
                            #'border-style': 'dotted none none',
                        }, 
                    ),
                ], 
                className="m-3 p-3",
                style={
                    'textAlign': 'center',
                    'border-radius': '10px',
                    'width': '50%'
                }   
            ),  className="justify-content-center",
            style={
                'marginTop': '0.5rem',
            },
        ),
    ],
)

# Tab 1 Contents Object- About Contents 
about_tab_contents = html.Div(id="about_id", children=[tab_1_layout, 
                             ])


# ---------------------------------------------------------------NON - WORKING LAYOUT OBJECTS-----------------------------------------------------

# A FEW NON - WORKING OBJECTS

non_working_page2_with_dcc_graphs = html.Div(children=
    [ 
        html.Div(
            [
                html.P(
                    "DATA SCIENCE PROJECTS",
                    style={
                        "font-size": 35.5,
                        "color": '#33374b',
                    },
                ),
                dcc.Markdown(
                    """
                    Machine learning models are powerful tools used to efficiently and effectively perform vital tasks and solve complex problems. 
                    An exponential increase in data across the modern world means organisations from a range of sectors are ready to deploy machine 
                    learning models. These models have a huge range of uses, whether machine learning in finance proactively monitoring bank transfers 
                    for signs of fraud, or machine learning in healthcare powering the next generation of diagnostic tools. 
                    """, 
                    style={
                        "font-family": 'montserrat thin',
                        "font-size": 13.5,
                        "color": '#33374b',
                        "padding": "0px 300px 0px 300px",
                    },
                ),
                html.Div(
                    three_horizontal_bars,
                    style={
                        "margin-left": "-30rem",
                        "textAlign": "center",
                        "padding": "10px 0px 0px 0px",
                    }
                ),
                html.Div(    
                    dbc.RadioItems(
                        [
                            {
                                "label": ['Project 1'], "value": 1,
                            },
                            {
                                "label": ['Project 2'], "value": 2,
                            },
                            {
                                "label": ['Project 3'], "value": 3,
                            },
                            {
                                "label": ['Project 4'], "value": 4,
                            },
                            {
                                "label": ['Project 5'], "value": 5,
                            },
                            {
                                "label": ['Project 6'], "value": 6, "disabled": True,
                            },
                        ],
                        id="projects_id",
                        inline=True, 
                        value=1,
                        className="d-flex align-items-center justify-content-around",
                        label_checked_style={
                            "color": "",
                        },
                        input_checked_style={
                            "background-color": "#DC20DF",
                            "border-color": "#4F3BD0",
                            "font-size": 18,
                        },
                    ),
                    style={
                        "padding": "25px 0px 30px 0px ",
                        'box-shadow': 'rgba(33, 35, 38, 0.1) 0px 10px 10px -10px',
                    },
                ),
            ], className = "header",
            style={
                "textAlign": 'center',
                "padding": "80px 0px 0px 0px",
                "position": "fixed",
                "background-color": 'white',
            },
        ),
        html.Div( className = "content",
            id="projects_page", 
            style={
                "padding": "410px 0px 0px 0px",
                "position": 'sticky',
                'position': '-webkit-sticky',
            },
            
        ),
    ], 
    style={
        "margin-left": "32rem",
        "width": '78.5vw',
        "background-color": '',
    },   
),

old_page2_layout_and_contents_part2 = html.Div(id="page2-container", children=
    [
        html.Div(
            [
                html.Div(children=
                    [
                        html.P(
                            "DATA SCIENCE PROJECTS",
                            style={
                                "font-size": 37,
                                'textAlign': 'center',
                                "padding": '27px 0px 10px 0px',
                                "color": '#33374b',
                                "opacity": '',
                            },
                        ),
                        html.Div(    
                            dbc.RadioItems(
                                [
                                    {
                                        "label":
                                            [
                                                html.Img(
                                                    src="/assets/health_1.png", 
                                                    height=22,
                                                    style={
                                                        "padding-left": 10,
                                                    },
                                                ),
                                                html.Span(
                                                    "Healthcare Reporting", 
                                                    style={
                                                        'font-size': 11,
                                                        "padding-left": 5,
                                                    }
                                                ),
                                            ],
                                        "value": 1,
                                    },
                                    {
                                        "label":
                                            [
                                                html.Img(
                                                    src="/assets/finance.png", 
                                                    height=22,
                                                    style={
                                                        "padding-left": 10,
                                                    },
                                                ),
                                                html.Span(
                                                    "Finance Reporting", 
                                                    style={
                                                        'font-size': 11,
                                                        "padding-left": 5,
                                                    }
                                                ),
                                            ],
                                        "value": 2,
                                    },
                                    {
                                        "label":
                                            [
                                                html.Img(
                                                    src="/assets/senti_2.png", 
                                                    height=22,
                                                    style={
                                                        "padding-left": 10,
                                                    },
                                                ),
                                                html.Span(
                                                    "Sentiment Analysis", 
                                                    style={
                                                        'font-size': 11,
                                                        "padding-left": 5,
                                                    }
                                                ),
                                            ],
                                        "value": 3,
                                    },
                                    {
                                        "label":
                                            [
                                                html.Img(
                                                    src="/assets/shipping_1.png", 
                                                    height=22,
                                                    style={
                                                        "padding-left": 10,
                                                    },
                                                ),
                                                html.Span(
                                                    "Transportation Analysis", 
                                                    style={
                                                        'font-size': 11,
                                                        "padding-left": 5,
                                                    }
                                                ),
                                            ],
                                        "value": 4,
                                    },
                                    {
                                        "label":
                                            [
                                                html.Img(
                                                    src="/assets/real_estate.png", 
                                                    height=22,
                                                    style={
                                                        "padding-left": 10,
                                                    },
                                                ),
                                                html.Span(
                                                    "Real Estate Housing Analysis", 
                                                    style={
                                                        'font-size': 11,
                                                        "padding-left": 5,
                                                    }
                                                ),
                                            ],
                                        "value": 5,
                                    },
                                    {
                                        "label":
                                            [
                                                html.Img(
                                                    src="/assets/edu_3.png", 
                                                    height=22,
                                                    style={
                                                        "padding-left": 10,
                                                    },
                                                ),
                                                html.Span(
                                                    "World Education Reporting", 
                                                    style={
                                                        'font-size': 11,
                                                        "padding-left": 5,
                                                    }
                                                ),
                                            ],
                                        "value": 6,
                                    },
                                ],
                                id="projects_id",
                                inline=True, 
                                value=1,
                                label_checked_style={
                                    "color": "",
                                },
                                input_checked_style={
                                    "background-color": "#DC20DF",
                                    "border-color": "#4F3BD0",
                                    "font-size": 18,
                                },
                                style={
                                    "padding": '0px',
                                    "color": 'white', #"#33374b", #
                                    "font-family": 'montserrat regular',
                                },
                            ), className='d-flex align-items-center justify-content-center',
                            style={
                                "background-color": '#33374b', 
                                "height": '3vh', 
                                "border-radius": '7px',
                                "width": '70%',
                                "margin-left": '17rem',
                                "padding": '20px'
                            },
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div( id="project_1_introduction_id", children=
                                            [
                                                # callback contents 
                                            ], 
                                            style={
                                                "textAlign": 'left',
                                                "margin-left": '1rem',
                                                "text-align": 'justify',
                                            }, 
                                        ),
                                    ], 
                                    style={'background-color': ''}, 
                                ),
                                dbc.Col(
                                    [
                                        html.Div( id="project_1_filter_id", children=
                                            [
                                                # #add filter items as per project description contents
                                            ],
                                            style={
                                                "background-color": '',
                                                "padding": '10px',
                                                "height": '15vh',
                                                'width': '36vw',
                                                "margin-left": '3rem', 
                                                'border-radius': '8px',
                                                'box-shadow': 'rgba(0, 0, 0, 0.09) 0px 0px 0px 1px',
                                            }
                                        ),
                                    ],
                                ),
                            ], 
                            style={
                                'background-color': '',
                                "padding": '50px 0px 0px 0px',
                            }
                        ),
                        html.Div(
                            three_horizontal_bars, #three_horizontal_bars_part2
                            style={
                                "margin-left": "-30rem",
                                "textAlign": "center",
                                "padding": "25px 0px 30px 0px",
                                'box-shadow': 'rgba(33, 35, 38, 0.1) 0px 10px 10px -10px',
                            }
                        ),
                    ], 
                ),
                html.Div(
                    id="projects_page",
                    style={
                        "width": "100%",
                        "maxWidth": "100%", 
                        "overflow": "auto", 
                        'flexShrink': '1', 
                        "maxHeight": "100%",
                        "padding": '40px 0px 20px 0px',
                    },
                ),
            ],
            style={
                "display": "flex", 
                "maxWidth": "100vw", 
                "overflow": "hidden",
                "flexGrow": "1", 
                "maxHeight": "100%", 
                "flexDirection": "column",
            },
        ),
    ], 
    style={
        "display": "flex", 
        "maxWidth": "100vw", 
        "overflow": "hidden", 
        "maxHeight": "100vh",
        "position": "absolute", 
        "width": "78.5vw", 
        "margin-left": '32rem',
    },
)


#_______________________________________________________________INAL IMPORTANT OBJECTS FOR PAGE 2________________________________________________

# FINAL PAGE2 LAYOUT!
page2_layout_and_contents = html.Div(id="page2-container", children=
    [
        html.Div(
            [
                html.Div(children=
                    [
                        html.P(
                            "DATA SCIENCE PROJECTS",
                            style={
                                "font-size": 37,
                                'textAlign': 'center',
                                "padding": '30px 0px 0px 0px',
                                "color": '#33374b',
                                "opacity": '',
                            },
                        ),
                        html.Div(
                            three_horizontal_bars, #three_horizontal_bars_part2
                            style={
                                "margin-left": "-30rem",
                                "textAlign": "center",
                                "padding": "0px 0px 40px 0px",
                            }
                        ),
                        dbc.Col(
                            [
                                html.Div( id="top-section", children=
                                    [
                                        "Add your top contents such as filters, short-descriptions and more"
                                    ],
                                    style={
                                        "background-color": '',
                                        "padding": '10px',
                                        "height": '11vh',
                                        'width': '100%', 
                                        'border-radius': '10px',
                                        'color': 'rgba(51, 55, 75, 0.4)',
                                        'opacity': '0.5',
                                        'justify-content': 'center',
                                        'display': 'flex',
                                        'align-items': 'center',
                                    }
                                ),
                            ], style={"padding": '15px',}
                        ),
                    ], 
                ),
                html.Div(
                    "hidden div",
                    style={
                        "color": 'white',
                        "padding": '10px 0px 0px 0px',
                        'box-shadow': 'rgba(33, 35, 38, 0.1) 0px 10px 10px -10px',
                    },
                ),
                html.Div(
                    [
                        dbc.Row(
                            [    
                                dbc.Col(
                                    dcc.Graph(
                                        figure=fig, 
                                        style={'height': '100%'}
                                    ), 
                                    style={
                                        'background-color': '',
                                        'width': '40%',
                                        'height': '40vh',
                                    }
                                ),
                                dbc.Col(
                                    dcc.Graph(
                                        figure=fig, 
                                        style={'height': '100%'}
                                    ), 
                                    style={
                                        'background-color': '',
                                        'width': '40%',
                                        'height': '40vh',
                                    }
                                ), 
                            ], class_name='d-flex justify-content-between',  
                        ),
                        dbc.Row(
                            [    
                                dbc.Col(
                                    dcc.Graph(
                                        figure=fig, 
                                        style={'height': '100%'}
                                    ), 
                                    style={
                                        'background-color': '',
                                        'width': '40%',
                                        'height': '40vh',
                                    }
                                ),
                                dbc.Col(
                                    dcc.Graph(
                                        figure=fig, 
                                        style={'height': '100%'}
                                    ), 
                                    style={
                                        'background-color': '',
                                        'width': '40%',
                                        'height': '40vh',
                                    }
                                ), 
                            ], class_name='d-flex justify-content-between',  
                        ),
                        dbc.Row(
                            [    
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ),
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ), 
                            ],
                            style={
                                'widht': '100%',
                                'height': '40vh',
                                'margin-top': '40px',
                            }, 
                            class_name='d-flex justify-content-around',    
                        ),
                        dbc.Row(
                            [    
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ),
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ), 
                            ],
                            style={
                                'widht': '100%',
                                'height': '40vh',
                                'margin-top': '40px',
                            }, 
                            class_name='d-flex justify-content-around',    
                        ),
                        dbc.Row(
                            [    
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ),
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ), 
                            ],
                            style={
                                'widht': '100%',
                                'height': '40vh',
                                'margin-top': '40px',
                            }, 
                            class_name='d-flex justify-content-around',    
                        ),
                        dbc.Row(
                            [    
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ),
                                dbc.Col(
                                    width=5,
                                    style={
                                        'widht': '40%',
                                        'height': '30vh',
                                        'background-color': '#F3F5FC',
                                        'border-radius': '10px',
                                    },
                                ), 
                            ],
                            style={
                                'widht': '100%',
                                'height': '40vh',
                                'margin-top': '40px',
                            }, 
                            class_name='d-flex justify-content-around',    
                        ),
                        dbc.Row(
                            [    
                                html.Div(
                                    "Thank you so much for your kind review and visit!",
                                    style={
                                        'border-radius': '10px',
                                        'widht': '50%',
                                        'height': '40vh',
                                        'background-color': '#F3F5FC',
                                        'color': 'rgba(79, 59, 208, 0.8)',
                                        # 'opacity': '0.8',
                                        'font-size': '40px',
                                    },
                                    className='d-flex justify-content-center align-items-center',  
                                ),
                            ], 
                            style={
                                'widht': '80%',
                                'height': '40vh',
                                'margin-top': '40px',
                                'padding': '0px 50px 50px 50px',
                                'margin-bottom': '140px',
                            },
                            class_name='d-flex justify-content-between',   
                        ),
                    ],
                    style={
                        "width": "100%",
                        "overflow": "auto", 
                        'margin-top': '40px',
                        "padding": '2px 0px 20px 0px',
                        'background-color': '',
                    },
                ),
            ],
        ),
    ], 
    style={
        "maxWidth": "100vw", 
        "overflow": "auto", 
        "maxHeight": "100vh",
        "position": "absolute", 
        "width": "78.5vw", 
        "margin-left": '32rem',
    },
)




#-----------------------------------------------------------------------------------------------------PAGES - Callbacks-------------------------------------------------------------------------------------------


@app.callback(
    Output("page-content", "children"), 
    [
        Input("url", "pathname"),
    ]
)

def render_page_content(pathname):
    # PAGE 01
    if pathname == "/":
        return  page1_layout_and_contents
    # PAGE 02
    elif pathname == "/ds-projects":
        return page2_layout_and_contents
    # PAGE 03
    elif pathname == "/help-me-improve":
        return html.P(
                "Oh cool, this is page 3!........and thanks so much for visiting!", 
                style={
                    "width": "78.5vw", 
                    "margin-left": '32rem',
                    'background-color': '',
                    'height': '98vh',
                    'color': 'rgba(79, 59, 208, 0.8)',
                    # 'opacity': '0.8',
                    'font-size': '40px',
                },
                className='d-flex justify-content-center align-items-center',
            )
    
    # If the user tries to reach a different page, return a 404 message
    else:
        return html.Div( children=[
                html.H1(
                    "404: Not found", 
                    className="text-danger"
                ),
                html.Hr(),
                html.P(
                    f"The pathname {pathname} was not recognised..." ,
                ),
            ],
            className="p-3 bg-light rounded-3",
            style={"textAlign": 'center'},
    )

# ---------------------------------------------------------PAGE 1 TABS - CALLBACKS -------------------------------------------------------------

@app.callback(
    Output("tab-content", "children"), 
    [
        Input("tabs", "active_tab"),
    ],
)
def switch_tab(at):
    # TAB 01
    if at == "intro":
        tab1_content = about_tab_contents
        return tab1_content



# PAGE 1 TABS - BUTTONS CALLBACKS : _____________________________
@app.callback(
    Output('tabs', 'active_tab'),
    [
        Input('click_button', 'n_clicks'),
    ],
    prevent_initial_call=True
)
def get_tabs(c):
    # if c: 
    #     return 'intro'
    return 'intro'   



# RUN THE APP
if __name__ == "__main__":
    app.run_server(debug=True, port=4442, use_reloader=False)
                


