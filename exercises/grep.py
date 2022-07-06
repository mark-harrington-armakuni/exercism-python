import os, re

WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER_PATH = "/data/"

"""
    Grep Method:

    # Open file
    # While file opened, read lines:
    # Try and Catch:
        # For each sentence in file:
            # If regex_string found in sentence, add line text to out put list of lines
                # if regex_string in sentence:
                    # Add to output strings

    # return output string of lines
"""
def grep_from_files(regex_string, search_file_names):
    output_sentences = []

    sentences = []

    reg_exp = re.compile(regex_string)

    is_mutiple_files = True if len(search_file_names) > 1 else False
    
    try:
        for file_name in search_file_names:
            with open(WORKING_DIRECTORY + DATA_FOLDER_PATH + file_name) as file:
                sentences =  file.readlines()

            for sentence in sentences:
                if reg_exp.search(sentence):
                    if is_mutiple_files:
                        output_sentences.append(file_name + ":" + sentence.strip())
                    else:
                        output_sentences.append(sentence.strip())

    except OSError as error:
        print("I HAD ISSUES: ", error)

    return output_sentences