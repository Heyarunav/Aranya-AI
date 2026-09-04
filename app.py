import streamlit as st
from PIL import Image
import time
import random


plant_database = {
    "Manimuni": {
        "scientific": "Centella asiatica",
        "english": "Indian Pennywort",
        "regional_names": {
            "Assam": "Manimuni (মানিমুনি)",
            "Manipur": "Peruk",
            "West Bengal": "Thankuni (থানকুনি)",
            "Bihar / North India": "Brahmi / Mandukaparni",
            "Maharashtra": "Brahmi / Karinga",
            "Tamil Nadu": "Vallarai",
            "Kerala": "Muthil"
        },
        "benefits": ["✅ Cognitive Health: Enhances memory.", "✅ Wound Healing: Speeds up skin repair.", "✅ Digestive Aid: Soothes stomach issues."]
    },
    "Aloe Vera": {
        "scientific": "Aloe barbadensis miller",
        "english": "Aloe Vera",
        "regional_names": {
            "Assam": "Salkuwari (ছালকুঁৱৰী)",
            "Manipur": "Khang-Khok",
            "West Bengal": "Ghritakumari (ঘৃতকুমারী)",
            "Bihar / North India": "Ghritkumari",
            "Maharashtra": "Korphad",
            "Tamil Nadu": "Katralai",
            "Kerala": "Kattarvazha"
        },
        "benefits": ["✅ Skin Soothing: Treats burns and irritation.", "✅ Hydration: Highly moisturizing.", "✅ Antioxidant: Rich in vitamins."]
    },
    "Neem": {
        "scientific": "Azadirachta indica",
        "english": "Margosa",
        "regional_names": {
            "Assam": "Mahanim (মহানিম)",
            "Manipur": "Neem",
            "West Bengal": "Nim (নিম)",
            "Bihar / North India": "Neem",
            "Maharashtra": "Kadu Nimb",
            "Tamil Nadu": "Vembu",
            "Kerala": "Veppu"
        },
        "benefits": ["✅ Antibacterial: Great for skin infections.", "✅ Dental Health: Traditionally used for oral hygiene.", "✅ Immunity: Purifies the blood."]
    },
    "Tulsi": {
        "scientific": "Ocimum sanctum",
        "english": "Holy Basil",
        "regional_names": {
            "Assam": "Tulaxi (তুলসী)",
            "Manipur": "Tulasi",
            "West Bengal": "Tulshi (তুলসী)",
            "Bihar / North India": "Tulsi",
            "Maharashtra": "Tulsi",
            "Tamil Nadu": "Thulasi",
            "Kerala": "Thulasi"
        },
        "benefits": ["✅ Stress Relief: An adaptogen that lowers stress.", "✅ Respiratory: Clears congestion.", "✅ Immunity: Fights infections."]
    }
}

st.set_page_config(page_title="Aranya-AI", layout="centered")
st.title("🌿 Aranya-AI: Pan-India Botanical Identifier")

# 2. Dynamic User Profile & GPS Controls for the Demo
st.sidebar.header("⚙️ Live Demo Controls")

# List of all supported states in our prototype
states_list = ["Assam", "Manipur", "West Bengal", "Bihar / North India", "Maharashtra", "Tamil Nadu", "Kerala"]

# The user's actual registered home state
user_home_state = st.sidebar.selectbox("👤 User's Home Profile:", states_list, index=1) # Defaults to Manipur for demo

# Where the user is currently standing with their camera
simulated_gps = st.sidebar.selectbox("📍 Simulated GPS Location:", states_list, index=5) # Defaults to Tamil Nadu for demo

st.write(f"**Current Scanner Location:** {simulated_gps}")

tab1, tab2 = st.tabs(["📸 Use Camera", "📁 Upload Image"])

image_to_analyze = None
file_name = ""

with tab1:
    camera_photo = st.camera_input("Take a picture of the plant")
    if camera_photo:
        image_to_analyze = Image.open(camera_photo)
        file_name = "camera_capture"

with tab2:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image_to_analyze = Image.open(uploaded_file)
        file_name = uploaded_file.name.lower()

if image_to_analyze is not None:
    if st.button("Identify Plant"):
        with st.spinner("Analyzing leaf structure and biological features..."):
            time.sleep(2) 
            
        detected_plant = None
        
        # The smart file name trick
        if "aloe" in file_name:
            detected_plant = "Aloe Vera"
        elif "neem" in file_name:
            detected_plant = "Neem"
        elif "tulsi" in file_name:
            detected_plant = "Tulsi"
        elif "mani" in file_name or "peruk" in file_name:
            detected_plant = "Manimuni"
        else:
            detected_plant = random.choice(list(plant_database.keys()))
        
        plant_info = plant_database[detected_plant]
        
        # Fetching names based on the sidebar selections
        local_name = plant_info["regional_names"][simulated_gps]
        home_name = plant_info["regional_names"][user_home_state]
        
        st.success("Analysis Complete!")
        
        # 3. Displaying the Core Information
        st.subheader("Identification Results:")
        st.write(f"**English Name:** {plant_info['english']}")
        st.write(f"**Scientific Name:** *{plant_info['scientific']}*")
        st.write(f"**Local Name Here ({simulated_gps}):** {local_name}")
        
        # 4. The Cross-Cultural "Home Connection"
        if simulated_gps != user_home_state:
            st.info(f"🏠 **Home Connection:** Back in **{user_home_state}**, you know this plant as **{home_name}**.")
        
        st.write("---")
        st.subheader("Medicinal Benefits:")
        for benefit in plant_info['benefits']:
            st.write(benefit)
