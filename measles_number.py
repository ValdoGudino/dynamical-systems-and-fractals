import plotly.express as px
import numpy as np
import pandas as pd


def f(p: float, k: float):
    return p + k * p * (1 - p)


def main():
    print('Calculation of Measles-Values')
    print('----------------------------\n\n')

    population: float = 0.0
    p: float = 0.3

    feedback_target: float = 3.5
    feedback_step: float = 0.0001

    maximal_iteration: int = 300

    d: list = []

    for k in np.arange(1.90, feedback_target + feedback_step, feedback_step):
        population = p
        skip = 275
        for i in range(maximal_iteration):
            population = f(population, k)
            if skip > 0:
                skip -= 1
            if skip == 0:
                d.append([k, population])

    df = pd.DataFrame(
        data=d, columns=['feedback', 'terminal_population'])
    fig = px.scatter(df, x='feedback',  y='terminal_population')
    fig.update_traces(marker=dict(size=1, line=dict(width=1, color="Black")),
                      selector=dict(mode='markers'))
    fig.update_layout(xaxis_range=[1.90, 3], yaxis_range=[0, 1.5])
    fig.show()


if __name__ == '__main__':
    main()
