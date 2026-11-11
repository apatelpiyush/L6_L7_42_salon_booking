import math
from hypothesis import given, strategies as st
from salon_booking import parse_booking, duration_average, payable_bill

anything = st.one_of(st.text(), st.none(), st.integers(), st.floats(), st.lists(st.integers()))


@given(st.text() | st.none())
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except Exception as e:
        assert False, f"parse_booking crashed with: {e}"


@given(st.text() | st.none())
def test_duration_average_no_crash(s):
    try:
        duration_average(s)
    except Exception as e:
        assert False, f"duration_average crashed with: {e}"


@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except Exception as e:
        assert False, f"payable_bill crashed with: {e}"


@given(anything)
def test_parse_booking_any_type_no_crash(s):
    parse_booking(s)


@given(anything)
def test_duration_average_any_type_no_crash(s):
    duration_average(s)


@given(anything)
def test_payable_bill_any_type_no_crash(s):
    payable_bill(s)


@given(st.text() | st.none())
def test_parse_booking_output_valid(s):
    result = parse_booking(s)
    if result is not None:
        service, minutes = result
        assert isinstance(service, str) and service
        assert math.isfinite(minutes) and minutes >= 0


@given(st.text() | st.none())
def test_duration_average_output_valid(s):
    result = duration_average(s)
    if result is not None:
        assert isinstance(result, int) and result >= 0


@given(st.text() | st.none())
def test_payable_bill_output_valid(s):
    result = payable_bill(s)
    if result is not None:
        assert math.isfinite(result) and result >= 0


@given(st.lists(st.integers(min_value=0, max_value=10000), min_size=1))
def test_duration_average_within_range(values):
    result = duration_average(",".join(str(v) for v in values))
    assert min(values) <= result <= max(values)


@given(st.integers(min_value=0, max_value=10**6), st.integers(min_value=0, max_value=10**6))
def test_payable_bill_valid_pair(bill, discount):
    result = payable_bill(f"{bill}|{discount}")
    assert result is not None and result >= 0
