from capture import take_screenshot
from vision_prompt import send_image_to_gpt
from scale import get_real_screen_resolution, scale_coordinates
import json

if __name__ == "__main__":
    # Step 1: Capture the screen
    screenshot_path = take_screenshot()
    
    # Step 2: Ask GPT-4o what resolution it sees
    prompt = (
    "You are a vision model that always receives an image resized by OpenAI. "
    "Please return the resolution (width and height in pixels) that you are perceiving this image to be, "
    "in JSON format only. Do not say anything else. Respond like this: {\"width\": 1024, \"height\": 576}"
)

    
    gpt_response = send_image_to_gpt(screenshot_path, prompt)

    print("🧠 GPT-4o Response:", gpt_response)

    # Step 3: Parse GPT's perceived resolution
    try:
        gpt_resolution = json.loads(gpt_response)
        print("✅ GPT-perceived resolution:", gpt_resolution)
    except json.JSONDecodeError:
        print("❌ Failed to parse GPT response.")
        gpt_resolution = None

    # Step 4: Compare to real resolution and test scaling
    if gpt_resolution and "width" in gpt_resolution and "height" in gpt_resolution:
        real_res = get_real_screen_resolution()
        gpt_res = (gpt_resolution["width"], gpt_resolution["height"])
        print("🖥️ Real screen resolution:", real_res)

        # Dummy coordinates from GPT (simulate GPT said click here)
        gpt_x, gpt_y = 500, 300
        scaled_x, scaled_y = scale_coordinates(gpt_x, gpt_y, gpt_res, real_res)
        print(f"🎯 Scaled click position: ({scaled_x}, {scaled_y})")
    else:
        print("⚠️ Skipping scaling due to missing resolution info.")
