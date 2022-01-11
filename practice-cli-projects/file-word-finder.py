import os

# How to find a word inside a file

def find_word(filename, word):
    with open(filename, 'r') as f:
        content = f.read()
    if word in content.lower():
        print(f"Yes! The word {word} is present in {filename}")
    else:
        print(f"No! the word {word} is not present in any of the files in this directory.")

if __name__ == "__main__":
    
    dir_contents = os.listdir()
    print(dir_contents)

    for files in dir_contents:
        if files.endswith('.txt'):                           # files extensions can also be changed
            print(f"Detecting 'twinkle' in {files}")         # twinle can be replaced by any word
            find_word(files, 'twinkle')
