
import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# 1. PIZZA PRICE TEST CASES

def test_invalid_pizza_size():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra-large", 2, False)


def test_negative_toppings():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_small_pizza_with_three_toppings():
    assert pizza_price("small", 3, False) == 320


def test_large_pizza_with_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680


def test_cheese_burst_for_small_pizza():
    with pytest.raises(ValueError, match="cheese burst not available"):
        pizza_price("small", 1, True)


def test_cheese_burst_for_medium_pizza():
    assert pizza_price("medium", 2, True) == 530


# 2. ORDER DISCOUNT TEST CASES

def test_order_below_300():
    assert order_discount(250, "tuesday", False) == 0


def test_tuesday_discount():
    assert order_discount(500, "tuesday", True) == 300


def test_weekend_discount():
    assert order_discount(500, "saturday", False) == 0
    assert order_discount(500, "sunday", False) == 0


def test_normal_weekday_discount():
    assert order_discount(500, "monday", False) == 50


# 3. DELIVERY STATUS TEST CASES

def test_delivery_distance_above_10_km():
    assert delivery_status(20, 12) == "not deliverable"


def test_delivery_on_time():
    assert delivery_status(30, 5) == "on time"


def test_delivery_late():
    assert delivery_status(40, 5) == "late"


def test_delivery_after_45_minutes():
    assert delivery_status(50, 5) == "free pizza"
