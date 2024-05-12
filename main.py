from Models.scanner import Scanner
from Models.dependency_parser import DependencyParser
from Models.grammatical_relation import GrammaticalRelation
from Models.logical_form import LogicalForm
from Models.procedural_semantic import ProceduralSemantic
from Models.database import Database

def main():
    with open("Output/lexicon.txt", "w", encoding="utf8") as lexiconFile:
        pass
    lexiconFile.close()

    with open("Output/dependencies.txt", "w", encoding="utf8") as dependencyFile:
        pass
    dependencyFile.close()
    
    with open("Output/grammatical_relation.txt", "w", encoding="utf8") as relationFile:
        pass
    relationFile.close()

    with open("Output/logical_form.txt", "w", encoding="utf8") as logicalFile:
        pass
    logicalFile.close()

    with open("Output/procedural_semantic.txt", "w", encoding="utf8") as proceduralFile:
        pass
    proceduralFile.close()

    with open("Output/answer.txt", "w", encoding="utf8") as resultFile:
        pass
    resultFile.close()

    with open("Input/query.txt", "r", encoding="utf8") as file:
        for line in file:
            # Scanner
            lexicons = Scanner.get_lexicons(line)
            with open("Output/lexicon.txt", "a", encoding="utf8") as lexiconFile:
                lexiconFile.write(f'Sentence: {line}Lexicons: {", ".join(lexicons)}\n\n\n')
            lexiconFile.close()

            # Dependency parser
            dependencyParser = DependencyParser(lexicons)
            dependencies = dependencyParser.parse()
            with open("Output/dependencies.txt", "a", encoding="utf8") as dependencyFile:
                dependencyFile.write('Sentence: {}Dependencies:\n{}\n\n\n'.format(line, '\n'.join(str(dependency) for dependency in dependencies)))
            dependencyFile.close()

            # Grammatical Relation
            relationModel = GrammaticalRelation(dependencies)
            relations = relationModel.process()
            with open("Output/grammatical_relation.txt", "a", encoding="utf8") as relationFile:
                relationFile.write('Sentence: {}Grammatical Relation:\n{}\n\n\n'.format(line, '\n'.join(relations)))
            relationFile.close()

            # Logical Form
            logical_model = LogicalForm(relations)
            logical_form = logical_model.process()
            with open("Output/logical_form.txt", "a", encoding="utf8") as logicalFile:
                logicalFile.write('Sentence: {}Logical Form: {}\n\n\n'.format(line, logical_form))
            logicalFile.close()

            procedural_semantic = ProceduralSemantic.process(logical_form)
            with open("Output/procedural_semantic.txt", "a", encoding="utf8") as proceduralFile:
                proceduralFile.write('Sentence: {}Procedural Semantic: {}\n\n\n'.format(line, procedural_semantic))
            proceduralFile.close()

            # Get answer from database
            database = Database()
            answer = database.query(procedural_semantic)
            with open("Output/answer.txt", "a", encoding="utf8") as resultFile:
                resultFile.write('Query: {}Answer: {}\n\n\n'.format(line, answer))
            resultFile.close()
    file.close()    

if __name__ == "__main__":
    main()