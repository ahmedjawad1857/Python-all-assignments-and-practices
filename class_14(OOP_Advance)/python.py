# Method Overloading



from typing import Union, overload

class Adder:
    @overload
    def add(self, x: int, y: int) -> int:
        ...
        
    @overload
    def add(self, x: float, y: float) -> float:
        ...
        
    @overload
    def add(self, x: str, y: str) -> str:
        ...
        
    
    def add(self, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        elif isinstance(x, float) and isinstance(y, float):
            return x + y
        elif isinstance(x, str) and isinstance(y, str):
            return x + y
        else:
            raise TypeError("Invalid argument types!")

# Usage examples
adder = Adder()
result1 = adder.add(1, 2)  # Should return 3
result2 = adder.add(1.9, 2.5)  # Should return 4.0
result3 = adder.add("Hello, ", "world!")  # Should return "Hello, world!"

print(result1)
print(result2)
print(result3)

# Overridding & polymorphism