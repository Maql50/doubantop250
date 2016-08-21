# coding:utf-8
import requests
import re
class Movie():
	def __init__(self, name, movie_type, year, score, actor=""):
		self.name = name
		self.actor = actor
		self.movie_type = movie_type
		self.year = year
		self.score = score

	def __str__(self):
		return self.name +	self.movie_type + self.year.replace(' ', '') + " " + self.score

class Douban():
	_url = 'https://movie.douban.com/top250'
	def __init__(self):
		self._movies = []

	def moviesTop250(self):
		for page in range(25):
			resp = requests.get(self._url + "?start=" + str(page*25))
			resp.encoding = 'utf-8'
			content = resp.content
			movies = re.findall(r'<div class="info">.*?<span class="title">(.*?)</span>.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?</div>', content, re.S)
			for movie in movies:
				director_actor = movie[1].split('<br>')[0].replace('&nbsp;',' ')
				director_actor = re.search(r'导演:(.*?)主演:(.*?)', director_actor, re.S)
				if director_actor:
					director = director_actor.groups(0)
					actor = director_actor.groups(1)
				year_country_type = movie[1].split('<br>')[1].replace('&nbsp;',' ').split('/')
				self._movies.append(Movie(name=movie[0], movie_type=year_country_type[2].replace('\n', ''), year=year_country_type[0], score=movie[2], actor=actor))
			for movie in self._movies:
				print movie

def main():
	Douban().moviesTop250()

if __name__ == '__main__':
	main()		

