from langdetect import detect_langs
text= "पायथन सीखने के लिए सबसे आसान भाषा है, आपको पहले पायथन से शुरुआत करनी होगी"
languages = detect_langs(text)
for language in languages:
    print(language.lang, language.prob)


