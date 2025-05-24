import pyautogui

def get_real_screen_resolution():
    """
    Get the actual screen resolution from the user's device.
    Returns:
        tuple: (width, height)
    """
    width, height = pyautogui.size()
    return width, height

def scale_coordinates(gpt_x, gpt_y, gpt_res, real_res):
    """
    Scale GPT-provided coordinates to match the actual screen resolution.
    
    Args:
        gpt_x (int): x-coordinate from GPT
        gpt_y (int): y-coordinate from GPT
        gpt_res (tuple): (width, height) GPT sees
        real_res (tuple): (width, height) of the actual screen
    
    Returns:
        tuple: Scaled (x, y) for real screen
    """
    scale_x = real_res[0] / gpt_res[0]
    scale_y = real_res[1] / gpt_res[1]
    return int(gpt_x * scale_x), int(gpt_y * scale_y)
