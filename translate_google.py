import requests
import json
import fileinput
import re
from googletrans import Translator

def read_file_to_string(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def replace_word_in_file(file_path, target_word, replacement_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            replaced_content = content.replace(target_word, replacement_word)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(replaced_content)

        print(f"Replacement complete: '{target_word}' replaced with '{replacement_word}'")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/act_i.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/act_ii.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/act_iii.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/act_iv_2.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/act_iv.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/completionist.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/culinary_delights.snbt"
#path =  "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/decorations.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/exploration.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/fishing.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/jolly_cooperation.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/other_hobbies.snbt"
#path = "ftbquests/quests/chapters/professions.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/storage_solutions.snbt"
#path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/test.snbt"
path = "/Users/eun/Desktop/Git/translate/ftbquests/quests/chapters/tutorial_island.snbt"

given_string = read_file_to_string(path)
pattern_1 = re.compile('description:(.+?)\]', re.DOTALL)
matches = pattern_1.findall(given_string)
temp = '\n'.join(matches)
pattern_2 = re.compile('"(.+?)"')
resultes = pattern_2.findall(temp)

translator = Translator()
for result in resultes:
    if result != "\n" :
        en_text = translator.translate(result, dest='ko')
        replace_word_in_file(path, result, en_text.text)