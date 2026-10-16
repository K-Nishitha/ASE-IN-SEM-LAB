# Movie Ticket Booking System

A small Python project demonstrating a movie-ticket workflow and automated checks with GitHub Actions.

## Requirements covered

- **Movie/show selection:** `show_movies()`
- **Seat selection:** `available_seats()` and `book_tickets()`
- **Payment:** `pay()`
- **Screen management:** `add_screen()` and `screen_status()`
- **Refund:** `refund()` releases the seats after a successful refund
- **Unit tests:** tests in `tests/test_booking.py`
- **GitHub Actions CI:** runs on every push and pull request, checks style with Ruff, then runs unit tests

> This is an educational, in-memory demo. Payment is simulated; it does not connect to a real payment gateway.

## Run locally

Python 3.12 or later is recommended.

```bash
python main.py
```

## Run unit tests

```bash
python -m unittest discover -s tests -v
```

## Run linting

```bash
python -m pip install ruff
ruff check .
```

## Demonstration workflow

1. Add screens and assign movies.
2. Display available movies.
3. View available seats on a selected screen.
4. Book seats and calculate the ticket amount.
5. Mark the booking as paid.
6. Display screen availability.
7. Refund the paid booking; the seats become available again.

## GitHub Actions setup

1. Create a GitHub repository and upload/push this project.
2. Keep the workflow at `.github/workflows/ci.yml`.
3. Every `git push` triggers **Python CI**. Pull requests trigger it too.
4. Open the repository's **Actions** tab to see the workflow run. A green check means linting and tests passed; a red cross means a check failed. Open the run and inspect the failing step/log.

Example Git commands:

```bash
git init
git add .
git commit -m "Add movie ticket booking project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own repository URL.
