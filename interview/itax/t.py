from collections import defaultdict
from dataclasses import dataclass
import unittest

t = """\
B BTC 680000.0 2.5 
B ETH 43000.0 12.0 
B BTC 690000.0 2.5 
S BTC 695000.0 3.0 
B ETH 43500.0 23.5 
S BTC 695000.0 1.0 
S ETH 45000.0 30.0
"""


@dataclass
class ITax:
    action: str
    coin_type: str
    price: float
    amount: float


def main(testcase: str):
    lines = testcase.splitlines()
    arr: list[ITax] = []
    # expected: {"BTC" : [(price, quantity), ..], "ETH": [(price, quantity), ..]
    map: dict[str, list[tuple[float, float]]] = defaultdict(list)

    for line in lines:
        action, coin_type, price, amount = line.split()
        arr.append(
            ITax(
                action=action,
                coin_type=coin_type,
                price=float(price),
                amount=float(amount),
            )
        )

    for item in arr:
        map[item.coin_type].append(
            (item.price, item.amount * (-1 if item.action == "B" else 1))
        )

    acc = 0
    for k, _ in map.items():
        queue = map[k]
        visited_buy: list[tuple[float, float]] = []
        while queue:
            n_buy = 0
            price, amount = queue.pop(0)
            if amount < 0:
                # buy
                visited_buy.append((price, amount))
            else:
                # sell
                for it in visited_buy:
                    n_buy += it[1]
                if abs(n_buy) < abs(amount):
                    raise ValueError("sell > buy")

            acc += price * amount

    return acc


class Test(unittest.TestCase):
    def test_amount_is_ok(self):
        expected = -833250.0
        self.assertEqual(main(t), expected)

    def test_amount_sell_greater_than_buy(self):
        t = """\
        B ETH 43000.0 1.0
        S ETH 45000.0 30.0
        """
        self.assertRaises(ValueError, main, t)

    def test_amount_sell_only(self):
        t = """\
        S ETH 45000.0 30.0
        """
        self.assertRaises(ValueError, main, t)


if __name__ == "__main__":
    unittest.main()
