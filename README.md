# Question Answering Project Using Rule-Based Approach

## Models
- **scanner.py**: Perform tokenization, take input from the file `input.txt`, tokenize, merge into lexicons and save results into the file `lexicon.txt`.
- **dependency_parser.py**: Find the dependencies among the lexicons, take input from the file `lexicon.txt` and save results into the file `dependencies.txt`.
- **grammatical_relation.py**: Generate the grammatical relations from the dependencies, take input from the file `dependencies.txt` and save results into the file `grammatical_relation.txt`.
- **logical_form.py**: Create the logical form from the grammatical relations, take input from the file `grammatical_relation.txt` and save results into the file `logical_form.txt`.
- **procedural_semantic.py**: Convert the logical form into procedural semantics, take input from the file `logical_form.txt` and save results into the file `procedural_semantic.txt`.
- **database.py**: Perform database queries and return answers, take input from the file `procedural_semantic.txt` and save results into the file `answer.txt`.

## How to Run This Project
Simply run the `main.py` file.
