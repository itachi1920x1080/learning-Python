def write_items_to_file(items, filename):
    try:
        with open(filename, 'w') as file:
            for item in items:
                file.write(item + '/')

    except Exception as e:
        print(f"Error writing to file: {e}")

def read_items_from_file(filename):
    try:
        with open(filename,'r') as file:
            items = file.readlines()
            print("Items read from file:")
            for item in items:
                if item:
                    print(item.strip())
            return [item.strip() for item in items]
    except FileNotFoundError:
        print("File not found")
        return []
    
def additem_to_file(item, filename):
    try:
        with open(filename,'a') as file :
            file.write(item + '/')
    except Exception as e:
        print(f"Error appending to file: {e}")
if __name__ == "__main__":
    items_to_write = []
    filename = 'items.txt'
    while True:
        try:
            print("\nMenu:")
            print("1. Write items to file")
            print("2. Read items from file")
            print("3. Add an item to file")
            print("4. Exit")
            choice = input("Choose an option: ")
            match choice:
                case '1':
                    write_items_to_file(items_to_write, filename)
                case '2':
                    read_items_from_file(filename)
                case '3':
                    new_item = input("Enter the item to add: ")
                    additem_to_file(new_item, filename)
                case '4':
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")