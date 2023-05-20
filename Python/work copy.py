import re


def find_all_phones(text):
    result = re.findall(r"((\+[0-9]{3}\([0-9]{2}\)[0-9]{3}\-)([0-9]{2}\-[0-9]{2}|[0-9]{1}\-[09]{3}))", text)
    res = []
    for phone in result:
        res.append(phone[0])
            
    return res


text = ' +380(67)777-7-771  +380(67)777-77-77  +380(67)111-777-777+380(67)777-77-787'

print()
print(find_all_phones(text))
print(['+380(67)777-7-771', '+380(67)777-77-77', '+380(67)777-77-78'])
print()