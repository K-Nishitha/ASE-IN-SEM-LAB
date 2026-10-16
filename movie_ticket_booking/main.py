"""Run a sample movie ticket booking workflow."""

from movie_ticket_booking.booking import MovieTicketBooking


def main() -> None:
    system = MovieTicketBooking(ticket_price=150)
    system.add_screen(1, "Interstellar", 5)
    system.add_screen(2, "Inside Out 2", 4)

    print("1. Movie selection:", system.show_movies())
    print("2. Available seats on Screen 1:", system.available_seats(1))

    booking = system.book_tickets(1, ["S1", "S2"])
    print(f"3. Booking #{booking.booking_id} created for {booking.movie}")
    print(f"   Seats: {booking.seats}; Amount: ₹{booking.amount:.2f}")

    system.pay(booking.booking_id)
    print("4. Payment successful.")
    print("5. Screen status:", system.screen_status())

    refunded_amount = system.refund(booking.booking_id)
    print(f"6. Refund successful: ₹{refunded_amount:.2f}")
    print("7. Seats after refund:", system.available_seats(1))


if __name__ == "__main__":
    main()
