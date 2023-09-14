class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HybridPriorityQueue:
    def __init__(self):
        self.heap = []
        self.map = [None] * 31

    def hash_function(self, priority):
        return priority % 31

    def insert(self, name, age, roomNo, phoneNo, priority):
        index = self.hash_function(priority)

        while self.map[index] is not None:
            index = (index + 1) % 31


        details = {
            "name": name,
            "age": age,
            "roomNo": roomNo,
            "phoneNo": phoneNo,
            "priority": priority,
        }
        self.heap.append(details)
        self.map[index] = HashNode(priority,len(self.heap) - 1)
        self.bubbleUp(len(self.heap) - 1)

    def bubbleUp(self, idx):
        parent_idx = (idx - 1) // 2
        while (
            idx > 0 and self.heap[parent_idx]["priority"] > self.heap[idx]["priority"]
        ):
            self.swap(idx, parent_idx)
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        i_priority = self.heap[i]["priority"]
        j_priority = self.heap[j]["priority"]
        key_i = self.hash_function(i_priority)
        key_j = self.hash_function(j_priority)
        self.map[key_i] = HashNode(i_priority,i)
        self.map[key_j] = HashNode(j_priority,j)

    def displayHeap(self):
        return self.heap
    
    def displayHash(self):
        print("HASH TABLE -> ")
        for item in self.map:
            if item is None:
                print(None)
            else:
                print(f"{item.key} => {item.value}")
    
    def search(self,priority):
        index = self.hash_function(priority)
        while self.map[index] is not None:
            if self.map[index].key == priority:
                return self.heap[self.map[index].value]
            index = (index + 1) % 31
        

        return None
    
    def delete(self,priority):
        index = self.hash_function(priority)

        dummy = HashNode(-1,-1)
        while self.map[index] is not None:
            if self.map[index].key == priority:
                temp = self.map[index]
                # print(self.map[index].key)
                self.map[index] = dummy
                # print(self.map[index].key)
                print("Item deleted")
                break
            index = (index + 1) % 31
        
        idx = temp.value
        self.swap(idx,len(self.heap)-1)
        # self.heap.pop()
        self.heap[len(self.heap)-1] = None
        self.bubbleUp(idx)
        self.bubbleDown(idx)

    def bubbleDown(self,idx):
        while True:
            left = 2*idx + 1
            right = 2*idx + 2
            smallest = idx
            if left < len(self.heap) and self.heap[left]["priority"] < self.heap[smallest]["priority"]:
                smallest = left
            if right < len(self.heap) and self.heap[right]["priority"] < self.heap[smallest]["priority"]:
                smallest = right
            if smallest != idx:
                self.swap(idx,smallest)
                idx = smallest
            else:
                break

    def maxPriority(self):
        return self.heap[0]
        

        


if __name__ == "__main__":
    hpq = HybridPriorityQueue()
    data_sets = {
        "Liam": {
            "age": 41,
            "room_number": 304,
            "phone_number": "555-5678",
            "priority": 2,
        },
        "Emily": {
            "age": 32,
            "room_number": 205,
            "phone_number": "555-1234",
            "priority": 1,
        },
        "Benjamin": {
            "age": 45,
            "room_number": 311,
            "phone_number": "555-5678",
            "priority": 17,
        },
        "Noah": {
            "age": 37,
            "room_number": 404,
            "phone_number": "555-4321",
            "priority": 4,
        },
        "Ava": {
            "age": 44,
            "room_number": 506,
            "phone_number": "555-8765",
            "priority": 5,
        },
        "Isabella": {
            "age": 31,
            "room_number": 206,
            "phone_number": "555-1234",
            "priority": 6,
        },
        "Sophia2": {
            "age": 43,
            "room_number": 515,
            "phone_number": "555-8765",
            "priority": 25,
        },
        "Alexander": {
            "age": 39,
            "room_number": 410,
            "phone_number": "555-4321",
            "priority": 14,
        },
        "Olivia": {
            "age": 28,
            "room_number": 103,
            "phone_number": "555-9090",
            "priority": 3,
        },
        "Sophia": {
            "age": 36,
            "room_number": 307,
            "phone_number": "555-5678",
            "priority": 7,
        },
        "Harper": {
            "age": 33,
            "room_number": 207,
            "phone_number": "555-1234",
            "priority": 11,
        },
        "Abigail": {
            "age": 27,
            "room_number": 110,
            "phone_number": "555-9090",
            "priority": 13,
        },
        "Mia": {
            "age": 29,
            "room_number": 108,
            "phone_number": "555-9090",
            "priority": 8,
        },
        "Charlotte": {
            "age": 38,
            "room_number": 409,
            "phone_number": "555-4321",
            "priority": 9,
        },
        "Amelia": {
            "age": 43,
            "room_number": 511,
            "phone_number": "555-8765",
            "priority": 10,
        },
        "Grace": {
            "age": 31,
            "room_number": 114,
            "phone_number": "555-9090",
            "priority": 23,
        },
        "Samuel": {
            "age": 37,
            "room_number": 209,
            "phone_number": "555-1234",
            "priority": 21,
        },
        "Elizabeth": {
            "age": 30,
            "room_number": 112,
            "phone_number": "555-9090",
            "priority": 18,
        },
        "Joseph": {
            "age": 26,
            "room_number": 513,
            "phone_number": "555-8765",
            "priority": 20,
        },
        "Henry": {
            "age": 35,
            "room_number": 412,
            "phone_number": "555-4321",
            "priority": 19,
        },
        "Evelyn": {
            "age": 40,
            "room_number": 309,
            "phone_number": "555-5678",
            "priority": 12,
        },
        "David": {
            "age": 38,
            "room_number": 414,
            "phone_number": "555-4321",
            "priority": 24,
        },
        "James": {
            "age": 42,
            "room_number": 512,
            "phone_number": "555-8765",
            "priority": 15,
        },
        "Daniel": {
            "age": 34,
            "room_number": 208,
            "phone_number": "555-1234",
            "priority": 16,
        },
        "Victoria": {
            "age": 44,
            "room_number": 313,
            "phone_number": "555-5678",
            "priority": 22,
        },
    }

    name_priority_dict = {}
    for name,priority in data_sets.items():
        name_priority_dict[name] = priority["priority"]

    
    # print(name_priority_dict)

    for name, details in data_sets.items():
        hpq.insert(name, details["age"], details["room_number"], details["phone_number"], details["priority"])

    # print(hpq.search(name_priority_dict["Noah"]))
    # print(hpq.abc())
    print("Searching : ")
    print(hpq.search(name_priority_dict["Noah"]))
    print("Deleting: ")
    hpq.delete(name_priority_dict["Noah"])
    # print(name_priority_dict["Noah"])
    print("Finding element with Max Priority: ")
    print(hpq.maxPriority())
    print("Displaying Heap : ")
    print(hpq.displayHeap())
    print("Displaying HahMap : ")
    print(hpq.displayHash())


