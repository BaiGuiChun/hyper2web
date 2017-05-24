# Super Fast HTTP2 Framework for Progressive Web Application

# Installation
Clone this project to your local directory. In this directory, 
```
python setup.py
```
This will automatically install `hyper2web` to the associated Python as a site-package.

I will make it available on PyPi once I have the first release.

## Python Version
Python3.5+

## Dependency
This project uses `h2` and `curio`.

[h2 Github](https://github.com/python-hyper/hyper-h2) [doc](https://python-hyper.org/h2/en/stable/)  
[curio Github](https://github.com/dabeaz/curio) [doc](https://curio.readthedocs.io/en/latest/)

# How to
Assuming you have a directory structure like
```
your project/
--public/
  --index.html
  --index.js
  ...
--app.py
```
Your `app.py` looks like
```python
from hyper2web import app

if __name__ == '__main__':

	# A basic callback style API is provided
	# The naming of this function is up to you
	async def post_echo(http, stream):
		# this route essentially echo the data received back to client
		print('data received:')
		print(str(stream.data, encoding='utf8'))
		await http.send_and_end(stream, stream.data)

	app = app.App(port=5000)
	app.post('name', post_echo)
	app.up()
```
Then run this script
```bash
python app.py
```
That's it! If you just want to serve static files, it's just 2 lines!
```python
from hyper2web import app
app.App(port=5000).up()
```

# Test
Python modules/packages and imports are confusing. You have to do
```python
python -m unittest test.The_Name_Of_the_Test_Script
```
under the root directory of this repo.

Or run
```python
python -m unittest discover test
```
to run all tests under `test/` dir.

There could be a better way but I am not sure yet. Again, `import` is confusing in Python once you get into packages.

# Misc
## Why did I create this framework?
April 23rd, 2017, Sunday, I woke up and felt bored and decided to create my own HTTP2 web framework.

Since I had little or some prior web knowledge, this would be a super learning and fun project for me.
