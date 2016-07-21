# cheermeup
## Requirements
+ python3.4+
+ sqlite3 (comes with python)

## Steps::
+ At terminal prompt type 
```
sqlite3 "funny.db"
```
+ In the sqlite-shell type
```
create table videos(title text, url text);
``` 
+ Go back to terminal prompt (ctrl+c)
+ to make the program executable change permissions
```
chmod 700 cheermup.py
```
+ create link to file in directory in PATH env variable
```
ln cheermup.py /usr/local/bin/cheerup
```
+ you're all set up :)

## cheer meh up
when you need a good pick-me-up type
```
cheerup
```

to get a random video you added..


## add videos
```
cheerup add -t "Title of video" -u "url-of-video"
```

