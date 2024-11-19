from langdetect import detect
text = "ನಿಮ್ಮ ಕೈಲಾದಷ್ಟು ಮಾಡಿ"
language = detect(text)
print(language)
