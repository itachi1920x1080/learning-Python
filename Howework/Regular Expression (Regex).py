import re

def regex_email_(text):
    # កែពី emill ទៅ email ដើម្បីឱ្យត្រូវន័យ
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # អ្នកអាចប្តូរ "*" ទៅជា "[HIDDEN]" ឬ "***" ដើម្បីឱ្យច្បាស់ជាងមុន
    results = re.sub(email_pattern, "***", text) 
    return results

input_text = input("Enter a string: ")
modified_text = regex_email_(input_text)

print("-" * 20)
print("Input string:", input_text)
print("Modified string:", modified_text)