Nail_style = ['Шеллак', 'Френч', 'Обычный лак', 'Гель-лак', 'Акрил']
Price = [2000, 1500, 1000, 3000, 3500]
Week = [4, 5, 4, 8, 6]

total_visits = sum(Week)

total_revenue = 0
for i in range(len(Nail_style)):
    revenue = Week[i] * Price[i]
    print(f"Выручка по {Nail_style[i]}: {revenue}")
    total_revenue += revenue

print(f"Общая выручка салона: {total_revenue}")

avg_revenue_per_day = total_revenue / 7
print(f"Средняя выручка в день: {avg_revenue_per_day:.2f}")
