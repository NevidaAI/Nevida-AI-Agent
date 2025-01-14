import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from gpu_monitor import GPUMonitor
import time

app = dash.Dash(__name__)
monitor = GPUMonitor()

app.layout = html.Div(children=[
    html.H1("Nevida AI - GPU Performance Dashboard"),
    dcc.Graph(id='gpu-metrics'),
    dcc.Interval(id='interval-update', interval=2000, n_intervals=0)  # 每2秒更新一次
])

@app.callback(
    Output('gpu-metrics', 'figure'),
    [Input('interval-update', 'n_intervals')]
)
def update_graph(n_intervals):
    metrics = monitor.get_gpu_metrics()
    figure = go.Figure()

    figure.add_trace(go.Bar(
        x=list(metrics.keys()),
        y=[metrics['temperature']],
        name='Temperature (°C)',
        marker_color='red'
    ))
    figure.add_trace(go.Bar(
        x=list(metrics.keys()),
        y=[metrics['gpu_utilization']],
        name='Utilization (%)',
        marker_color='blue'
    ))
    figure.add_trace(go.Bar(
        x=list(metrics.keys()),
        y=[metrics['power_draw']],
        name='Power Draw (W)',
        marker_color='green'
    ))

    figure.update_layout(
        title="Real-Time GPU Metrics",
        xaxis_title="Metrics",
        yaxis_title="Values",
        barmode='group'
    )

    return figure

if __name__ == "__main__":
    app.run_server(debug=True)
