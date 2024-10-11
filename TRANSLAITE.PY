from googletrans import Translator

# إنشاء كائن الترجمة
translator = Translator()

# النص الذي تريد ترجمته
text = "الله يطول بعمرك"

# الترجمة إلى العربية
translated_text = translator.translate(text, dest='en')

# عرض الترجمة
print(translated_text.text)
