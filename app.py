
import easyocr
import gradio as gr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'hi'])

# Function for OCR and search functionality
def process_image(image, keyword):
    result = reader.readtext(image, detail=0)
    extracted_text = " ".join(result)
    
    # Check if the keyword is in the text
    if keyword.lower() in extracted_text.lower():
        return f"Keyword '{keyword}' found in the text.", extracted_text
    else:
        return f"Keyword '{keyword}' not found.", extracted_text

# Gradio interface
interface = gr.Interface(fn=process_image, 
                         inputs=["image", "text"], 
                         outputs=["text", "text"], 
                         title="OCR and Document Search",
                         description="Upload an image, extract text, and search for keywords")

# Launch the app
if __name__ == "__main__":
    interface.launch()
