class Rectangle:
      def __init__(self, width, length):
            self.width = width
            self.length = length

      def get_area(self):
            return (self.width * self.length)
      
      def get_perimeter(self):
            return (self.width + self.width + self.length + self.length)
      
rect = Rectangle(20, 40)

print("A rectangle has been created with width 20 and length 40. Function calls below:\n")

print(rect.get_area(), rect.get_perimeter())