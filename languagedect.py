from langdetect import detect_langs

text= 
languages = detect_langs(text)
for language in languages:
    print(language.lang, language.prob)


