# pytterns
This library implement design-patterns and common functions for python

### Installation
```
pip install pytterns
```

### Builder
How to create a class builder:

```Python
from pytterns.Build import Build

# Create a class and decorate de class with Build
@Build
class Test:
    def __init__(self) -> None:
        self.attribute_1: str = None
        self.attribute_2: int = None

test_obj = Test().attribute_1('attribute_1').attribute_2(1).build

print(test_obj.attribute_1)
print(test_obj.attribute_2)
```