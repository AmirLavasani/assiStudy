'''
    This class help us to preprocess the input.
    Input is list of professors names along with their emails. l
'''
import codecs

class preProcessor:
    def __init__(self, authors_name_file_path="data/authors.txt"):
        self.authors_name_file_path = authors_name_file_path
    
    def read_authors_from_file(self):
        authors_list = []
        with codecs.open(self.authors_name_file_path, 'r', 'utf8') as f:
            for line in f:
                line = line.strip()
                authors_list.append(line)
        
        return authors_list