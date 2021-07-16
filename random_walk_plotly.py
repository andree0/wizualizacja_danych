import re
from matplotlib.colors import Colormap
import numpy as np
from plotly.graph_objs import Heatmap, Layout, Scatter
from plotly import offline

from random_walk import RandomWalk

# Przygotowanie danych błądzenia losowego i wyświetlanie punktów.
rw = RandomWalk(50000)
rw.fill_walk()

# Wizualizacja wyników
data = [Scatter(x=rw.x_values, y=rw.y_values, mode='markers',
    marker=dict(
            size=3,
            colorscale='Blues',
            color=[i for i in range(rw.num_points)]
        )
    )]

# Ukryci osi i siatki tła
hide_axis = {
    'showticklabels': False, 
    'showgrid': False,
    'zeroline': False,
    'showline': False
    }

my_layout = Layout(
    title='Wykres błądzenia losowego',
    xaxis=hide_axis,
    yaxis=hide_axis
    
)
offline.plot({'data': data, 'layout': my_layout}, filename='random_walk.html')