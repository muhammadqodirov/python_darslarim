# a='https://ya.ru'
# b='google.com'
# c='http://ai.fi'
def normalize_url(text):
    if  'https://' in text:
        return text
    elif 'https://' not in text:
        return 'https://'+ text
    # elif 'http://' in text
print(normalize_url('https://google'))
# normalize_url('https://ya.ru')  # 'https://ya.ru'
# normalize_url('google.com')  # 'https://google.com'
# normalize_url('http://ai.fi')  # 'https://ai.fi'