from googletrans import Translator

translator = Translator()
# result = translator.translate('hello world')

translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='gu')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)

# print(result.src)
# print(result.dest)
# print(result.origin)
# print(result.text)
# print(result.pronunciation)

# result = translator.translate('Mikä on nimesi', src='fi')
# result = translator.translate('Mikä on nimesi', dest='fr')

# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')