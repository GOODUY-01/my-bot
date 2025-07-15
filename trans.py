from googletrans import Translator

def tarjimon(message):
    tarjimonbek = Translator()
    til = tarjimonbek.detect(message).lang
    if til == "uz":
        return tarjimonbek.translate(message, "en").text
    elif til == "en":
        return tarjimonbek.translate(message, "uz").text