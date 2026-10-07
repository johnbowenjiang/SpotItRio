SpotItRio — Math 134B AI-Open Challenge
=========================================

FILES
-----
index.html       Playable digital SpotItRio game. Open it in a modern web browser.
verification.py Independent computational verification of the full deck.
README.txt       This explanation.

WHAT WE BUILT
-------------
The game contains exactly 57 cards with exactly 8 symbols on each card.
For every pair of distinct cards, there is exactly one shared symbol.
The game plays a 10-round match, keeps score, and uses sudden death for a tie.

COMPUTATIONAL VERIFICATION
--------------------------
Run:

    python3 verification.py

Expected result:

    SpotItRio verification: PASS
    Cards: 57
    Symbols per card: 8
    Distinct card pairs checked: 1596
    Invalid pairs: 0
    Every pair of distinct cards shares exactly one symbol.

WHY THE DECK WORKS
------------------
The deck is based on the finite projective plane PG(2,7).

There are 57 points/symbols and 57 lines/cards because

    7^2 + 7 + 1 = 57.

Each projective line contains

    7 + 1 = 8

points, so every card contains exactly 8 symbols.

The construction used in the program is:

1. 49 cards of the form y = m x + b modulo 7.
2. 7 vertical cards of the form x = a.
3. 1 line-at-infinity card.

The 57 symbols are 49 affine points plus 8 points at infinity.
A basic property of a projective plane is that any two distinct lines intersect
in exactly one point. Since lines are cards and points are symbols, any two
cards share exactly one symbol.

The program independently checks all

    C(57,2) = 1596

distinct card pairs and confirms that every intersection has size exactly 1.

HOW TO PLAY
-----------
Open index.html in a browser and press Start Match.
Player 1 uses the left card and Player 2 uses the right card.
The first player to click the one symbol appearing on both cards earns a point.
After 10 rounds, the player with more points wins. A tie goes to sudden death.

SHARING
-------
The Share/QR feature works for other devices after index.html is hosted at a
public web address. When opened only as a local file, the QR code points to that
local file and cannot be opened by other devices.
