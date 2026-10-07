"""Computational verification for the SpotItRio 57-card deck.

Construction: projective plane PG(2,7).
- 49 affine points (x,y) over Z_7
- 8 points at infinity
- 57 cards/lines total
- 8 symbols on every card
"""

Q = 7


def mod(n):
    return n % Q


def build_deck():
    deck = []

    # 49 non-vertical affine lines: y = m x + b (mod 7).
    # Each gets its slope's point at infinity I_m.
    for m in range(Q):
        for b in range(Q):
            card = [f"P{x}{mod(m * x + b)}" for x in range(Q)]
            card.append(f"I{m}")
            deck.append(card)

    # 7 vertical lines x = a, each with the vertical point at infinity IV.
    for a in range(Q):
        card = [f"P{a}{y}" for y in range(Q)]
        card.append("IV")
        deck.append(card)

    # The line at infinity contains all 8 points at infinity.
    deck.append([f"I{m}" for m in range(Q)] + ["IV"])

    return deck


def verify_deck(deck):
    assert len(deck) == 57, f"Expected 57 cards, found {len(deck)}"

    for i, card in enumerate(deck, start=1):
        assert len(card) == 8, f"Card {i} has {len(card)} symbols instead of 8"
        assert len(set(card)) == 8, f"Card {i} contains a repeated symbol"

    checked_pairs = 0
    failures = []

    for i in range(len(deck)):
        for j in range(i + 1, len(deck)):
            checked_pairs += 1
            common = set(deck[i]).intersection(deck[j])
            if len(common) != 1:
                failures.append((i + 1, j + 1, sorted(common)))

    assert checked_pairs == 1596, f"Expected 1,596 pairs, checked {checked_pairs}"
    assert not failures, f"Found invalid card pairs: {failures[:10]}"

    return checked_pairs


if __name__ == "__main__":
    deck = build_deck()
    pair_count = verify_deck(deck)

    print("SpotItRio verification: PASS")
    print(f"Cards: {len(deck)}")
    print("Symbols per card: 8")
    print(f"Distinct card pairs checked: {pair_count}")
    print("Invalid pairs: 0")
    print("Every pair of distinct cards shares exactly one symbol.")
