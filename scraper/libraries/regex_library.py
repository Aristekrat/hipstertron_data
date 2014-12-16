import re

regex = {
	# Worked but didn't work in my first attempt. The double quotes are properly escaped but it didn't find results.
	links: re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][A^>]*.>"),
	months: re.compile('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec')
}