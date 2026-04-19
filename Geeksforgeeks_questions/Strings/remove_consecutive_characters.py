import re
def remove_duplicates(str):
    return re.sub(r'(.)\1+', r'\1', str)