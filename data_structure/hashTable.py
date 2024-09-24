class HashTable:
    def __init__(self, length = 5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]
    
    def set(self, key, value):
        index = hash(key) % self.max_len
        for i, (k, v) in enumerate(self.table[index]):
            if k == key: # 기존 키의 값을 갱신
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))  # 새 키-값 쌍 추가

    def get(self, key):
        index = hash(key) % self.max_len
        value = self.table[index]
        if not value:
            return None
        for v in value:
            if v[0] == key:
                return v[1]
        return None

if __name__ == '__main__':
    capital = HashTable()
    country = ["Korea", "America", "China", "England", "Turkiye"]
    city = ["Seoul", "Washington", "Beijing", "London", "Ankara"]
    for co, ci in zip(country, city):
        capital.set(co, ci)
        
    print("Hash Table State")
    print("====================")
    for i, v in enumerate(capital.table):
        print(i, v)
    print()
    print("====================")
    print(f"Captial of America = {capital.get('America')}")
    print(f"Captial of Korea = {capital.get('Korea')}")
    print(f"Captial of England = {capital.get('England')}")
    print(f"Captial of China = {capital.get('China')}")
    print(f"Captial of Japan = {capital.get('Japan')}")
    print(f"Captial of Türkiye = {capital.get('Turkiye')}")