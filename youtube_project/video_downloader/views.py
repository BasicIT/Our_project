from django.shortcuts import render
from django.http import HttpResponse
from apiclient.discovery import build
import urllib.request
import cgi
import json
from youtube_search import YoutubeSearch

# Create your views here.

api_key = 'AIzaSyCurwIFtb9Mv0VRgWVaNlpQZ_PwwJ326XY'

def home(request):
	return render(request, 'video_downloader/index.html')

def search(request):

	# searcht=self.request.url
	path_info = request.META.get('QUERY_STRING')
	input_ = path_info.rsplit('=', 1)[1]
	result=YoutubeSearch(input_,max_results=20).to_json()
	data = json.loads(result)
	
	x = len(data["videos"])
	# l = []
	# for i in range(15):
		

	# 	title = data["videos"][i]["title"]
	# 	l.append(title)
	# 	# thumbnail = data["videos"][i]["thumbnails"][0]
	# 	# l.append(thumbnail)
	
	# k = []
	# for i in range(15):
	# 	thumbnail = data["videos"][i]["thumbnails"][0]
	# 	k.append(thumbnail)


	content={'results': data["videos"]
		}		
		


	# content = json.load(results)
	# api_key = 'AIzaSyCurwIFtb9Mv0VRgWVaNlpQZ_PwwJ326XY'
	# youtube = build('youtube', 'v3', developerKey=api_key)
	# req = youtube.search().list(q=input_, part='snippet', type='video', maxResults=20)
	return render(request, 'video_downloader/searched.html', content)
	# return HttpResponse(l)
