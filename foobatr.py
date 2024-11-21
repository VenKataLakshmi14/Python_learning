from typing import List

def foobar(n: int, conditions: dict = {3: "foo", 5: "bar", 15: "foobar"}) -> List[str]:
    return [max((conditions[k] for k in conditions if i % k == 0), default=str(i)) for i in range(1, n+1)]


n = 20
print(foobar(n))

