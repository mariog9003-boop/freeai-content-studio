import streamlit as st

st.set_page_config(
    page_title="FreeAI Content Studio Pro", 
    page_icon="🚀", 
    layout="centered"
)

# 🎨 PREMIUM CYBERPUNK DARK NEON INTERFACE DESIGN
st.markdown("""<style>
    .main {background-color: #0d0e12;} 
    /* Input Area Styling */
    textarea {background-color: #161920 !important; color: #ffffff !important; border: 1px solid #2d3345 !important; border-radius: 10px !important;}
    /* Main Action Button */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #ff4b4b 0%, #ff758c 100%); 
        color: white; border: none; border-radius: 10px; width: 100%; height: 52px; 
        font-weight: bold; font-size: 16px; box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {transform: translateY(-2px); box-shadow: 0px 6px 20px rgba(255, 75, 75, 0.6);}
    /* Monetization Studio Box */
    .monetize-box {
        background: linear-gradient(145deg, #131622, #1a1d30); 
        padding: 30px; border-radius: 16px; border: 2px solid #6366f1; 
        text-align: center; margin-top: 40px; box-shadow: 0px 8px 30px rgba(99, 102, 241, 0.25);
    }
    .premium-badge {background-color: #6366f1; color: white; padding: 5px 14px; border-radius: 20px; font-size: 11px; font-weight: bold; letter-spacing: 1px;}
    /* Status Counters */
    .counter-badge {background-color: #1e2330; padding: 6px 12px; border-radius: 6px; border: 1px solid #2d3345; font-size: 13px; color: #a0aec0;}
</style>""", unsafe_allow_html=True)

# 🚀 PREMIUM LOCAL ALGORITHM ENGINE
def execute_bullet_summarizer(text_input, style_preset):
    sentences = [s.strip() for s in text_input.replace('\n', ' ').split('.') if len(s.strip()) > 8]
    if len(sentences) == 0:
        return "⚡ System Notice: Please paste a longer text paragraph to extract viral core insights."
    
    key_points = sentences[:3] if len(sentences) >= 3 else sentences
    
    if style_preset == "Short Viral Hook":
        formatted_summary = "### ⚡ Viral Hook Variations:\n\n"
        formatted_summary += f"🔥 *Option 1: Did you know that {key_points[0]}? Here is the truth...*\n\n"
        if len(key_points) > 1:
            formatted_summary += f"👀 *Option 2: Stop scrolling if you want to understand how {key_points[1]}...*\n"
        else:
            formatted_summary += f"👀 *Option 2: Stop scrolling if you want to see the complete breakdown...*\n"
    elif style_preset == "Bullet Highlights":
        formatted_summary = "### ✨ Executive Key Highlights:\n\n"
        for idx, point in enumerate(key_points, 1):
            formatted_summary += f"*{idx}️⃣ {point}.*\n"
    else:  # LinkedIn/X Post
        formatted_summary = "### 📝 Ready-to-Post Social Script:\n\n"
        formatted_summary += f"🧠 **The Core Breakdown:**\n\n{key_points[0]}.\n\n"
        if len(key_points) > 1:
            formatted_summary += f"💡 **Why this matters:** {key_points[1]}.\n\n"
        formatted_summary += "👇 What are your thoughts on this? Let me know below! #Insight #Growth"
        
    return formatted_summary

st.title("🚀 FreeAI Content Studio Pro")
st.subheader("Transform boring text, blogs, or scripts into highly engaging social media formats instantly.")

st.markdown("<p style='font-size: 14px; color: #718096; margin-bottom: 5px;'>⚡ 1-Click Transformation Style Preset:</p>", unsafe_allow_html=True)
selected_preset = st.radio(
    label="Choose Output Style Preset",
    options=["Bullet Highlights", "Short Viral Hook", "LinkedIn / X Social Post"],
    horizontal=True,
    label_visibility="collapsed"
)

user_text = st.text_area("Paste your source text here:", height=220, placeholder="Enter text paragraphs, YouTube transcripts, or articles here...")

if user_text:
    words = len(user_text.split())
    chars = len(user_text)
    st.markdown(f"<span class='counter-badge'>📊 Words: <b>{words}</b></span> &nbsp; <span class='counter-badge'>🔤 Characters: <b>{chars}</b></span>", unsafe_allow_html=True)

if st.button("⚡ Transform Content Instantly"):
    if user_text.strip() == "":
        st.warning("Please enter text first!")
    else:
        with st.spinner("Processing semantic data matrices..."):
            ai_output = execute_bullet_summarizer(user_text, selected_preset)
            st.success("✨ Formatting Matrix Complete!")
            st.info(ai_output)

# THE FINAL MONETIZED UPGRADE HUB (Pre-linked to your personal channel link)
st.markdown("---")
st.markdown("""
<div class="monetize-box">
    <span class="premium-badge">PRO MEMBERSHIP</span>
    <h3 style="margin-top:12px; color:white; font-size:24px;">🚀 Unlock FreeAI Studio Premium</h3>
    <p style="color:#a0aec0; font-size:14px; max-width: 500px; margin: 0 auto 15px auto;">Tired of basic generation limits? Get lifetime unlimited high-speed access, long-form book processing, and unlock 15+ specialized creator styles.</p>
    <p style="font-size:20px; font-weight:bold; color:#34d399; margin-bottom:20px;">One-Time Payment • Lifetime Value</p>
<a href="https://www.buymeacoffee.com/hazelnut77" target="_blank">
        <button style="background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%); color:white; border:none; padding:14px 40px; border-radius:10px; font-size:16px; font-weight:bold; cursor:pointer; width:100%; box-shadow: 0px 4px 15px rgba(99, 102, 241, 0.4);">
            💳 Secure Lifetime Access
        </button>
    </a>
</div>
""", unsafe_allow_html=True)
