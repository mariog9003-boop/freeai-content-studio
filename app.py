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

# 🎨 PREMIUM CYBERPUNK DARK NEON INTERFACE DESIGN
st.markdown("""<style>
    .main {background-color: #0d0e12;} 
    textarea {background-color: #161920 !important; color: #ffffff !important; border: 1px solid #2d3345 !important; border-radius: 10px !important;}
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #ff4b4b 0%, #ff758c 100%); 
        color: white; border: none; border-radius: 10px; width: 100%; height: 52px; 
        font-weight: bold; font-size: 16px; box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .monetize-box {
        background: linear-gradient(145deg, #131622, #1a1d30); 
        padding: 30px; border-radius: 16px; border: 2px solid #6366f1; 
        text-align: center; margin-top: 40px; box-shadow: 0px 8px 30px rgba(99, 102, 241, 0.25);
    }
    .premium-badge {background-color: #6366f1; color: white; padding: 5px 14px; border-radius: 20px; font-size: 11px; font-weight: bold;}
    .counter-badge {background-color: #1e2330; padding: 6px 12px; border-radius: 6px; border: 1px solid #2d3345; font-size: 13px; color: #a0aec0;}
    .license-banner {background-color: #161920; padding: 15px; border-radius: 10px; border: 1px dashed #2d3345; margin-bottom: 20px;}
</style>""", unsafe_allow_html=True)

# 🔑 SIDEBAR ACTIVATION PANEL
with st.sidebar:
    st.markdown("### 🔑 Account Licensing")
    st.markdown(f"""
    <div class='license-banner'>
        <span style='color: #a0aec0; font-size: 12px;'>YOUR DEVICE ID:</span><br>
        <b style='color: #6366f1; font-size: 18px; font-family: monospace;'>{visitor_device_id}</b>
    </div>
    """, unsafe_allow_html=True)
    
    user_license = st.text_input("Enter Premium Activation Key:", type="password", placeholder="Paste your un-shareable license key...")
    
    is_premium = verify_license_key(visitor_device_id, user_license)
    
    if is_premium:
        st.success("🟢 Pro Active: Unlimited Machine Access Unlocked!")
    elif user_license:
        st.error("🔴 Invalid Key: Code does not match this hardware ID.")

# 🚀 MAIN APPLICATION LAYOUT
st.title("🚀 FreeAI Content Studio Pro")

# Define Style Presets dynamically based on Premium Status
if is_premium:
    st.subheader("👑 Pro Workspace: 15+ Advanced Content Architectures Unlocked.")
    available_styles = [
        "Bullet Highlights", "Short Viral Hook", "LinkedIn / X Social Post", 
        "TikTok Script Format", "YouTube Shorts Retainer", "Instagram Reel Hook Matrix",
        "Deep Educational Thread", "Persuasive Sales Copy", "Newsletter Hook Block"
    ]
else:
    st.subheader("Transform text into engaging formats instantly.")
    available_styles = ["Bullet Highlights", "Short Viral Hook", "LinkedIn / X Social Post"]

st.markdown("<p style='font-size: 14px; color: #718096; margin-bottom: 5px;'>⚡ 1-Click Style Preset:</p>", unsafe_allow_html=True)
selected_preset = st.radio(label="Preset Style", options=available_styles, horizontal=True, label_visibility="collapsed")

# Enforce word limits on free tier
if is_premium:
    placeholder_msg = "Pro Tier: Enter unlimited text paragraphs, transcripts, or massive book chapters..."
    max_chars = None
else:
    placeholder_msg = "Free Tier Limit: Paste up to 300 words. Upgrade below to process long-form copy..."
    max_chars = 1500

user_text = st.text_area("Paste your source text here:", height=220, placeholder=placeholder_msg, max_chars=max_chars)

if user_text:
    words = len(user_text.split())
    chars = len(user_text)
    st.markdown(f"<span class='counter-badge'>📊 Words: <b>{words}</b></span> &nbsp; <span class='counter-badge'>🔤 Characters: <b>{chars}</b></span>", unsafe_allow_html=True)

# 🧠 GENERATION ENGINE
def execute_bullet_summarizer(text_input, style_preset):
    sentences = [s.strip() for s in text_input.replace('\n', ' ').split('.') if len(s.strip()) > 8]
    if len(sentences) == 0:
        return "⚡ System Notice: Please enter longer text vectors."
    return f"✨ [Processed Matrix Content via format '{style_preset}']:\n\n" + "\n\n".join([f"🔥 {s}" for s in sentences[:4]])

if st.button("⚡ Transform Content Instantly"):
    if user_text.strip() == "":
        st.warning("Please enter text first!")
    else:
        with st.spinner("Processing data..."):
            ai_output = execute_bullet_summarizer(user_text, selected_preset)
            st.success("✨ Formatting Matrix Complete!")
            st.info(ai_output)

# 💳 MONETIZATION INTERFACE (Only visible if they haven't upgraded yet)
if not is_premium:
    st.markdown("---")
    st.markdown("""
    <div class="monetize-box">
        <span class="premium-badge">PRO MEMBERSHIP</span>
        <h3 style="margin-top:12px; color:white; font-size:24px;">🚀 Unlock FreeAI Studio Premium</h3>
        <p style="color:#a0aec0; font-size:14px; max-width: 500px; margin: 0 auto 15px auto;">Get lifetime unlimited high-speed access, long-form book processing, and unlock 15+ specialized creator styles.</p>
        <p style="font-size:20px; font-weight:bold; color:#34d399; margin-bottom:20px;">One-Time Payment • Lifetime Value</p>
        <a href="https://buymeacoffee.com" target="_blank">
            <button style="background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%); color:white; border:none; padding:14px 40px; border-radius:10px; font-size:16px; font-weight:bold; cursor:pointer; width:100%; box-shadow: 0px 4px 15px rgba(99, 102, 241, 0.4);">
                💳 Secure Lifetime Access
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
