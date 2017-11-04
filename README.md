# surge
A math problem generator for my son that gets more difficult as he gets better, powered by a flask restful API.

To start:

```
$ git clone https://github.com/tmthyjames/surge.git
$ cd surge
$ pip install -r requirements.txt
$ psql -f sql/SURGE-#1.sql -d surge
$ python app/app.py
```

The app should now be running on http://localhost:5000
