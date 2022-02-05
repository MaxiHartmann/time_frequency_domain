import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np
pi = np.pi

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6("INPUT: Fouriercoefficients"),
    html.Div("f(f) = a0/2 + ak cos(kt) + bk sin(kt)"),
    html.Div(["k = ", dcc.Input(id='k', value=3.0, type='number') ]),
    html.Br(),
    html.Div(["a0 = ", dcc.Input(id='a0', value=1.0, type='number') ]),
    html.Div(
        [
            "a1 = ", 
            dcc.Slider(min=-100, max=100, step=1, value=0, id='a1', tooltip={"placement": "bottom", "always_visible": True}),
            "b1 = ",
            dcc.Slider(min=-100, max=100, step=1, value=0, id='b1', tooltip={"placement": "bottom", "always_visible": True}),
        ]
    ),
    html.Div(
        [
            "a2 = ", 
            dcc.Input(id='a2', value=0.0, type='number'),
            "b2 = ",
            dcc.Input(id='b2', value=0.0, type='number'),
        ]
    ),
    html.Div(
        [
            "a3 = ", 
            dcc.Input(id='a3', value=0.0, type='number'),
            "b3 = ",
            dcc.Input(id='b3', value=0.0, type='number'),
        ]
    ),
    html.Div(
        [
            "a4 = ", 
            dcc.Input(id='a4', value=0.0, type='number'),
            "b4 = ",
            dcc.Input(id='b4', value=0.0, type='number'),
        ]
    ),
    html.Div(
        [
            "a5 = ", 
            dcc.Input(id='a5', value=0.0, type='number'),
            "b5 = ",
            dcc.Input(id='b5', value=0.0, type='number'),
        ]
    ),
    html.Div(id='my-output'),
    dcc.Graph(id='graph')
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Output(component_id='graph', component_property='figure'),
    Input(component_id='k', component_property='value'),
    Input(component_id='a0', component_property='value'),
    Input(component_id='a1', component_property='value'),
    Input(component_id='a2', component_property='value'),
    Input(component_id='a3', component_property='value'),
    Input(component_id='a4', component_property='value'),
    Input(component_id='a5', component_property='value'),
    Input(component_id='b1', component_property='value'),
    Input(component_id='b2', component_property='value'),
    Input(component_id='b3', component_property='value'),
    Input(component_id='b4', component_property='value'),
    Input(component_id='b5', component_property='value')
)
def update_output_div(k, a0, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5):
    text="""f(t) = {} / 2 
    + {}*cos(1*t) + {}*sin(1*t)
    + {}*cos(2*t) + {}*sin(2*t)
    + {}*cos(3*t) + {}*sin(3*t)
    + {}*cos(4*t) + {}*sin(4*t)
    + {}*cos(5*t) + {}*sin(5*t)
    """.format(a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5)
    
    # xmin=pi*xmin
    # xmax=pi*xmax

    # t=np.linspace(xmin, xmax, samples)
    t=np.linspace(-2*pi, 2*pi, 500)
    y = a0/2. + \
        a1*np.cos(1*t) + b1*np.cos(1*t) + \
        a2*np.cos(2*t) + b2*np.cos(2*t) + \
        a3*np.cos(3*t) + b3*np.cos(3*t) + \
        a4*np.cos(4*t) + b4*np.cos(4*t) + \
        a5*np.cos(5*t) + b5*np.cos(5*t)
    fig=go.Figure()
    fig.add_trace(
        go.Scatter(
            x=t, 
            y=y, 
            mode="markers+lines"
        )
    )

    #define data for annotations
    # xa = [-pi, -pi/2, 0, pi/2, pi]
    # textxa = ['$-\\pi$]', '$-\\pi/2$]', '$0$]', '$\\pi/2$]', '$\\pi$]']

    # axis_style=dict(
    #     showline=False, 
    #     zeroline=True, 
    #     # showticklabels=False, 
    #     # ticks='',
    #     showgrid=False)

    # fig.update_layout(
    #     width=1000, height=700,
    #     font_size=13,
    #     xaxis = axis_style,
    #     yaxis = axis_style,
    #     xaxis_range=[xmin, xmax],
    #     yaxis_range=[ymin, ymax],
    #     # hovermode='closest',
    #     # legend_x= 0,
    #     # legend_y=0.85
    # )

    return text, fig


if __name__ == '__main__':
    app.run_server(debug=True)
