from config import (
    GUEST_FILE,
    ROOM_FILE,
    RESERVATION_FILE,
    RESERVATION_STATUSES
)

from storage import load_data, save_data

from utils import (
    generate_id,
    find_by_id,
    calculate_nights,
    current_date,
    money
)


def dates_overlap(start1, end1, start2, end2):
    return start1 < end2 and start2 < end1


def room_is_available(
    room_id,
    check_in,
    check_out,
    reservations
):
    for reservation in reservations:

        if reservation["room_id"] != room_id:
            continue

        if reservation["status"] == "Cancelled":
            continue

        if reservation["status"] == "Checked Out":
            continue

        if dates_overlap(
            check_in,
            check_out,
            reservation["check_in"],
            reservation["check_out"]
        ):
            return False

    return True


def create_reservation():
    guests = load_data(GUEST_FILE)
    rooms = load_data(ROOM_FILE)
    reservations = load_data(RESERVATION_FILE)

    if not guests:
        print("Please add a guest first.")
        return

    if not rooms:
        print("Please add rooms first.")
        return

    guest_id = input("Enter Guest ID: ").strip()

    guest = find_by_id(guests, guest_id)

    if not guest:
        print("Guest not found.")
        return

    print("\nRooms:")

    for room in rooms:
        print(
            f"{room['id']} | "
            f"Room {room['room_number']} | "
            f"{room['type']} | "
            f"{money(room['price'])}"
        )

    room_id = input("Enter Room ID: ").strip()

    room = find_by_id(rooms, room_id)

    if not room:
        print("Room not found.")
        return

    check_in = input(
        "Enter check-in date (YYYY-MM-DD): "
    ).strip()

    check_out = input(
        "Enter check-out date (YYYY-MM-DD): "
    ).strip()

    try:
        nights = calculate_nights(
            check_in,
            check_out
        )
    except ValueError:
        print("Invalid date format.")
        return

    if nights <= 0:
        print("Check-out must be after check-in.")
        return

    if not room_is_available(
        room["id"],
        check_in,
        check_out,
        reservations
    ):
        print("Room is already booked for these dates.")
        return

    room_charge = room["price"] * nights

    reservation = {
        "id": generate_id(reservations, "RES"),
        "guest_id": guest["id"],
        "guest_name": guest["name"],
        "room_id": room["id"],
        "room_number": room["room_number"],
        "room_type": room["type"],
        "price_per_night": room["price"],
        "check_in": check_in,
        "check_out": check_out,
        "nights": nights,
        "room_charge": room_charge,
        "extra_charges": 0,
        "gst": 0,
        "grand_total": room_charge,
        "paid": 0,
        "status": "Reserved",
        "created_at": current_date()
    }

    reservations.append(reservation)

    room["status"] = "Reserved"

    save_data(RESERVATION_FILE, reservations)
    save_data(ROOM_FILE, rooms)

    print("\nReservation created successfully.")
    print(f"Reservation ID: {reservation['id']}")
    print(f"Total: {money(room_charge)}")


def view_reservations():
    reservations = load_data(RESERVATION_FILE)

    if not reservations:
        print("No reservations found.")
        return

    print("\n" + "=" * 90)
    print("RESERVATIONS")
    print("=" * 90)

    for reservation in reservations:
        print(
            f"ID: {reservation['id']} | "
            f"Guest: {reservation['guest_name']} | "
            f"Room: {reservation['room_number']} | "
            f"{reservation['check_in']} to "
            f"{reservation['check_out']} | "
            f"Status: {reservation['status']} | "
            f"Total: {money(reservation['grand_total'])}"
        )


def reservation_details():
    reservations = load_data(RESERVATION_FILE)

    reservation_id = input(
        "Enter Reservation ID: "
    ).strip()

    reservation = find_by_id(
        reservations,
        reservation_id
    )

    if not reservation:
        print("Reservation not found.")
        return

    print("\n" + "=" * 70)
    print("RESERVATION DETAILS")
    print("=" * 70)

    print(f"Reservation ID : {reservation['id']}")
    print(f"Guest          : {reservation['guest_name']}")
    print(f"Room           : {reservation['room_number']}")
    print(f"Room Type      : {reservation['room_type']}")
    print(f"Check-in       : {reservation['check_in']}")
    print(f"Check-out      : {reservation['check_out']}")
    print(f"Nights         : {reservation['nights']}")
    print(
        f"Room Charge    : "
        f"{money(reservation['room_charge'])}"
    )
    print(
        f"Extra Charges  : "
        f"{money(reservation['extra_charges'])}"
    )
    print(
        f"GST            : "
        f"{money(reservation['gst'])}"
    )
    print(
        f"Grand Total    : "
        f"{money(reservation['grand_total'])}"
    )
    print(
        f"Paid           : "
        f"{money(reservation['paid'])}"
    )
    print(f"Status         : {reservation['status']}")


def update_status():
    reservations = load_data(RESERVATION_FILE)
    rooms = load_data(ROOM_FILE)

    reservation_id = input(
        "Enter Reservation ID: "
    ).strip()

    reservation = find_by_id(
        reservations,
        reservation_id
    )

    if not reservation:
        print("Reservation not found.")
        return

    print("\nStatus Options")

    for index, status in enumerate(
        RESERVATION_STATUSES,
        start=1
    ):
        print(f"{index}. {status}")

    try:
        choice = int(input("Select status: "))
        status = RESERVATION_STATUSES[choice - 1]
    except (ValueError, IndexError):
        print("Invalid status.")
        return

    reservation["status"] = status

    room = find_by_id(
        rooms,
        reservation["room_id"]
    )

    if room:
        if status == "Checked In":
            room["status"] = "Occupied"

        elif status in ["Checked Out", "Cancelled"]:
            room["status"] = "Available"

        else:
            room["status"] = "Reserved"

    save_data(RESERVATION_FILE, reservations)
    save_data(ROOM_FILE, rooms)

    print("Reservation status updated.")


def add_extra_charges():
    reservations = load_data(RESERVATION_FILE)

    reservation_id = input(
        "Enter Reservation ID: "
    ).strip()

    reservation = find_by_id(
        reservations,
        reservation_id
    )

    if not reservation:
        print("Reservation not found.")
        return

    try:
        amount = float(
            input("Enter extra charge amount: ")
        )
    except ValueError:
        print("Invalid amount.")
        return

    if amount < 0:
        print("Amount cannot be negative.")
        return

    reservation["extra_charges"] += amount

    subtotal = (
        reservation["room_charge"]
        + reservation["extra_charges"]
    )

    reservation["gst"] = subtotal * 18 / 100

    reservation["grand_total"] = (
        subtotal + reservation["gst"]
    )

    save_data(RESERVATION_FILE, reservations)

    print("Extra charge added successfully.")
    print(
        f"New Total: "
        f"{money(reservation['grand_total'])}"
    )


def search_reservations():
    reservations = load_data(RESERVATION_FILE)

    keyword = input(
        "Enter reservation ID, guest, or room number: "
    ).strip().lower()

    results = [
        reservation
        for reservation in reservations
        if keyword in reservation["id"].lower()
        or keyword in reservation["guest_name"].lower()
        or keyword in reservation["room_number"].lower()
    ]

    if not results:
        print("No reservations found.")
        return

    for reservation in results:
        print(
            f"{reservation['id']} | "
            f"{reservation['guest_name']} | "
            f"Room {reservation['room_number']} | "
            f"{reservation['status']}"
        )
