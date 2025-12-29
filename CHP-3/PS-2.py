letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

print(letter.replace("<|NAME|>", "Parth").replace("<|DATE|>", "29th december 2025"))