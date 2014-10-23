import os

if os.environ['DEV_ENV'] == 'production':
	prefix = 'scraper/site_specific/'
elif os.environ['DEV_ENV'] == 'local':
	prefix = 'scraper/site_specific/'

exec(compile(open(prefix + 'gothic.py', "rb").read(), 'gothic.py', 'exec'))
exec(compile(open(prefix + 'fillmore.py', "rb").read(), 'fillmore.py', 'exec'))
exec(compile(open(prefix + 'firstbank.py', "rb").read(), 'firstbank.py', 'exec'))
exec(compile(open(prefix + 'bluebird.py', "rb").read(), 'bluebird.py', 'exec'))
exec(compile(open(prefix + 'ogden.py', "rb").read(), 'ogden.py', 'exec'))
exec(compile(open(prefix + 'red_rocks.py', "rb").read(), 'red_rocks.py', 'exec'))
exec(compile(open(prefix + 'pepsi_center.py', "rb").read(), 'pepsi_center.py', 'exec'))
exec(compile(open(prefix + 'paramount.py', "rb").read(), 'paramount.py', 'exec'))
#exec(compile(open(prefix + 'fiddlers_green.py', "rb").read(), 'fiddlers_green.py', 'exec')) This one needs to be updated before reintegration
exec(compile(open(prefix + 'fox.py', "rb").read(), 'fox.py', 'exec'))