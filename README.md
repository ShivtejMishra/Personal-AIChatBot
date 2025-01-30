
# **Ollama AI Chatbot Application**

This is a simple **Streamlit** app that uses the **Ollama** model to create a local AI chatbot. You can select from multiple models installed on your system, and the chatbot will respond with a typing animation effect.

## **Prerequisites**

To run this application, you need the following:

1. **Ollama** installed on your system.
2. Python 3.7 or higher installed.
3. The `streamlit`, `ollama`, and `time` Python packages installed.

## **Installation Steps**

### **1. Download and Install Ollama**

1. **Download Ollama:**
   - Visit [Ollama Official Website](https://ollama.com/) and download the appropriate version for your operating system (Windows/macOS/Linux).
   
2. **Install Ollama:**
   - Follow the installation instructions on the website or use your package manager to install it. For example, on macOS:

     ```bash
     brew install ollama
     ```

3. **Verify Installation:**
   - After installation, verify that Ollama is installed by running the following command in your terminal:

     ```bash
     ollama --version
     ```

   - This should return the installed version of Ollama.

### **2. Pull a Model in Ollama**

1. **Pull a Model:**
   - Ollama supports various models. To pull a model (e.g., `mistral`), run:

     ```bash
     ollama pull mistral
     ```

   - This command will download the `mistral` model and make it available for use.

2. **Check Installed Models:**
   - To list all models installed on your system, run:

     ```bash
     ollama list
     ```

   - This will display all available models on your machine.

### **3. Install Required Python Packages**

1. **Create a Virtual Environment (optional but recommended):**

   If you're using a virtual environment, create and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. **Install Dependencies:**
   - Install the required Python packages by running:

     ```bash
     pip install streamlit ollama
     ```

### **4. Run the Application**

1. **Create the Python Script:**
   - Create a Python script (e.g., `app.py`) and paste the provided Streamlit application code.

2. **Run the Streamlit App:**
   - In the terminal, navigate to the directory where your `app.py` is located and run the following command:

     ```bash
     streamlit run app.py
     ```

3. **Open the Application:**
   - The app will open in your default web browser. If it doesn’t open automatically, visit [http://localhost:8501](http://localhost:8501).

### **5. Using the Application**

- On the left sidebar, you will see a dropdown menu where you can select the AI model you want to use.
- Type a message in the input box and hit "Enter" to send it.
- The chatbot will respond with a smooth typing animation effect.

---

