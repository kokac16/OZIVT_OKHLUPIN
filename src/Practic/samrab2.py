results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

best_results = sorted(results)[:3]

worst_results = sorted(results)[-3:]

above_10_results = [result for result in results if result >= 10]

print("Три лучших результата:", best_results)
print("Три худших результата:", worst_results)
print("Все результаты начиная с 10:", above_10_results)