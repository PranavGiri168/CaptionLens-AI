#install stransformers library
import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration,BlipProcessor

# Initialize the processor and model from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_img(input_img:np.ndarray):
    raw_img=Image.fromarray(input_img).convert('RGB')
    
    inputs=processor(raw_img,return_tensors='pt')
    out=model.generate(**inputs,max_length=50)
    caption=processor.decode(out[0],skip_special_tokens=True)

    return caption


iface = gr.Interface(
    fn=caption_img, 
    inputs=gr.Image(), 
    outputs="text",
    title="CaptionLens AI – Image Caption Generator",
    description="This is a simple web app for generating captions for images using a trained model."
)
iface.launch()