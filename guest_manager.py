from config import GUEST_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_guest():
    guests = load_data(GUEST_FILE)

    name = input("Enter guest name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    id_proof = input("Enter ID proof number: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    guest = {
        "id": generate_id(guests, "G"),
        "name": name,
        "phone": phone,
        "email": email,
        "id_proof": id_proof
    }

    guests.append(guest)

    save_data(GUEST_FILE, guests)

    print("\nGuest added successfully.")
    print(f"Guest ID: {guest['id']}")


def view_guests():
    guests = load_data(GUEST_FILE)

    if not guests:
        print("No guests found.")
        return

    print("\n" + "=" * 75)
    print("GUEST LIST")
    print("=" * 75)

    for guest in guests:
        print(f"ID       : {guest['id']}")
        print(f"Name     : {guest['name']}")
        print(f"Phone    : {guest['phone']}")
        print(f"Email    : {guest['email']}")
        print(f"ID Proof : {guest['id_proof']}")
        print("-" * 75)


def search_guest():
    guests = load_data(GUEST_FILE)

    keyword = input(
        "Enter guest ID, name, phone, or email: "
    ).strip().lower()

    results = [
        guest
        for guest in guests
        if keyword in guest["id"].lower()
        or keyword in guest["name"].lower()
        or keyword in guest["phone"].lower()
        or keyword in guest["email"].lower()
    ]

    if not results:
        print("No guests found.")
        return

    for guest in results:
        print(
            f"{guest['id']} | "
            f"{guest['name']} | "
            f"{guest['phone']} | "
            f"{guest['email']}"
        )


def delete_guest():
    guests = load_data(GUEST_FILE)

    guest_id = input("Enter Guest ID: ").strip()

    guest = find_by_id(guests, guest_id)

    if not guest:
        print("Guest not found.")
        return

    guests.remove(guest)

    save_data(GUEST_FILE, guests)

    print("Guest deleted successfully.")
