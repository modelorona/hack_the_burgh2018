import botometer

# set up the botometer
mashape_key = 'C0eUvCzWdDmshsbXAnK53fQRJUTtp1Km5x1jsnTQ2tMwIUruEp'
twitter_app_auth = {
    'consumer_key': 'rpmEbImgFwEHzOUFifA1peRcw',
    'consumer_secret': 'agIECASC9skRiOVmanRVJO4XlDbTRk4vGU8a8lPBLl3OybkD6n',
    'access_token': '972495546719010817-mjkyaHgxXExdrUFLfzOtt5F3K1cm0wJ',
    'access_token_secret': '2ylFoxJ5W09JFTfACVtTzmzVOlUX48B1Uao4ktZccmOPQ'
}


# call this with the user url to check its scores
def check_user(id=None, screen_name=None):
    bom = botometer.Botometer(wait_on_ratelimit=True, mashape_key=mashape_key,**twitter_app_auth)
    result = None
    if id is not None:
        # check by user id
        result = bom.check_account(id)
    elif screen_name is not None:
        # check by screen name
        result = bom.check_account(screen_name)
    else:  # some nonsense with the params
        return None

    # content * 2 / 7
    print("original:")
    print(result)
    print()
    print("new average:")
    avg = 0
    for key, value in result['categories'].items():
        if key == 'content':
            avg += 2*value
        avg += value
    print(str(avg/7))
