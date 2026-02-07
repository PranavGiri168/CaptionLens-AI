



# CaptionLens AI – Image Caption Generator

## 📌 Project Overview

**CaptionLens AI** is a deep-learning powered web application that automatically generates descriptive captions for images using the **BLIP (Bootstrapping Language-Image Pretraining)** model from Hugging Face Transformers.
The application provides an interactive web interface built with **Gradio**, allowing users to upload images and instantly receive AI-generated captions.

---

## 🚀 Features

* Upload an image and generate an automatic caption
* Deep Learning model (BLIP) for high-quality caption generation
* Interactive web interface using Gradio
* Real-time caption generation
* Easy deployment and extension for multilingual captioning or multiple caption outputs

---

## 🧠 Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* BLIP Image Captioning Model
* Gradio
* NumPy
* Pillow (PIL)

-----------

## 📂 Project Structure

```
CaptionLens/
│
├── main.py              # Main application script
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
└── sample_images/       # Example images (optional)
```

---

## ⚙️ Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/PranavGiri168/CaptionLens-AI.git
cd captionlens-ai
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the application

```bash
python main.py
```

The application will start locally at:

```
http://127.0.0.1:7860
```

---

## 🖼 Example Workflow

1. Upload an image through the web interface
2. The BLIP model processes the image
3. AI generates a descriptive caption
4. Caption is displayed instantly

---

## 📊 Model Used

* **Model:** Salesforce BLIP Image Captioning Base
* **Source:** Hugging Face Transformers
* **Architecture:** Vision Encoder + Text Decoder Transformer

---

## 🔮 Future Improvements

* Multiple caption generation (Top-K captions)
* Caption confidence score
* Multilingual caption translation
* Caption download option
* Deployment on Hugging Face Spaces / Docker
* Image tagging using CLIP

---

## 👨‍💻 Author

**Pranav Giri**

---

## ⭐ Contributing

Contributions are welcome!
Feel free to fork the repository and submit pull requests for improvements.

---

## 📜 License

This project is open-source and available under the MIT License.

---


