from typing import List


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
  for item in items:
    item.name = item.name.encode("utf-8").decode("unicode-escape")
    item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")