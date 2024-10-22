import streamlit as st
import pandas as pd
from deep_translator import GoogleTranslator

# Load the idioms CSV file
idioms_df = pd.read_csv(r'C:\Users\Abhay Pratap\Desktop\Google Translation\merged_data.csv')


# Function to detect if the sentence is an idiom
def detect_idiom(sentence):
    idiom_row = idioms_df[idioms_df['idiom'].str.lower() == sentence.lower()]
    if not idiom_row.empty:
        return True, idiom_row['def'].values[0]
    return False, sentence


# Function to translate sentences or idioms
def translate_sentence(sentence, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)

    # Check if the sentence is an idiom
    is_idiom, linguistic_meaning = detect_idiom(sentence)

    if is_idiom:
        if target_language == 'en':
            # Return only the linguistic meaning if the target language is English
            return f"**Linguistic meaning of '{sentence}':**\n\n{linguistic_meaning}"
        else:
            # Translate the linguistic meaning to the selected language
            translated = translator.translate(linguistic_meaning)
            return (f"**Linguistic meaning of '{sentence}':**\n\n{linguistic_meaning}\n\n"
                    f"**Translated to {target_language}:**\n\n{translated}")
    else:
        # If not an idiom, translate the original sentence
        translated = translator.translate(sentence)
        return f"**Original text translated to {target_language}:**\n\n{translated}"


# Full language names to their codes mapping
languages_dict = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Korean": "ko",
    "Kurdish (Kurmanji)": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Odia (Oriya)": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots Gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}

# Streamlit interface
st.markdown('<style>body{background-color: Blue;}</style>', unsafe_allow_html=True)

# Dropdown list with full language names
option = st.selectbox('Select Language', list(languages_dict.keys()))

# Text input for the sentence/idiom
text = st.text_area('Input the text')

# Translate button
if st.button('Translate'):
    # Get the language code based on the selected full language name
    selected_language_code = languages_dict[option]

    # Translate the sentence or idiom using the selected language
    translation_result = translate_sentence(text, target_language=selected_language_code)

    # Display the translated text or idiom meaning
    st.markdown(translation_result)
