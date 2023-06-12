class MyDictionary:
    def __init__(self):
        self.dictionary = {}

    def add(self, key, value):
        self.dictionary[key] = value

    def remove(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def update(self, key, value):
        if key in self.dictionary:
            self.dictionary[key] = value
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def sort(self):
        sorted_dict = dict(sorted(self.dictionary.items()))
        self.dictionary = sorted_dict

    def search(self, value):
        keys = []
        for key, val in self.dictionary.items():
            if val == value:
                keys.append(key)
        return keys

    def print_values(self):
        for key, value in self.dictionary.items():
            print(f"Key: {key}, Value: {value}")


# Example usage
my_dict = MyDictionary()

my_dict.add("apple", 10)
my_dict.add("banana", 5)
my_dict.add("orange", 7)

my_dict.print_values()

my_dict.remove("banana")

my_dict.update("orange", 12)

sorted_dict = my_dict.sort()

keys = my_dict.search(7)
print("Keys with value 7:", keys)
