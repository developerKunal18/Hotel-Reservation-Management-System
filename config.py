import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

GUEST_FILE = os.path.join(DATA_DIR, "guests.json")
ROOM_FILE = os.path.join(DATA_DIR, "rooms.json")
RESERVATION_FILE = os.path.join(DATA_DIR, "reservations.json")
PAYMENT_FILE = os.path.join(DATA_DIR, "payments.json")

GST_RATE = 18

ROOM_TYPES = [
    "Single",
    "Double",
    "Deluxe",
    "Suite"
]

RESERVATION_STATUSES = [
    "Reserved",
    "Checked In",
    "Checked Out",
    "Cancelled"
]
