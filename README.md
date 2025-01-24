# Image Analysis with Ollama and Streamlit

### **Project Setup**

#### **Creating a Virtual Environment**

1. **Create a virtual environment** to isolate the project dependencies:

   On Windows:

   ```bash
   python -m venv venv
   ```

   On macOS/Linux:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:

   On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

### Installation

1. First Install [Ollama Vision](https://ollama.com/blog/llama3.2-vision).

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Streamlit app by running the following command:

   ```bash
   streamlit run main.py
   ```

## How It Works

- **Image Upload**: The user uploads an image through a file uploader.
- **Image Preprocessing**: The image is converted into a base64-encoded string to send to the **Ollama API** for analysis.
- **AI Analysis**: The **Llama 3.2 Vision Model** from **Ollama** generates a detailed description of the image, evaluates by the given prompt.
- **Displaying Results**: The analysis results are displayed in an expandable section for easy viewing.
