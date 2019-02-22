import facebook # pip install facebook-sdk
import json
import networkx as nx # pip install networkx
import requests # pip install requests
from networkx.readwrite import json_graph
from collections import Counter
from functools import reduce
import operator
#from MyPackages import *


token = '' #貼上token
graph = facebook.GraphAPI(access_token = token)
me_info = graph.get_object('me')
print ('我的Facebook名字是：', me_info['name']) #key為name，取出該key之value


url = 'https://graph.facebook.com/%s?fields=posts.limit(100)&access_token=%s'
r = requests.get(url % ( 'me' , token,) )
response = json.loads(r.content)
#posts = graph.get_connections(id = 'me', connection_name = 'posts',limit=100)

likes_list = []
comments_list = []
message=[]
if response.get('posts'): #have posts
    for post in response['posts']['data']:
        pid = post['id'] #get the post id
    
        #取出文章
        if 'message' in post:
            print ('時間：', post['created_time'])

            message.append(post['message'])
            print ('內容：', post['message']+'\n')

            #取出留言
            url2 = 'https://graph.facebook.com/%s?fields=comments.limit(5)&access_token=%s'
            r2 = requests.get(url2 % (pid, token,) )
            response2=json.loads(r2.content)

            if response2.get('comments'): #have commetns
                comments_list = []
                for comment in response2['comments']['data']:
                    if 'message' in comment:
                        #print ('留言者',comment['name'])
                        #print ('時間：', comment['created_time'])

                        comments_list.append(comment['message'])
                        #print ('內容：', comment['message'])
                #print("共有"+str(len(comments_list))+"則回應")

                
                        #讀出讚數
                        url3 = 'https://graph.facebook.com/%s?fields=likes.limit(5)&access_token=%s'
                        r3 = requests.get(url3 % (pid, token,) )
                        response3=json.loads(r3.content)

                        if response3.get('likes'): #have likes
                            likes_list = []
                            for like in response3['likes']['data']:
                                if 'name' in like:
                                    likes_list.append(like['name'])
                                    #print('按讚者',like['name'])
                        print("共有"+str(len(likes_list))+"個讚")
                        print("共有"+str(len(comments_list))+"則回應\n")
                
print("共有"+str(len(message))+"篇貼文")

