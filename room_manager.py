from config import ROOM_FILE, ROOM_TYPES
from storage import load_data, save_data
from utils import generate_id, find_by_id, money


def add_room():
    rooms = load_data(ROOM_FILE)

    room_number = input("Enter room number: ").strip()

    for room in rooms:
        if room["room_number"] == room_number:
            print("Room number already exists.")
            return

    print("\nRoom Types:")

    for index, room_type in enumerate(ROOM_TYPES, start=1):
        print(f"{index}. {room_type}")

    try:
        choice = int(input("Select room type: "))
        room_type = ROOM_TYPES[choice - 1]
    except (ValueError, IndexError):
        print("Invalid room type.")
        return

    try:
        price = float(input("Enter price per night: "))
    except ValueError:
        print("Invalid price.")
        return

    if price < 0:
        print("Price cannot be negative.")
        return

    room = {
        "id": generate_id(rooms, "R"),
        "room_number": room_number,
        "type": room_type,
        "price": price,
        "status": "Available"
    }

    rooms.append(room)

    save_data(ROOM_FILE, rooms)

    print("\nRoom added successfully.")
    print(f"Room ID: {room['id']}")


def view_rooms():
    rooms = load_data(ROOM_FILE)

    if not rooms:
        print("No rooms found.")
        return

    print("\n" + "=" * 80)
    print("ROOM LIST")
    print("=" * 80)

    for room in rooms:
        print(f"ID          : {room['id']}")
        print(f"Room Number : {room['room_number']}")
        print(f"Type        : {room['type']}")
        print(f"Price       : {money(room['price'])}")
        print(f"Status      : {room['status']}")
        print("-" * 80)


def available_rooms():
    rooms = load_data(ROOM_FILE)

    results = [
        room
        for room in rooms
        if room["status"] == "Available"
    ]

    if not results:
        print("No available rooms.")
        return

    print("\nAvailable Rooms")

    for room in results:
        print(
            f"{room['id']} | "
            f"Room {room['room_number']} | "
            f"{room['type']} | "
            f"{money(room['price'])}"
        )


def search_room():
    rooms = load_data(ROOM_FILE)

    keyword = input(
        "Enter room ID, number, or type: "
    ).strip().lower()

    results = [
        room
        for room in rooms
        if keyword in room["id"].lower()
        or keyword in room["room_number"].lower()
        or keyword in room["type"].lower()
    ]

    if not results:
        print("No rooms found.")
        return

    for room in results:
        print(
            f"{room['id']} | "
            f"Room {room['room_number']} | "
            f"{room['type']} | "
            f"{room['status']}"
        )
