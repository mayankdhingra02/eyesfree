from PIL import ImageGrab

def take_screenshot(save_path="screenshot.png"):
    image = ImageGrab.grab()
    image.save(save_path)
    return save_path
