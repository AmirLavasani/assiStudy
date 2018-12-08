'''
    This is a class storing professor info including:
    articles: title, similarity, link, summary, published, ...
    overall similarity
'''

class Professor:
    def __init__(self, name):
        self.name = name
        self.articles = []
        self.overall_similarity = 0
    
    def pars_arxiv_response(self, arxiv_response):
        # arxiv response inculding following info:
        # updated
        # updated_parsed
        # published_parsed
        # title
        # authors
        # summary_detail
        # summary
        # links
        # guidislink
        # title_detail
        # tags
        # link
        # author
        # published
        # author_detail
        # id
        # arxiv_primary_category
        # arxiv_comment
        # we store only title, summary, link, published
        # we can add any future required field in the following loop
        for resp in arxiv_response:
            resp_info_dict = {}
            resp_info_dict['title'] = resp['title']
            resp_info_dict['link'] = resp['link']            
            resp_info_dict['summary'] = resp['summary']
            resp_info_dict['published'] = resp['published']
            self.articles.append(resp_info_dict)
    
    def export_articles_summaries_list(self):
        summaries = []
        for article in self.articles:
            summaries.append(article['summary'])
        return summaries

    def parse_similarity_list(self, similarity_list):
        if len(similarity_list) != len(self.articles):
            raise ValueError('Length of professor articles differ from length of similarity list.')
        for i, info in enumerate(self.articles):
            info['similarity'] = similarity_list[i]
        self.overall_similarity = reduce(lambda x, y: x + y, similarity_list) / len(similarity_list)
        self.sorted_articles_by_similarity = sorted(self.articles, key=lambda k: k['similarity'])
    
    def export_sorted_articles_list_by_similarity(self, articles_count):
        return self.sorted_articles_by_similarity[:articles_count]