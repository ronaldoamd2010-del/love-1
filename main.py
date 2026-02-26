ig@pl62, [26/02/2026 5:02 PM]
import streamlit as st
import datetime
import random
import time
import base64

# ===== Page Config =====
st.set_page_config(
    page_title="💝 For Lamis 💝",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== Session State =====
if "page" not in st.session_state:
    st.session_state.page = "main"
if "show_message" not in st.session_state:
    st.session_state.show_message = False
if "show_promise" not in st.session_state:
    st.session_state.show_promise = False
if "music_playing" not in st.session_state:
    st.session_state.music_playing = False
if "heart_click" not in st.session_state:
    st.session_state.heart_click = 0
if "love_count" not in st.session_state:
    st.session_state.love_count = 0
if "gift_opened" not in st.session_state:
    st.session_state.gift_opened = False

# ===== Interactive Enhancements =====
if "reaction_count" not in st.session_state:
    st.session_state.reaction_count = 0
if "last_reaction" not in st.session_state:
    st.session_state.last_reaction = None
if "heart_messages" not in st.session_state:
    st.session_state.heart_messages = [
        "💭 I'm thinking of you...",
        "🎵 You're the melody in my heart",
        "🌙 You are my moon and stars",
        "💝 Lamis... my queen",
        "⭐ You're the prettiest star",
        "🌹 Every rose is for you",
        "💌 You're always on my mind",
        "💫 My whole world"
    ]
if "sound_played" not in st.session_state:
    st.session_state.sound_played = False

# ===== Real Time Timer - Dubai Time (UTC+4) =====
# First chat: November 27, 2024
if "first_chat_date" not in st.session_state:
    st.session_state.first_chat_date = datetime.datetime(2024, 11, 27, tzinfo=datetime.timezone(datetime.timedelta(hours=4)))

# Birthday: 79 days from now
if "birthday_date" not in st.session_state:
    now_dubai = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=4)))
    st.session_state.birthday_date = now_dubai + datetime.timedelta(days=79)

# ===== Custom CSS - Purple Theme =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700;900&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
        color: #333333 !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #e6e6fa 0%, #d8bfd8 50%, #dda0dd 100%);
        background-attachment: fixed;
        transition: background 1s ease;
    }
    
    h1, h2, h3, h4, h5, h6, p, div, span {
        color: #333333 !important;
    }
    
    /* Main Heart */
    .main-heart {
        position: relative;
        width: 200px;
        height: 200px;
        margin: 0 auto 30px;
        animation: heartbeat 1.5s ease-in-out infinite;
        cursor: pointer;
        filter: drop-shadow(0 0 30px rgba(147, 112, 219, 0.5));
    }
    
    @keyframes heartbeat {
        0% { transform: scale(1); }
        14% { transform: scale(1.2); }
        28% { transform: scale(1); }
        42% { transform: scale(1.2); }
        70% { transform: scale(1); }
    }
    
    /* Main Card */
    .card {
        background: rgba(255, 255, 255, 0.98);
        border-radius: 40px;
        padding: 40px;
        box-shadow: 0 30px 60px rgba(147, 112, 219, 0.2);
        border: 3px solid #9370db;
        margin: 20px 0;
        animation: cardAppear 1s ease-out;
    }
    
    @keyframes cardAppear {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Title */
    .title {
        font-size: 60px;
        font-weight: 900;
        color: #6a5acd !important;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 0 #e6e6fa;

ig@pl62, [26/02/2026 5:02 PM]
}
    
    /* Floating Hearts */
    .floating-heart {
        position: fixed;
        font-size: 20px;
        animation: float 4s infinite;
        pointer-events: none;
        z-index: 999;
        color: #9370db !important;
    }
    
    @keyframes float {
        0% {
            transform: translateY(100vh) rotate(0deg);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100px) rotate(360deg);
            opacity: 0;
        }
    }
    
    /* Message Box */
    .message-box {
        background: #f0e6ff;
        border-radius: 30px;
        padding: 30px;
        border: 3px dashed #9370db;
        position: relative;
        margin: 30px 0;
    }
    
    .message-box::before {
        content: "💌";
        position: absolute;
        top: -20px;
        right: -20px;
        font-size: 40px;
        background: white;
        border-radius: 50%;
        padding: 10px;
        box-shadow: 0 5px 15px rgba(147, 112, 219, 0.3);
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: rotate(-5deg); }
        50% { transform: rotate(5deg) translateY(-5px); }
    }
    
    /* Highlighted Text */
    .highlight {
        font-size: 28px;
        font-weight: 900;
        color: #6a5acd !important;
        display: inline-block;
        animation: glow 2s infinite;
    }
    
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px #d8bfd8; }
        50% { text-shadow: 0 0 30px #9370db; }
    }
    
    /* Promise Box */
    .promise-box {
        background: #2c2c2c;
        color: white !important;
        padding: 40px;
        border-radius: 20px;
        margin: 20px 0;
        border: 3px solid #9370db;
        position: relative;
        overflow: hidden;
    }
    
    .promise-box h3, .promise-box p, .promise-box div {
        color: white !important;
    }
    
    .promise-box::before {
        content: "💝";
        position: absolute;
        top: 10px;
        left: 10px;
        font-size: 50px;
        opacity: 0.1;
        animation: rotate 10s infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #9370db, #6a5acd) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 15px 30px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        border: 2px solid white !important;
        width: 100%;
        margin: 5px 0;
        box-shadow: 0 10px 20px rgba(147, 112, 219, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(106, 90, 205, 0.4) !important;
    }
    
    /* Music Box */
    .music-box {
        background: #f0e6ff;
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        border: 2px solid #9370db;
        text-align: center;
    }
    
    .vinyl-record {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1a1a1a, #333);
        animation: spin 4s linear infinite;
        margin: 0 auto 15px;
        border: 3px solid white;
        box-shadow: 0 0 20px rgba(147, 112, 219, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white !important;
        font-size: 30px;
    }
    
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* Gift Box */
    .gift-box {
        background: linear-gradient(135deg, #9370db, #6a5acd);

ig@pl62, [26/02/2026 5:02 PM]
border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 3px solid white;
        animation: giftPulse 2s infinite;
    }
    
    .gift-box h3, .gift-box div {
        color: white !important;
    }
    
    @keyframes giftPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .gift-box:hover {
        transform: scale(1.05) rotate(2deg);
        box-shadow: 0 20px 40px rgba(147, 112, 219, 0.4);
    }
    
    .gift-content {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        border: 2px solid #9370db;
    }
    
    /* Countdown */
    .countdown-box {
        background: #f0e6ff;
        border-radius: 100px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
        border: 2px solid #9370db;
    }
    
    .timer {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    
    .time-unit {
        background: white;
        border-radius: 15px;
        padding: 10px;
        min-width: 70px;
        border: 2px solid #9370db;
    }
    
    .time-number {
        font-size: 36px;
        font-weight: 900;
        color: #6a5acd !important;
    }
    
    .time-label {
        color: #666 !important;
    }
    
    /* Photo Album */
    .photo-album {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 15px;
        margin: 30px 0;
    }
    
    .photo-frame {
        aspect-ratio: 1;
        background: linear-gradient(45deg, #9370db, #6a5acd);
        padding: 5px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .photo-frame:hover {
        transform: scale(1.05) rotate(3deg);
    }
    
    .photo-placeholder {
        width: 100%;
        height: 100%;
        background: white;
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
    }
    
    /* Signature */
    .signature {
        text-align: center;
        margin-top: 40px;
        font-size: 24px;
        font-weight: 900;
        color: #6a5acd !important;
    }
    
    .signature div {
        color: #6a5acd !important;
    }
    
    /* Neon Text Effect */
    .neon-text {
        color: #fff;
        text-shadow: 
            0 0 7px #fff,
            0 0 10px #fff,
            0 0 21px #fff,
            0 0 42px #9370db,
            0 0 82px #9370db,
            0 0 92px #9370db,
            0 0 102px #9370db,
            0 0 151px #9370db;
        animation: flicker 1.5s infinite alternate;
    }
    
    @keyframes flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% {
            text-shadow: 
                0 0 4px #fff,
                0 0 11px #fff,
                0 0 19px #fff,
                0 0 40px #9370db,
                0 0 80px #9370db,
                0 0 90px #9370db,
                0 0 100px #9370db,
                0 0 150px #9370db;
        }
        20%, 24%, 55% {        
            text-shadow: none;
        }
    }
    
    /* Hover Card Effect */
    .hover-card {
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    
    .hover-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 30px 60px rgba(147, 112, 219, 0.3);
    }
    
    /* Typing Effect */
    .typing-effect {
        overflow: hidden;
        border-right: .15em solid #9370db;
        white-space: nowrap;
        margin: 0 auto;
        animation: 
            typing 3.5s steps(40, end),
            blink-caret .75s step-end infinite;

ig@pl62, [26/02/2026 5:02 PM]
}
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: #9370db; }
    }
    
    /* Mobile Responsive */
    @media (max-width: 768px) {
        .title {
            font-size: 40px;
        }
        .timer {
            gap: 10px;
        }
        .time-unit {
            min-width: 50px;
        }
        .time-number {
            font-size: 24px;
        }
    }
    
    iframe {
        border-radius: 10px;
        border: 2px solid #9370db;
    }
</style>
""", unsafe_allow_html=True)

# ===== Helper Functions =====
def create_floating_hearts():
    """Generate floating hearts"""
    hearts_html = ""
    for i in range(20):
        left = random.randint(0, 100)
        delay = random.uniform(0, 4)
        size = random.randint(15, 25)
        hearts = ["❤️", "💖", "💝", "💗", "💓", "💕", "💜", "💞"]
        heart = random.choice(hearts)
        hearts_html += f"""
        <div class="floating-heart" style="
            left: {left}%;
            animation-delay: {delay}s;
            font-size: {size}px;
        ">{heart}</div>
        """
    return hearts_html

# ===== Dubai Time Functions =====
def get_dubai_time():
    """Get current time in Dubai (UTC+4)"""
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=4)))

def time_since_first_chat():
    """Time since first chat (Nov 27, 2024)"""
    now = get_dubai_time()
    first_chat = datetime.datetime(2024, 11, 27, tzinfo=datetime.timezone(datetime.timedelta(hours=4)))
    diff = now - first_chat
    return diff.days

def time_until_birthday():
    """Time until Lamis's birthday (79 days from now)"""
    now = get_dubai_time()
    diff = st.session_state.birthday_date - now
    return max(0, diff.days)

def get_time_of_day_greeting():
    """Greeting based on Dubai time"""
    hour = get_dubai_time().hour
    if hour < 12:
        return "🌅 Good morning my Lamis"
    elif hour < 17:
        return "☀️ Good afternoon beautiful"
    elif hour < 20:
        return "🌆 Good evening my queen"
    else:
        return "🌙 Good night Lamis, dream of me"

# ===== Interactive Functions =====
def get_random_heart_message():
    """Random message when clicking heart"""
    return random.choice(st.session_state.heart_messages)

def add_reaction(reaction_type):
    """Track reactions"""
    st.session_state.reaction_count += 1
    st.session_state.last_reaction = {
        "type": reaction_type,
        "time": get_dubai_time().strftime("%H:%M"),
        "count": st.session_state.reaction_count
    }

# ===== Main Page =====
def main():
    # Floating hearts
    st.markdown(create_floating_hearts(), unsafe_allow_html=True)
    
    # Header with heart
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="main-heart">
            <svg viewBox="0 0 32 29.6" style="width:100%; height:100%; fill: #9370db;">
                <path d="M23.6,0c-3.4,0-6.3,2.7-7.6,5.6C14.7,2.7,11.8,0,8.4,0C3.8,0,0,3.8,0,8.4c0,9.4,9.5,11.9,16,21.2
                c6.1-9.3,16-12.1,16-21.2C32,3.8,28.2,0,23.6,0z"/>
            </svg>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("💜 Click the heart"):
            st.session_state.heart_click += 1
            add_reaction("heart_click")
            if st.session_state.heart_click % 5 == 0:
                st.balloons()
    
    st.markdown("<h1 class='title'>For You Lamis 💝</h1>", unsafe_allow_html=True)
    
    # Time-based Greeting (Dubai Time)
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #f0e6ff, #e6d5ff);
        padding: 15px;
        border-radius: 50px;
        text-align: center;

ig@pl62, [26/02/2026 5:02 PM]
margin: 10px 0 20px 0;
        border: 2px solid #9370db;
    ">
        <h3 style="color: #6a5acd; margin: 0;">{get_time_of_day_greeting()}</h3>
        <p style="color: #666; margin: 5px 0 0 0; font-size: 14px;">
            🕒 Dubai Time: {get_dubai_time().strftime("%I:%M %p, %B %d, %Y")}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Heart Messages
    if st.session_state.heart_click > 0:
        if st.session_state.heart_click % 3 == 0:
            st.markdown(f"""
            <div class="pop-in" style="
                background: rgba(255, 255, 255, 0.9);
                padding: 15px;
                border-radius: 50px;
                text-align: center;
                margin: 10px 0;
                border: 2px solid #9370db;
            ">
                <p style="color: #6a5acd; font-size: 18px; margin: 0;">
                    {get_random_heart_message()}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        if st.session_state.heart_click == 10:
            st.balloons()
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #ffd700, #9370db);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                margin: 20px 0;
                border: 3px solid white;
            ">
                <h3 style="color: white; margin: 0;">✨ 10 times you touched my heart ✨</h3>
                <p style="color: white;">Each time I love you more 💜</p>
            </div>
            """, unsafe_allow_html=True)
        
        if st.session_state.heart_click == 25:
            st.snow()
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #87CEEB, #9370db);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                margin: 20px 0;
                border: 3px solid white;
            ">
                <h3 style="color: white; margin: 0;">❄️ 25 times... ❄️</h3>
                <p style="color: white;">You are my whole world 💕</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Main Card
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Photos
        st.markdown("""
        <div class="photo-album">
            <div class="photo-frame"><div class="photo-placeholder">👧🏼</div></div>
            <div class="photo-frame"><div class="photo-placeholder">👦🏿</div></div>
            <div class="photo-frame"><div class="photo-placeholder">💜</div></div>
            <div class="photo-frame"><div class="photo-placeholder">🌹</div></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Time Trackers
        st.markdown("---")
        st.markdown("### ⏰ Our Time Together", unsafe_allow_html=True)
        
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            days_since = time_since_first_chat()
            st.markdown(f"""
            <div class="hover-card" style="
                background: white;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                border: 2px solid #9370db;
                box-shadow: 0 5px 15px rgba(147,112,219,0.2);
            ">
                <h4 style="color: #6a5acd;">⏰ Since First Chat</h4>
                <div style="font-size: 48px; font-weight: 900; color: #9370db;">{days_since}</div>
                <div style="color: #666;">days</div>
                <p style="color: #888; font-size: 14px; margin-top: 10px;">
                    November 27, 2024 - the day you changed my life 💜
                </p>
            </div>

ig@pl62, [26/02/2026 5:02 PM]
""", unsafe_allow_html=True)
        
        with col_t2:
            days_until = time_until_birthday()
            if days_until > 0:
                st.markdown(f"""
                <div class="hover-card" style="
                    background: white;
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    border: 2px solid #9370db;
                    box-shadow: 0 5px 15px rgba(147,112,219,0.2);
                ">
                    <h4 style="color: #6a5acd;">🎂 Until Your Birthday</h4>
                    <div style="font-size: 48px; font-weight: 900; color: #9370db;">{days_until}</div>
                    <div style="color: #666;">days</div>
                    <p style="color: #888; font-size: 14px; margin-top: 10px;">
                        Can't wait to celebrate you! 🎉
                    </p>
