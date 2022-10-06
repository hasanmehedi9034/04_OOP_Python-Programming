fibo_series = [0, 1]

for i in range(2, 11):
    fibo_series.append(fibo_series[i - 1] + fibo_series[i - 2])

for element in fibo_series:
    print(element, end=" ")
