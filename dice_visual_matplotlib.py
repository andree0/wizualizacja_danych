from matplotlib import pyplot as plt

from die import Die


# Utworzenie kośći typu D8
die_1 = Die()
die_2 = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liśćie.
results = [die_1.roll() + die_2.roll() for _ in range(1000000)]

# Analiza wyników

# Maksymalny możliwy wynik
max_result = die_1.num_sides + die_2.num_sides

# Wszystkie możliwe wyniki
scores = range(2, max_result + 1)

# Częstotliwość występowania danego wyniku
frequencies = [results.count(value) for value in scores]

# Określenie stylu wykresu
plt.style.use('seaborn')

# Określenie wielkości wykresu poprzez parametry figsize i dpi.
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
ax.bar(scores, frequencies)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Wynik rzucania dwiema kośćmi D6 milion razy", fontsize=24)
ax.set_xlabel("Wynik", fontsize=14, )
ax.set_ylabel("Częstotliwość występowania wartości", fontsize=14)

# Zdefiniowanie wielkośći etykiet
ax.set_xticks(scores)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.ticklabel_format(useOffset=False, style='plain')

plt.show()