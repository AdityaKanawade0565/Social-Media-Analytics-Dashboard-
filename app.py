from flask import Flask, render_template, request, redirect, url_for
from youtube_data import get_youtube, get_channel_stats, get_playlist_id, get_video_ids, get_video_details
from instagram_data import get_instagram_stats

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/youtube/form')
def youtube_form():
    return render_template('forms/youtube_form.html')

@app.route('/instagram/form')
def instagram_form():
    return render_template('forms/instagram_form.html')

@app.route('/facebook/form')
def facebook_form():
    return render_template('forms/facebook_form.html')

@app.route('/youtube/process', methods=['POST'])
def process_youtube_form():
    # Process the form data (you can add your logic here)
    channel_id = request.form['channel_id']

    # Call the YouTube data functions
    youtube = get_youtube()
    channel_stats = get_channel_stats(youtube, channel_id)
    
    if not channel_stats:
        # Handle the case where channel data could not be retrieved
        return render_template('error.html', message="Error fetching channel data")

    playlist_id = get_playlist_id(youtube, channel_id)
    video_ids = get_video_ids(youtube, playlist_id)
    video_details = get_video_details(youtube, video_ids)

    # Convert 'Views' to int before passing it to the template
    for video in video_details:
        video['Views'] = int(video['Views'])
        video['Likes'] = int(video['Likes'])  # Add this line to convert 'Likes' to int

    # Pass the data to the template
    return render_template('youtube_dashboard.html', channel_stats=channel_stats, video_details=video_details)


@app.route('/instagram/process', methods=['POST'])
def process_instagram_form():
    username = request.form['username']
    password = request.form['password']

    try:
        # Call the Instagram data function
        instagram_stats = get_instagram_stats(username, password)

        if not instagram_stats:
            # Handle the case where Instagram data could not be retrieved
            return render_template('error.html', message="Error fetching Instagram data. Please try again later.")

        # Pass the data to the template
        return render_template('instagram_dashboard.html', instagram_stats=instagram_stats)

    except Exception as e:
        # Print or log the exception details
        print(f"An error occurred while fetching Instagram data: {e}")

        # Handle the error in a way that suits your application
        return render_template('error.html', message=f"An unexpected error occurred: {e}")
    
@app.route('/facebook/process', methods=['POST'])
def process_facebook_form():
    username = request.form['username']
    # Process the form data (you can add your logic here)
    return redirect(url_for('facebook_dashboard'))

@app.route('/youtube/dashboard')
def youtube_dashboard():
    # Add YouTube dashboard logic here
    return "YouTube Dashboard"

@app.route('/instagram/dashboard')
def instagram_dashboard():
    # Add Instagram dashboard logic here
    return "Instagram Dashboard"

@app.route('/facebook/dashboard')
def facebook_dashboard():
    # Add Facebook dashboard logic here
    return "Facebook Dashboard"

if __name__ == '__main__':
    app.run(debug=True)
