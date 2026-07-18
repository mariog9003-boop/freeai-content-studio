import streamlit as st
import hashlib
import time

st.set_page_config(page_title="Faceless Script Engine Pro", page_icon="🎬", layout="centered")

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

# 🎨 CYBERPUNK DARK NEON INDUSTRIAL CSS DESIGN
st.markdown("""<style>
    .main {background-color: #0b0c10;} 
    textarea {background-color: #1f2833 !important; color: #ffffff !important; border: 1px solid #ff007f !important; border-radius: 12px !important; font-size: 15px !important;}
    
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #ff007f 0%, #7928ca 100%); 
        color: white; border: none; border-radius: 12px; width: 100%; height: 56px; 
        font-weight: 800; font-size: 18px; box-shadow: 0px 5px 25px rgba(255, 0, 127, 0.4);
    }
    
    .monetize-box {
        background: linear-gradient(145deg, #1f2833, #0b0c10); 
        padding: 40px; border-radius: 20px; border: 2px solid #ff007f; 
        text-align: center; margin-top: 45px; box-shadow: 0px 12px 40px rgba(255, 0, 127, 0.2);
    }
    .premium-badge {background-color: #ff007f; color: white; padding: 6px 18px; border-radius: 20px; font-size: 11px; font-weight: bold;}
    .counter-badge {background-color: #1f2833; padding: 6px 14px; border-radius: 8px; border: 1px solid #ff007f; font-size: 13px; color: #c5c6c7;}
    .license-banner {background-color: #1f2833; padding: 15px; border-radius: 10px; border: 1px dashed #ff007f; margin-bottom: 20px;}
    .feature-tag {background-color: #1f2833; color: #ff007f; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: bold; border: 1px solid rgba(255,0,127,0.3);}
</style>""", unsafe_allow_html=True)

# 🔑 SIDEBAR ACTIVATION PANEL
with st.sidebar:
    st.markdown("### 🔑 Licencia del Sistema")
    st.markdown(f"<div class='license-banner'><span style='color: #c5c6c7; font-size: 11px;'>TU DEVICE ID:</span><br><b style='color: #ff007f; font-size: 19px; font-family: monospace;'>{visitor_device_id}</b></div>", unsafe_allow_html=True)
    
    user_license = st.text_input("Ingresa tu Clave Premium Key:", type="password", placeholder="Pega tu clave aquí...")
    is_premium = verify_license_key(visitor_device_id, user_license)
    
    if is_premium:
        st.success("👑 Modo Pro Activo: Computación Ilimitada!")
    elif user_license:
        st.error("🔴 Error de Validación.")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### 🛠️ Enlaces de Soporte")
    st.sidebar.markdown("[🔑 Obtener Clave Premium Pro](https://buymeacoffee.com)")
    st.sidebar.markdown("[☕ Ir a mi página Buy Me a Coffee](https://buymeacoffee.com)")

# 🚀 MAIN APPLICATION LAYOUT
st.markdown("<h1 style='color: white; font-size: 40px; font-weight: 800; margin-bottom: 0px;'>🎬 Faceless Script Engine Pro</h1>", unsafe_allow_html=True)

if is_premium:
    st.markdown("<h3><span style='color:#ff007f;'>👑 Panel Pro</span> • Generación Ininterrumpida Activada</h3>", unsafe_allow_html=True)
    available_styles = [
        "🔥 Guion Estilo Viral Curiosidad (TikTok/Reels)", 
        "🧠 Guion Educativo / Retención Extrema (Shorts)", 
        "💰 Guion de Ventas para Afiliados (TikTok Shop)",
        "🎭 Narración de Historias / Dark Documentaries"
    ]
else:
    st.markdown("<h3 style='color: #c5c6c7; font-size: 17px; font-weight: 400; margin-top: 5px;'>Generador automático de guiones con ganchos psicológicos y direcciones visuales para canales automatizados.</h3>", unsafe_allow_html=True)
    available_styles = [
        "🔥 Guion Estilo Viral Curiosidad (TikTok/Reels)", 
        "🧠 Guion Educativo / Retención Extrema (Shorts)",
        "🔒 💰 Guion de Ventas para Afiliados (Pro Only)",
        "🔒 🎭 Narración de Historias / Dark Documentaries (Pro Only)"
    ]

st.markdown("<br><p style='font-size: 14px; color: #ff007f; font-weight: bold; margin-bottom: 5px;'>⚡ Elige la Estructura de Retención de la IA:</p>", unsafe_allow_html=True)
selected_preset = st.selectbox("Preset Selector", options=available_styles, label_visibility="collapsed")

placeholder_msg = "Pega aquí cualquier noticia, transcripción de YouTube o artículo largo para convertirlo en un guion viral..."
user_text = st.text_area("Inserta el Texto Base o Noticia Cruda:", height=240, placeholder=placeholder_msg)

if user_text:
    st.markdown(f"<span class='counter-badge'>📊 Palabras Leídas: <b>{len(user_text.split())}</b></span> &nbsp; <span class='counter-badge'>🔤 Caracteres Analizados: <b>{len(user_text)}</b></span>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 🧠 INTERACTIVE GENERATION REFACTOR ENGINE
def build_viral_faceless_script(text_input, style_preset):
    sentences = [s.strip() for s in text_input.replace('\n', ' ').split('.') if len(s.strip()) > 5]
    if len(sentences) == 0: 
        return "⚠️ Error: Por favor pega un texto más largo para poder extraer la data semántica."
    
    p = sentences[0]
    s = sentences[1] if len(sentences) > 1 else p
    e = sentences[2] if len(sentences) > 2 else s
    
    if "Curiosidad" in style_preset:
        script = f"""🚨 **GUION VIRAL DETECTADO (ESTILO: CURIOSIDAD EXTREMA)**\n"""
        script += f"⏳ **Duración estimada:** 45-50 Segundos\n"
        script += f"--------------------------------------------------\n\n"
        script += f"🎬 **ESCENA 1 (0-3s) - EL GANCHO ENVENENADO:**\n"
        script += f"📸 *Visual:* [Video en bucle de un mapa cyberpunk o datos digitales moviéndose rápido. Texto gigante en pantalla: \"Esto te lo ocultaron\"] \n"
        script += f"🎙️ *Audio (Voz de IA Inteligente):* \"¡Deja de hacer lo que estás haciendo! El 99% de las personas no tienen idea de que {p.lower()}... Pero la verdad acaba de salir a la luz.\" \n\n"
        script += f"🎬 **ESCENA 2 (3-15s) - EL DESARROLLO DEL MISTERIO:**\n"
        script += f"📸 *Visual:* [Corte rápido a metraje de archivo de personas sorprendidas o laboratorios de alta tecnología. Filtro oscuro oscilante] \n"
        script += f"🎙️ *Audio:* \"Todo comenzó cuando los analistas descubrieron que {s.lower()}. Esto cambia por completo las reglas del juego.\" \n\n"
        script += f"🎬 **ESCENA 3 (15-35s) - EL PUNTO DE QUIEBRE Y RETENCIÓN:**\n"
        script += f"📸 *Visual:* [Zoom dramático a gráficos ascendentes en rojo neón con efectos de sonido glitch] \n"
        script += f"🎙️ *Audio:* \"Y lo peor no es eso. Lo que realmente asusta es que cuando {e.lower()}, los sistemas tradicionales colapsan de golpe.\" \n\n"
        script += f"🎬 **ESCENA 4 (35-45s) - LLAMADA A LA ACCIÓN (CTA):**\n"
        script += f"📸 *Visual:* [Aparece el botón de Seguir parpadeando en la pantalla con una flecha brillante] \n"
        script += f"🎙️ *Audio:* \"Si no quieres quedarte atrás mientras el mundo cambia, dale al botón de seguir ahora mismo para dominar el algoritmo diario. ¿Tú qué opinas de esto? Te leo en los comentarios.\""
        return script
        
    elif "Educativo" in style_preset:
        script = f"""🧠 **GUION INFORTATIVO / RETENCIÓN DE RETE (ALTA VALORACIÓN)**\n"""
        script += f"⏳ **Duración estimada:** 50 Segundos\n"
        script += f"--------------------------------------------------\n\n"
        script += f"🎬 **ESCENA 1 (0-3s) - EL PROBLEMA AGUDO:**\n"
        script += f"📸 *Visual:* [Un clip de B-Roll de alguien estresado frente a una computadora, tipografía limpia y minimalista] \n"
        script += f"🎙️ *Audio:* \"Si quieres entender el futuro de este problema, tienes que saber cómo {p.lower()}. Es un secreto a voces.\" \n\n"
        script += f"🎬 **ESCENA 2 (3-20s) - EXPLICACIÓN TÉCNICA:**\n"
        script += f"📸 *Visual:* [Diagramas e iconos vectoriales apareciendo uno tras otro con transiciones dinámicas] \n"
        script += f"🎙️ *Audio:* \"La razón es simple pero impactante: {s.lower()}. Esto crea un efecto dominó inmediato.\" \n\n"
        script += f"🎬 **ESCENA 3 (20-40s) - APLICACIÓN PRÁCTICA:**\n"
        script += f"📸 *Visual:* [Pantalla dividida mostrando código o un tutorial rápido paso a paso en video] \n"
        script += f"🎙️ *Audio:* \"Para aprovechar esto a tu favor, recuerda que {e.lower()}. Quienes apliquen esto primero ganarán este año.\" \n\n"
        script += f"🎬 **ESCENA 4 (40-50s) - CIERRE ESTRATÉGICO:**\n"
        script += f"📸 *Visual:* [Texto centrado: \"Únete a la Comunidad Pro\" e icono de guardar video] \n"
        script += f"🎙️ *Audio:* \"Guarda este video para que no se te olvide y comparte esto con alguien que necesite despertar hoy mismo.\""
        return script
        
    elif "Ventas" in style_preset:
        script = f"""💰 **GUION EXTREMO DE VENTAS / MARKETING DE AFILIADOS**\n"""
        script += f"⏳ **Duración estimada:** 40 Segundos\n"
        script += f"--------------------------------------------------\n\n"
        script += f"🎬 **ESCENA 1 (0-4s) - EL ANZUELO COMERCIAL:**\n"
        script += f"📸 *Visual:* [Un unboxing en primer plano a toda velocidad o el uso del producto físico mostrando un resultado brutal]\n"
        script += f"🎙️ *Audio:* \"Esta es la verdadera razón por la cual tu solución actual es obsoleta. Mira lo que pasa cuando {p.lower()}. Es increíble.\" \n\n"
        script += f"🎬 **ESCENA 2 (4-25s) - LA DEMOSTRACIÓN DE VALOR:**\n"
        script += f"📸 *Visual:* [Macro tomas del producto resolviendo un problema con subtítulos automáticos brillantes]\n"
