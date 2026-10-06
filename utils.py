from datetime import datetime


def current_date():
    return datetime.now().strftime("%Y-%m-%d")


def generate_id(items, prefix):
    if not items:
        return f"{prefix}001"

    numbers = []

    for item in items:
        item_id = item.get("id", "")

        if item_id.startswith(prefix):
            try:
                numbers.append(
                    int(item_id[len(prefix):])
                )
            except ValueError:
                pass

    next_number = max(numbers, default=0) + 1

    return f"{prefix}{next_number:03d}"


def find_by_id(items, item_id):
    for item in items:
        if item.get("id", "").lower() == item_id.lower():
            return item

    return None


def parse_date(value):
    return datetime.strptime(value, "%Y-%m-%d")


def calculate_nights(check_in, check_out):
    start = parse_date(check_in)
    end = parse_date(check_out)

    return (end - start).days


def money(value):
    return f"₹{value:.2f}"
