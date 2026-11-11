import math


def parse_booking(text):
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    service = parts[0].strip()
    if not service:
        return None
    try:
        minutes = float(parts[1])
    except (ValueError, OverflowError):
        return None
    if not math.isfinite(minutes) or minutes < 0:
        return None
    return service.title(), minutes


def duration_average(durations_csv):
    if not isinstance(durations_csv, str):
        return None
    items = durations_csv.split(',')
    values = []
    for item in items:
        try:
            value = int(item.strip())
        except (ValueError, OverflowError):
            return None
        if value < 0:
            return None
        values.append(value)
    if not values:
        return None
    return sum(values) // len(values)


def payable_bill(text):
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    try:
        bill = float(parts[0])
        discount = float(parts[1])
    except (ValueError, OverflowError):
        return None
    if not (math.isfinite(bill) and math.isfinite(discount)):
        return None
    if bill < 0 or discount < 0:
        return None
    total = bill * 1.18 - discount
    if not math.isfinite(total):
        return None
    return max(total, 0)


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    result = parse_booking(user_input)
    if result is None:
        print("Invalid input")
    else:
        print("Service and Duration:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    result = duration_average(user_input)
    if result is None:
        print("Invalid input")
    else:
        print("Average Duration:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    result = payable_bill(user_input)
    if result is None:
        print("Invalid input")
    else:
        print("Payable Bill:", result)


if __name__ == "__main__":
    main()
