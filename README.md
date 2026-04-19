# Cinema Seat Reservation System

A simple Python console application for managing seat reservations in a cinema.

## Features

- Display available and occupied seats
- Reserve a seat
- Cancel a reservation
- Show free seats
- Calculate summary of seats
- Persistent storage of seat data using JSON

## Installation

1. Ensure you have Python 3.14+ installed.
2. Clone the repository.
3. Install dependencies: `uv sync`
4. For development: `uv sync --group dev`

## How to Run

Run the application: `uv run python main.py`

## Testing

Run tests: `uv run pytest`

## Project Structure

- `main.py`: Main application code with Cinema class
- `tests/`: Unit tests
- `seats.json`: Persistent seat data (created automatically)

## Technologies Used

- Python 3.14+
- JSON for data persistence
- Pytest for testing

## License

This project is open source. Feel free to contribute!
