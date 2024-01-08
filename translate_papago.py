import requests
import json
import fileinput
import re

def translate(text, source, target):
    CLIENT_ID, CLIENT_SECRET = '0tCqMe998uhF1sG5EuYl', '6w2X8E2YzH'
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'Content-Type': 'application/json',
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    data = {'source': source, 'target': target, 'text': text}
    response = requests.post(url, json.dumps(data), headers=headers)
    return response.json()['message']['result']['translatedText']

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

        print(f"Replacement complete: '{target_word}' replaced with '{replacement_word}'.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

path = "/Users/eun/Desktop/Git/translate/act_i.snbt"

given_string = read_file_to_string(path)
pattern_1 = re.compile('description:(.+?)\]', re.DOTALL)
matches = pattern_1.findall(given_string)
temp = '\n'.join(matches)
pattern_2 = re.compile('"(.+?)"')
resultes = pattern_2.findall(temp)
engs = resultes;

for result, eng in zip(resultes, engs):
    if result != "\n" :
	    en_text = translate(result, 'en', 'ko')
	    replace_word_in_file(path, eng, en_text)