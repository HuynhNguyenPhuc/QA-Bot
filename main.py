from Models.scanner import Scanner
from Models.dependency_parser import DependencyParser
import pickle

def main():
    with open("Output/lexicon.txt", "w", encoding="utf8") as lexiconFile:
        pass
    with open("Output/dependencies.txt", "w", encoding="utf8") as dependencyFile:
        pass

    with open("Input/query.txt", "r", encoding="utf8") as file:
        for line in file:
            # Scanner
            lexicons = Scanner.get_lexicons(line)
            with open("Output/lexicon.txt", "a", encoding="utf8") as lexiconFile:
                lexiconFile.write(f'Sentence: {line}Lexicons: {", ".join(lexicons)}\n\n\n')

            # Dependency parser
            parser = DependencyParser(lexicons)
            dependencies = parser.parse()
            with open("Output/dependencies.txt", "a", encoding="utf8") as dependencyFile:
                dependencyFile.write('Sentence: {}Dependencies:\n{}\n\n\n'.format(line, '\n'.join(str(dependency) for dependency in dependencies)))
    file.close()
    # text = "Có môn học nào không được dạy trong 1 năm học, cho biết tên, mã số môn học và năm học ?"
    # lexicons = Scanner.get_lexicons(text)
    # parser = DependencyParser(lexicons)
    # print(parser.parse())
    

if __name__ == "__main__":
    main()