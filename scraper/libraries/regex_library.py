import re

patterns = {
	# Worked but didn't work in my first attempt. The double quotes are properly escaped but it didn't find results.
	"links": re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][A^>]*.>"),
	"months": re.compile('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec'),
	"price": re.compile('\$\d{1,4}(.\d{1,2})?'),
	"urls": re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'),
	"href": re.compile('href=[\'"]?([^\'" >]+)')
}