# import os

print("Now running scraper")

# if os.environ['DEV_ENV'] == 'production':
# 	prefix = 'scraper/site_specific/'
# elif os.environ['DEV_ENV'] == 'local':
# 	prefix = 'scraper/site_specific/'

exec(compile(open('scraper/site_specific/gothic_alt.py', "rb").read(), 'gothic_alt.py', 'exec'))
exec(compile(open('scraper/site_specific/fillmore.py', "rb").read(), 'fillmore.py', 'exec'))
exec(compile(open('scraper/site_specific/firstbank_alt.py', "rb").read(), 'firstbank_alt.py', 'exec'))
exec(compile(open('scraper/site_specific/bluebird_alt.py', "rb").read(), 'bluebird_alt.py', 'exec'))
exec(compile(open('scraper/site_specific/ogden_alt.py', "rb").read(), 'ogden_alt.py', 'exec'))
exec(compile(open('scraper/site_specific/red_rocks.py', "rb").read(), 'red_rocks.py', 'exec'))
exec(compile(open('scraper/site_specific/pepsi_center.py', "rb").read(), 'pepsi_center.py', 'exec'))
exec(compile(open('scraper/site_specific/paramount.py', "rb").read(), 'paramount.py', 'exec'))
#exec(compile(open(prefix + 'fiddlers_green.py', "rb").read(), 'fiddlers_green.py', 'exec')) This one needs to be updated before reintegration
exec(compile(open('scraper/site_specific/fox.py', "rb").read(), 'fox.py', 'exec'))

print("Scrape completed")