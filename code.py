pip install requests

import requests

# Replace with your values
ACCESS_TOKEN = "YOUR_INSTAGRAM_ACCESS_TOKEN"
INSTAGRAM_ACCOUNT_ID = "YOUR_IG_BUSINESS_ACCOUNT_ID"

# Step 1: Upload an image to the container
image_url = "https://www.example.com/sample.jpg"  # Publicly accessible image URL
caption = "🚀 Hello Instagram! This post was made using Python & the Instagram Graph API. #Python #Automation"

create_url = f"https://graph.facebook.com/v21.0/{INSTAGRAM_ACCOUNT_ID}/media"
create_payload = {
    "image_url": image_url,
    "caption": caption,
    "access_token": ACCESS_TOKEN
}

create_res = requests.post(create_url, data=create_payload)
if create_res.status_code != 200:
    print("❌ Error creating media:", create_res.text)
    exit()

media_id = create_res.json()["id"]
print("✅ Media container created:", media_id)

# Step 2: Publish the media
publish_url = f"https://graph.facebook.com/v21.0/{INSTAGRAM_ACCOUNT_ID}/media_publish"
publish_payload = {
    "creation_id": media_id,
    "access_token": ACCESS_TOKEN
}

publish_res = requests.post(publish_url, data=publish_payload)
if publish_res.status_code == 200:
    print("✅ Post published successfully:", publish_res.json())
else:
    print("❌ Error publishing:", publish_res.text)
