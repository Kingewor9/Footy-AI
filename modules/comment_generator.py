import random
import config as cfg
from google import genai
from google.genai import types

# Initialize the Gemini Client globally
# It will automatically use the GEMINI_API_KEY from config.py
try:
    client = genai.Client(api_key=cfg.GEMINI_API_KEY)
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    client = None

# Your core instruction for the AI model
SYSTEM_INSTRUCTION = (
    "You are a knowledgeable and engaging football fan (soccer) comment bot. "
    "Your response must be a single, short, one-liner statement that sounds like a true, opinionated fan. "
    "Use simple English, avoid all emojis, complex grammar, or punctuation (only periods, no commas or dashes). "
    "The comment must contribute meaningfully to the post's content and be under 100 characters. "
    "Focus on match tactics, player performance, transfers, or league implications. "
    "Examples: 'That tackle was crucial', 'Need better midfield cover', 'The manager got the tactics wrong', 'Next week will be massive'"
)

# Fallback comments in case the AI API fails
FALLBACK_COMMENTS = [
    "Great take on the formation today",
    "We need more consistency in the final third",
    "Midfield battle was absolutely key in that match",
    "Should have finished that chance clinicaly",
    "The transfer market is going to be wild this summer"
]


def generate_comment(post_text: str, mode="RANDOM"):
    if mode == "RANDOM":
        # Keep the existing static comment logic for RANDOM mode
        return random.choice(cfg.COMMENTS)
    
    if mode == "AI" and client:
        # Construct the user prompt, giving the AI the post to comment on
        user_prompt = f"The channel post text is: \"{post_text}\""
        
        try:
            # Call the Gemini API
            response = client.models.generate_content(
                model='gemini-2.5-flash', # A fast and capable model for this task
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    # Setting temperature low encourages more focused, less random output
                    temperature=0.5, 
                )
            )
            
            # The AI might return extra text or formatting; we'll strip it down
            ai_comment = response.text.strip()
            
            if ai_comment:
                print(f"AI-Generated Comment: '{ai_comment}'")
                return ai_comment
            
            # Fallback if AI returns an empty string
            print("AI returned an empty comment. Using fallback.")
            
        except Exception as e:
            print(f"Error calling Gemini API: {e}. Using fallback comment.")
            
        # Fallback to a random static comment if AI generation fails or is empty
        return random.choice(FALLBACK_COMMENTS)

    # If the client couldn't be initialized or mode is neither, return original placeholder logic
    return f"(AI simulated comment related to: {post_text[:50]}...)"


# You should define the COMMENTS list in config.py if it is used globally, 
# or ensure you are not relying on the old static list in this file. 
# Since your listener uses cfg.MODE, we ensure the function handles the logic above.
# If you want to keep the old static comments for the 'RANDOM' mode, 
# you should move the list from the old file into config.py as cfg.COMMENTS.
# For simplicity, I'll assume you keep the original comments in a separate file for now, 
# but if you get an error that cfg.COMMENTS doesn't exist, you'll need to move them.