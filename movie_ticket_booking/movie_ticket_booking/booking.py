"""Simple in-memory movie ticket booking demo."""

from dataclasses import dataclass, field


@dataclass
class Screen:
    screen_id: int
    movie: str
    total_seats: int
    booked_seats: set[str] = field(default_factory=set)


@dataclass
class Booking:
    booking_id: int
    screen_id: int
    movie: str
    seats: list[str]
    amount: float
    paid: bool = False
    refunded: bool = False


class MovieTicketBooking:
    """Supports movie selection, seat selection, payment, screens, and refunds."""

    def __init__(self, ticket_price: float = 150.0) -> None:
        if ticket_price <= 0:
            raise ValueError("Ticket price must be positive.")
        self.ticket_price = ticket_price
        self.screens: dict[int, Screen] = {}
        self.bookings: dict[int, Booking] = {}
        self._next_booking_id = 1

    def add_screen(self, screen_id: int, movie: str, total_seats: int) -> None:
        if screen_id in self.screens:
            raise ValueError("Screen already exists.")
        if not movie.strip() or total_seats < 1:
            raise ValueError("Provide a movie name and at least one seat.")
        self.screens[screen_id] = Screen(screen_id, movie, total_seats)

    def show_movies(self) -> list[str]:
        """Return the movie choices currently assigned to screens."""
        return sorted({screen.movie for screen in self.screens.values()})

    def available_seats(self, screen_id: int) -> list[str]:
        screen = self._get_screen(screen_id)
        all_seats = [f"S{i}" for i in range(1, screen.total_seats + 1)]
        return [seat for seat in all_seats if seat not in screen.booked_seats]

    def book_tickets(self, screen_id: int, seats: list[str]) -> Booking:
        screen = self._get_screen(screen_id)
        if not seats:
            raise ValueError("Select at least one seat.")
        if len(set(seats)) != len(seats):
            raise ValueError("Duplicate seat selection.")
        available = set(self.available_seats(screen_id))
        if any(seat not in available for seat in seats):
            raise ValueError("One or more seats are unavailable or invalid.")

        screen.booked_seats.update(seats)
        booking = Booking(
            booking_id=self._next_booking_id,
            screen_id=screen_id,
            movie=screen.movie,
            seats=list(seats),
            amount=len(seats) * self.ticket_price,
        )
        self.bookings[booking.booking_id] = booking
        self._next_booking_id += 1
        return booking

    def pay(self, booking_id: int) -> Booking:
        booking = self._get_booking(booking_id)
        if booking.refunded:
            raise ValueError("Cannot pay for a refunded booking.")
        booking.paid = True
        return booking

    def refund(self, booking_id: int) -> float:
        booking = self._get_booking(booking_id)
        if not booking.paid:
            raise ValueError("Only paid bookings can be refunded.")
        if booking.refunded:
            raise ValueError("Booking has already been refunded.")
        booking.refunded = True
        self.screens[booking.screen_id].booked_seats.difference_update(booking.seats)
        return booking.amount

    def screen_status(self) -> list[dict[str, object]]:
        """Show each screen, its movie, and seat availability."""
        return [
            {
                "screen_id": screen.screen_id,
                "movie": screen.movie,
                "total_seats": screen.total_seats,
                "available_seats": len(self.available_seats(screen.screen_id)),
            }
            for screen in sorted(self.screens.values(), key=lambda item: item.screen_id)
        ]

    def _get_screen(self, screen_id: int) -> Screen:
        if screen_id not in self.screens:
            raise ValueError("Screen not found.")
        return self.screens[screen_id]

    def _get_booking(self, booking_id: int) -> Booking:
        if booking_id not in self.bookings:
            raise ValueError("Booking not found.")
        return self.bookings[booking_id]
