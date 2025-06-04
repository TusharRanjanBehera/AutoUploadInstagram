from instagrapi import Client

# Initialize the client
cl = Client()

# Login to Instagram
username = "dilki8210"
password = "Rabbit@1996"
cl.login(username, password)

# Fetch the user's feed
feed = cl.user_feed(cl.user_id)

# Display the first post
if feed:
    first_post = feed[0]
    print("Caption:", first_post.caption_text)
    print("Image URL:", first_post.thumbnail_url)
    print("Post URL:", f"https://www.instagram.com/p/{first_post.code}/")
else:
    print("No posts found in the feed.")