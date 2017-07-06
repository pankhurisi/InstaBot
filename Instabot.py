import requests
import urllib

APP_ACCESS_TOKEN = '1943018362.461a955.12a586002daf46859def8db521710a5f'
# Token Owner: pankhurisingh
BASE_URL = 'https://api.instagram.com/v1/'


# Function declaration for self info
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % APP_ACCESS_TOKEN
    print 'GET request url : %s' % request_url
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


# Function declaration for getting other user's id by username
def get_other_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


# Function declaration to get information of a user by username
def get_other_user_info(insta_username):
    other_user_id = get_other_user_id(insta_username)
    if other_user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (other_user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'


# Function declaration to get my recent post
def get_my_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % APP_ACCESS_TOKEN
    print 'GET request url : %s' % request_url
    my_media = requests.get(request_url).json()
    if my_media['meta']['code'] == 200:
        if len(my_media['data']):
            image_name = my_media['data'][0]['id'] + '.jpeg'
            image_url = my_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'
    return None


# Function declaration to get other user's recent post
def get_other_users_post(insta_username):
    other_user_id = get_other_user_id(insta_username)
    if other_user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (other_user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    other_user_media = requests.get(request_url).json()

    if other_user_media['meta']['code'] == 200:
        if len(other_user_media['data']):
            image_name = other_user_media['data'][0]['id'] + '.jpeg'
            image_url = other_user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print "Post does not exist!"
    else:
        print "Status code other than 200 received!"
    return None


# Function declaration to get id of recent post by the other user
def get_other_user_post_id(insta_username):
    other_user_id = get_other_user_id(insta_username)
    if other_user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (other_user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    other_user_media = requests.get(request_url).json()

    if other_user_media['meta']['code'] == 200:
        if len(other_user_media['data']):
            return other_user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


# Function declaration to like recent post of other user
def like_post_of_other_user(insta_username):
    media_id = get_other_user_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % media_id
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % request_url
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'


# Function declaration to get the recent post liked by me
def post_liked():
    request_url = (BASE_URL + 'users/self/media/liked?access_token=%s') % APP_ACCESS_TOKEN
    print 'GET request url : %s' % request_url
    my_media = requests.get(request_url).json()
    if my_media['meta']['code'] == 200:
        if len(my_media['data']):
            print "Media liked by me:" + my_media['data'][0]['images']['standard_resolution']['url']
        else:
            print 'Post does not exist!'
    else:
        print "request not valid!"


# Function declaration to get the list of likes on recent post of other user
def get_list_of_likes(insta_username):
    media_id = get_other_user_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    like_info = requests.get(request_url).json()

    if like_info['meta']['code'] == 200:
        if len(like_info['data']):
            for x in range(0, len(like_info['data'])):
                print like_info['data'][x]['username']
        else:
            print "no likes yet!"
    else:
        print 'Status code other than 200 received!'


# Function declaration to comment on a recent post of other user
def post_comment(insta_username):
    media_id = get_other_user_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % media_id
    print 'POST request url : %s' % request_url

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
        print "Unable to add comment. Try again!"


# Function declaration to get list of comments on recent post of other user
def get_list_of_comments(insta_username):
    media_id = get_other_user_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                print "comment: %s || User: %s" % (comment_info['data'][x]['text'],
                                                   comment_info['data'][x]['from']['username'])
        else:
            print "no comments yet!"
    else:
        print 'Status code other than 200 received!'


def start_bot():
    while True:
        print '\n'
        print 'Welcome to InstaBot! '
        print 'Menu:'
        print "a.Get my details\n"
        print "b.Get details of a other user using username of the user\n"
        print "c.Get my recent post\n"
        print "d.Get recent post of other user using username\n"
        print "e.Like the recent post of other user using username\n"
        print "f.Make a comment on the recent post of other user using username\n"
        print "g.get my recent liked media\n"
        print "h.Get list of comments on recent post of a user using username\n"
        print "i.Get list of likes on recent post of a user using username\n"
        print "j.Exit"

# nested loop
        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_other_user_info(insta_username)
        elif choice == "c":
            get_my_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_other_users_post(insta_username)
        elif choice == "e":
            insta_username = raw_input("Enter the username of the user: ")
            like_post_of_other_user(insta_username)
        elif choice == "f":
            insta_username = raw_input("Enter the username of the user: ")
            post_comment(insta_username)
        elif choice == "g":
            post_liked()
        elif choice == "h":
            insta_username = raw_input("Enter the username of the user: ")
            get_list_of_comments(insta_username)
        elif choice == "i":
            insta_username = raw_input("Enter the username of the user: ")
            get_list_of_likes(insta_username)
        elif choice == "j":
            exit()
        else:
            print "wrong choice"

start_bot()
