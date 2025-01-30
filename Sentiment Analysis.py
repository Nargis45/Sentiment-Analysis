import streamlit as st
import pandas as pd

df = pd.read_excel(r'C:\Users\nasreenn\Documents\MyProject\postman_response\updated_sa_report.xlsx')

# Extract comments
df['clean_comment'] = df['clean_comment'].str.capitalize()

positive_comments = df[df["roberta"] == "positive"]["clean_comment"].tolist()
neutral_comments = df[df["roberta"] == "neutral"]["clean_comment"].tolist()
negative_comments = df[df["roberta"] == "negative"]["clean_comment"].tolist()

# Pass Data to Frontend
st.components.v1.html(f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ background-color: black; color: white; text-align: center; overflow: hidden; margin: 0; }}
        
        .container {{
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100vh;
            display: flex;
        }}

        .section {{
            width: 33.3%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            position: relative;
            overflow: hidden;
        }}

        /* Gradient backgrounds for each section */
        .positive {{ background: linear-gradient(to top, #4CAF50, #1e3c72); }}
        .neutral {{ background: linear-gradient(to top, #A9A9A9, #434343); }}
        .negative {{ background: linear-gradient(to top, #FF5733, #900C3F); }}

        /* Vertical divider line */
        .divider {{
            position: absolute;
            top: 0;
            bottom: 0;
            width: 5px;
            background-color: white;
            opacity: 0.5;
            z-index: 10;
        }}

        .comment-box {{
            position: absolute;
            width: auto;
            max-width: 250px;
            padding: 10px 15px;
            border-radius: 15px;
            font-size: 1.0em;
            color: white;
            text-align: center;
            opacity: 0;
            animation: floatUp 4s ease-in-out forwards, explode 2s ease-out 4s forwards;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
            transition: transform 0.3s ease-out;
        }}

        /* Different colors for each type */
        .positive .comment-box {{ background-color: #76c893; box-shadow: 0 0 15px #76c893; }}
        .neutral .comment-box {{ background-color: #bbbbbb; box-shadow: 0 0 15px #bbbbbb; }}
        .negative .comment-box {{ background-color: #ff5733; box-shadow: 0 0 15px #ff5733; }}

        /* Emojis for explosion effect */
        .emoji {{
            position: absolute;
            font-size: 2em;
            opacity: 0;
            transform: scale(0);
            animation: popEmoji 1s ease-out 4s forwards;
        }}

        /* Floating animation with random motion */
        @keyframes floatUp {{
            0% {{ transform: translateY(0) scale(1); opacity: 1; }}
            50% {{ transform: translateY(-50vh) scale(1.05); }}
            100% {{ transform: translateY(-100vh) scale(1.1); opacity: 1; }}
        }}

        /* Explosion effect with particle glow */
        @keyframes explode {{
            0% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(1.7); opacity: 0.5; filter: blur(5px); }}
            100% {{ transform: scale(2); opacity: 0; filter: blur(10px); }}
        }}

        /* Emoji pop-up animation */
        @keyframes popEmoji {{
            0% {{ transform: scale(0); opacity: 0; }}
            50% {{ transform: scale(1.5); opacity: 1; }}
            100% {{ transform: scale(2); opacity: 0; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Positive section -->
        <div class="section positive" id="positive-section">Positive(55%)</div>
        <!-- Vertical divider line -->
        <div class="divider"></div>
        <!-- Neutral section -->
        <div class="section neutral" id="neutral-section">Neutral(34%)</div>
        <!-- Vertical divider line -->
        <div class="divider"></div>
        <!-- Negative section -->
        <div class="section negative" id="negative-section">Negative(11%)</div>
    </div>

    <script>
        let positiveComments = {positive_comments};
        let neutralComments = {neutral_comments};
        let negativeComments = {negative_comments};

        let positiveEmojis = ["🎉", "😃", "✨", "💖"];
        let neutralEmojis = ["😐", "🤔", "🤷‍♂️"];
        let negativeEmojis = ["💥", "🔥", "😡", "⚡"];

        function createFloatingComments(comments, sectionId, colorClass, emojis) {{
            let section = document.getElementById(sectionId);
            if (!section) {{
                console.error("Section not found: " + sectionId);
                return;
            }}

            comments.forEach((comment, index) => {{
                setTimeout(() => {{
                    let div = document.createElement("div");
                    div.className = "comment-box " + colorClass;
                    div.innerText = comment;
                    div.style.left = "50%";  // Center the comments horizontally
                    div.style.transform = "translateX(-50%)";  // Adjust for exact centering
                    let emoji = document.createElement("div");
                    emoji.className = "emoji";
                    emoji.innerText = emojis[Math.floor(Math.random() * emojis.length)];
                    emoji.style.left = Math.random() * 60 + "%";  // Random emoji position within section
                    emoji.style.bottom = Math.random() * 50 + "%"; // Random bottom position for variety

                    section.appendChild(div);
                    section.appendChild(emoji);

                    setTimeout(() => {{
                        emoji.style.opacity = 1;
                        emoji.style.transform = "scale(1.5)";
                    }}, 4000);  // Emoji appears after floatUp animation
                    
                }}, index * 1500); // Staggered effect
            }});
        }}

        document.addEventListener("DOMContentLoaded", function() {{
            createFloatingComments(positiveComments, "positive-section", "positive", positiveEmojis);
            createFloatingComments(neutralComments, "neutral-section", "neutral", neutralEmojis);
            createFloatingComments(negativeComments, "negative-section", "negative", negativeEmojis);
        }});
    </script>
</body>
</html>
""", height=600)
