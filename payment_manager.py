from config import PAYMENT_FILE, RESERVATION_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id, current_date, money


def record_payment():
    payments = load_data(PAYMENT_FILE)
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

    balance = (
        reservation["grand_total"]
        - reservation["paid"]
    )

    print(f"Total Amount : {money(reservation['grand_total'])}")
    print(f"Paid         : {money(reservation['paid'])}")
    print(f"Balance      : {money(balance)}")

    if balance <= 0:
        print("No payment is pending.")
        return

    try:
        amount = float(
            input("Enter payment amount: ")
        )
    except ValueError:
        print("Invalid amount.")
        return

    if amount <= 0:
        print("Payment must be greater than zero.")
        return

    if amount > balance:
        print("Payment cannot exceed pending balance.")
        return

    payment = {
        "id": generate_id(payments, "PAY"),
        "reservation_id": reservation["id"],
        "guest_name": reservation["guest_name"],
        "amount": amount,
        "date": current_date()
    }

    payments.append(payment)

    reservation["paid"] += amount

    save_data(PAYMENT_FILE, payments)
    save_data(RESERVATION_FILE, reservations)

    print("\nPayment recorded successfully.")
    print(f"Payment ID: {payment['id']}")


def view_payments():
    payments = load_data(PAYMENT_FILE)

    if not payments:
        print("No payments found.")
        return

    print("\n" + "=" * 75)
    print("PAYMENT HISTORY")
    print("=" * 75)

    for payment in payments:
        print(
            f"{payment['id']} | "
            f"{payment['reservation_id']} | "
            f"{payment['guest_name']} | "
            f"{money(payment['amount'])} | "
            f"{payment['date']}"
        )


def reservation_balance():
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

    balance = (
        reservation["grand_total"]
        - reservation["paid"]
    )

    print(f"\nGrand Total : {money(reservation['grand_total'])}")
    print(f"Paid        : {money(reservation['paid'])}")
    print(f"Balance     : {money(balance)}")
