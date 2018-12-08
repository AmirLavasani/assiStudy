'''
    This class will help us to search archiv papers based on author name or subject. 
'''

from urllib import quote_plus
from urllib import urlencode
from urllib import urlretrieve
import feedparser

#https://github.com/lukasschwab/arxiv.py/blob/master/arxiv/arxiv.py credit

class ArxivSearch:
    def __init__(self, arxiv_root_url="http://export.arxiv.org/api/query?"):
        self.arxiv_root_url = arxiv_root_url

    def fetch_articles_by_author(self, author_name, 
                                id_list=[], 
                                start=0, 
                                max_results=50, 
                                sort_by="submittedDate", 
                                sort_order="descending"):

        search_query = "au:{}+AND+cat:cs.AI".format(author_name)
        # sortBy can be "relevance", "lastUpdatedDate", "submittedDate"
        # sortOrder can be either "ascending" or "descending"
        url_args = urlencode({"search_query": search_query, 
                        "id_list": ','.join(id_list),
                        "start": start,
                        "max_results": max_results,
                        "sortBy": sort_by,
                        "sortOrder": sort_order})
        res = feedparser.parse(self.arxiv_root_url + url_args)
        return res

    # TODO fetch data by following prefixes    
    ''' 
    prefix	explanation
    ti	Title
    au	Author
    abs	Abstract
    co	Comment
    jr	Journal Reference
    cat	Subject Category
    rn	Report Number
    id	Id (use id_list instead)
    all	All of the above
    '''


def test():
    arxiv = ArxivSearch()    
    res = arxiv.fetch_articles_by_author("hinton")
    sample = res['entries'][0]
    print sample['summary']

if __name__ == "__main__":    
    test()