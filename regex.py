import re
pattern=r"\bapple\b"
text="I love apple "
match=re.search(pattern,text)
if match:
    print("Match found",match.group())
else:
    print("Match not found")


sub=re.sub(pattern,"Mango",text)
print(sub)