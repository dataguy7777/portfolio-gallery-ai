# src/streamlit_app.py

import os
import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Import helper functions and components
from utils.helpers import image_to_base64
from components.tile import create_tile

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# For debugging: Display current working directory and script directory
# Remove or comment out these lines in production
st.write(f"**Current Working Directory:** {os.getcwd()}")
st.write(f"**Script Directory:** {current_dir}")

# Set the page configuration first
st.set_page_config(
    page_title="My Projects Dashboard",
    page_icon="🧰",
    layout="wide",
)

# Add custom CSS
def load_css():
    css_path = os.path.join(current_dir, '../assets/styles/custom.css')
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {css_path}")

load_css()

# Title and description
st.title("🚀 My Projects")
st.markdown("""
Welcome to my projects dashboard! Click on any tile below to explore the respective project.
""")

# Define project details with all images pointing to project2.jpg as a placeholder
projects = [
    {
        "name": "Project One",
        "image": os.path.join(current_dir, "../assets/images/project2.jpg"),
        "link": "https://github.com/username/project-one"
    },
    {
        "name": "Project Two",
        "image": os.path.join(current_dir, "../assets/images/project2.jpg"),
        "link": "https://github.com/username/project-two"
    },
    {
        "name": "Project Three",
        "image": os.path.join(current_dir, "../assets/images/project2.jpg"),
        "link": "https://github.com/username/project-three"
    },
    {
        "name": "Project Four",
        "image": os.path.join(current_dir, "../assets/images/project2.jpg"),
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
