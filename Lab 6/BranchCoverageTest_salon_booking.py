import pytest
from salon_booking import extra_time_charge, can_book, arrival_status


def test_within_included_time():
    assert extra_time_charge("haircut", 20, "junior", False) == 0


def test_unknown_service():
    with pytest.raises(ValueError):
        extra_time_charge("massage", 30, "junior", False)


def test_negative_duration():
    with pytest.raises(ValueError):
        extra_time_charge("haircut", -1, "junior", False)


def test_zero_duration():
    assert extra_time_charge("spa", 0, "senior", False) == 0


def test_exactly_included_time():
    assert extra_time_charge("haircut", 30, "junior", False) == 0


def test_member_gets_extra_15_minutes():
    assert extra_time_charge("haircut", 45, "junior", True) == 0
    assert extra_time_charge("haircut", 46, "junior", True) == 10


def test_non_member_no_bonus():
    assert extra_time_charge("haircut", 45, "junior", False) == 150


def test_member_spa_no_bonus():
    assert extra_time_charge("spa", 100, "junior", True) == 100


def test_member_colour_bonus():
    assert extra_time_charge("colour", 80, "junior", True) == 50


def test_junior_rate():
    assert extra_time_charge("haircut", 50, "junior", False) == 200


def test_mid_rate():
    assert extra_time_charge("haircut", 50, "mid", False) == 360


def test_senior_rate_short_overrun():
    assert extra_time_charge("haircut", 50, "senior", False) == 360


def test_overrun_boundary_60():
    assert extra_time_charge("haircut", 90, "junior", False) == 600


def test_overrun_boundary_61():
    assert extra_time_charge("haircut", 91, "junior", False) == 1098


def test_long_overrun_junior():
    assert extra_time_charge("haircut", 100, "junior", False) == 1260


def test_long_overrun_mid():
    assert extra_time_charge("haircut", 100, "mid", False) == 1820


def test_long_overrun_senior():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100


def test_can_book():
    assert can_book(2, 1, False) is True


def test_walk_in_small_party():
    assert can_book(2, 1, True) is True


def test_walk_in_large_party():
    assert can_book(3, 1, True) is False


def test_booking_party_too_large():
    assert can_book(5, 1, False) is False


def test_booking_max_party_two_services():
    assert can_book(4, 2, False) is True


def test_booking_too_many_services():
    assert can_book(4, 3, False) is False


def test_arrival_plain_weekday():
    assert arrival_status(5, False, False) == "open"
    assert arrival_status(4, False, False) == "late"
    assert arrival_status(-10, False, False) == "late"
    assert arrival_status(-11, False, False) == "closed"


def test_arrival_colour_weekday():
    assert arrival_status(10, True, False) == "open"
    assert arrival_status(9, True, False) == "late"
    assert arrival_status(-5, True, False) == "late"
    assert arrival_status(-6, True, False) == "closed"


def test_arrival_plain_weekend():
    assert arrival_status(15, False, True) == "open"
    assert arrival_status(14, False, True) == "late"
    assert arrival_status(0, False, True) == "late"
    assert arrival_status(-1, False, True) == "closed"


def test_arrival_colour_weekend():
    assert arrival_status(20, True, True) == "open"
    assert arrival_status(19, True, True) == "late"
    assert arrival_status(5, True, True) == "late"
    assert arrival_status(4, True, True) == "closed"
