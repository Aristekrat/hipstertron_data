print("Now running scraper")

exec(compile(open('scraper/site_specific/ogden.py', "rb").read(), 'ogden.py', 'exec'))
exec(compile(open('scraper/site_specific/gothic.py', "rb").read(), 'gothic.py', 'exec'))
#exec(compile(open('scraper/site_specific/fillmore.py', "rb").read(), 'fillmore.py', 'exec'))
exec(compile(open('scraper/site_specific/bluebird.py', "rb").read(), 'bluebird.py', 'exec'))
exec(compile(open('scraper/site_specific/first_bank.py', "rb").read(), 'first_bank.py', 'exec'))
exec(compile(open('scraper/site_specific/red_rocks.py', "rb").read(), 'red_rocks.py', 'exec'))
exec(compile(open('scraper/site_specific/paramount.py', "rb").read(), 'paramount.py', 'exec'))
exec(compile(open('scraper/site_specific/fiddlers_green.py', "rb").read(), 'fiddlers_green.py', 'exec'))
exec(compile(open('scraper/site_specific/fox.py', "rb").read(), 'fox.py', 'exec'))
exec(compile(open('scraper/site_specific/pepsi_center_selenium.py', "rb").read(), 'pepsi_center_selenium.py', 'exec'))

print("Scrape completed")