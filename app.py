import streamlit as st
import hashlib

st.set_page_config(
    page_title="FreeAI Content Studio Pro", 
    page_icon="🚀", 
    layout="centered"
)

# 🔒 HIGH-SECURITY CRYPTO ENGINE (Prevents Sharing)
SECRET_SALT = "4928252a986d373e57a7cbb9403febc3c4d06d207708d6551111540a169712bdbc0c25f030cc58ba"

def generate_hardware_id():
    """Generates a unique, consistent fingerprint for the user's browser device context."""
    user_agent = st.context.headers.get("User-Agent", "DefaultBrowser")
    remote_ip = st.context.headers.get("X-Forwarded-For", "LocalIP")
    raw_id = f"{user_agent}-{remote_ip}"
    return hashlib.md5(raw_id.encode()).hexdigest()[:8].upper()

def verify_license_key(hardware_id, inputted_key):
    """Checks if the entered key is mathematically tied to this specific machine ID."""
    if not inputted_key:
        return False
    correct_hash = hashlib.sha256(f"{hardware_id}-{SECRET_SALT}".encode()).hexdigest()[:12].upper()
    return inputted_key.strip().upper() == correct_hash

# Fetch this visitor's un-shareable Device Fingerprint
visitor_device_id = generate_hardware_id()

# 🎨 PREMIUM CYBERPUNK DARK NEON STYLING
st.markdown("""<style>
    .main {background-color: #0b0c10;} 
    /* Soft glowing input fields */
    textarea {background-color: #1f2833 !important; color: #ffffff !important; border: 1px solid #45f3ff !important; border-radius: 12px !important; font-size: 15px !important;}
    
    /* Hot Neon Action Button */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); 
        color: #0b0c10; border: none; border-radius: 12px; width: 100%; height: 55px; 
        font-weight: bold; font-size: 18px; box-shadow: 0px 4px 20px rgba(0, 242, 254, 0.4);
        transition: all 0.3s ease; letter-spacing: 0.5px;
    }
    div.stButton > button:first-child:hover {transform: translateY(-2px); box-shadow: 0px 6px 25px rgba(0, 242, 254, 0.7); color: #0b0c10;}
    
    /* High-Tier Monetization Box */
    .monetize-box {
        background: linear-gradient(145deg, #1f2833, #0b0c10); 
        padding: 35px; border-radius: 20px; border: 2px solid #00f2fe; 
        text-align: center; margin-top: 40px; box-shadow: 0px 10px 35px rgba(0, 242, 254, 0.15);
    }
    .premium-badge {background-color: #00f2fe; color: #0b0c10; padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: bold; letter-spacing: 1px;}
    .counter-badge {background-color: #1f2833; padding: 6px 14px; border-radius: 8px; border: 1px solid #45f3ff; font-size: 13px; color: #c5c6c7;}
    .license-banner {background-color: #1f2833; padding: 15px; border-radius: 10px; border: 1px dashed #00f2fe; margin-bottom: 20px;}
    
    /* Output Showcase Styling */
    .output-box {background-color: #1f2833; border-left: 5px solid #00f2fe; padding: 20px; border-radius: 8px; color: white;}
</style>""", unsafe_allow_html=True)

# 🔑 SIDEBAR ACTIVATION PANEL
with st.sidebar:
    st.markdown("### 🔑 System Licensing")
    st.markdown(f"""
    <div class='license-banner'>
        <span style='color: #c5c6c7; font-size: 11px;'>YOUR DEVICE ID:</span><br>
        <b style='color: #00f2fe; font-size: 19px; font-family: monospace;'>{visitor_device_id}</b>
    </div>
    """, unsafe_allow_html=True)
    
    user_license = st.text_input("Enter Premium Activation Key:", type="password", placeholder="Paste your un-shareable license key...")
    is_premium = verify_license_key(visitor_device_id, user_license)
    
    if is_premium:
        st.success("👑 Pro Unlocked: Full Engine Active!")
    elif user_license:
        st.error("🔴 Verification Failure: Token Mismatch.")

# 🚀 MAIN APPLICATION LAYOUT
st.markdown("<h1 style='color: white; font-size: 38px;'>🚀 FreeAI Content Studio Pro</h1>", unsafe_allow_html=True)

# Define Advanced Style Presets dynamically based on Premium Status
if is_premium:
    st.markdown("<h3><span style='color:#00f2fe;'>👑 Pro Workspace</span> Enabled: 9 Core Architectures Available</h3>", unsafe_allow_html=True)
    available_styles = [
        "🔥 TikTok Viral Reel", "📸 IG Reel Hook Matrix", "🎥 YouTube Short Retainer",
        "💼 LinkedIn Thought Leader", "🧵 X (Twitter) Deep Thread", "📧 Premium Newsletter Block",
        "✨ Core Bullet Highlights", "🧠 Hook Variation Engine", "💰 High-Converting Sales Copy"
    ]
else:
    st.markdown("<h3 style='color: #c5c6c7; font-size: 18px;'>Transform dry text, scripts, or links into high-retention formats instantly.</h3>", unsafe_allow_html=True)
    available_styles = ["✨ Core Bullet Highlights", "🧠 Hook Variation Engine", "💼 LinkedIn Thought Leader"]

st.markdown("<br><p style='font-size: 14px; color: #66fcf1; font-weight: bold;'>⚡ 1-Click Transformation Engine Preset:</p>", unsafe_allow_html=True)
selected_preset = st.selectbox("Preset Style Selector", options=available_styles, label_visibility="collapsed")

# Enforce word limits on free tier
if is_premium:
    placeholder_msg = "Pro Tier Unrestricted: Paste massive script files, complete podcast transcripts, or full ebook chapters..."
    max_chars = None
else:
    placeholder_msg = "Free Tier Restrained: Paste text up to 300 words. Upgrade to Pro below to process unlimited characters and long-form files..."
    max_chars = 1500

user_text = st.text_area("Paste your source text here:", height=240, placeholder=placeholder_msg, max_chars=max_chars)

if user_text:
    words = len(user_text.split())
    chars = len(user_text)
    st.markdown(f"<span class='counter-badge'>📊 Word Vector: <b>{words}</b></span> &nbsp; <span class='counter-badge'>🔤 Character Vector: <b>{chars}</b></span>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# 🧠 INTERACTIVE GENERATION REFACTOR ENGINE
def execute_bullet_summarizer(text_input, style_preset):
    sentences = [s.strip() for s in text_input.replace('\n', ' ').split('.') if len(s.strip()) > 8]
    if len(sentences) == 0:
        return "⚡ System Notice: Please enter a longer source text vector to process semantic insights."
    
    lead_point = sentences[0] if len(sentences) > 0 else "your content"
    sub_point = sentences[1] if len(sentences) > 1 else lead_point
    
    if "TikTok" in style_preset or "Short" in style_preset or "IG" in style_preset:
        return f"🎬 **FACELESS SHORT-FORM VIDEO SCRIPT**\n\n**Visual:** [Fast panning screen cut showing high-contrast neon text]\n\n**Hook (First 2 Seconds):** \"Stop scrolling if you want to understand how {lead_point.lower()}! Here is the brutal truth standard workflows hide from you...\"\n\n**Body Frame:** \"Most people fail because they ignore this. The matrix reveals that {sub_point.lower()}. This single shift changes everything.\"\n\n**Call to Action:** \"Drop a follow to lock in your daily data leverage loop. Don't fall behind.\""
    elif "LinkedIn" in style_preset or "Thread" in style_preset:
        return f"💼 **HIGH-RETENTION PROFESSIONAL WRITING**\n\nI used to think traditional processes worked. I was entirely wrong.\n\nHere is the real breakdown behind how {lead_point.lower()}:\n\n• **The Structural Catalyst:** {sub_point}.\n• **Why This Matters:** It creates an immediate processing advantage for creators.\n\nTraditional operators will fall behind in 2026. The future belongs entirely to automated iteration.\n\nAgree? Let me know your thoughts in the comment loop matrix below. #Growth #Scale"
    elif "Sales" in style_preset:
        return f"💰 **HIGH-CONVERTING PERSUASIVE SALES COPY**\n\nAre you still losing attention because of outdated presentation frameworks?\n\nIt is costing you money every single hour. Here is your unfair competitive advantage: **{lead_point}**.\n\nThis isn't an iterative choice—it is a mandatory survival tool. Because our system tracks that {sub_point.lower()}.\n\n👇 Click the secure checkout gateway link right now to bypass the free limits forever."
    else:
        return f"✨ **EXECUTIVE CORE INSIGHT MATRICES**\n\n• 🧬 **Primary Data Hook Vector:** {lead_point}.\n• ⚡ **Secondary Dynamic Operational Node:** {sub_point}."

if st.button("⚡ TRANSFORM CONTENT INSTANTLY"):
    if user_text.strip() == "":
        st.warning("Please enter your text first!")
    else:
        with st.spinner("Compiling tactical semantic data matrices..."):
            ai_output = execute_bullet_summarizer(user_text, selected_preset)
            st.success("✨ Optimization Complete!")
            
            # Displays output inside a gorgeously styled box
            st.markdown(f"<div class='output-box'>{ai_output.replace('\n', '<br>')}</div>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# 💳 HIGH-TIER MONETIZATION INTERFACE (Only visible if they haven't upgraded yet)
if not is_premium:
    st.markdown("---")
    st.markdown("""
    <div class="monetize-box">
        <span class="premium-badge">PRO MEMBERSHIP ACCESS</span>
        <h3 style="margin-top:14px; color:white; font-size:26px;">🚀 Scale Up to FreeAI Studio Premium</h3>
        <p style="color:#c5c6c7; font-size:14.5px; max-width: 520px; margin: 0 auto 15px auto;">Stop hitting basic processing limits. Secure lifetime unlimited character clearance, long-form transcript scraping, and unlock 9+ high-retention creator writing presets instantly.</p>
        <p style="font-size:22px; font-weight:bold; color:#00f2fe; margin-bottom:22px;">One-Time Payment • Lifetime Value</p>
        <a href="https://buymeacoffee.com" target="_blank">
            <button style="background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); color:#0b0c10; border:none; padding:15px 45px; border-radius:12px; font-size:16.5px; font-weight:bold; cursor:pointer; width:100%; box-shadow: 0px 4px 18px rgba(0, 242, 254, 0.4);">
                💳 Secure Lifetime Access Upgrade
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
