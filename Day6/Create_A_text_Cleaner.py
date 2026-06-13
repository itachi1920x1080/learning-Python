import re


def clean (text):
    #Remove punctuation
    text = re.sub(r"[^\w\s]","", text)  # ជំនួសអក្សរពិសេសជាមួយចន្លោះ
    text = "".join(text.split())  # ដកចេញចន្លោះអតិបរមា
    #removr extar spaces
    text= "".join(text.split())
    #conver to  lowercase
    return text.lower()
    # return text

# input_text = " Hello, World.!!! welcome to Python programming.  "
input_text = str(input("Enter your text: "))
cleaned_text = clean(input_text)
print("Original Text:", input_text)
print("Cleaned Text:", cleaned_text)



