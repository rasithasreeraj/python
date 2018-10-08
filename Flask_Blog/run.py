from flaskblog import create_app

app = create_app()

#  Inorder to run script without using command 'flask run', but using command 'python filename.py' include the below code
#  if below code is not included, [i.e if we are not using python to run the code,
#  every time we closes and reopen cmd, we need to set the env variables again//* lazy loading
#  flask run command is to be used along with env variables

if __name__ == '__main__':
    app.run(debug=True)
#  https://github.com/realpython/discover-flask  --check out this as well

