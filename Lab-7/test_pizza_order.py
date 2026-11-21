
import pytest
from hypothesis import given, strategies as st

from pizza_order import toppings_price, pizza_inches, split_bill


# TOPPINGS PRICE TESTS

@given(st.sampled_from(["cheese", "olives", "onion", "paneer"]))
def test_valid_topping_price(topping):
    expected = {
        "cheese": 40,
        "olives": 30,
        "onion": 20,
        "paneer": 50
    }
    assert toppings_price(topping) == expected[topping]


@given(st.sampled_from([
    "", "pepperoni", "cheese,", ",cheese",
    "cheese,unknown", "unknown"
]))
def test_invalid_toppings(s):
    with pytest.raises(ValueError):
        toppings_price(s)


@given(st.one_of(st.text(), st.none()))
def test_toppings_price_no_crash(s):
    try:
        result = toppings_price(s)
        assert isinstance(result, int)
    except ValueError:
        pass


# PIZZA SIZE TESTS

@given(st.sampled_from(["S", "M", "L", "s", "m", "l"]))
def test_valid_pizza_inches(size):
    expected = {"S": 8, "M": 10, "L": 12}
    assert pizza_inches(size) == expected[size.upper()]


@given(st.text().filter(lambda s: s.strip().upper() not in ["S", "M", "L"]))
def test_invalid_pizza_size(size):
    with pytest.raises(ValueError):
        pizza_inches(size)


@given(st.one_of(st.text(), st.none()))
def test_pizza_inches_no_crash(s):
    try:
        result = pizza_inches(s)
        assert result in [8, 10, 12]
    except ValueError:
        pass


# SPLIT BILL TESTS

@given(
    st.integers(min_value=0, max_value=100000),
    st.integers(min_value=1, max_value=1000)
)
def test_valid_split_bill(total, people):
    assert split_bill(f"{total}/{people}") == round(total / people, 2)


@given(st.text().filter(lambda s: s.count("/") != 1))
def test_invalid_split_bill_format(s):
    with pytest.raises(ValueError):
        split_bill(s)


@given(st.integers(min_value=0, max_value=100000))
def test_split_bill_zero_people(total):
    with pytest.raises(ValueError):
        split_bill(f"{total}/0")


@given(st.one_of(st.text(), st.none()))
def test_split_bill_no_crash(s):
    try:
        result = split_bill(s)
        assert isinstance(result, float)
    except ValueError:
        pass
