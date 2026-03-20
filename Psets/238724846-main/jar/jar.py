from sys import exit

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        self.size += n
        return f"🍪" * self.size

    def withdraw(self, n):
        self.size -= n
        return f"🍪" * self.size

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if not capacity > 0:
            raise ValueError("Enter a positive decimal")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size exceeded the jar's capacity")
        if size < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size = size

def main():
    try:
        Ncookies = int(input("How many cookies do you want? "))
    except ValueError:
        exit("Invaild input")

    jar1 = Jar(size=Ncookies)
    print(jar1)
    jar1 = jar1.deposit(2)
    print(jar1)

if __name__ == "__main__":
    main()
