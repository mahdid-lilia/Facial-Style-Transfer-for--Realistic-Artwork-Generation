# Facial-Style-Transfer-for-Realistic-Artwork-Generation

## Stylize Script
This script allows you to stylize images using a pre-trained model. It takes command-line arguments to specify the input image, the checkpoint file containing the pre-trained model, and the path to save the stylized image.

### Requirements

- Python 3.x
- torch
- opencv-python
- torchvision

### Usage

1. Clone the repository:
   ```shell
   $ git clone https://github.com/mahdid-lilia/Facial-Style-Transfer-for-Realistic-Artwork-Generation.git
   $ cd Facial-Style-Transfer-for-Realistic-Artwork-Generation
   ```

2. Run the script with the following command:

   ```shell
   python setup.py <option> <arguments>
   ```

   Replace `<option>` and `<arguments>` with the appropriate values:

   - `<option>`: Specify the option for stylizing the image. Currently, options supported are `single_image` and `folder`.
   - `<arguments>`:
     - `--content`: Path to the content image (for single image stylization) or folder path containing images (for batch stylization).
     - `--checkpoint`: Path to the checkpoint file containing the pre-trained model.
     - `--save`: Path to save the stylized image or folder path to save stylized images.
     - `--model`: Specify the model name for stylization.
     - Additional arguments specific to the chosen model (e.g., `alpha` for `TransformerResNextNetwork_Pruned` model).

### Example
Stylize a single image:
   ```shell
   content_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/test_1.jpeg"
   checkpoint_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/models/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_d1500.pth"
   output_path="image.png"
   model_name="TransformerResNextNetwork_Pruned"
   alpha=0.3

   python setup.py single_image --content "$content_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name" "$alpha"
   ```

Stylize images in a folder:
   ```shell
   folder_path="/workspaces/Facial-Style-Transfer-for-Realistic-Artwork-Generation/data/test/"
   checkpoint_path="models/3. TransformerResNextNetwork_Pruned03/checkpoints/checkpoint_d1500.pth"
   output_path="data/output/3. TransformerResNextNetwork_Pruned03/"
   model_name="TransformerResNextNetwork_Pruned"
   alpha=0.3

   python setup.py folder --folder "$folder_path" --checkpoint "$checkpoint_path" --save "$output_path" --model "$model_name" "$alpha"
   ```


## Test Results




<div style="background-color: #ffffff; padding: 20px; border-radius: 10px;">
    <h1 style="color: blue;">Streamlit App Demo</h1>
    <p style="color: #333;">This is our Streamlit web application for Facial Style Transfer, allowing users to apply artistic styles to their images in a realistic manner. The application offers a selection of our previous pre-trained models. Users should follow these steps to stylize their images:</p>
    <ol style="color: #333;">
        <li>Choose a model from the dropdown menu provided.</li>
        <li>Upload your own image using the file uploader.</li>
        <li>Adjust any additional parameters, such as alpha value for certain models.</li>
        <li>Click the "Stylize Image" button to apply the chosen model's style to the uploaded image.</li>
    </ol>
    <img src="streamlit_app/streamlit_app__demo.gif" alt="Streamlit App Demo" style="border-radius: 5px; margin-top: 20px; width: 100%;">
</div>













