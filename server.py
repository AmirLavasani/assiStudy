# -*- coding: utf-8 -*-
'''
    This is http server for requesting the engine
'''



from flask import Flask, request, render_template
app = Flask(__name__, static_url_path='/static') #create the Flask app
from pipeline import Pipeline
from templateGenerator import TemplateGenerator

@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')

@app.route('/search', methods=['POST', 'GET'])
def return_json_result():    
	data = clean_from_data(request.form)
	pline = Pipeline()
	print data
	res = pline.explore(student_summary=data['abstract'],
						professors_list=data['prof_list'],
						search_papers=data['search_papers'],
						return_papers=data['return_papers'])
	temgen = TemplateGenerator()
	return temgen.generate(res)

def clean_from_data(form):
	data = request.form
	cleaned_data = {}
	cleaned_data['user_name'] = data['user_name'].strip()
	cleaned_data['return_papers'] = int(data['return_papers'])
	cleaned_data['search_papers'] = int(data['search_papers'])
	cleaned_data['prof_list'] = [s.strip() for s in data['prof_list'].split('\n')]
	if cleaned_data['prof_list'] == [u'']:
		cleaned_data['prof_list'] = []
	cleaned_data['abstract'] = [s.strip() for s in data['abstract'].split('\n')]
	if cleaned_data['abstract'] == [u'']:
		cleaned_data['abstract'] = []
	print cleaned_data['abstract']
	return cleaned_data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #run app in debug mode on port 5000


