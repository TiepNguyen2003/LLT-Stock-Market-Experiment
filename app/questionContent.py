import csv
import os

class QuestionContent:
    _questions = {}
    _csv_file = os.path.join(os.path.dirname(__file__), 'questions.csv')  # Path relative to this class file
    
    '''
    Deprecated, finds questions and returns them
    '''
    @classmethod
    def getQuestion(cls,id):

        if (int(id) != id):
            raise ValueError("Id is not an integer")
        
        id = int(id)
        # Check if questions have already been loaded
        if not cls._questions:
            try:
                with open(cls._csv_file, mode='r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cls._questions[int(row['id'])] = row['content']
            except FileNotFoundError:
                print("Current directory " + os.getcwd())
                raise FileNotFoundError(f"CSV file '{cls._csv_file}' not found.")
            except KeyError as e:
                raise KeyError(f"CSV file is missing expected column: {e}")

        # Return the requested question
        print(cls._questions)

        return cls._questions.get(id)
