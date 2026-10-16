import unittest

from movie_ticket_booking.booking import MovieTicketBooking


class MovieTicketBookingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.system = MovieTicketBooking(ticket_price=150)
        self.system.add_screen(1, "Interstellar", 3)
        self.system.add_screen(2, "Inside Out 2", 2)

    def test_movie_selection_and_screen_management(self) -> None:
        self.assertEqual(self.system.show_movies(), ["Inside Out 2", "Interstellar"])
        status = self.system.screen_status()
        self.assertEqual(len(status), 2)
        self.assertEqual(status[0]["available_seats"], 3)

    def test_booking_payment_and_refund_workflow(self) -> None:
        booking = self.system.book_tickets(1, ["S1", "S2"])
        self.assertEqual(booking.amount, 300)
        self.assertNotIn("S1", self.system.available_seats(1))

        self.system.pay(booking.booking_id)
        refund_amount = self.system.refund(booking.booking_id)

        self.assertEqual(refund_amount, 300)
        self.assertTrue(booking.refunded)
        self.assertIn("S1", self.system.available_seats(1))

    def test_cannot_book_an_unavailable_seat(self) -> None:
        self.system.book_tickets(1, ["S1"])
        with self.assertRaises(ValueError):
            self.system.book_tickets(1, ["S1"])

    def test_cannot_refund_unpaid_booking(self) -> None:
        booking = self.system.book_tickets(1, ["S1"])
        with self.assertRaises(ValueError):
            self.system.refund(booking.booking_id)


if __name__ == "__main__":
    unittest.main()
