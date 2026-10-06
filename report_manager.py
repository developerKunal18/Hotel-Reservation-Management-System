from config import RESERVATION_FILE, ROOM_FILE
from storage import load_data
from utils import money


def hotel_statistics():
    reservations = load_data(RESERVATION_FILE)
    rooms = load_data(ROOM_FILE)

    total_rooms = len(rooms)

    available = sum(
        1
        for room in rooms
        if room["status"] == "Available"
    )

    occupied = sum(
        1
        for room in rooms
        if room["status"] == "Occupied"
    )

    reserved = sum(
        1
        for room in rooms
        if room["status"] == "Reserved"
    )

    revenue = sum(
        reservation["paid"]
        for reservation in reservations
    )

    print("\n" + "=" * 55)
    print("HOTEL STATISTICS")
    print("=" * 55)

    print(f"Total Rooms       : {total_rooms}")
    print(f"Available Rooms   : {available}")
    print(f"Reserved Rooms    : {reserved}")
    print(f"Occupied Rooms    : {occupied}")
    print(f"Reservations      : {len(reservations)}")
    print(f"Collected Revenue : {money(revenue)}")


def reservation_status_report():
    reservations = load_data(RESERVATION_FILE)

    statuses = {}

    for reservation in reservations:
        status = reservation["status"]

        if status not in statuses:
            statuses[status] = 0

        statuses[status] += 1

    print("\nReservation Status Report")

    if not statuses:
        print("No reservations found.")
        return

    for status, count in statuses.items():
        print(f"{status}: {count}")
