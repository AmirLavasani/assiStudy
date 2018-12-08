# -*- coding: utf-8 -*-
'''
    This is the main pipeline
    # fetch related professors
    # extract top articles of each professor
    # assigning a similarity to each article
    # assigning an overall similarity to each professor
    # sort by similarity in works between prospective student and each professor
    # note the student of best similarities and related papers to read
    # prepare an email based on similarity using top similar articles of that professor
    # suggest email and papers by order
'''

from preprocessor import preProcessor
from arxivSearch import ArxivSearch
from tqdm import tqdm
from articleSimilarity import OverAllSimilarity
from operator import itemgetter
from professor import Professor
from resultMerger import ResultMerger


class Pipeline:
    def __init__(self):
        self.preProcessor = preProcessor()
        self.ArxivSearch = ArxivSearch()                
    
    def explore(self, student_summary=[], professors_list=[], search_papers=10, return_papers=3):
        if professors_list == []:
            professors_list = self.preProcessor.read_authors_from_file()
        if student_summary == []:
            # TODO: return an error message 
            student_summary = ["student work is empty !"]
            
        oas = OverAllSimilarity(student_summary=student_summary)
        resmerg = ResultMerger()
        for author in tqdm(professors_list):
            # retrieving an author articles from arxiv. config in arxivsearch
            resp = self.ArxivSearch.fetch_articles_by_author(author, max_results=search_papers)            
            # TODO: check response status
            # new professor            
            prof = Professor(author)
            # pars arxiv response for each professor
            prof.pars_arxiv_response(resp['entries'])
            # export professors only summary per article
            professor_articles_summaries = prof.export_articles_summaries_list()
            # calculate over all similarity along with a list of each article similarity
            professor_similarities = oas.calculate_overall_similarity(professor_articles_summaries)
            # adding list of similarities to each professors article list
            prof.parse_similarity_list(professor_similarities)
            # adding the completed professor object to result merger object
            resmerg.append_professor(prof)

        # printing resultMerger final results
        return resmerg.export_final_json(return_papers)

def main():
    p = Pipeline()
    print p.explore()

if __name__ == "__main__":    
    main()