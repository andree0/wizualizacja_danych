from matplotlib import pyplot as plt

# dane wejściowe i wyjściowe
x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]
       
# Zdefiniowanie stylu wykresu i utworzenie go
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

# Zdefiniowanie wielkośći etykiet
ax.tick_params(axis='both', which='major', labelsize=14)
ax.ticklabel_format(useOffset=False, style='plain')

# Wyświetlenie wykresu
plt.show()
