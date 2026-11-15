# ticketdesk_login.py
import streamlit as st
import re

# --- Page Config ---
st.set_page_config(
    page_title="TicketHub — เข้าสู่ระบบ",
    page_icon="🎫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
<style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    /* Root variables */
    :root {
        --ink-900: #14212C;
        --ink-700: #2C4356;
        --slate-500: #5C7285;
        --slate-300: #9FAEBA;
        --paper-50: #F5F7F9;
        --paper-0: #FFFFFF;
        --stamp-100: #F5EBDA;
        --line-200: #E3E7EB;
        --success-600: #2F7D5D;
        --success-100: #E3F1EA;
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 20px;
        --font-display: 'Space Grotesk', sans-serif;
        --font-body: 'Inter', sans-serif;
        --font-mono: 'IBM Plex Mono', monospace;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {background: var(--paper-50);}

    /* Main container */
    .main-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 32px 16px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Card shell - grid layout */
    .auth-shell {
        display: grid;
        grid-template-columns: 1.05fr 1fr;
        background: var(--paper-0);
        border-radius: var(--radius-lg);
        overflow: hidden;
        box-shadow: 0 24px 48px -24px rgba(20,33,44,0.4);
        width: 100%;
        min-height: 620px;
        position: relative;
    }

    /* Brand panel */
    .brand-panel {
        background: linear-gradient(165deg, var(--ink-900) 0%, var(--ink-700) 100%);
        color: var(--paper-0);
        padding: 48px 44px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .brand-mark {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: var(--font-display);
        font-weight: 600;
        font-size: 18px;
        letter-spacing: 0.01em;
    }

    .brand-copy {
        margin-top: 40px;
    }

    .brand-eyebrow {
        font-family: var(--font-mono);
        font-size: 12px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--slate-300);
        margin: 0 0 16px;
    }

    .brand-headline {
        font-family: var(--font-display);
        font-weight: 600;
        font-size: clamp(26px, 3vw, 32px);
        line-height: 1.3;
        margin: 0 0 16px;
        max-width: 22ch;
    }

    .brand-sub {
        font-size: 15px;
        line-height: 1.7;
        color: var(--slate-300);
        margin: 0;
        max-width: 38ch;
    }

    .brand-footer {
        margin-top: 40px;
        font-size: 12px;
        color: var(--slate-300);
        display: flex;
        flex-direction: column;
        gap: 4px;
    }

    /* Ticket stub */
    .ticket-stub {
        margin-top: 40px;
        background: rgba(255,255,255,0.06);
        border: 1px dashed rgba(255,255,255,0.28);
        border-radius: var(--radius-md);
        padding: 18px 20px;
        max-width: 340px;
        transform: rotate(-1.6deg);
        backdrop-filter: blur(2px);
    }

    .stub-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
    }

    .stub-id {
        font-family: var(--font-mono);
        font-size: 13px;
        letter-spacing: 0.04em;
        color: var(--paper-0);
    }

    .stub-status {
        font-family: var(--font-mono);
        font-size: 11px;
        letter-spacing: 0.06em;
        background: var(--success-100);
        color: var(--success-600);
        padding: 3px 9px;
        border-radius: 999px;
    }

    .stub-subject {
        font-size: 14px;
        line-height: 1.5;
        margin: 0 0 12px;
        color: var(--paper-0);
    }

    .stub-meta {
        display: flex;
        gap: 16px;
        font-size: 12px;
        color: var(--slate-300);
        font-family: var(--font-mono);
    }

    /* Seam (divider) */
    .seam {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 51.2%;
        width: 28px;
        transform: translateX(-50%);
        z-index: 2;
        background-image: radial-gradient(circle, var(--paper-0) 0 4px, transparent 4.3px);
        background-size: 28px 22px;
        background-position: center;
        background-repeat: repeat-y;
        pointer-events: none;
    }
    .seam::after {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        left: 50%;
        border-left: 1px dashed var(--slate-300);
        transform: translateX(-50%);
        opacity: 0.5;
    }

    /* Form panel */
    .form-panel {
        padding: 48px 48px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .form-head {
        margin-bottom: 28px;
    }

    /* Tabs */
    .tabs-container {
        position: relative;
        display: flex;
        gap: 28px;
        border-bottom: 1px solid var(--line-200);
        margin-bottom: 28px;
    }

    .tab-btn {
        background: none;
        border: none;
        padding: 0 0 14px;
        font-family: var(--font-body);
        font-weight: 600;
        font-size: 15px;
        color: var(--slate-500);
        cursor: pointer;
        transition: color 0.2s ease;
    }

    .tab-btn:hover {
        color: var(--ink-900);
    }

    .tab-btn.active {
        color: var(--ink-900);
    }

    .tab-indicator {
        position: absolute;
        bottom: -1px;
        height: 2px;
        background: var(--ink-900);
        transition: transform 0.25s ease, width 0.25s ease;
    }

    .form-title {
        font-family: var(--font-display);
        font-weight: 600;
        font-size: 22px;
        margin: 0 0 6px;
    }

    .form-desc {
        font-size: 14px;
        color: var(--slate-500);
        margin: 0 0 24px;
    }

    /* Form fields */
    .stTextInput > div > div > input {
        font-family: var(--font-body) !important;
        font-size: 14px !important;
        padding: 11px 14px !important;
        border: 1px solid var(--line-200) !important;
        border-radius: var(--radius-sm) !important;
        background: var(--paper-0) !important;
        color: var(--ink-900) !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--ink-700) !important;
        box-shadow: 0 0 0 3px rgba(44,67,86,0.14) !important;
    }

    .stCheckbox > div {
        font-size: 13px !important;
        color: var(--slate-500) !important;
    }

    .stButton > button {
        width: 100% !important;
        padding: 12px 16px !important;
        background: var(--ink-900) !important;
        color: var(--paper-0) !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-family: var(--font-body) !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        cursor: pointer !important;
        transition: background 0.15s ease !important;
    }

    .stButton > button:hover {
        background: var(--ink-700) !important;
    }

    .divider {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 20px 0;
        color: var(--slate-300);
        font-size: 12px;
    }
    .divider::before, .divider::after {
        content: "";
        flex: 1;
        height: 1px;
        background: var(--line-200);
    }

    .btn-outline {
        width: 100%;
        padding: 11px 16px;
        background: var(--paper-0);
        color: var(--ink-900);
        border: 1px solid var(--line-200);
        border-radius: var(--radius-sm);
        font-family: var(--font-body);
        font-weight: 600;
        font-size: 14px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        transition: border-color 0.15s ease, background 0.15s ease;
    }
    .btn-outline:hover {
        border-color: var(--slate-300);
        background: var(--paper-50);
    }

    .switch-line {
        margin-top: 22px;
        text-align: center;
        font-size: 13px;
        color: var(--slate-500);
    }
    .switch-line a {
        color: var(--ink-700);
        text-decoration: none;
        cursor: pointer;
        font-weight: 600;
    }
    .switch-line a:hover {
        text-decoration: underline;
    }

    .note-box {
        display: flex;
        gap: 10px;
        background: var(--stamp-100);
        border: 1px solid #E7D5B4;
        border-radius: var(--radius-sm);
        padding: 12px 14px;
        font-size: 12.5px;
        line-height: 1.55;
        color: #6B4E1E;
        margin-bottom: 20px;
    }

    .row-between {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 22px;
        font-size: 13px;
    }

    a {
        color: var(--ink-700);
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }

    /* Responsive */
    @media (max-width: 860px) {
        .auth-shell {
            grid-template-columns: 1fr;
            min-height: 0;
        }
        .seam { display: none; }
        .brand-panel { padding: 36px 28px; }
        .brand-copy { margin-top: 24px; }
        .ticket-stub { margin-top: 24px; max-width: 100%; }
        .form-panel { padding: 36px 28px; }
    }

    /* Hide labels if needed */
    .stTextInput label, .stCheckbox label {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: var(--ink-700) !important;
    }

    .stAlert {
        padding: 12px 14px !important;
        border-radius: var(--radius-sm) !important;
    }

    /* Smooth transitions */
    .auth-form {
        transition: opacity 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "login"

if "login_success" not in st.session_state:
    st.session_state.login_success = False

if "register_success" not in st.session_state:
    st.session_state.register_success = False

# --- Functions ---
def switch_tab(tab_name):
    st.session_state.active_tab = tab_name
    st.session_state.login_success = False
    st.session_state.register_success = False

def handle_login(email, password, remember):
    # Mock login - in real app, validate against database
    if email and password:
        st.session_state.login_success = True
        st.success("✅ เข้าสู่ระบบสำเร็จ! ยินดีต้อนรับกลับ")
        return True
    else:
        st.error("❌ กรุณากรอกอีเมลและรหัสผ่านให้ครบถ้วน")
        return False

def handle_register(name, email, password, password2, agree):
    # Validation
    if not name or not email or not password or not password2:
        st.error("❌ กรุณากรอกข้อมูลให้ครบถ้วน")
        return False

    if password != password2:
        st.error("❌ รหัสผ่านไม่ตรงกัน กรุณาลองอีกครั้ง")
        return False

    if len(password) < 8:
        st.error("❌ รหัสผ่านต้องมีความยาวอย่างน้อย 8 ตัวอักษร")
        return False

    if not agree:
        st.error("❌ กรุณายอมรับข้อกำหนดการใช้งาน")
        return False

    # Mock registration
    st.session_state.register_success = True
    st.success("✅ สร้างบัญชีสำเร็จ! กรุณารอการอนุมัติจากผู้ดูแลระบบ")
    return True

# --- Main Layout ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="auth-shell">', unsafe_allow_html=True)

# --- Brand Panel ---
st.markdown("""
<div class="brand-panel">
    <div>
        <div class="brand-mark">
            <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
                <path d="M3 9.5C3 8.12 4.12 7 5.5 7H20.5C21.88 7 23 8.12 23 9.5V10.5C21.34 10.5 20 11.84 20 13.5C20 15.16 21.34 16.5 23 16.5V17.5C23 18.88 21.88 20 20.5 20H5.5C4.12 20 3 18.88 3 17.5V16.5C4.66 16.5 6 15.16 6 13.5C6 11.84 4.66 10.5 3 10.5V9.5Z" stroke="#F5F7F9" stroke-width="1.6" stroke-linejoin="round"/>
                <path d="M11 7.5V19.5" stroke="#F5F7F9" stroke-width="1.4" stroke-dasharray="2.5 2.5"/>
            </svg>
            TicketHub
        </div>
        <div class="brand-copy">
            <p class="brand-eyebrow">Support Ticket Management</p>
            <h1 class="brand-headline">ระบบจัดการตั๋วสนับสนุนขององค์กร</h1>
            <p class="brand-sub">รับเรื่อง มอบหมายงาน และติดตามสถานะการแก้ไขปัญหา ได้ในที่เดียว</p>
        </div>
    </div>
    <div class="brand-footer">
        <span>ใช้งานเฉพาะภายในองค์กร</span>
        <span>เข้าสู่ระบบด้วยบัญชีที่ได้รับอนุมัติเท่านั้น</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Seam ---
st.markdown('<div class="seam" aria-hidden="true"></div>', unsafe_allow_html=True)

# --- Form Panel ---
st.markdown('<div class="form-panel">', unsafe_allow_html=True)

# --- Tabs ---
active = st.session_state.active_tab

st.markdown(f"""
<div class="form-head">
    <div class="tabs-container" role="tablist">
        <button class="tab-btn {'active' if active == 'login' else ''}" 
                onclick="document.querySelector('[data-testid=\'stMarkdown\']').click()" 
                data-tab="login">เข้าสู่ระบบ</button>
        <button class="tab-btn {'active' if active == 'register' else ''}" 
                onclick="document.querySelector('[data-testid=\'stMarkdown\']').click()" 
                data-tab="register">สมัครสมาชิก</button>
        <span class="tab-indicator" style="width: {'80px' if active == 'login' else '85px'}; transform: translateX({0 if active == 'login' else '108'}px);"></span>
    </div>
    <h2 class="form-title">{'ยินดีต้อนรับกลับ' if active == 'login' else 'สร้างบัญชีใหม่'}</h2>
    <p class="form-desc">{'เข้าสู่ระบบเพื่อจัดการตั๋วสนับสนุนของคุณ' if active == 'login' else 'สมัครสมาชิกเพื่อแจ้งปัญหาและติดตามสถานะตั๋วของคุณ'}</p>
</div>
""", unsafe_allow_html=True)

# --- Login Form ---
if active == "login":
    with st.container():
        st.markdown('<div class="auth-form">', unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("อีเมลหรือชื่อผู้ใช้งาน", placeholder="name@organization.com")
            password = st.text_input("รหัสผ่าน", placeholder="กรอกรหัสผ่านของคุณ", type="password")

            col1, col2 = st.columns([2, 1])
            with col1:
                remember = st.checkbox("จดจำการเข้าสู่ระบบ")
            with col2:
                st.markdown('<div style="text-align:right; padding-top:6px;"><a href="#">ลืมรหัสผ่าน?</a></div>', unsafe_allow_html=True)

            submitted = st.form_submit_button("เข้าสู่ระบบ", use_container_width=True)

            if submitted:
                handle_login(email, password, remember)

        st.markdown('<div class="divider">หรือ</div>', unsafe_allow_html=True)

        # SSO Button
        st.markdown("""
        <button class="btn-outline" style="width:100%;">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <rect x="1" y="1" width="6" height="6" fill="#2C4356"/>
                <rect x="9" y="1" width="6" height="6" fill="#5C7285"/>
                <rect x="1" y="9" width="6" height="6" fill="#5C7285"/>
                <rect x="9" y="9" width="6" height="6" fill="#2C4356"/>
            </svg>
            เข้าสู่ระบบด้วยบัญชีองค์กร (SSO)
        </button>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <p class="switch-line">ยังไม่มีบัญชี? <a onclick="switch_tab('register')">สมัครสมาชิก</a></p>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# --- Register Form ---
else:
    with st.container():
        st.markdown('<div class="auth-form">', unsafe_allow_html=True)

        st.markdown("""
        <div class="note-box">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <circle cx="8" cy="8" r="6.5" stroke="#A9752B" stroke-width="1.3"/>
                <path d="M8 5.3V8.3" stroke="#A9752B" stroke-width="1.3" stroke-linecap="round"/>
                <circle cx="8" cy="10.6" r="0.7" fill="#A9752B"/>
            </svg>
            <span>ระบบนี้ใช้งาน<strong>เฉพาะภายในองค์กร</strong> กรุณาลงทะเบียนด้วยอีเมลองค์กรของคุณ บัญชีจะเปิดใช้งานได้หลังผู้ดูแลระบบตรวจสอบและอนุมัติ</span>
        </div>
        """, unsafe_allow_html=True)

        with st.form("register_form", clear_on_submit=False):
            name = st.text_input("ชื่อ-นามสกุล", placeholder="กรอกชื่อ-นามสกุลของคุณ")
            email = st.text_input("อีเมล", placeholder="name@organization.com")
            password = st.text_input("รหัสผ่าน", placeholder="อย่างน้อย 8 ตัวอักษร", type="password")
            password2 = st.text_input("ยืนยันรหัสผ่าน", placeholder="กรอกรหัสผ่านอีกครั้ง", type="password")
            agree = st.checkbox("ฉันยอมรับข้อกำหนดการใช้งานและนโยบายความเป็นส่วนตัว")

            submitted = st.form_submit_button("สร้างบัญชี", use_container_width=True)

            if submitted:
                handle_register(name, email, password, password2, agree)

        st.markdown(f"""
        <p class="switch-line">มีบัญชีอยู่แล้ว? <a onclick="switch_tab('login')">เข้าสู่ระบบ</a></p>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # form-panel
st.markdown('</div>', unsafe_allow_html=True)  # auth-shell
st.markdown('</div>', unsafe_allow_html=True)  # main-container

# --- JavaScript for tab switching ---
st.markdown("""
<script>
function switch_tab(tab) {
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'tab_switch';
    input.value = tab;
    document.body.appendChild(input);
    input.dispatchEvent(new Event('change'));
}

// Handle tab switching via query params
const urlParams = new URLSearchParams(window.location.search);
const tab = urlParams.get('tab');
if (tab && (tab === 'login' || tab === 'register')) {
    switch_tab(tab);
}
</script>
""", unsafe_allow_html=True)

# --- Handle tab switching via query params ---
import streamlit as st

query_params = st.query_params
if "tab" in query_params:
    tab_value = query_params["tab"]
    if tab_value in ["login", "register"]:
        st.session_state.active_tab = tab_value
        st.rerun()