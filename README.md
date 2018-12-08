# assiStudy

This is a repository for a smart assistant in finding the best phd professor for you. 

# How does it work!
This repository retrieve your professors papers from [Arxiv](arxiv.org) and with use of a similarity algorithm finds the most similar papers to your work and return the sorted list of papers. 

# Installation
```sh
$ git clone https://github.com/AmirLavasani/assiStudy.git
$ cd assiStudy
$ pip install -r requirements.txt
$ python server.py
```
Then in your browser go to http://localhost:5000

# Docker
```sh
$ sudo docker build -t "assistudy:v1.0" .
$ sudo docker run assistudy:v1.0
```
After running docker you can accsess the panel again using http://localhost:5000

# Web Panel
go to http://localhost:5000 and you'll see a search form like below:
![Screenshot](../assets/assistudy-index.png?raw=true)
- Type the name of the professors you are interested in their works in "list of professors" section. Writing the full name will provide better result. 
- Select maximum papers result for each professor. 
- Select the maximum number of papers to search in "paper search" dropdown.
- In summary section write down your thesis summary or your articles summary separated by newline. 

Explore the most relative papers of your interested professors. 