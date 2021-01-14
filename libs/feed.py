"""
feed-reader class
v.1.0
2020 by magiclab

Usage:
  feed.py FEED
  feed.py --help
  feed.py --version

Options:
  FEED                                  RSS Feed             
  --version                             Show version info

"""

from docopt import docopt
import feedparser

class Feed:
    def __init__(self,feed):
        try:
            self.feed = feedparser.parse(feed).entries
        except:
            self.feed = False

    def download(self):
        if self.feed:
            return [{'title':post.title,'href':post.links[0]['href']} for post in self.feed]
        else:
            return False

    def test(self):
        if self.feed:
            for post in self.feed:
                print(post.title,end="\n\n\n")
        else:
            print('something went wrong')

if __name__ == "__main__":
    arguments = docopt(__doc__, version='feed-reader class v.1.0')
    feed = Feed(arguments['FEED'])
    for item in feed.download():
        print('Title:',item['title'])
        print('Path:',item['href'])
