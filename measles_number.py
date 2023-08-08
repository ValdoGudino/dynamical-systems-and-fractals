def f(p: float, k: float):
    return p + k * p * (1 - p)


def main():
    print('Calculation of Measles-Values')
    print('----------------------------\n\n')

    population: float = 0.3
    feedback: float = 2.3
    maximal_iteration: int = 30

    for i in range(maximal_iteration):
        population = f(population, feedback)
        print(
            f'After {i} Iterations p has the value : {round(population, 4):.4f}')


if __name__ == '__main__':
    main()
