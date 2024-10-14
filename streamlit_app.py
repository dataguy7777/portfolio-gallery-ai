import os
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# ------------------------------
# Helper Functions
# ------------------------------

def image_to_base64(image, format="JPEG"):
    """
    Convert a PIL Image to a base64 string.

    Args:
        image (PIL.Image.Image): The image to convert.
        format (str): The format to save the image in (e.g., "JPEG", "PNG").

    Returns:
        str: Base64 encoded string of the image.
    """
    try:
        buffered = BytesIO()
        image.save(buffered, format=format)
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception as e:
        st.error(f"Error converting image to base64: {e}")
        return ""

# ------------------------------
# Component Functions
# ------------------------------

def create_tile(image_path, project_name, project_link):
    """
    Create a project tile with an image and a clickable link.

    Args:
        image_path (str): Path to the project image.
        project_name (str): Name of the project.
        project_link (str): URL to the project.
    """
    # Attempt to open the image
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
        return
    except Exception as e:
        st.error(f"Error loading image {image_path}: {e}")
        return

    # Convert image to base64
    img_base64 = image_to_base64(img, format="JPEG")
    if not img_base64:
        st.error(f"Failed to convert image to base64: {image_path}")
        return

    # Generate HTML for the tile
    tile_html = f"""
    <div class="tile">
        <img src="data:image/jpeg;base64,{img_base64}" alt="{project_name}">
        <h3><a href="{project_link}" target="_blank">{project_name}</a></h3>
    </div>
    """
    st.markdown(tile_html, unsafe_allow_html=True)

# ------------------------------
# Page Configuration
# ------------------------------

st.set_page_config(
    page_title="My Projects Dashboard",
    page_icon="🧰",
    layout="wide",
)

# ------------------------------
# Load Custom CSS
# ------------------------------

def load_css():
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'styles', 'custom.css')
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {css_path}")

load_css()

# ------------------------------
# Title and Description
# ------------------------------

st.title("🚀 My Projects")
st.markdown("""
Welcome to my projects dashboard! Click on any tile below to explore the respective project.
""")

# ------------------------------
# Define Project Details
# ------------------------------

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the placeholder image
placeholder_image = os.path.join(current_dir, 'assets', 'images', 'project2.jpg')

# Verify that the placeholder image exists
if not os.path.exists(placeholder_image):
    st.error(f"Placeholder image not found: {placeholder_image}")
else:
    # Define project details with all images pointing to the placeholder
    projects = [
        {
            "name": "Project One",
            "image": placeholder_image,
            "link": "https://github.com/username/project-one"
        },
        {
            "name": "Project Two",
            "image": placeholder_image,
            "link": "https://github.com/username/project-two"
        },
        {
            "name": "Project Three",
            "image": placeholder_image,
            "link": "https://github.com/username/project-three"
        },
        {
            "name": "Project Four",
            "image": placeholder_image,
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
