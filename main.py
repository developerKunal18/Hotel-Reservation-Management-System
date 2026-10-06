import os

from config import (
    DATA_DIR,
    GUEST_FILE,
    ROOM_FILE,
    RESERVATION_FILE,
    PAYMENT_FILE
)

from storage import save_data

from guest_manager import (
    add_guest,
    view_guests,
    search_guest,
    delete_guest
)

from room_manager import (
    add_room,
    view_rooms,
    available_rooms,
    search_room
)

from reservation_manager import (
    create_reservation,
    view_reservations,
    reservation_details,
    update_status,
    add_extra_charges,
    search_reservations
)

from payment_manager import (
    record_payment,
    view_payments,
    reservation_balance
)

from report_manager import (
    hotel_statistics,
    reservation_status_report
)


def initialize_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    files = [
        GUEST_FILE,
        ROOM_FILE,
        RESERVATION_FILE,
        PAYMENT_FILE
    ]

    for filename in files:
        if not os.path.exists(filename):
            save_data(filename, [])


def show_menu():
    print("\n")
    print("=" * 65)
    print("          HOTEL RESERVATION MANAGEMENT SYSTEM")
    print("=" * 65)

    print("\nGUEST MANAGEMENT")
    print("1. Add Guest")
    print("2. View Guests")
    print("3. Search Guest")
    print("4. Delete Guest")

    print("\nROOM MANAGEMENT")
    print("5. Add Room")
    print("6. View Rooms")
    print("7. Available Rooms")
    print("8. Search Room")

    print("\nRESERVATIONS")
    print("9. Create Reservation")
    print("10. View Reservations")
    print("11. Reservation Details")
    print("12. Update Reservation Status")
    print("13. Add Extra Charges")
    print("14. Search Reservations")

    print("\nPAYMENTS")
    print("15. Record Payment")
    print("16. View Payments")
    print("17. Check Balance")

    print("\nREPORTS")
    print("18. Hotel Statistics")
    print("19. Reservation Status Report")

    print("\n20. Exit")

    print("=" * 65)


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_guest()

        elif choice == "2":
            view_guests()

        elif choice == "3":
            search_guest()

        elif choice == "4":
            delete_guest()

        elif choice == "5":
            add_room()

        elif choice == "6":
            view_rooms()

        elif choice == "7":
            available_rooms()

        elif choice == "8":
            search_room()

        elif choice == "9":
            create_reservation()

        elif choice == "10":
            view_reservations()

        elif choice == "11":
            reservation_details()

        elif choice == "12":
            update_status()

        elif choice == "13":
            add_extra_charges()

        elif choice == "14":
            search_reservations()

        elif choice == "15":
            record_payment()

        elif choice == "16":
            view_payments()

        elif choice == "17":
            reservation_balance()

        elif choice == "18":
            hotel_statistics()

        elif choice == "19":
            reservation_status_report()

        elif choice == "20":
            print(
                "Thank you for using "
                "Hotel Reservation Management System."
            )
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
