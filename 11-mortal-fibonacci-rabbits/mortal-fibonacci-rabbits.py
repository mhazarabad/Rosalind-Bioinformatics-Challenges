
def Mortal_Fibonacci_Rabbits(cycle, mortality_age, offsprings=1):
    from collections import deque
    """
    ## params
        cycle: an integer represents the number of months
        mortality_age: an integer represents the number of months that rabbits will live
    """
    population=deque([1,1])
    current_fibonachi=3
    not_productive=population[0]
    productive=population[1]
    dead=0
    next_population=0
    while current_fibonachi<cycle+1:
        next_population=not_productive*offsprings+productive
        if len(population)>=mortality_age:# if the population is greater than the mortality age, then we need to remove the dead rabbits
            dead=population[0]
            next_population=next_population-dead
        if len(population)>=mortality_age+1:# if the population is greater than the mortality age, then we need to remove the dead rabbits
            population.popleft()

        population.append(next_population)

        not_productive,productive=productive,next_population
        current_fibonachi+=1
    return population[-1]

print(Mortal_Fibonacci_Rabbits(cycle=84,mortality_age=19,offsprings=1))
