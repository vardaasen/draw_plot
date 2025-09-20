import ipywidgets as widgets
from IPython.display import display

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import scipy.stats as stats

def draw_plot(b):
    
    GRAPH_DATA = {min: 0,max: 10}
    GRAPH_MEAN = 0
    GRAPH_DATA_STEP = 0.1
    GRAPH_STD = GRAPH_DATA_STEP
    EMPIRICAL_Y_LIM = {min: (-4 * GRAPH_STD) 
                       + min(np.sin(np.arange(GRAPH_DATA[min],
                                              GRAPH_DATA[max],
                                              GRAPH_DATA_STEP))),
                       max: (4 * GRAPH_STD) 
                       + max(np.sin(np.arange(GRAPH_DATA[min],
                                              GRAPH_DATA[max],
                                              GRAPH_DATA_STEP)))
                      }
    data = {
        'X': np.arange(GRAPH_DATA[min], 
                       GRAPH_DATA[max], 
                       GRAPH_DATA_STEP),
        'Y': np.sin(np.arange(GRAPH_DATA[min], 
                              GRAPH_DATA[max], 
                              GRAPH_DATA_STEP)) 
        + np.random.normal(GRAPH_MEAN, 
                           GRAPH_STD, 
                           len(np.arange(GRAPH_DATA[min], 
                                         GRAPH_DATA[max], 
                                         GRAPH_DATA_STEP)))
        }

    df = pd.DataFrame(data)

    slope, intercept, r_value, p_value, std_err = stats.linregress(df['X'], df['Y'])
    regression_line = slope * df['X'] + intercept
    formula_text = f'y = {slope:.2f}x {intercept:+.2f}'

    ax.clear()
    ax.plot(df['X'], df['Y'], label='Original Data')
    ax.plot(df['X'], regression_line, color='red', linestyle='--', label='Linear Regression')
    ax.set_title('Sine Wave with Noise and Regression')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()
    ax.set_xlim(GRAPH_DATA[min], GRAPH_DATA[max])
    ax.set_ylim(EMPIRICAL_Y_LIM[min], EMPIRICAL_Y_LIM[max])
    ax.text(0.05, 
            0.95, 
            formula_text, 
            transform=ax.transAxes,
            fontsize=12,
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.5',
                      fc='wheat',
                      alpha=0.5))
    
    fig.canvas.draw()

%matplotlib widget

fig, ax = plt.subplots(figsize=(5,4))
ax.set_title("Here is the button you click")

plot_button = widgets.Button(description="Generate and Display Graph")
plot_button.on_click(draw_plot)
display(plot_button)

draw_plot(None)
