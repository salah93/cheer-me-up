# cheermeup
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
+ create symbolic link in directory in PATH env variable
```
ln -s cheermup.py /usr/local/bin/cheermeup
```
+ you're all set up :)

## cheer meh up
when you need a good pick-me-up type
```
cheermeup
```

to get a random video you added..


## add videos
```
cheermeup add -t "Title of video" -u "url-of-video"
```

