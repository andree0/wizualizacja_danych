from matplotlib import pyplot as plt
from random import choice


class RandomWalk():

    def __init__(self, num_points=5000) -> None:
        """Inicjalizacja atrybutów błądzenia."""
        self.num_points = num_points

        #punkt początkowy ma współrzędne (0, 0)
        self.x_values = [0]
        self.y_values = [0]
    
    @staticmethod
    def get_step():
        """Generowanie wartości kroku.
        Zwraca wartość kroku, czyli iloczyn kierunku i dystansu."""
        return choice([1, -1]) * choice(range(0, 9))

    def fill_walk(self):
        """Wygenerowanie wszystkich punktów dla błądzenia losowego."""

        # Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby punktów.
        while len(self.x_values) < self.num_points:

            # Ustalenie kierunku oraz odległości do pokonania w tym kierunku.
            x_step = self.get_step()
            y_step = self.get_step()

            # Odrzucenie ruchów, które prowadzą donikąd.
            if x_step == 0 and y_step == 0:
                continue

            # Ustalenie nastepnych wartości X i Y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


if __name__ == '__main__':

    while True:
        # Przygotowanie danych błądzenia losowego i wyświetlanie punktów.
        rw = RandomWalk(50000)
        rw.fill_walk()

        # Wyświetlanie punktóœ błądzenia losowego.
        plt.style.use('classic')
        point_numbers = range(rw.num_points)

        # Określenie wielkości wykresu poprzez parametry figsize i dpi.
        fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
        ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
            cmap=plt.cm.Blues, edgecolors='none', s=1)

        # Podkreślenie pierwszego i ostatniego punktu bładzenia losowego.
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

        # Ukrycie osi.
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.show()
        keep_running = input("Utworzyć kolejne bładzenie losowe ? (t/n): ")
        if keep_running == 'n':
            break

