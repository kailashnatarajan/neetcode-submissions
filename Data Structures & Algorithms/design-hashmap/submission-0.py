class Node:
    def __init__(self, value):
        self.key = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = Node(value)

    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key].key
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)