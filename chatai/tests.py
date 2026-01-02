#==============================================
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

print("=== Tekin chat (CTRL+C yoki 'exit' bilan chiqish) ===")

while True:
    try:
        savol = input("\nSavolni yozing: ")
        if savol.lower() == "exit":
            print("Dastur yakunlandi.")
            break

        # Faqat gemini-2.5-flash ishlatiladi
        javob = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=savol
        )
        print("*" * 45)
        print("✅ Javob:", javob.text)
        print("*"* 45)

    except KeyboardInterrupt:
        print("\nDastur to'xtatildi.")
        break
    except Exception as e:
        print("❌ Xatolik yuz berdi:", e)
