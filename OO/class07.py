import enum

# Colors = enum.Enum("Colors", ["RED", "BLUE", "WHITE"])
# print(Colors.RED)

class Colors(enum.Enum):

    RED = enum.auto()
    BLUE = enum.auto()
    WHITE = enum.auto()

print(Colors.RED)
print(Colors.RED.value)