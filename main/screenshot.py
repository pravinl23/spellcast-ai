import tkinter as tk
import os
from PIL import ImageGrab

# Load region from the file region_data.txt which is collected by the program on setup_region.py
def load_region():
    with open('region_data.txt', 'r') as f:
        region_data = f.read().split(',')
        # after region data is extracted remove the region_data.txt file
        os.remove('region_data.txt')
        return tuple(map(int, region_data))

def take_screenshot():
    # Take a screenshot of the specified region
    screenshot_path = "grid.png"
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)  # Delete the previous screenshot if it exists already
    
    left, top, width, height = region
    right = left + width
    bottom = top + height
    
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save(screenshot_path)

    root.destroy()


if __name__ == "__main__":

    region = load_region()
    # Create the popup window for defining region
    root = tk.Tk()
    # This is for the actual window not button
    root.title("Spellcast AI")
    root.geometry("300x100")
    root.configure(bg="azure2")

    # This is for the button on the popup window
    button = tk.Button(
        root,
        text="Get Words",
        font='Helvetica 18 bold',
        command=take_screenshot # Calls the define_region function on click
    )

    button.pack(pady=20)

    # Start the tkinter event loop to display the popup window
    root.mainloop()