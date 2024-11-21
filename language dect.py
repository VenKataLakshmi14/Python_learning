from langdetect import detect
text = "हाय आप अभी क्या कर रहे हैं? मुझे तुरंत जवाब चाहिए"
language = detect(text)
print(language)
