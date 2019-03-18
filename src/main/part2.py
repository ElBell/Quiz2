from typing import Dict, Any, List


class Router:
    def __init__(self):
        self.map: Dict[str, str] = {}

    def add(self, path: str, controller: str):
        self.map[path] = controller

    def update(self, path: str, controller: str):
        if path in self.map:
            self.map[path] = controller

    def get_controller(self, path: str):
        if path in self.map:
            return self.map[path]
        return None

    def size(self):
        return len(self.map)

    def remove(self, path: str):
        if path in self.map:
            del self.map[path]

    def to_string(self) -> str:
        result: str = ""
        for element in self.map:
            result = element + " -> " + self.map[element] + "\n" + result
        return result


class ListUtility:
    def __init__(self):
        self.list: List[Any] = []

    def add(self, value_to_add: Any):
        self.list.append(value_to_add)

    def size(self) -> int:
        return len(self.list)

    def most_common(self) -> Any:
        return max(self.list, key=self.list.count)

    def join(self) -> str:
        return str(self.list)[1:-1]

    def get_unique(self) -> List[Any]:
        return list(set(self.list))

    def contains(self, value: Any) -> bool:
        return value in self.list


class ArrayUtility:
    @staticmethod
    def rotate(array: List[Any], index: int) -> List[Any]:
        return array[index:] + array[: index]

    @staticmethod
    def most_common(array: List[Any]):
        return max(array, key=array.count)

    @staticmethod
    def merge(array1: List[Any], array2: List[Any]) -> List[Any]:
        return array1 + array2

    @staticmethod
    def count_occurrence(array1: List[Any], array2: List[Any], value: Any) -> int:
        return (array1 + array2).count(value)
