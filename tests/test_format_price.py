from led_ticker_crypto._ticker_render import _format_price


def test_normal_price_keeps_four_decimals():
    assert _format_price(50000.1234) == "50,000.1234"
    assert _format_price(3000.5) == "3,000.5000"


def test_value_at_one_uses_four_decimals():
    assert _format_price(1.0) == "1.0000"


def test_sub_cent_shows_significant_figures_not_zero():
    s = _format_price(4.64e-06)
    assert s not in ("0.0000", "0")
    assert float(s.replace(",", "")) > 0
    assert "4640" in s.replace(".", "").replace(",", "")


def test_zero_is_zeroed():
    assert _format_price(0.0) == "0.0000"


def test_small_but_above_one_cent():
    assert _format_price(0.1234) == "0.1234"
