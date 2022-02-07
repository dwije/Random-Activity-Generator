'''     1. read urls from JSON file from takeout
        2. Obtain video ids from url by splitting the string after '=' until end of string
        unless there is a timestamp afterwards
        3. extract tags from each video using .list and place them into a data structure
'''

from googleapiclient.discovery import build
import json

api_key = 'AIzaSyDeU0YQ9g623MmQsjQ9lyg9wR-pkhMIssY'

youtube = build('youtube','v3',developerKey = api_key)

with open('/home/ankit/Downloads/Takeout/YouTube and YouTube Music/history/watch-history.json') as file:
    data = json.load(file)

id_array = []
counter = 0
for item in data:
    identity = item['titleUrl'][-11:]
    id_array.append(identity)
    if counter == 48:
        break
    counter+=1


#print(id_array)
print()

request = youtube.videos().list(
    part = 'snippet',
    id = id_array
    )
response = request.execute()

categorieIDs = []
tags = []
counter = 0
for video_info in response['items']:
    video_cat = video_info['snippet']['categoryId']
    categorieIDs.append(video_cat)
    if counter != 14 and counter != 17 and counter != 28 and counter != 43:
        tag_cat = video_info['snippet']['tags'][0:3]
        #print(tag_cat)
        tags.append(tag_cat)
    if counter == 48:
        break
    counter+=1

#print(categorieIDs)
#print()

cat_counts = {1: 0, 2: 0, 10: 0, 15: 0, 17: 0, 19: 0, 20: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0}
for id in categorieIDs:
    cat_counts[int(id)] += 1

#print(cat_counts)

max_num = 0
selected_cat = 0
for num in cat_counts:
    if cat_counts[num] > max_num:
        max_num = cat_counts[num]
        selected_cat = num

print('Frequency of most watched category: %d' %(max_num))
cat_name = ''

if selected_cat == 1:
    cat_name = 'Film and Animation'
elif selected_cat == 2:
    cat_name = 'Autos and Vehicles'
elif selected_cat == 10:
    cat_name = 'Music'
elif selected_cat == 15:
    cat_name = 'Pets and Animals'
elif selected_cat == 17:
    cat_name = 'Sports'
elif selected_cat == 19:
    cat_name = 'Travel and Events'
elif selected_cat == 20:
    cat_name = 'Gaming'
elif selected_cat == 22:
    cat_name = 'People and Blogs'
elif selected_cat == 23:
    cat_name = 'Comedy'
elif selected_cat == 24:
    cat_name = 'Entertainment'
elif selected_cat == 25:
    cat_name = 'News and Politics'
elif selected_cat == 26:
    cat_name = 'How to and Style'
elif selected_cat == 27:
    cat_name = 'Education'
elif selected_cat == 28:
    cat_name = 'Science and Technology'
elif selected_cat == 29:
    cat_name = 'Nonprofits and Activism'

print('Most watched category: %s'%(cat_name))

tag_counts = {}

tagslist = []
for tagl in tags:
    for tag in tagl:
        tagslist.append(tag)

#print(tagslist)
for tag in tagslist:
    counter = 0
    for tag2 in tagslist:
        if tag == tag2:
            counter+=1
    tag_counts[tag] = counter

max_num = 0
max_tag = ''
for tag in tag_counts:
    if tag_counts[tag] > max_num:
        max_num = tag_counts[tag]
        max_tag = tag

print('Frequency of most watched tag: %s' %(max_num))
print('Most watched tag: %s'%(max_tag))


