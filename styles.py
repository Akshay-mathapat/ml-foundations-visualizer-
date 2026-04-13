def load_css():
    return """
    <style>

    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
    }

    /* Glass Card Effect */
    .glass {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 10px;
        background: linear-gradient(45deg, #ff6ec4, #7873f5);
        color: white;
        border: none;
        padding: 10px 20px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
    }

    /* Inputs */
    input, textarea {
        border-radius: 10px !important;
    }

    /* Smooth Fade Animation */
    .fade-in {
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }

    </style>
    """