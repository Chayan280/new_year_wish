import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Happy New Year 2026 💕",
    page_icon="🎆",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# YAHAN APNI GIRLFRIEND KA NAAM DAALO
GIRLFRIEND_NAME = "Darling"

# Custom CSS - Fully Mobile Responsive
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600&display=swap');
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 10px;
    }
    
    /* Mobile responsive container */
    .main-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 15px;
    }
    
    .big-title {
        font-family: 'Dancing Script', cursive;
        font-size: clamp(2em, 8vw, 4em);
        font-weight: bold;
        text-align: center;
        color: #FFD700;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        animation: glow 2s ease-in-out infinite;
        margin: 15px 0;
        line-height: 1.2;
    }
    
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 20px #FFD700, 0 0 30px #FFD700; }
        50% { text-shadow: 0 0 40px #FFD700, 0 0 60px #FFD700; }
    }
    
    .love-message {
        font-family: 'Poppins', sans-serif;
        font-size: clamp(1em, 4vw, 1.3em);
        text-align: center;
        color: white;
        padding: 20px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        margin: 20px 0;
        line-height: 1.8;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .animated-sticker {
        text-align: center;
        font-size: clamp(3em, 15vw, 6em);
        margin: 20px 0;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-15px) scale(1.1); }
    }
    
    .rotating-hearts {
        text-align: center;
        font-size: clamp(2em, 10vw, 4em);
        animation: rotate 4s linear infinite;
        margin: 20px 0;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .bouncing-emoji {
        display: inline-block;
        animation: bounce 1.5s ease-in-out infinite;
        font-size: clamp(2em, 8vw, 3em);
        margin: 0 5px;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    .heart-pulse {
        text-align: center;
        font-size: clamp(3em, 12vw, 5em);
        animation: pulse 1.5s ease-in-out infinite;
        margin: 30px 0;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.3); }
    }
    
    .fireworks {
        text-align: center;
        font-size: clamp(1.5em, 6vw, 2.5em);
        margin: 20px 0;
        animation: sparkle 2s ease-in-out infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.15); }
    }
    
    .flower-garden {
        text-align: center;
        font-size: clamp(2em, 8vw, 3em);
        margin: 20px 0;
    }
    
    .flower-garden span {
        display: inline-block;
        animation: sway 2s ease-in-out infinite;
        margin: 0 3px;
    }
    
    .flower-garden span:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .flower-garden span:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    .flower-garden span:nth-child(4) {
        animation-delay: 0.6s;
    }
    
    .flower-garden span:nth-child(5) {
        animation-delay: 0.8s;
    }
    
    @keyframes sway {
        0%, 100% { transform: rotate(-10deg); }
        50% { transform: rotate(10deg); }
    }
    
    .love-quote {
        font-family: 'Dancing Script', cursive;
        font-size: clamp(1.3em, 5vw, 2em);
        color: #FFD700;
        text-align: center;
        margin: 25px 0;
        font-style: italic;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .cute-sticker-box {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .dancing-couple {
        font-size: clamp(4em, 18vw, 8em);
        animation: dance 2s ease-in-out infinite;
        display: inline-block;
    }
    
    @keyframes dance {
        0%, 100% { transform: rotate(-5deg) translateX(-10px); }
        50% { transform: rotate(5deg) translateX(10px); }
    }
    
    .reason-item {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 15px;
        padding: 15px;
        margin: 12px 0;
        color: white;
        font-size: clamp(1em, 4vw, 1.2em);
        text-align: center;
        animation: slideIn 0.5s ease-out;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .next-button {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        color: #333;
        padding: 15px 40px;
        border-radius: 50px;
        font-size: clamp(1.1em, 4.5vw, 1.4em);
        font-weight: bold;
        border: none;
        cursor: pointer;
        box-shadow: 0 8px 20px rgba(255,215,0,0.4);
        transition: all 0.3s;
        margin: 30px 0;
        font-family: 'Poppins', sans-serif;
    }
    
    .next-button:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 30px rgba(255,215,0,0.6);
    }
    
    .celebration-emoji {
        display: inline-block;
        animation: celebrate 1s ease-in-out infinite;
        font-size: clamp(2em, 8vw, 3em);
    }
    
    @keyframes celebrate {
        0%, 100% { transform: rotate(-15deg); }
        50% { transform: rotate(15deg); }
    }
    
    .love-birds {
        font-size: clamp(3em, 12vw, 5em);
        text-align: center;
        animation: fly 4s ease-in-out infinite;
    }
    
    @keyframes fly {
        0%, 100% { transform: translateX(-20px); }
        50% { transform: translateX(20px); }
    }
    
    /* Responsive spacing */
    @media (max-width: 768px) {
        .stApp {
            padding: 5px;
        }
        .love-message {
            padding: 15px;
            margin: 15px 0;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

def next_page():
    if st.session_state.current_page < 4:
        st.session_state.current_page += 1
        st.rerun()

def show_magic():
    st.balloons()
    time.sleep(0.3)
    st.snow()

# PAGE 1: WELCOME & HAPPY NEW YEAR
if st.session_state.current_page == 1:
    st.markdown('<div class="fireworks">🎆 🎇 ✨ 🎉 🎊 ✨ 🎇 🎆</div>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="big-title">Happy New Year 2026!</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="animated-sticker">🥳</div>', unsafe_allow_html=True)
    
    message = f"""
    <div class="love-message">
        <strong style="font-size: 1.4em;">To My Dearest {GIRLFRIEND_NAME} 😘,</strong><br><br>
        
        As we welcome 2026 together, I want you to know
        that you are my greatest blessing! ✨
        
        Every moment with you is magical,
        and I can't wait to create more beautiful memories
        with you this year! 💕
        
        You are my everything! 💖
    </div>
    """
    st.markdown(message, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cute-sticker-box">
        <div class="dancing-couple">👦💕👧</div>
        <div class="love-quote">"Together is my favorite place to be"</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="flower-garden"><span>🌹</span><span>🌸</span><span>🌺</span><span>🌻</span><span>🌷</span></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Click for Magic! ✨", key="magic1", use_container_width=True):
            show_magic()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("💕 Click Here Sweetie 💕", key="next1", use_container_width=True):
            next_page()
    
    st.markdown('<div class="fireworks">✨ 💫 ⭐ 🌟 ✨ 💫 ⭐ 🌟 ✨</div>', unsafe_allow_html=True)

# PAGE 2: WHY I LOVE YOU
elif st.session_state.current_page == 2:
    st.markdown('<div class="rotating-hearts">💖 💕 💗</div>', unsafe_allow_html=True)
    
    st.markdown(f'<h1 class="big-title">I Love You so much Baby..😘</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="love-birds">🕊️ 💕 🕊️</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="love-quote">"You are my today and all of my tomorrows"</div>', unsafe_allow_html=True)
    
    reasons = [
        "💕 Your beautiful smile that lights up my world",
        "🌟 The way you make me feel special every day",
        "🌻 Your caring and loving nature",
        "💝 Your laugh that makes everything better",
        "🌹 The comfort I feel when I'm with you",
        "💫 How you inspire me to be better",
        "🎀 Your presence that makes life beautiful",
        "💗 The way you love me unconditionally",
        "🌸 Simply everything about YOU!",
    ]
    
    st.markdown('<div style="text-align: center; color: white; font-size: clamp(1.1em, 4vw, 1.4em); margin: 20px 0;">Here are just some reasons why you\'re so special:</div>', unsafe_allow_html=True)
    
    for i, reason in enumerate(reasons):
        st.markdown(f'<div class="reason-item">{reason}</div>', unsafe_allow_html=True)
        if i % 3 == 0:
            time.sleep(0.02)
    
    st.markdown("""
    <div class="cute-sticker-box">
        <div class="bouncing-emoji">😍</div>
        <div class="bouncing-emoji">💖</div>
        <div class="bouncing-emoji">🥰</div>
        <p style="color: white; font-size: clamp(1em, 4vw, 1.3em); margin-top: 20px;">
        And a million more reasons that I discover every day! 💕
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💕 Click Me cutee🙃 💕", key="next2", use_container_width=True):
            next_page()

# PAGE 3: OUR BEAUTIFUL FUTURE
elif st.session_state.current_page == 3:
    st.markdown('<div class="animated-sticker">🌈</div>', unsafe_allow_html=True)
    
    st.markdown(f'<h1 class="big-title">Our Future Together</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="love-quote">"The best is yet to come"</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cute-sticker-box">
        <div style="font-size: clamp(4em, 16vw, 7em);">🏡</div>
        <p style="color: white; font-size: clamp(1em, 4vw, 1.3em); margin-top: 15px; line-height: 1.8;">
        Building a beautiful life together,<br>
        filled with love, laughter, and endless memories 💕
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    future_message = f"""
    <div class="love-message">
        <h3 style="color: #FFD700; font-size: clamp(1.3em, 5vw, 2em); margin-bottom: 20px;">
        ✨ My Dreams With You ✨
        </h3>
        
        
        ✈️ Traveling the world together
        
        🏡 Creating our perfect home
        
        💍 Growing old hand in hand
        
        🎯 Achieving all our dreams as a team
        
        😊 Making you smile every single day
        
        💕 Loving you more with each passing moment
        
        🌟 Building a lifetime of happiness together

        Forever starts with you 💖
        
    </div>
    """
    st.markdown(future_message, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cute-sticker-box">
        <div class="celebration-emoji">🎊</div>
        <div class="celebration-emoji">💑</div>
        <div class="celebration-emoji">🎊</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💕 Next Page Baby..☺️ 💕", key="next3", use_container_width=True):
            next_page()

# PAGE 4: FINAL MESSAGE
elif st.session_state.current_page == 4:
    st.markdown('<div class="fireworks">🎆 ✨ 🎇 💫 🎉 💫 🎇 ✨ 🎆</div>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="big-title">I Love You!</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="heart-pulse">❤️</div>', unsafe_allow_html=True)
    
    final_message = f"""
    <div class="love-message">
        <h2 style="color: #FFD700; font-size: clamp(1.4em, 6vw, 2.5em); margin-bottom: 25px;">
        Dear {GIRLFRIEND_NAME} ,
        </h2>
        
        
        Thank you for being YOU! 💕
        
        Thank you for loving me,
        for supporting me,
        for making me laugh,
        and for making every day special! ✨
        
        You are my best friend,
        my love,
        my everything! 💖
        
        Here's to an amazing 2026 together,
        filled with love, joy, and countless adventures! 🌟
        
        I LOVE YOU MORE THAN ANYTHING! 💕

    </div>
    """
    st.markdown(final_message, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cute-sticker-box">
        <div style="font-size: clamp(5em, 20vw, 9em); margin: 20px 0;">
        💑
        </div>
        <div class="flower-garden">
            <span>🌹</span><span>💕</span><span>🌺</span><span>💖</span><span>🌻</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎉 Celebrate! 🎉", key="celebrate", use_container_width=True):
            st.balloons()
            st.success(f"\n Happy New Year {GIRLFRIEND_NAME}! I love you! 💕 \n  Only and solely yours, Chayan 😊")
            time.sleep(0.5)
            st.snow()
    
    st.markdown('<div class="fireworks">💖 ✨ 💕 ✨ 💗 ✨ 💝 ✨ 💖</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<p style='text-align: center; color: white; font-size: clamp(0.9em, 3.5vw, 1.1em); opacity: 0.9;'>
Made with infinite ❤️ for {GIRLFRIEND_NAME}<br>
Happy New Year 2026! 🎆
</p>

""", unsafe_allow_html=True)

