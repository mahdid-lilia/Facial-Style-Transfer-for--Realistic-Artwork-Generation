import streamlit as st

import sys
sys.path.append('/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/')

from PIL import Image
from src.utils import stylize, experimental
import tempfile

def main():
    st.title("Facial Style Transfer for Realistic Artwork Generation")

    # Model selection
    model_options = [
        "TransformerNetworkV2",
        "TransformerResNextNetwork_Pruned"
    ]
    # Handle alpha value for TransformerResNextNetwork_Pruned model
    selected_model = st.selectbox("Select Model", model_options)
    if selected_model == "TransformerResNextNetwork_Pruned":
        alpha = st.slider("Alpha", 0.3, 1.0, 0.3, 0.7)
        model = experimental.TransformerResNextNetwork_Pruned(alpha)
    else:
        model = getattr(experimental, selected_model)()
        alpha = None

        
    # Display style image based on selected model and alpha value
    style_image_path = get_style_image_path(selected_model, alpha)
    style_image = Image.open(style_image_path)
    st.image(style_image, caption="Style Image", use_column_width=False)


    # Define checkpoint path and content path based on selected model and alpha
    checkpoint_path = "/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/models"
    if selected_model == "TransformerResNextNetwork_Pruned":
        if alpha == 1.0:
            selected_path = "/7. mosaic_TransformerResNextNetwork_Pruned10/checkpoints/checkpoint_5000.pth"
        elif alpha == 0.3:
            selected_path = "/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_d1500.pth"
    elif selected_model == "TransformerNetworkV2":
        selected_path = "/5. mosaic_TransformerNetworkV2/checkpoints/checkpoint_d2500.pth"

    checkpoint = checkpoint_path + selected_path

    # Image upload
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        save_button = st.button("Stylize Image")

        if save_button:
            # Create a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
                temp_file.write(uploaded_image.read())
                temp_file_path = temp_file.name

            # Specify the save path here
            save_image_path = "/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/streamlit_app/output/image.png"
            
            # Call the stylize_image function with the additional parameters
            stylize_image(checkpoint, temp_file_path, save_image_path, model)
            
            # Display the stylized image (optional)
            st.image(save_image_path, caption="Stylized Image", use_column_width=True)

            # Display style image, content image, and generated image in three columns
            st.write("### Style, Content, and Generated Images")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(style_image, caption="Style Image", use_column_width=True)
            with col2:
                if uploaded_image is not None:
                    st.image(uploaded_image, caption="Content Image", use_column_width=True)
            with col3:
                if save_button:
                    st.image(save_image_path, caption="Generated Image", use_column_width=True)

def stylize_image(checkpoint, content_image_path, save_image_path, model):
    # Perform stylization using the selected model
    stylize.stylize(checkpoint, content_image_path, save_image_path, model)

def get_style_image_path(selected_model, alpha):
    if selected_model == "TransformerResNextNetwork_Pruned":
        if alpha == 1.0:
            return "/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/streamlit_app/style_image/7. mosaic_TransformerResNextNetwork_Pruned10.png"
        elif alpha == 0.3:
            return "/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/streamlit_app/style_image/3. mosaic_TransformerResNextNetwork_Pruned03.png"
       
    elif selected_model == "TransformerNetworkV2":
        return "/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/streamlit_app/style_image/5. mosaic_TransformerNetworkV2.png"
    else:
        # Default to an empty string if no style image is found
        return ""
    
if __name__ == "__main__":
    main()
