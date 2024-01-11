class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class HomeDesigner:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def calculate_total_area(self):
        total_area = sum(room.calculate_area() for room in self.rooms)
        return total_area


def main():
    designer = HomeDesigner()

    while True:
        print("1. Add Room")
        print("2. Calculate Total Area")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter room name: ")
            length = float(input("Enter room length: "))
            width = float(input("Enter room width: "))
            room = Room(name, length, width)
            designer.add_room(room)
            print("Room added successfully!")

        elif choice == "2":
            total_area = designer.calculate_total_area()
            print(f"Total area of the home: {total_area} square units")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
