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


def test_member_bonus_time():
    assert extra_time_charge("colour", 80, "junior", True) == 50


def test_junior_rate():
    assert extra_time_charge("haircut", 50, "junior", False) == 200


def test_standard_rate():
    assert extra_time_charge("haircut", 50, "mid", False) == 360


def test_long_overrun_junior():
    assert extra_time_charge("haircut", 100, "junior", False) == 1260


def test_long_overrun_senior():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100


def test_can_book():
    assert can_book(2, 1, False) is True


def test_walk_in():
    assert can_book(2, 5, True) is True


def test_party_too_large():
    assert can_book(5, 1, False) is False


def test_arrival_open():
    assert arrival_status(20, True, True) == "open"


def test_arrival_late():
    assert arrival_status(0, False, False) == "late"


def test_arrival_closed():
    assert arrival_status(-20, False, False) == "closed"
