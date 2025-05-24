from capture import take_screenshot
from vision_prompt import send_image_to_gpt

if __name__ == "__main__":
    screenshot_path = take_screenshot()
    prompt = "Please describe all visible UI elements on the screen."
    result = send_image_to_gpt(screenshot_path, prompt)
    print("🧠 GPT-4 Vision Response:\n", result)
