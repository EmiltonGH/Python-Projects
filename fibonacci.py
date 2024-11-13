def fibonacci_series(n):
    if n <= 0:
        return "Number should be a positive integer."
    series = [0,1]
    for i in range(2,n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    return series[:n]

print(fibonacci_series(10))