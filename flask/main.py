from flask import twitter, db
import sys
import subprocess

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No argument given")
    else:
        # assume two arguments, whether id or screen name
        if sys.argv[1] == '-id':
            twitter.check_user(id=int(sys.argv[2]))
        elif sys.argv[1] == '-sc':
            twitter.check_user(screen_name=str(sys.argv[2]))
        elif sys.argv[1] == '-gs':
            file = open('params.txt', 'w')  # will contain the parameter to run
            file.write(str(sys.argv[2]))
            file.close()
            command = 'python gsearch.py'
            subprocess.call(command.split())
            # output, error = process.communicate()
            opt = open('gsr.txt', 'r')
            for line in opt:
                print(db.find_in_db(line))
        elif sys.argv[1] == '-d':
            # check the domain age of the given site url
            pass
        else:
            print("Fail")

# get the link
# google search it
# get all the results
# compare them to all bad fake sites in database

