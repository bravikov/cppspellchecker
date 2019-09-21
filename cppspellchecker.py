import argparse
import re
import os


def camel_case_split(string: str):
    return re.sub('([a-z])([A-Z])', r'\1 \2', string).split()


def get_dictionary(folder: str):
    if folder:
        dictionaries_folder = folder
    else:
        base_folder = os.path.dirname(os.path.realpath(__file__))
        dictionaries_folder = os.path.join(base_folder, 'dictionaries')
    file_paths = []
    for filename in os.listdir(dictionaries_folder):
        if not filename.endswith('.dic'):
            continue
        file_path = os.path.join(dictionaries_folder, filename)
        file_paths.append(file_path)
    return get_dictionary_from_files(file_paths)


def get_dictionary_from_files(file_paths: list):
    words = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    words.append(line)
    unique_words = set(words)
    return unique_words


def main():
    parser = argparse.ArgumentParser(description='C++ Spell Checker')
    parser.add_argument('-t', '--unique-typo-list', action='store_true',
                        help='print list of unique typos')
    parser.add_argument('-l', '--lower-bound', default=1, type=int,
                        help='print unique typo if it occurs less than "LOWER_BOUND" times. Default: 1.')
    parser.add_argument('-u', '--upper-bound', default=1000000, type=int,
                        help='print unique typo if it occurs less than "UPPER_BOUND" times. Default: 1000000.')
    parser.add_argument('-d', '--dictionaries-folder', default='', type=str,
                        help='path to folder with dictionaries')
    parser.add_argument('files', metavar='file', type=str, nargs='+', help='files for checking')
    arguments = parser.parse_args()
    filenames = arguments.files
    dictionary = get_dictionary(arguments.dictionaries_folder)
    global_unique_words = {}
    for filename in filenames:
        with open(filename, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
                sentences = re.findall('[a-zA-Z]{2,}', line)
                words = []
                for sentence in sentences:
                    if not sentence:
                        continue
                    words += camel_case_split(sentence)
                if not words:
                    continue
                unique_words = set()
                for word in words:
                    word = word.lower()
                    if len(word) > 1:
                        unique_words.add(word)
                        if arguments.unique_typo_list:
                            if word not in dictionary:
                                global_unique_words[word] = global_unique_words.get(word, int(0)) + 1
                for unique_word in unique_words:
                    if unique_word not in dictionary:
                        if not arguments.unique_typo_list:
                            print('"{}" from {}:{}'.format(unique_word, filename, line_count))

    if arguments.unique_typo_list:
        for word in global_unique_words:
            count = global_unique_words[word]
            if arguments.lower_bound <= count <= arguments.upper_bound:
                print(word)


if __name__ == "__main__":
    main()
