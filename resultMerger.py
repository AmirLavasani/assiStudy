'''
    This class will merge the results of similarities of articles.
    It has a list of professors' objects and their article similarities along with over all similarity
    It will export the final merged results
'''
from professor import Professor
import json


class ResultMerger:
    def __init__(self, professors=[]):
        self.professors = professors

    def append_professor(self, professor):
        self.professors.append(professor)

    def sort_professors(self):
        return sorted(self.professors, key=lambda x: x.overall_similarity)

    def export_final_result(self):
        for prof in self.sort_professors():
            print "Professor:\t{}".format(prof.name)
            print "overall professor similarity:\t{}".format(prof.overall_similarity)
            for article in prof.export_sorted_articles_list_by_similarity(3):
                print "top articles:{}\n".format(article)
    
    def export_final_json(self, return_papers):
        json_res = []
        for prof in self.sort_professors():
            json_res.append((prof.name, prof.overall_similarity, prof.export_sorted_articles_list_by_similarity(return_papers)))
        return json.dumps(json_res)