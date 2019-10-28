import sys
sys.path.append('https://danieljabailey.github.io/timex_extractor_demo/Lib/site-packages')
from browser import bind, self

from regex_parser import find_timexes as re_find_timexes
from regex_data import timex_res, anti_timex_res
from bayes_extractor import find_timexes as bayes_find_timexes
from bayes_data import get_tables as bayes_tables

def run_regex(toks):
    s = [{'token':t} for t in toks]
    result = re_find_timexes(s, timex_res, anti_timex_res, quiet=True)
    return result

def run_bayes(toks):
    s = [{'token':t} for t in toks]
    result = bayes_find_timexes(s, 0.13, bayes_tables())
    return result

@bind(self, "message")
def message(evt):
    c, *data = evt.data
    if c == 'run':
        toks = data[0]
        result = run_bayes(toks)
        self.send(['bayes', toks, result])
        result = run_regex(toks)
        self.send(['regex', toks, result])

self.send(["loaded"])
