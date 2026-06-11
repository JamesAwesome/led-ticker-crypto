import pytest

from led_ticker_crypto.coingecko import _resolve_symbols

COIN_LIST = [
    {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"},
    {"id": "ethereum", "symbol": "eth", "name": "Ethereum"},
    {"id": "binance-peg-ethereum", "symbol": "eth", "name": "Binance-Peg Ethereum"},
]


def test_unique_symbol_resolves():
    assert _resolve_symbols(["BTC"], COIN_LIST) == [("BTC", "bitcoin")]


def test_unknown_symbol_raises():
    with pytest.raises(ValueError, match="not found"):
        _resolve_symbols(["NOPE"], COIN_LIST)


def test_ambiguous_symbol_raises_listing_candidates():
    with pytest.raises(ValueError) as exc:
        _resolve_symbols(["ETH"], COIN_LIST)
    msg = str(exc.value)
    assert "ethereum" in msg and "binance-peg-ethereum" in msg
    assert "symbol_id" in msg  # tells the user how to disambiguate
