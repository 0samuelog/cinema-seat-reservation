import json
import os


class Cinema:
    """A class to manage cinema seat reservations."""

    def __init__(self, num_seats=8, data_file='seats.json'):
        """Initialize the cinema with a given number of seats and data file."""
        self.num_seats = num_seats
        self.data_file = data_file
        self.seats = self.load_seats()

    def load_seats(self):
        """Load seat data from file or initialize to all free."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return [0] * self.num_seats

    def save_seats(self):
        """Save current seat data to file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.seats, f)

    def show_seats(self):
        """Display the current status of all seats."""
        print("- Cadeiras:")
        for i in range(len(self.seats)):
            status = "L" if self.seats[i] == 0 else "O"
            print(f"[{i + 1}: {status}] ", end=" ")
        print()

    def reserve_seat(self, seat_num):
        """Reserve a seat if available. Returns True if successful."""
        if 1 <= seat_num <= self.num_seats:
            pos = seat_num - 1
            if self.seats[pos] == 0:
                self.seats[pos] = 1
                self.save_seats()
                print(f"Cadeira {seat_num} reservada com sucesso!")
                return True
            else:
                print("Essa cadeira já está reservada, selecione outra.")
                return False
        else:
            print("Número da cadeira inválido!")
            return False

    def cancel_reservation(self, seat_num):
        """Cancel reservation for a seat if occupied. Returns True if successful."""
        if 1 <= seat_num <= self.num_seats:
            pos = seat_num - 1
            if self.seats[pos] == 1:
                self.seats[pos] = 0
                self.save_seats()
                print(f"Reserva da cadeira {seat_num} cancelada com sucesso!")
                return True
            else:
                print("Essa cadeira não está ocupada.")
                return False
        else:
            print("Número da cadeira inválido!")
            return False

    def show_free_seats(self):
        """Display all free seats."""
        free_seats = [i + 1 for i, s in enumerate(self.seats) if s == 0]
        print("- Cadeiras livres: ", end=" ")
        print(" ".join(map(str, free_seats)))
        if not free_seats:
            print("Nenhuma cadeira está livre!")
        else:
            print(f"{len(free_seats)} cadeiras estão livres!")

    def calculate_summary(self):
        """Display a summary of total, free, and occupied seats."""
        free = sum(1 for s in self.seats if s == 0)
        occupied = self.num_seats - free
        print("- Resumo:")
        print()
        print(f"Total de cadeiras: {self.num_seats}")
        print("-----------------------")
        print(f"Livres: {free} | Ocupadas: {occupied}")
        print()


def menu():
    print("\n===================")
    print("SISTEMA - CINEMA")
    print("===================\n")
    print("1 - Mostrar cadeiras")
    print("2 - Reservar cadeira")
    print("3 - Cancelar reserva")
    print("4 - Mostrar livres")
    print("5 - Calcular resumo")
    print("0 - Sair\n")


def main():
    cinema = Cinema()
    while True:
        menu()
        try:
            opcao = int(input("- Escolha uma opção: "))
            print()
        except ValueError:
            print("Insira apenas números!")
            continue

        if opcao == 1:
            cinema.show_seats()
        elif opcao == 2:
            try:
                seat = int(input(f"- Insira o número da cadeira (1 a {cinema.num_seats}): "))
                cinema.reserve_seat(seat)
            except ValueError:
                print("Insira apenas números!")
        elif opcao == 3:
            try:
                seat = int(input(f"- Insira o número da cadeira (1 a {cinema.num_seats}): "))
                cinema.cancel_reservation(seat)
            except ValueError:
                print("Insira apenas números!")
        elif opcao == 4:
            cinema.show_free_seats()
        elif opcao == 5:
            cinema.calculate_summary()
        elif opcao == 0:
            print("Desligando o sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
