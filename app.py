import streamlit as st

def suggest_seal(seal_type, temperature, pressure, media, speed, application):
    materials = {
        "o-ring": {
            "very_low": {
                "main": "Silicone (VMQ)",
                "description": "Excellent flexibility at low temperatures, used for static applications.",
                "reason": "Chosen for its superior flexibility and temperature resistance.",
                "alternative": "Neoprene",
                "purchase": "Available from suppliers like McMaster-Carr or Grainger."
            },
            "low": {
                "main": "Nitrile (NBR)",
                "description": "Good resistance to oils and moderate temperatures.",
                "reason": "Optimal for oil-based environments.",
                "alternative": "EPDM",
                "purchase": "Available at industrial supply stores."
            },
            "medium": {
                "main": "EPDM",
                "description": "Great for hot water and steam environments.",
                "reason": "Excellent heat resistance.",
                "alternative": "Viton (FKM)",
                "purchase": "Available on Amazon."
            },
            "high": {
                "main": "Viton (FKM)",
                "description": "Resistant to high temperatures and aggressive chemicals.",
                "reason": "Best for chemical environments.",
                "alternative": "Perfluoroelastomer (FFKM)",
                "purchase": "Available from Parker or SKF."
            },
            "extreme": {
                "main": "Perfluoroelastomer (FFKM)",
                "description": "Handles extreme conditions with aggressive media.",
                "reason": "Ultimate chemical and thermal resistance.",
                "alternative": "Viton (FKM)",
                "purchase": "Available from DuPont or specialty distributors."
            }
        },
        "gasket": {
            "very_low": {
                "main": "Nitrile (NBR)",
                "description": "Suitable for low pressures, offers good oil resistance.",
                "reason": "Cost-effective and oil resistant.",
                "alternative": "EPDM",
                "purchase": "Available from gasket suppliers."
            },
            "low": {
                "main": "Neoprene",
                "description": "Good for moderate pressure and weather resistance.",
                "reason": "Weather and ozone resistance.",
                "alternative": "SBR (Styrene Butadiene Rubber)",
                "purchase": "Available at industrial suppliers."
            },
            "medium": {
                "main": "EPDM",
                "description": "Great for hot water and steam.",
                "reason": "Ideal for steam applications.",
                "alternative": "Viton (FKM)",
                "purchase": "Available from gasket suppliers."
            },
            "high": {
                "main": "Viton (FKM)",
                "description": "Handles high temperatures and aggressive chemicals.",
                "reason": "Perfect for challenging conditions.",
                "alternative": "Silicone",
                "purchase": "Available from high-performance suppliers."
            },
            "extreme": {
                "main": "PTFE (Teflon®)",
                "description": "Best for extreme chemical environments.",
                "reason": "Unmatched chemical resistance.",
                "alternative": "Metal gaskets",
                "purchase": "Available at specialty suppliers."
            }
        }
    }

    pressure_category = categorize_pressure(pressure)
    material_info = materials.get(seal_type, {}).get(pressure_category, None)

    if material_info:
        return pressure_category, f"""
        **Material:** {material_info['main']}  
        **Description:** {material_info['description']}  
        **Reason:** {material_info['reason']}  
        **Alternative:** {material_info['alternative']}  
        **Purchase:** {material_info['purchase']}
        """
    else:
        return pressure_category, "Material information not available."

def categorize_pressure(pressure):
    if pressure < 100000:
        return "very_low"
    elif pressure < 500000:
        return "low"
    elif pressure < 1500000:
        return "medium"
    elif pressure < 5000000:
        return "high"
    else:
        return "extreme"

# Streamlit UI
st.title("🧠 Pocket Seal Guru")
st.markdown("This app helps you select the right seal material based on your engineering parameters.")
st.markdown("📧 For personalized help, contact: **pocket.seal.guru@gmail.com**")

seal_type = st.selectbox("Select Seal Type", ["o-ring", "gasket"])
temperature = st.number_input("Operating Temperature (°C)", min_value=0.0)
pressure = st.number_input("Pressure (Pa)", min_value=0.0)
media = st.selectbox("Select Media", ["Water", "Oil", "Steam", "Acid", "Gas", "N/A"])
speed = st.number_input("Speed (m/s)", min_value=0.0)

if seal_type == "o-ring":
    application = st.selectbox("Application Type", ["axial", "radial", "dovetail", "reciprocating", "rotary", "oscillating", "N/A"])
else:
    application = st.selectbox("Application Type", ["flat face", "raised face", "tongue and groove", "N/A"])

if st.button("Suggest Seal Material"):
    rating, result = suggest_seal(seal_type, temperature, pressure, media, speed, application)
    st.subheader(f"🔍 Application Rating: {rating.upper()}")
    st.markdown(result)
    st.info("📘 Tip: Always verify chemical compatibility for your specific application.")
