class EmailMasker:
    def __init__(self, mask_char='x'):
        self.mask_char = mask_char

    def mask(self, email):
        if '@' not in email:
            return email 
        local_part, domain = email.split('@')
        masked_local = self.mask_char * len(local_part)
        return f"{masked_local}@{domain}"


email_masker = EmailMasker(mask_char='x')
print(email_masker.mask("aaaa@aaa.com")) 
print(email_masker.mask("my.email@example.com"))


class PhoneMasker:
    def __init__(self, mask_char='x', mask_length=3):
        self.mask_char = mask_char
        self.mask_length = mask_length

    def mask(self, phone):
        phone = ' '.join(phone.split())
        non_space_chars = phone.replace(' ', '')
        mask_start = max(len(non_space_chars) - self.mask_length, 0)
        masked_number = (
            non_space_chars[:mask_start] + self.mask_char * self.mask_length
        )
        result, i = '', 0
        for char in phone:
            if char == ' ':
                result += ' '
            else:
                result += masked_number[i]
                i += 1
        return result


phone_masker = PhoneMasker(mask_char='x', mask_length=5)
print(phone_masker.mask("+7 666 777 888"))
print(phone_masker.mask("+7 666 777       888"))


import re

class SkypeMasker:
    def __init__(self, mask_char='x'):
        self.mask_char = mask_char

    def mask(self, skype_str):
        if skype_str.startswith("skype:"):
            return f"skype:{self.mask_char*3}"
        
        pattern = r'(<a href="skype:)([^?]+)(\?call">skype</a>)'
        return re.sub(pattern, r'\1' + self.mask_char*3 + r'\3', skype_str)


skype_masker = SkypeMasker(mask_char='x')
print(skype_masker.mask("skype:alex.max"))
print(skype_masker.mask('<a href="skype:alex.max?call">skype</a>'))

