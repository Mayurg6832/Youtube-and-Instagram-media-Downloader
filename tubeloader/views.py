from django.shortcuts import render,redirect
from django.http import HttpResponse
from pytube import YouTube
import os
from django.contrib import messages
from instalooter.looters import PostLooter
# Create your views here.

def index(request):
	return render(request,'tubeloader/index.html')

def insta(request):
	return render(request,'tubeloader/insta.html')
def redir(request):
	return redirect('../instavid')

def get_link(request):
	homedir=os.path.expanduser("~")
	dirs=homedir+'/Downloads'
	if request.method == "POST":
		link=request.POST.get('linkk')
		obj=YouTube(link)
		reso=[]
		strm=obj.streams.first()
		strm.download(homedir+'/Downloads')
		messages.success(request,'video downloaded')
	return redir(request)

def get_insta(request):
	homedir=os.path.expanduser("~")
	dirs=homedir+'/Downloads'
	if request.method=='POST' and 'get_video' in request.POST:
		link=request.POST.get('links')
		PostLooter(link).download_videos(dirs)
	elif request.method=='POST' and 'get_photo' in request.POST:
		link=request.POST.get('links')
		PostLooter(link).download(dirs)
	return redir(request)




