import instaloader
import json
import re

def clean_text(text):
    # Remove non-alphanumeric characters and leading/trailing whitespaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).strip()
    return cleaned_text


def get_instagram_stats(username, password):
    L = instaloader.Instaloader()

    try:
        # Optionally, login or load session
        L.context.username = username
        L.context.password = password
        L.login(username, password)  # Ask password on the terminal
    except instaloader.exceptions.InstaloaderException as e:
        L.context.log(f"Login failed: {e}")
        return None  # Return None to indicate login failure

    profile = instaloader.Profile.from_username(L.context, username)

    # Create a dictionary to store Instagram statistics
    instagram_stats = {
        "username": profile.username,
        "full_name": clean_text(profile.full_name),
        "followers_count": profile.followers,
        "following_count": profile.followees,
        "bio": clean_text(profile.biography),
        "posts": [],
        "likes_vs_hashtags": {
            "likes": [],
            "hashtags": []
        }
    }

    # Populate the dictionary with post information
    for post in profile.get_posts():
        hashtags = [tag.strip("#") for tag in post.caption_hashtags] if post.caption_hashtags else []
        cleaned_caption = clean_text(post.caption)

        post_info = {
            "title": post.title,
            "likes_count": post.likes,
            "comments_count": post.comments,
            "caption": cleaned_caption,
            "hashtags": hashtags,
            "date": post.date.strftime("%Y-%m-%d %H:%M:%S")
        }
        instagram_stats["posts"].append(post_info)

        # Update likes_vs_hashtags data
        instagram_stats["likes_vs_hashtags"]["likes"].append(post.likes)
        instagram_stats["likes_vs_hashtags"]["hashtags"].append(", ".join(hashtags))

    return instagram_stats
