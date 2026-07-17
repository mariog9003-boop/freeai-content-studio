import streamlit as st
import hashlib
import time

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

# 🎨 ADVANCED CYBERPUNK DARK NEON INDUSTRIAL CSS DESIGN
st.markdown("""<style>
    .main {background-color: #0b0c10;} 
    /* Deep workspace viewport panels */
    textarea {background-color: #1f2833 !important; color: #ffffff !important; border: 1px solid #45f3ff !important; border-radius: 12px !important; font-size: 15px !important;}
    
    /* Glowing Neon Primary Execution Array */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); 
        color: #0b0c10; border: none; border-radius: 12px; width: 100%; height: 56px; 
        font-weight: 800; font-size: 18px; box-shadow: 0px 5px 25px rgba(0, 242, 254, 0.4);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); letter-spacing: 0.5px;
    }
    div.stButton > button:first-child:hover {transform: translateY(-2px); box-shadow: 0px 8px 30px rgba(0, 242, 254, 0.7); color: #0b0c10;}
    
    /* High-Tier Monetization Box */
    .monetize-box {
        background: linear-gradient(145deg, #1f2833, #0b0c10); 
        padding: 40px; border-radius: 20px; border: 2px solid #00f2fe; 
        text-align: center; margin-top: 45px; box-shadow: 0px 12px 40px rgba(0, 242, 254, 0.2);
    }
    .premium-badge {background-color: #00f2fe; color: #0b0c10; padding: 6px 18px; border-radius: 20px; font-size: 11px; font-weight: bold; letter-spacing: 1px;}
    .counter-badge {background-color: #1f2833; padding: 6px 14px; border-radius: 8px; border: 1px solid #45f3ff; font-size: 13px; color: #c5c6c7;}
    .license-banner {background-color: #1f2833; padding: 15px; border-radius: 10px; border: 1px dashed #00f2fe; margin-bottom: 20px;}
    
    /* Premium Semantic Content Box */
    .output-box {background-color: #11161d; border-left: 5px solid #00f2fe; padding: 25px; border-radius: 12px; color: #f1f1f1; font-size: 15.5px; line-height: 1.6;}
    .feature-tag {background-color: #1f2833; color: #00f2fe; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold; border: 1px solid rgba(0,242,254,0.3);}
</style>""", unsafe_allow_html=True)

# 🔑 SIDEBAR ACTIVATION PANEL
with st.sidebar:
    st.markdown("### 🔑 System Licensing Control")
    st.markdown(f"""
    <div class='license-banner'>
        <span style='color: #c5c6c7; font-size: 11px;'>YOUR DEVICE ID:</span><br>
        <b style='color: #00f2fe; font-size: 19px; font-family: monospace;'>{visitor_device_id}</b>
    </div>
    """, unsafe_allow_html=True)
    
    user_license = st.text_input("Enter Premium Activation Key:", type="password", placeholder="Paste your un-shareable license key...")
    is_premium = verify_license_key(visitor_device_id, user_license)
    
    if is_premium:
        st.success("👑 Pro Unlocked: Enterprise Engine Active!")
    elif user_license:
        st.error("🔴 Verification Failure: Token Mismatch.")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### 🛠️ Links & Support")
    st.sidebar.markdown("[🔑 Get a Premium Activation Key Here](https://buymeacoffee.com)")
    st.sidebar.markdown("[☕ Buy Me a Coffee / Support Page](https://buymeacoffee.com)")

# 🚀 MAIN APPLICATION LAYOUT
st.markdown("<h1 style='color: white; font-size: 40px; font-weight: 800; margin-bottom: 0px;'>🚀 FreeAI Content Studio Pro</h1>", unsafe_allow_html=True)

# Define Advanced Style Presets dynamically based on Premium Status
if is_premium:
    st.markdown("<h3><span style='color:#00f2fe;'>👑 Pro Workspace</span> Enabled • Unlimited Compute</h3>", unsafe_allow_html=True)
    available_styles = [
        "🔥 TikTok Viral Short-Form Script", "📸 Instagram Reel Hook Matrix", "🔑 YouTube Shorts Retention Layout",
        "💼 LinkedIn Thought Leader Post", "🧵 X (Twitter) Deep Value Thread", "📧 Premium Newsletter Issue Block",
        "✨ Core Executive Bullet Highlights", "🧠 Advanced Hook Variation Engine", "💰 High-Converting Copywriting Framework"
    ]
else:
    st.markdown("<h3 style='color: #c5c6c7; font-size: 17px; font-weight: 400; margin-top: 5px;'>Advanced semantic intelligence arrays converting source documents into high-retention social assets.</h3>", unsafe_allow_html=True)
    available_styles = [
        "✨ Core Executive Bullet Highlights", 
        "🧠 Advanced Hook Variation Engine", 
        "💼 LinkedIn Thought Leader Post",
        "🔒 🔥 TikTok Viral Short-Form Script (Pro)", 
        "🔒 📸 Instagram Reel Hook Matrix (Pro)",
        "🔒 🔑 YouTube Shorts Retention Layout (Pro)",
        "🔒 🧵 X (Twitter) Deep Value Thread (Pro)",
        "🔒 📧 Premium Newsletter Issue Block (Pro)",
        "🔒 💰 High-Converting Copywriting Framework (Pro)"
    ]

st.markdown("<br><p style='font-size: 14px; color: #45f3ff; font-weight: bold; margin-bottom: 5px;'>⚡ Select Tactical Processing Preset Target:</p>", unsafe_allow_html=True)
selected_preset = st.selectbox("Preset Style Selector", options=available_styles, label_visibility="collapsed")

# Enforce word limits on free tier
if is_premium:
    placeholder_msg = "Pro Tier Enabled: Paste unlimited source scripts, structural link copy, podcast transcripts, or complete textbook chapters..."
    max_chars = None
else:
    placeholder_msg = "Free Tier Allocation: Paste source text up to 300 words. Upgrade below to clear limits and unlock all 9+ multi-channel writing matrices..."
    max_chars = 1500

user_text = st.text_area("Source Vector Text Entry Box:", height=240, placeholder=placeholder_msg, max_chars=max_chars)

if user_text:
    words = len(user_text.split())
    chars = len(user_text)
    st.markdown(f"<span class='counter-badge'>📊 Source Word Vector: <b>{words}</b></span> &nbsp; <span class='counter-badge'>🔤 Character Array: <b>{chars}</b></span>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# 🧠 ROBUST INTERNAL PARSING ENGINE
def run_semantic_ai_engine(text_input, style_preset):
    sentences = [s.strip() for s in text_input.replace('\n', ' ').split('.') if len(s.strip()) > 5]
    
    if len(sentences) == 0:
        return "⚠️ Matrix Read Alert: The entry text is too brief to extract deep semantic properties. Paste a longer paragraph."
    
    primary_topic = sentences[0]
    secondary_argument = sentences[1] if len(sentences) > 1 else primary_topic
    supporting_evidence = sentences[2] if len(sentences) > 2 else secondary_argument
    concluding_insight = sentences[-1] if len(sentences) > 3 else "The old frameworks are completely dead."

    # Parse and structure outputs based on strategic presets
    if "TikTok" in style_preset or "Shorts" in style_preset or "IG" in style_preset or "Retention" in style_preset:
        output_str = "🎬 **HIGH-RETENTION SHORT-FORM VIDEO SCRIPT**\n\n"
        output_str += "🎥 **Visual Frame 1 (0-3s):** Fast flashing high-contrast text overlay on screen. Loop video of glowing structures.\n"
        output_str += f"🎙️ **Audio Hook:** \"Stop wasting time trying to manually figure out how {primary_topic.lower()}! Here is the brutal truth the algorithms hide from you...\"\n\n"
        output_str += "🎥 **Visual Frame 2 (3-10s):** Zoom in tight on workspace results window panels.\n"
        output_str += f"🎙️ **Audio Body:** \"Most content creators fail because they track basic parameters. The data matrices reveal that {secondary_argument.lower()}. Because when {supporting_evidence.lower()}, traditional workflows completely shatter.\"\n\n"
        output_str += "🎥 **Visual Frame 3 (10-15s):** Smooth tracking pan shot pointing directly to profile link layout blocks.\n"
        output_str += "🎙️ **Audio Outro:** \"Drop an asset follow to secure your daily analytical advantage loop. Do not fall behind the speed curve. Click my bio tracking node right now.\""
        return output_str

    elif "LinkedIn" in style_preset or "Thread" in style_preset:
        output_str = "💼 **HIGH-AUTHORITY VALUE ARCHITECTURE**\n\n"
        output_str += "I used to think standard organizational methods worked. I was entirely wrong.\n\n"
        output_str += f"Here is the real execution data behind how {primary_topic.lower()}:\n\n"
        output_str += f"• **1. The Core Catalyst Node:** {secondary_argument}.\n"
        output_str += f"• **2. The Underappreciated Shift:** When {supporting_evidence.lower()}, it creates an un-matched operational leverage layer for developers.\n\n"
        output_str += f"**The reality?** {concluding_insight}. Traditional operators will be completely out-paced by automation models before the end of this year.\n\n"
        output_str += "What is your specific team roadmap to handle this shift? Let's discuss in the comment loop parameters below. 👇 #Growth #Innovation #Scale"
        return output_str

    elif "Sales" in style_preset or "Framework" in style_preset:
        output_str = "💰 **PERSUASIVE CONVERSION MATRIX COPY**\n\n"
