import os

os.system("python3 get_selenium_source.py gothic")
os.system("python3 get_selenium_source.py ogden")
os.system("python3 get_selenium_source.py bluebird")
os.system("python3 get_selenium_source.py first_bank")

os.system("python3 get_bs4_source.py fillmore")
os.system("python3 get_bs4_source.py fox")
os.system("python3 get_bs4_source.py paramount")
os.system("python3 get_bs4_source.py pepsi_center")
os.system("python3 get_bs4_source.py red_rocks")

print ("All source files created")