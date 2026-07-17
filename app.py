import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Advanced Semantic Intelligence",
    page_icon="🚀",
    layout="wide"
)

# ----------------- SIDEBAR: LICENSING CONTROL -----------------
st.sidebar.markdown("### 🔑 System Licensing Control")

# Custom styled dark card for the Device ID to match your image
st.sidebar.markdown(
    """
    <div style="background-color: #1a2436; padding: 15px; border-radius: 10px; border: 2px dashed #00ffd2; text-align: center; margin-bottom: 20px;">
        <span style="color: #8fa0ba; font-size: 11px; font-weight: bold; letter-spacing: 1px; display: block; margin-bottom: 5px;">YOUR DEVICE ID:</span>
        <span style="color: #00ffd2; font-size: 22px; font-weight: bold; font-family: monospace;">91C74EDC</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Key Input Field
license_key = st.sidebar.text_input(
    "Enter Premium Activation Key:",
    type="password",
    placeholder="Paste your un-shareable license key"
)

st.sidebar.markdown("---")

# Added Links (Using your GitHub handle 'mariog9003' as default)
st.sidebar.markdown("#### 🛠️ Links & Support")
st.sidebar.markdown("[🔑 Get a Premium Activation Key Here](https://buymeacoffee.com/hazelnut77)")
st.sidebar.markdown("[☕ Buy Me a Coffee / Support Page](https://buymeacoffee.com/hazelnut77)")


# ----------------- MAIN PAGE CONTENT -----------------
st.markdown("# 🚀")
st.markdown(
    "<p style='color: #8fa0ba; font-size: 16px;'>Advanced semantic intelligence arrays converting source documents into high-retention social assets.</p>", 
    unsafe_allow_html=True
)

# Preset Target Dropdown
preset = st.selectbox(
    "⚡ Select Tactical Processing Preset Target:",
    ["✨ Core Executive Bullet Highlights", "📝 Summary Generation", "📊 Sentiment Analysis Extraction"]
)

# Default text placeholder matching your image
default_text = (
    "Im reaching out to invite you to a 20 minute demo of an an all in one mobile app that can "
    "help to your business grow and save time. quick question, Which one of those would be "
    "more beneficial to you? .what's more of a headache for you right now: not enough help, "
    "not having enough work or lack of time in your day? I'm with Housecall Pro. Part of what "
    "we do is turn your paperwork, missed calls, and scheduling headaches into automated operations . "
    "Quick question? Do you have 20 minutes to take a look right now? It's a free presentation through zoom."
)

# Main Text Entry Box
source_text = st.text_area(
    "Source Vector Text Entry Box:",
    value=default_text,
    height=200
)

# Dynamic Word and Character Metrics Calculation
word_count = len(source_text.split()) if source_text else 0
char_count = len(source_text) if source_text else 0

st.markdown("<br>", unsafe_allow_html=True)

# Metrics Grid Footer
col1, col2, _ = st.columns([1.5, 1.5, 5])

with col1:
    st.markdown(
        f"""
        <div style="background-color: #1a2436; padding: 8px 12px; border-radius: 5px; text-align: center; border-left: 5px solid #00ffd2;">
            <span style="color: #ffffff; font-size: 14px; font-weight: 500;">📊 Source Word Vector: {word_count}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="background-color: #1a2436; padding: 8px 12px; border-radius: 5px; text-align: center; border-left: 5px solid #00ffd2;">
            <span style="color: #ffffff; font-size: 14px; font-weight: 500;">💻 Character Array: {char_count}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
