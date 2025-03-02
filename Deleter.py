import requests

def create_gradient_text(text, start_color, end_color):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (0, 2, 4))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (0, 2, 4))
    
    steps = len(text)
    step_r = (end_rgb[0] - start_rgb[0]) / steps
    step_g = (end_rgb[1] - start_rgb[1]) / steps
    step_b = (end_rgb[2] - start_rgb[2]) / steps
    
    gradient_text = ""
    for i, char in enumerate(text):
        r = int(start_rgb[0] + (step_r * i))
        g = int(start_rgb[1] + (step_g * i))
        b = int(start_rgb[2] + (step_b * i))
        gradient_text += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
    
    return gradient_text

def delete_discord_webhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print(create_gradient_text("Webhook deleted successfully.", "ffffff", "800080"))
        else:
            print(create_gradient_text("Failed to delete the webhook.", "ffffff", "800080"))
    except requests.exceptions.RequestException as e:
        print(create_gradient_text(f"An error occurred while deleting the webhook: {e}", "ffffff", "800080"))

def delete_webhooks_from_file(file_path):
    with open(file_path, 'r') as file:
        webhook_urls = file.readlines()
        for webhook_url in webhook_urls:
            webhook_url = webhook_url.strip()
            delete_discord_webhook(webhook_url)

def delete_webhooks_from_input():
    webhook_urls = input("Enter the Discord Webhook URLs to delete (separated by newline): ")
    for webhook_url in webhook_urls.split('\n'):
        webhook_url = webhook_url.strip()
        delete_discord_webhook(webhook_url)

choice = input("Choose an option:\n1. Import from file\n2. Import from copy/paste\n")

if choice == '1':
    file_path = r"ACTUAL_PATH_TO_YOUR_WEBHOOKS_FILE.txt" # replace with actual path to your webhook urls txt
    delete_webhooks_from_file(file_path)
elif choice == '2':
    delete_webhooks_from_input()
else:
    print(create_gradient_text("Invalid choice. Please enter '1' or '2'.", "ffffff", "800080"))