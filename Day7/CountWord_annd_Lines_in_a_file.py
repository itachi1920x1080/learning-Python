def count(file):
    try :
        with open (file , 'r') as file :
            lines = file.readlines()
            line_coun  = len(lines)
        #     word_count = 0
        #     for line in lines :
        #         words = line.split()
        #         word_count += len(words)
        # return line_coun , word_count
        word_count = sum(len(line.split()) for line in lines)
        print(f"File name: {file.name}")
        print(f"Number of lines: {line_coun}")
        print(f"Number of words: {word_count}")
        return line_coun , word_count
    except FileNotFoundError :
        return "File not found"

count_result = count('sample.txt')