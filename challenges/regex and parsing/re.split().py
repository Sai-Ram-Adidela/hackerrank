"""
Title     : Re.Split()
Subdomain : HackerRank/Python3/Challenges/Regex and Parsing
Domain    : Python3
Author    : Sai Ram Adidela
Created   : 23 Sep 2019
"""
regex_pattern = r"['.,']"

import re
print("\n".join(re.split(regex_pattern, input())))
