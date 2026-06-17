import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import (
    search_listings,
    suggest_outfit,
    create_fit_card
)

from utils.data_loader import (
    get_example_wardrobe,
    get_empty_wardrobe
)


# ── search_listings tests ───────────────────────────────────────────────────

def test_search_returns_results():
    results = search_listings(
        "vintage graphic tee",
        size=None,
        max_price=50
    )

    assert isinstance(results, list)
    assert len(results) > 0


def test_search_empty_results():
    results = search_listings(
        "designer ballgown",
        size="XXS",
        max_price=5
    )

    assert results == []


def test_search_price_filter():
    results = search_listings(
        "jacket",
        size=None,
        max_price=10
    )

    assert all(
        item["price"] <= 10
        for item in results
    )


# ── suggest_outfit tests ────────────────────────────────────────────────────

def test_suggest_outfit_empty_wardrobe():
    item = search_listings(
        "graphic tee",
        size=None,
        max_price=50
    )[0]

    result = suggest_outfit(
        item,
        get_empty_wardrobe()
    )

    assert isinstance(result, str)
    assert len(result.strip()) > 0


def test_suggest_outfit_example_wardrobe():
    item = search_listings(
        "graphic tee",
        size=None,
        max_price=50
    )[0]

    result = suggest_outfit(
        item,
        get_example_wardrobe()
    )

    assert isinstance(result, str)
    assert len(result.strip()) > 0


# ── create_fit_card tests ───────────────────────────────────────────────────

def test_fit_card_empty_outfit():
    item = search_listings(
        "graphic tee",
        size=None,
        max_price=50
    )[0]

    result = create_fit_card(
        "",
        item
    )

    assert isinstance(result, str)
    assert "Unable" in result


def test_fit_card_valid_outfit():
    item = search_listings(
        "graphic tee",
        size=None,
        max_price=50
    )[0]

    result = create_fit_card(
        "Pair the graphic tee with baggy jeans and chunky sneakers.",
        item
    )

    assert isinstance(result, str)
    assert len(result.strip()) > 0