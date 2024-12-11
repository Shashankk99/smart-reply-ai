import streamlit as st

# Set page configuration
st.set_page_config(page_title="Smart Reply AI", page_icon="📧", layout="wide")

# Custom CSS for styling and animations
st.markdown("""
    <style>
        /* Global Styles */
        body {
            background-color: #1c1e26;
            color: #f5f5f5;
            margin: 0; 
            padding: 0;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }

        /* Title Styles */
        h1.title {
            font-size: 3em;
            font-weight: bold;
            margin: 20px 0;
            padding: 0;
            text-align: center;
            background: linear-gradient(45deg, #4CAF50, #FF00FF, #00FFFF, #4CAF50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: hueRotateText 5s infinite linear;
        }

        /* Title Animation */
        @keyframes hueRotateText {
            0% { filter: hue-rotate(0deg); }
            100% { filter: hue-rotate(360deg); }
        }

        /* Image Row Layout using CSS Grid */
        .image-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px auto;
            max-width: 1300px;
        }

        /* Image Container Styles */
        .image-container {
            position: relative;
            display: flex;
            justify-content: center;
            width: 100%;
            max-width: 600px;
            padding: 10px;
            background: linear-gradient(90deg, #4CAF50, #FF00FF, #00FFFF, #4CAF50);
            background-size: 600% 600%;
            animation: borderGlow 9s infinite alternate;
            border-radius: 20px;
            box-sizing: border-box;
            overflow: hidden;
        }

        /* Image Styles */
        .image-container img {
            width: 100%;
            border-radius: 15px;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.6);
            transition: transform 0.3s ease-in-out;
            z-index: 1;
        }

        /* Image Hover Effect */
        .image-container img:hover {
            transform: scale(1.05);
        }

        /* Overlay Text on Images */
        .image-container::after {
            content: 'Revolutionize Your Email Workflow';
            position: absolute;
            bottom: 10px;
            left: 10px;
            background: rgba(0,0,0,0.6);
            color: #fff;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.9em;
            opacity: 0;
            transition: opacity 0.3s ease-in-out;
        }

        .image-container:hover::after {
            opacity: 1;
        }

        /* Border Glow Animation */
        @keyframes borderGlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Responsive Adjustments for Tablets */
        @media(max-width: 768px) {
            h1.title {
                font-size: 2em;
            }
            .image-container {
                max-width: 90%;
            }
            .image-row {
                gap: 15px;
            }
        }

        /* Responsive Adjustments for Mobile Devices */
        @media(max-width: 480px) {
            h1.title {
                font-size: 1.5em;
            }
            .image-row {
                grid-template-columns: 1fr;
                align-items: center;
            }
            .image-container {
                max-width: 100%;
            }
        }

        /* Button Styles */
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
            padding: 10px 20px;
            font-size: 1em;
        }

        .stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.05);  
        }

        /* Divider Style */
        hr {
            border: 0;
            height: 1px;
            background: #4CAF50;
            margin: 40px 0;
        }

        /* Link Styles */
        a {
            color: #4CAF50;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">Smart Reply AI</h1>', unsafe_allow_html=True)

# Images displayed side by side with lightbox links
st.markdown("""
<div class="image-row">
    <div class="image-container">
        <a href="#">
            <img src="https://ideogram.ai/assets/image/lossless/response/uNFFPU16T3aKlRMB4dY20g" alt="Smart Reply AI Illustration 1" />
        </a>
    </div>
    <div class="image-container">
        <a href="#">
            <img src="https://ideogram.ai/assets/image/lossless/response/5RMvGyhbQYy2tkMFMPrOMw" alt="Smart Reply AI Illustration 2" />
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Brief introduction
st.markdown("""
**Smart Reply AI** is a feature-rich email follow-up management solution, integrating seamlessly with your inbox to handle reminders, notifications, and AI-generated draft responses—all within a polished, responsive interface.

This synopsis provides a comprehensive overview of its core features, technical architecture, and future roadmap.
""")

# Additional sections with expanders
with st.expander("System Architecture & FlutterFlow Integration"):
    st.markdown("""
    **Core Components:**
    - **FlutterFlow Frontend:**  
      FlutterFlow enables rapid UI construction, intuitive visual logic, and robust Firebase integration, ensuring a responsive and scalable mobile experience.
    
    - **Firebase Backend:**
      - **Authentication:** Secure sign-in (e.g., Google) integrated directly within FlutterFlow.
      - **Firestore:** Store user profiles, tokens, reminders, and AI drafts. FlutterFlow’s Firestore actions simplify data operations and UI updates.
      - **Cloud Functions:** Handle server-side tasks (email fetching, OAuth, notifications, GPT queries) triggered via Custom Actions from FlutterFlow.

    - **External Services:**
      - **Email APIs (Gmail/Outlook):** OAuth-secured inbox access. Cloud Functions fetch emails and update Firestore, with FlutterFlow reflecting changes instantly.
      - **OpenAI GPT:** Cloud Functions query GPT for draft suggestions. Firestore stores results, and FlutterFlow displays them for editing and sending.
    
    **Data Flow Example:**
    1. User logs in through FlutterFlow’s auth widget.
    2. “Connect Email” triggers a Custom Action calling a Cloud Function for OAuth and email retrieval.
    3. Emails appear in a Firestore-powered list on the dashboard, updating in real-time.
    4. User sets reminders via a FlutterFlow DateTime picker. Firestore stores these reminders.
    5. Cloud Functions monitor reminders, sending push notifications via FCM, integrated into FlutterFlow.
    6. AI drafts: A Custom Action requests GPT-based drafts via a Cloud Function. Firestore stores the draft, and FlutterFlow’s UI displays it instantly for final tweaks.
    
    """)

with st.expander("1. Authentication & Secure Email Linking 🔑"):
    st.markdown("""
    **Overview:**
    Users authenticate with Google or other methods via FlutterFlow. A "Connect Email" button triggers a Cloud Function to handle OAuth and securely store tokens in Firestore.

    **User Value:**
    - Smooth onboarding.
    - Secure inbox access under user control.
    - No manual token handling on the client.
    """)

with st.expander("2. Dashboard & Email Retrieval 📩"):
    st.markdown("""
    **Overview:**
    The dashboard, a Firestore-bound list in FlutterFlow, shows pending emails. A “Refresh” action calls a Cloud Function to fetch unread emails. Changes appear instantly, leveraging FlutterFlow’s real-time updates.

    **User Value:**
    - Clear view of pending follow-ups.
    - Real-time synchronization ensures reliability.
    - Quick scanning and sorting of emails.

    **Technical Snippet (Cloud Function):**
    """)
    st.code("""
import functions_framework
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from firebase_admin import firestore

@functions_framework.http
def fetch_unread_emails(request):
    user_id = request.args.get('user_id')
    # Retrieve tokens from Firestore (omitted)
    creds = Credentials(...)  
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', q='is:unread').execute()
    messages = results.get('messages', [])

    db = firestore.client()
    email_refs = db.collection('users').document(user_id).collection('emails')

    for msg in messages:
        email_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = email_data.get("payload", {}).get("headers", [])
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "No Subject")
        sender = next((h["value"] for h in headers if h["name"] == "From"), "Unknown Sender")
        snippet = email_data.get("snippet", "")
        email_refs.add({"subject": subject, "from": sender, "snippet": snippet})

    return {"status": "success"}
    """)

with st.expander("3. Intelligent Reminders & Notifications ⏰"):
    st.markdown("""
    **Overview:**
    Reminders set via FlutterFlow widgets are stored in Firestore. Cloud Functions check them and send push notifications via FCM at the correct times. FlutterFlow integrates notifications effortlessly.

    **User Value:**
    - Timely reminders prevent missed follow-ups.
    - Reduced mental overhead.
    """)

with st.expander("4. AI-Driven Draft Generation 🤖"):
    st.markdown("""
    **Overview:**
    A Custom Action requests GPT drafts via a Cloud Function. Results are stored in Firestore and displayed in FlutterFlow, allowing immediate edits and sending.

    **User Value:**
    - Saves time drafting emails.
    - Ensures consistent, polished replies.
    """)

with st.expander("5. Polished UI/UX, Privacy & User Trust 🛡️"):
    st.markdown("""
    **Overview:**
    FlutterFlow’s design tools yield a clean, intuitive interface. Privacy policies, tooltips, and guided onboarding are easily integrated, building user confidence.

    **User Value:**
    - Transparent data handling.
    - Easy, enjoyable interactions.
    - Responsive design for various devices.
    """)

with st.expander("6. Monetization & Future Roadmap 🚀"):
    st.markdown("""
    **Overview:**
    Tiered offerings can provide advanced AI capabilities, unlimited reminders, and CRM integrations. FlutterFlow’s extensibility supports adding payment pages, analytics, and quick feature updates.

    **User Value:**
    - Flexible plans to match user needs.
    - Continuous improvements ensure long-term value.
    """)

# Divider
st.markdown("<hr>", unsafe_allow_html=True)

# Call to Action
st.markdown("### Ready to Elevate Your Email Follow-Up Strategy?")
if st.button("🚀 Learn More"):
    st.markdown("[Click here to contact the developer](https:meredadoji.com/)")
