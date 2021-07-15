from random import randint

from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die():
    """Klasa przedstawiająca pojedynczą kość do gry."""

    def __init__(self, num_sides=6) -> None:
        """Przyjęcie założenia, że kości do gry ma postać sześcianu."""
        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartośći z zakresu 1 do liczby ścianek,
        które ma kość do gry."""
        return randint(1, self.num_sides)


if __name__ == '__main__':

    # Utworzenie kości typu D6
    die = Die()

    # Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
    results = [die.roll() for _ in range(1000)]

    # Analiza wyników
    frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

    # Wizualizacja wyników
    x_values = list(range(1, die.num_sides + 1))
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Wynik'}
    y_axis_config = {'title': 'Częstotliwość występowania wartości'}
    my_layout = Layout(
        title='Wynik rzucania pojedynczą kością D6 tysiąc razy',
        xaxis=x_axis_config, yaxis=y_axis_config
    )
    offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
