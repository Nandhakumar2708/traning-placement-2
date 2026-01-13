class Solution(object):
    def maximumPopulation(self, logs):
        arr = []
        for birth, death in logs:
            arr.append((birth, 1))
            arr.append((death, -1))
        arr.sort()
        early_year, max_population, sum_population = -1, 0, 0
        for year, count in arr:
            sum_population += count
            if sum_population > max_population:
                early_year = year
                max_population = sum_population
        return early_year
