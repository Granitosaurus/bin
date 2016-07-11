#!/bin/python3
import os
import subprocess
import requests
from parsel import Selector
from urllib.parse import urljoin

"""
Checks stackoverflow for new topics
"""

HISTORY_FILENAME = os.path.expanduser('~/.so_check_history')


class Notify:

    def find_latest(self, count=3):
        resp = requests.get('http://stackoverflow.com/questions/tagged/scrapy')
        sel = Selector(text=resp.text)
        questions = sel.xpath("//div[@id='questions']/div")[:count]
        for q in questions:
            qid = q.xpath('@id').re('\d+')[0]
            if self.check_id(qid):
                continue
            title = q.xpath(".//h3/a/text()").extract_first('')
            url = "http://stackoverflow.com/questions/{}".format(qid)
            subprocess.Popen(['/home/dex/bin/cron_notify', title, url])
            self.write_id(qid)

    @staticmethod
    def check_id(qid):
        if not os.path.isfile(HISTORY_FILENAME):
            return False
        with open(HISTORY_FILENAME, 'r+') as f:
            return qid in f.read()

    @staticmethod
    def write_id(qid):
        with open(HISTORY_FILENAME, 'a+') as f:
            f.write('{}\n'.format(qid))


if __name__ == '__main__':
    notifier = Notify()
    notifier.find_latest()
