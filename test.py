import re
${policy}=Threat
str1='Info: MID 34 'Threat' feeds source alienvault detected malicious domain: vhacked.ddns.net in: Envelope Sender'
reg='.*${policy}.*'
print(re.search(reg,str1))