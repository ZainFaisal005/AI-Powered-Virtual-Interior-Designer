# 🎨✨ AI-Powered Virtual Interior Designer  
Transform your creative vision into reality using the **AI-Powered Virtual Interior Designer**! This project leverages **transformers** and **deep learning** models to generate stunning room designs based on user input.  

---

## 🚀 **Project Overview**  
This project is a web application designed to create beautiful, AI-generated interior designs. It uses a **transformer-based model** for image generation, providing users the ability to customize:  
- 🏠 **Room Type**: Living Room, Bedroom, Kitchen, etc.  
- 🎨 **Style**: Modern, Vintage, Minimalist, etc.  
- 🌈 **Color**: Blue, Black, Red, and combinations (e.g., "Blue and Black")  
- 📏 **Dimensions**: Specify image resolution (e.g., 512x512)  

---

## 🌟 **Features**  
- ✅ **Dynamic Image Generation** using Hugging Face Transformers  
- ✅ **User-Friendly Interface** with Real-Time Feedback  
- ✅ **Downloadable Designs** in High Quality  
- ✅ **Responsive and Aesthetically Pleasing UI**  
- ✅ **Error Handling and Validation**  

---

## 🛠️ **Project Structure**  
```
├── AI-Powered-Virtual-Interior-Designer
│   ├── app.py                # Flask web application
│   ├── generator.py          # AI Image generation script
│   ├── requirements.txt      # Project dependencies
│   ├── Dockerfile            # Docker configuration for Hugging Face deployment
│   ├── static
│   │   ├── style.css         # Styling for frontend
|   |   ├── script.js         # applying functanalities
│   ├── templates
│   │   ├── index.html        # Main frontend page
└── README.md                 # Project documentation
```

## ⚙️ **Installation Guide**  

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/AI-Powered-Virtual-Interior-Designer.git
cd AI-Powered-Virtual-Interior-Designer
```

---

### ✅ 2. Setup Virtual Environment
It’s recommended to use a virtual environment to avoid package conflicts.  
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

---

### ✅ 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

### ✅ 4. Run the Application
```bash
python app.py
```
Access the app at **`http://127.0.0.1:7860`** in your web browser.  

---


# Install dependencies
RUN `pip install --no-cache-dir -r requirements.txt`


## 🖥️ **How to Use**  

1. Open the web app.  
2. Enter the following inputs:  
   - **Room Type:** Living Room  
   - **Style:** Modern  
   - **Color:** Blue and White  
   - **Dimensions:** 512x512  
3. Click **Generate Design**.  
4. 🎨 **Wait for the AI magic to happen!**  
5. View the generated design on the same page.  
6. Click **⬇️ Download Image** to save your design.  

---

## 🐞 **Common Issues & Solutions**  

1. **Loading Forever Issue**  
   - Ensure all dependencies are correctly installed.  
   - Check internet connectivity for model downloads.  
   - Verify the correct Hugging Face model is used.  

2. **Environment Issues**  
   - Recreate the virtual environment and install packages again.  
   - Ensure Docker is installed correctly.  

3. **Incorrect Image Generation**  
   - Verify inputs, especially dimensions and style.  
   - Use predefined color names or valid combinations.  

---

## 💡 **Future Enhancements**  
- 🪄 Add more customization options (furniture, lighting, etc.).  
- 🏡 Multi-room designs and layouts.  
- 💬 Real-time chat assistant for design advice.  
- 🖌️ Style transfer and texture options.  
- 🟢 Interactive 3D Visualization.  

---

## 🤝 **Contributing**  
Contributions are welcome! Please fork the repo, create a new branch, and make a pull request.  

---

## 💬 **Support & Feedback**  
If you encounter any issues or have suggestions, feel free to:  
- Open an issue in the repository  
- Reach out via email: [your-email@example.com](zainfaisal280@gmail.com)  

---

## 🏷️ **License**  
This project is licensed under the **MIT License**.  

---

## 🎉 **Thank You for Using AI-Powered Virtual Interior Designer!**  
Unleash your creativity and redefine your space with AI! 🌟
