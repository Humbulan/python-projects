import os # This should be at the very top

# Define the file name where photos will be stored
PHOTO_FILE = "my_photos.txt"

# --- load_photos function definition ---
def load_photos():
    # ... (your load_photos code with debug prints) ...

# --- save_photos function definition ---
def save_photos(photos):
    # ... (your save_photos code with debug prints) ...

# --- display_photos function definition (THIS IS THE ONE THAT WAS MISSING OR MISPLACED) ---
def display_photos(photos):
    if not photos:
        print("Your photo roll is empty.")
    else:
        print("\n--- Your Photo Roll ---")
        for i, photo in enumerate(photos):
            print(f"{i + 1}. {photo}")
        print("-----------------------")

# --- add_photo function definition ---
def add_photo(photos):
    photo_name = input("Enter photo name (or 'q' to quit): ")
    if photo_name.lower() != 'q':
        photos.append(photo_name)
        print(f"'{photo_name}' added to your roll.")
    return photo_name # Return the input directly

# --- main function definition (should be below all functions it calls) ---
def main():
    my_photos = load_photos()

    print("Welcome to your simple Photo Roll Manager!")

    while True:
        display_photos(my_photos) # This line calls display_photos
        user_input = add_photo(my_photos)
        if user_input.lower() == 'q':
            break

    save_photos(my_photos)
    print("Exiting Photo Roll Manager. Goodbye!")

# --- Entry point for the script ---
if __name__ == "__main__":
    main()

