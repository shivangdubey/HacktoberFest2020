from translate import Translator

translator = Translator(to_lang="zh")
cmd = input("Enter text that to be translated : ")
try:
    translation = translator.translate(cmd)
    print(translation)

except Exception as e:
    print("An Error Found\n")
    raise e


