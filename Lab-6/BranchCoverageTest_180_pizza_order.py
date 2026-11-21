import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# PIZZA PRICE BRANCH TESTS

def test_invalid_size():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra-large", 2, False)


def test_valid_size():
    assert pizza_price("medium", 2, False) == 430


def test_negative_toppings():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_zero_toppings():
    assert pizza_price("small", 0, False) == 200


def test_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680


def test_three_toppings():
    assert pizza_price("small", 3, False) == 320


def test_cheese_burst_small():
    with pytest.raises(ValueError, match="cheese burst not available"):
        pizza_price("small", 1, True)


def test_cheese_burst_medium():
    assert pizza_price("medium", 2, True) == 530


def test_without_cheese_burst():
    assert pizza_price("large", 1, False) == 540


# ORDER DISCOUNT BRANCH TESTS

def test_order_below_300():
    assert order_discount(250, "tuesday", False) == 0


def test_tuesday_discount():
    assert order_discount(500, "tuesday", False) == 250


def test_saturday_discount():
    assert order_discount(500, "saturday", False) == 0


def test_sunday_discount():
    assert order_discount(500, "sunday", False) == 0


def test_normal_weekday_discount():
    assert order_discount(500, "monday", False) == 50


# DELIVERY STATUS BRANCH TESTS

def test_distance_above_10():
    assert delivery_status(20, 12) == "not deliverable"


def test_distance_within_10():
    assert delivery_status(20, 5) == "on time"


def test_delivery_within_30_minutes():
    assert delivery_status(30, 5) == "on time"


def test_delivery_between_31_and_45_minutes():
    assert delivery_status(40, 5) == "late"


def test_delivery_after_45_minutes():
    assert delivery_status(50, 5) == "free pizza"