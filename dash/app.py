import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np
pi = np.pi

def dft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div("f(t) = a1*cos(2pi*(f1*t)) + a2*cos(2*pi(f2*t))"),
    html.Div(["a1 = ", dcc.Input(id='a1', value=1.0, type='number') ]),
    html.Div(["f1 = ", dcc.Input(id='f1', value=1.0, type='number') ]),
    html.Div(["a2 = ", dcc.Input(id='a2', value=0.0, type='number') ]),
    html.Div(["f2 = ", dcc.Input(id='f2', value=0.0, type='number') ]),
    html.Br(),
    html.Div(["xmin = ", dcc.Input(id='xmin', value=0.0, type='number') ]),
    html.Div(["xmax = ", dcc.Input(id='xmax', value=1.0, type='number') ]),
    html.Div(["ymin = ", dcc.Input(id='ymin', value=-1.0, type='number') ]),
    html.Div(["ymax = ", dcc.Input(id='ymax', value=1.0, type='number') ]),
    html.Div(["samples = ", dcc.Input(id='samples', value=1000.0, type='number') ]),
    html.Div(id='my-output'),
    dcc.Graph(id='graph')
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Output(component_id='graph', component_property='figure'),
    Input(component_id='a1', component_property='value'),
    Input(component_id='f1', component_property='value'),
    Input(component_id='a2', component_property='value'),
    Input(component_id='f2', component_property='value'),
    Input(component_id='xmin', component_property='value'),
    Input(component_id='xmax', component_property='value'),
    Input(component_id='ymin', component_property='value'),
    Input(component_id='ymax', component_property='value'),
    Input(component_id='samples', component_property='value')
)
def update_output_div(a1, f1, a2, f2, xmin, xmax, ymin, ymax, samples):
    text="f(t) = {}*cos(2pi*({}*t)) + {}*cos(2*pi({}*t))".format(a1, f1, a2, f2)
    xmin=pi*xmin
    xmax=pi*xmax

    t=np.linspace(xmin, xmax, samples)
    y=a1*np.cos(2*pi*f1*t) + a2*np.cos(2*pi*f2*t)
    fig=go.Figure()
    fig.add_trace(
        go.Scatter(
            x=t, 
            y=y, 
            mode="markers+lines"
        )
    )

    #define data for annotations
    xa = [-pi, -pi/2, 0, pi/2, pi]
    textxa = ['$-\\pi$]', '$-\\pi/2$]', '$0$]', '$\\pi/2$]', '$\\pi$]']

    axis_style=dict(
        showline=False, 
        zeroline=True, 
        # showticklabels=False, 
        # ticks='',
        showgrid=False)

    fig.update_layout(
        width=1000, height=700,
        font_size=13,
        xaxis = axis_style,
        yaxis = axis_style,
        xaxis_range=[xmin, xmax],
        yaxis_range=[ymin, ymax],
        # hovermode='closest',
        # legend_x= 0,
        # legend_y=0.85
    )

    return text, fig


if __name__ == '__main__':
    app.run_server(debug=True)
