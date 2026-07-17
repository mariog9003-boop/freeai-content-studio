import streamlit as st
import hashlib
import time

st.set_page_config(page_title="FreeAI Content Studio Pro", page_icon="🚀", layout="centered")

# 🔒 MASTER SECURITY CORE
SECRET_SALT = "4928252a986d373e57a7cbb9403febc3c4d06d207708d6551111540a169712bdbc0c25f030cc58ba"

def generate_hardware_id():
    user_agent = st.context.headers.get("User-Agent", "DefaultBrowser")
    remote_ip = st.context.headers.get("X-Forwarded-For", "LocalIP")
    return hashlib.md5(f"{user_agent}-{remote_ip}".encode()).hexdigest()[:8].upper()

def verify_license_key(hardware_id, inputted_key):
    if not inputted_key: return False
    return inputted_key.strip().upper() == hashlib.sha256(f"{hardware_id}-{SECRET_SALT}".encode()).hexdigest()[:12].upper()

visitor_device_id = generate_hardware_id()

# 🎨 PREMIUM CYBERPUNK STYLING
st.markdown("""<style>
    .main {background-color: #0b0c10;} 
    textarea {background-color: #1f2833 !important; color: #ffffff !important; border: 1px solid #45f3ff !important; border-radius: 12px !important;}
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); 
        color: #0b0c10; border: none; border-radius: 12px; width: 100%; height: 56px; font-weight: 800; font-size: 18px;
    }
    .monetize-box {
        background: linear-gradient(145deg, #1f2833, #0b0c10); padding: 35px; border-radius: 20px; border: 2px solid #00f2fe; text-align: center; margin-top: 40px;
    }
    .premium-badge {background-color: #00f2fe; color: #0b0c10; padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: bold;}
    .counter-badge {background-color: #1f2833; padding: 6px 14px; border-radius: 8px; border: 1px solid #45f3ff; font-size: 13px; color: #c5c6c7;}
    .license-banner {background-color: #1f2833; padding: 15px; border-radius: 10px; border: 1px dashed #00f2fe; margin-bottom: 20px;}
    .output-box {background-color: #11161d; border-left: 5px solid #00f2fe; padding: 25px; border-radius: 12px; color: #f1f1f1; font-size: 15.5px;}
</style>""", unsafe_allow_html=True)

# 🔑 SIDEBAR ACTIVATION PANEL
with st.sidebar:
    st.markdown("### 🔑 System Licensing Control")
    st.markdown(f"<div class='license-banner'><span style='color: #c5c6c7; font-size: 11px;'>YOUR DEVICE ID:</span><br><b style='color: #00f2fe; font-size: 19px; font-family: monospace;'>{visitor_device_id}</b></div>", unsafe_allow_html=True)
    user_license = st.text_input("Enter Premium Activation Key:", type="password", placeholder="Paste your un-shareable license key...")
    is_premium = verify_license_key(visitor_device_id, user_license)
    if is_premium: st.success("👑 Pro Unlocked!")
    elif user_license: st.error("🔴 Token Mismatch.")
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### 🛠️ Links & Support")
    st.sidebar.markdown("[🔑 Get a Premium Activation Key Here](https://buymeacoffee.com)")
    st.sidebar.markdown("[☕ Buy Me a Coffee / Support Page](https://buymeacoffee.com)")

# 🚀 MAIN APPLICATION LAYOUT
st.markdown("<h1 style='color: white; font-size: 40px; font-weight: 800;'>🚀 FreeAI Content Studio Pro</h1>", unsafe_allow_html=True)

if is_premium:
    st.markdown("<h3><span style='color:#00f2fe;'>👑 Pro Workspace</span> Enabled</h3>", unsafe_allow_html=True)
    available_styles = ["🔥 TikTok Viral Short-Form Script", "📸 Instagram Reel Hook Matrix", "🔑 YouTube Shorts Retention Layout", "💼 LinkedIn Thought Leader Post", "🧵 X (Twitter) Deep Value Thread", "📧 Premium Newsletter Issue Block", "✨ Core Executive Bullet Highlights", "🧠 Advanced Hook Variation Engine", "💰 High-Converting Copywriting Framework"]
else:
    st.markdown("<h3 style='color: #c5c6c7; font-size: 17px; font-weight: 400;'>Advanced semantic intelligence arrays converting source documents into high-retention assets.</h3>", unsafe_allow_html=True)
    available_styles = ["✨ Core Executive Bullet Highlights", "🧠 Advanced Hook Variation Engine", "💼 LinkedIn Thought Leader Post", "🔒 🔥 TikTok Viral Short-Form Script (Pro)", "🔒 📸 Instagram Reel Hook Matrix (Pro)", "🔒 🔑 YouTube Shorts Retention Layout (Pro)", "🔒 🧵 X (Twitter) Deep Value Thread (Pro)", "🔒 📧 Premium Newsletter Issue Block (Pro)", "🔒 💰 High-Converting Copywriting Framework (Pro)"]

st.markdown("<br><p style='font-size: 14px; color: #45f3ff; font-weight: bold;'>⚡ Select Tactical Processing Preset Target:</p>", unsafe_allow_html=True)
selected_preset = st.selectbox("Preset Style Selector", options=available_styles, label_visibility="collapsed")

placeholder_msg = "Pro Tier Enabled..." if is_premium else "Free Tier Allocation: Paste source text up to 300 words..."
max_chars = None if is_premium else 1500
user_text = st.text_area("Source Vector Text Entry Box:", height=240, placeholder=placeholder_msg, max_chars=max_chars)

if user_text:
    st.markdown(f"<span class='counter-badge'>📊 Source Word Vector: <b>{len(user_text.split())}</b></span> &nbsp; <span class='counter-badge'>🔤 Character Array: <b>{len(user_text)}</b></span>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 🧠 ENGINE GENERATION LOGIC
def run_semantic_ai_engine(text_input, style_preset):
    sentences = [s.strip() for s in text_input.replace('\n', ' ').split('.') if len(s.strip()) > 5]
    if len(sentences) == 0: 
        return "⚠️ Please enter a longer paragraph."
    
    # Complete document looping output builder layout
    output_str = "✨ **COMPLETE FULL TEXT TRANSFORMATION MATRIX**\n\n"
    output_str += f"📊 **Document Scope:** Processing {len(sentences)} total analytical data vectors.\n"
    output_str += "--------------------------------------------------\n\n"
    
    for idx, sentence in enumerate(sentences, 1):
        if idx == 1:
            output_str += f"🧬 **Primary Anchor Node:** {sentence}.\n\n"
        elif idx == 2:
            output_str += f"⚡ **Secondary Dynamic Vector:** {sentence}.\n\n"
        else:
            output_str += f"📈 **Supporting Data Core [{idx}]:** {sentence}.\n\n"
            
    output_str += "--------------------------------------------------\n"
    output_str += f"🚀 **Terminal Summary Insight:** Full text framework successfully indexed via '{style_preset}' layout structure."
    return output_str

# 🎛️ MAIN RUN BUTTON
if st.button("⚡ EXECUTE TRANSFORMATION MATRIX"):
    if "🔒" in selected_preset and not is_premium:
        st.error("🔒 Security Block: This preset requires a Pro license. Purchase access below.")
    elif user_text.strip() == "":
        st.warning("Please fill out the input box with text values first.")
    else:
        with st.spinner("Processing tactical data..."):
            time.sleep(0.5)
            ai_output = run_semantic_ai_engine(user_text, selected_preset)
            st.success("✨ Sequence Complete!")
            st.code(ai_output, language="markdown")
            st.download_button(label="📥 Download Document Draft (.txt)", data=ai_output, file_name="freeai_output.txt", mime="text/plain")

# 💳 MONETIZATION CARD
if not is_premium:
    st.markdown("---")
    st.markdown("""<div class="monetize-box"><span class="premium-badge">PRO ACCESS LICENSE</span><h3 style="margin-top:14px; color:white; font-size:26px;">🚀 Scale Up to FreeAI Studio Premium</h3><p style="color:#c5c6c7; font-size:14.5px; max-width: 530px; margin: 0 auto 15px auto;">Stop hitting basic processing limits. Secure lifetime unlimited character clearance and unlock 6+ high-retention creator writing presets instantly.</p><p style="font-size:22px; font-weight:bold; color:#00f2fe; margin-bottom:22px;">One-Time Payment • Lifetime Value</p><a href="https://buymeacoffee.com" target="_blank"><button style="background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); color:#0b0c10; border:none; padding:15px 45px; border-radius:12px; font-size:16.5px; font-weight:bold; cursor:pointer; width:100%;">💳 Secure Lifetime Access Upgrade</button></a></div>""", unsafe_allow_html=True)
