import plotly.express as px
import numpy as np
import pandas as pd


def f(p: float, k: float):
    return p + k * p * (1 - p)


def small_k_value_set():
    population: float = 0.0
    p: float = 0.3

    feedback_target: float = 3.0
    feedback_step: float = 0.5

    maximal_iteration: int = 10

    d: list = []

    for k in np.arange(0.5, feedback_target + feedback_step, feedback_step):
        population = p
        for i in range(maximal_iteration):
            population = f(population, k)
            d.append([k, population])

    df = pd.DataFrame(
        data=d, columns=['feedback', 'terminal_population'])
    fig = px.scatter(df, x='feedback',  y='terminal_population')
    fig.update_traces(marker=dict(size=5, line=dict(width=1, color="Black")),
                      selector=dict(mode='markers'))
    fig.update_layout(xaxis_range=[0.4, 3.1], yaxis_range=[0, 1.5])
    fig.show()


def larger_k_value_set():
    population: float = 0.0
    p: float = 0.3

    feedback_target: float = 3.0
    feedback_step: float = 0.001

    maximal_iteration: int = 50

    d: list = []

    for k in np.arange(0.5, feedback_target + feedback_step, feedback_step):
        population = p
        for i in range(maximal_iteration):
            population = f(population, k)
            d.append([k, population])

    df = pd.DataFrame(
        data=d, columns=['feedback', 'terminal_population'])
    fig = px.scatter(df, x='feedback',  y='terminal_population')
    fig.update_traces(marker=dict(size=1, line=dict(width=1, color="Black")),
                      selector=dict(mode='markers'))
    fig.update_layout(xaxis_range=[0.5, 3.0], yaxis_range=[0, 1.5])
    fig.show()


def bifurcation():
    population: float = 0.0
    p: float = 0.3

    feedback_target: float = 3.0
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


def main():
    print('Calculation of Measles-Values')
    print('----------------------------\n\n')
    small_k_value_set()
    larger_k_value_set()
    bifurcation()


if __name__ == '__main__':
    main()
