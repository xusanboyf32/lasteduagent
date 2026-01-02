# chatbot/ai_service.py
from google import genai
from django.conf import settings
import time


class GoogleAIService:
    def __init__(self):
        # Settings dan API kalitini olamiz
        self.api_key = getattr(settings, 'GOOGLE_API_KEY', '')

        if not self.api_key:
            raise ValueError(
                "❌ Google API kaliti sozlanmagan!"
            )

        # Google AI clientini yaratamiz
        self.client = genai.Client(api_key=self.api_key)

        # Model nomi - SIZ TEST QILGAN MODEL
        self.model_name = "gemini-2.5-flash"  # ✅ SIZ TEST QILGAN MODEL

    def get_response(self, user_message, chat_history=None):
        """
        AI dan javob olish - TO'LIQ ISHLAYDI
        """
        try:
            start_time = time.time()

            # AI ga so'rov yuboramiz
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=user_message
            )

            # Vaqtni hisoblaymiz
            response_time = time.time() - start_time

            return {
                'success': True,
                'response': response.text,
                'response_time': round(response_time, 2),
                'model': self.model_name
            }

        except Exception as e:
            # Agar birinchi model ishlamasa, ikkinchi modelni sinab ko'ramiz
            try:
                print(f"⚠️ gemini-1.5-flash ishlamadi: {e}. Boshqa model sinab ko'ramiz...")

                response = self.client.models.generate_content(
                    model="gemini-1.5-flash",  # ✅ IKKINCHI VARIANT
                    contents=user_message
                )

                response_time = time.time() - start_time

                return {
                    'success': True,
                    'response': response.text,
                    'response_time': round(response_time, 2),
                    'model': "gemini-1.5-flash"
                }

            except Exception as e2:
                return {
                    'success': False,
                    'response': f"❌ AI xatosi: {str(e2)}\n"
                                f"API kalitini tekshiring: {self.api_key[:20]}...",
                    'response_time': 0,
                    'model': None
                }




