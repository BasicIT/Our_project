from django.shortcuts import render
from django.http import HttpResponse
from apiclient.discovery import build
import urllib.request
import cgi
from youtube_search import YoutubeSearch
# Create your views here.

api_key = 'AIzaSyCurwIFtb9Mv0VRgWVaNlpQZ_PwwJ326XY'

def home(request):
	return render(request, 'video_downloader/index.html')

def search(request):

	# searcht=self.request.url
	path_info = request.META.get('QUERY_STRING')
	input_ = path_info.rsplit('=', 1)[1]
	results=YoutubeSearch(input_,max_results=20).to_json()

	# api_key = 'AIzaSyCurwIFtb9Mv0VRgWVaNlpQZ_PwwJ326XY'
	# youtube = build('youtube', 'v3', developerKey=api_key)
	# req = youtube.search().list(q=input_, part='snippet', type='video', maxResults=20)
	return HttpResponse(results)
	# return render(request, 'video_downloader/index.html')
