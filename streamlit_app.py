import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Add custom CSS
st.markdown(
    """
    <style>
    .tile {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        transition: transform 0.2s, box-shadow 0.2s;
        background-color: #f9f9f9;
    }
    .tile:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    .tile img {
        max-width: 100%;
        height: auto;
        border-radius: 5px;
    }
    .tile h3 {
        margin-top: 10px;
    }
    .tile a {
        text-decoration: none;
        color: #333;
    }
    .tile a:hover {
        color: #007BFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the page configuration
st.set_page_config(
    page_title="My Projects Dashboard",
    page_icon="🧰",
    layout="wide",
)

# Title and description
st.title("🚀 My Projects")
st.markdown("""
Welcome to my projects dashboard! Click on any tile below to explore the respective project.
""")

# Function to create a project tile with HTML
def create_tile(image_path, project_name, project_link):
    img = Image.open(image_path)
    img_base64 = image_to_base64(img)
    tile_html = f"""
    <div class="tile">
        <img src="data:image/png;base64,{img_base64}" alt="{project_name}">
        <h3><a href="{project_link}" target="_blank">{project_name}</a></h3>
    </div>
    """
    st.markdown(tile_html, unsafe_allow_html=True)

# Define project details
projects = [
    {
        "name": "Project One",
        "image": "assets/project1.png",
        "link": "https://github.com/username/project-one"
    },
    {
        "name": "Project Two",
        "image": "assets/project2.png",
        "link": "https://github.com/username/project-two"
    },
    {
        "name": "Project Three",
        "image": "assets/project3.png",
        "link": "https://github.com/username/project-three"
    },
    {
        "name": "Project Four",
        "image": "assets/project4.png",
        "link": "https://github.com/username/project-four"
    },
    # Add more projects as needed
]

# Number of columns per row
cols_per_row = 2

# Create the grid of tiles using Streamlit's columns
for i in range(0, len(projects), cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(projects):
            project = projects[i + j]
            with cols[j]:
                create_tile(project["image"], project["name"], project["link"])
