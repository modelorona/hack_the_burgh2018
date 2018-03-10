import twitter
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No argument given")
    else:
        # assume two arguments, whether id or screen name
        if sys.argv[1] == '-id':
            twitter.check_user(id=int(sys.argv[2]))
        elif sys.argv[1] == '-screen':
            twitter.check_user(screen_name=str(sys.argv[2]))
        else:
            print("Fail")

