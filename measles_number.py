import plotly.express as px
import numpy as np
import pandas as pd


def f(p: float, k: float):
    return p + k * p * (1 - p)


def main():
    print('Calculation of Measles-Values')
    print('----------------------------\n\n')

    population: float = 0.0
    population_target: float = 1.0
    popluation_step: float = 0.01
    p: float = 0.3

    feedback: float = 0.0
    feedback_target: float = 3.0
    feedback_step: float = 0.05

    maximal_iteration: int = 30

    d: list = []

    for p in np.arange(0, population_target, popluation_step):
        population = p
        for k in np.arange(0.5, feedback_target, feedback_step):
            for i in range(maximal_iteration):
                population = f(population, k)
                d.append([k, p, population])

    df = pd.DataFrame(
        data=d, columns=['feedback', 'initial_population', 'terminal_population'])
    fig = px.scatter_3d(df, x='feedback', y='initial_population',
                        z='terminal_population')
    fig.show()


if __name__ == '__main__':
    main()
