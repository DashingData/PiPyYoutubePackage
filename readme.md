# 📺 YoutubePackage: Embed & Explore YouTube Videos in Jupyter

Welcome to the `YoutubePackage` 📦 — an easy-to-use Python package to:
- Embed YouTube videos directly in Jupyter Notebooks
- Fetch and preview metadata like video title, thumbnail, and author





# Installation (Editable Mode for Devs)
In terminal (run this in your project root folder):                  




 pip install -e .






# Import the Functions

from Youtube_package.embed import embed_youtube


from Youtube_package.metadata import fetch_video_metadata



from Youtube_package.preview import preview_youtube








#  Embed a YouTube Video in Notebook

This will show an embedded player (works only in Jupyter Notebook)


  
embed_youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")









# Fetch Video Metadata (title, author, thumbnail)
metadata = fetch_video_metadata("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


metadata










# Preview Video with Thumbnail & Title
preview_youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")










#  Error Handling Examples

# Should raise ValueError (invalid YouTube link)
try:

    embed_youtube("https://example.com/invalid")
    
except ValueError as e:

    print("Error:", e)








#  What's Coming Next? (Future Scope)


- Playlist embedding
- Channel preview
- Custom theme/styling for previews
- Auto-fetch captions, duration, views











