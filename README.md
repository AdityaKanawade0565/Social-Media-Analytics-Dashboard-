# Social Media Dashboard

## Overview

This project is a Social Media Dashboard built using Flask, integrating data from YouTube and Instagram. It provides insights into YouTube channel statistics and Instagram user information.

## Features

- **YouTube Dashboard:**
  - View channel stats, including subscribers, views, and total videos.
  - Explore detailed information on individual videos.
  - Visualize data with Plotly charts.

- **Instagram Dashboard:**
  - Retrieve user information, such as username, followers, and bio.
  - Explore recent posts with details like likes, comments, and hashtags.
  - Visualize user interaction with Chart.js.

## Technologies Used

- **Backend:**
  - Flask (Python web framework)
  - YouTube Data API for video data
  - Instaloader library for user data

- **Frontend:**
  - HTML templates with Jinja templating
  - Bootstrap for responsive and stylish UI
  - Chart.js and Plotly for data visualization

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AdityaKanawade0565/social-media-dashboard.git
   cd social-media-dashboard

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Set up API keys:**

  Obtain API keys for YouTube and Instagram.
  Update the keys in the appropriate configuration files.

4. **Run the application:**
    ```bash
    python app.py

5. Open your browser and navigate to http://localhost:5000 to access the dashboard.

## Folder Structure

- `static/`: Contains static files (CSS, JS, images).
- `templates/`: HTML templates for different pages.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements or bug fixes.
