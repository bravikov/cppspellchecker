import os
import cppspellchecker as checker


def test_dictionary():
    base_folder = os.path.dirname(os.path.realpath(__file__))
    filenames = ['test1.dic', 'test2.dic']
    file_paths = [os.path.join(base_folder, filename) for filename in filenames]
    dictionary = checker.get_dictionary_from_files(file_paths)
    assert dictionary == {'aaa', 'bbb', 'ccc', 'ddd'}
