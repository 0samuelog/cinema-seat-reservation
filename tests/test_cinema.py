import json
import os
import tempfile
import pytest
from main import Cinema


class TestCinema:
    def test_init_default(self):
        cinema = Cinema()
        assert cinema.num_seats == 8
        assert cinema.seats == [0] * 8
        assert cinema.data_file == 'seats.json'

    def test_load_seats_existing_file(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump([1, 0, 1, 0], f)
            temp_file = f.name
        try:
            cinema = Cinema(num_seats=4, data_file=temp_file)
            assert cinema.seats == [1, 0, 1, 0]
        finally:
            os.unlink(temp_file)

    def test_load_seats_no_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = os.path.join(temp_dir, 'nonexistent.json')
            cinema = Cinema(num_seats=5, data_file=data_file)
            assert cinema.seats == [0] * 5

    def test_save_seats(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_file = f.name
        try:
            cinema = Cinema(num_seats=3, data_file=temp_file)
            cinema.seats = [1, 0, 1]
            cinema.save_seats()
            with open(temp_file, 'r') as f:
                data = json.load(f)
            assert data == [1, 0, 1]
        finally:
            os.unlink(temp_file)

    def test_reserve_seat_valid_free(self):
        cinema = Cinema(num_seats=4)
        result = cinema.reserve_seat(2)
        assert result is True
        assert cinema.seats[1] == 1

    def test_reserve_seat_valid_occupied(self):
        cinema = Cinema(num_seats=4)
        cinema.seats[1] = 1
        result = cinema.reserve_seat(2)
        assert result is False
        assert cinema.seats[1] == 1

    def test_reserve_seat_invalid(self):
        cinema = Cinema(num_seats=4)
        result = cinema.reserve_seat(5)
        assert result is False
        assert cinema.seats == [0] * 4

    def test_cancel_reservation_valid_occupied(self):
        cinema = Cinema(num_seats=4)
        cinema.seats[1] = 1
        result = cinema.cancel_reservation(2)
        assert result is True
        assert cinema.seats[1] == 0

    def test_cancel_reservation_valid_free(self):
        cinema = Cinema(num_seats=4)
        result = cinema.cancel_reservation(2)
        assert result is False
        assert cinema.seats[1] == 0

    def test_cancel_reservation_invalid(self):
        cinema = Cinema(num_seats=4)
        result = cinema.cancel_reservation(5)
        assert result is False

    def test_show_free_seats(self, capsys):
        cinema = Cinema(num_seats=4)
        cinema.seats = [1, 0, 1, 0]
        cinema.show_free_seats()
        captured = capsys.readouterr()
        assert "2 4" in captured.out
        assert "2 cadeiras estão livres!" in captured.out

    def test_calculate_summary(self, capsys):
        cinema = Cinema(num_seats=4)
        cinema.seats = [1, 0, 1, 0]
        cinema.calculate_summary()
        captured = capsys.readouterr()
        assert "Total de cadeiras: 4" in captured.out
        assert "Livres: 2 | Ocupadas: 2" in captured.out
