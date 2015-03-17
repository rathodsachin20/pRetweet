import json
import _mysql
import sys
import MySQLdb as mdb
from dateutil.parser import parse
import glob

def create_table():
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tweets \
                     (id VARCHAR(100) PRIMARY KEY, \
                      isRetweeted VARCHAR(6), \
                      tweet_created_at INTEGER, \
                      user_created_at INTEGER, \
                      retweeted VARCHAR(6), \
                      text VARCHAR(500), \
                      retweet_count INTEGER, \
                      followers_count INTEGER, \
                      friends_count INTEGER, \
                      user_mentions INTEGER, \
                      urls_count INTEGER, \
                      hashtags_count INTEGER, \
                      favourites_count INTEGER \
                      );")

        ver = cur.fetchone()
        print "Output Create table: %s " % ver

    except mdb.Error, e:
        print "Error in create %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:        
        if con:    
            con.close()

def insert_row(r):
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
        #print r
        #for s in r:
        #    print unicode(s)
        #cur.execute("INSERT INTO tweets VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8})".format((unicode(s) for s in r)))
        #cur.execute("INSERT INTO tweets VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8})".format(tuple(unicode(s) for s in r)))
        t = tuple(unicode(s).encode('utf-8') for s in r)
        #print t
        cur.execute("INSERT INTO tweets VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ", t)

        #ver = cur.fetchone()
        #print "insert Output : %s"% ver
        con.commit()

    except mdb.Error, e:
        print "Error in insert %d: %s"% (e.args[0],e.args[1])
    finally:        
        if con:    
            con.close()

def drop_table():
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS tweets")

        ver = cur.fetchone()
        print "Output : %s " % ver

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:        
        if con:    
            con.close()


if __name__ == "__main__":
    for fname in glob.glob("*.json"):
        print "file:", fname
        with open(fname) as f:
            data = json.load(f)

        create_table()
        for t in data:
            if 'user' in t:
                if t['user']['lang'] == 'en' and ('retweeted_status' in t):
                    tweet_created_at = int(parse(t['retweeted_status']['created_at']).strftime("%s"))
                    user_created_at = int(parse(t['retweeted_status']['user']['created_at']).strftime("%s"))
                    row = [t['retweeted_status']['id_str'], 'True', tweet_created_at, user_created_at, t['retweeted_status']['retweeted'], t['retweeted_status']['text'], t['retweeted_status']['retweet_count'], t['retweeted_status']['user']['followers_count'], t['retweeted_status']['user']['friends_count'], len(t['retweeted_status']['entities']['user_mentions']),  len(t['retweeted_status']['entities']['urls']),  len(t['retweeted_status']['entities']['hashtags']), t['retweeted_status']['user']['favourites_count']]
                    #print row
                    insert_row(row)
            else:
                print 'No user'
        
        for t in data:
            if 'user' in t:
                if t['user']['lang'] == 'en' and not('retweeted_status' in t):
                    tweet_created_at = int(parse(t['created_at']).strftime("%s"))
                    user_created_at = int(parse(t['user']['created_at']).strftime("%s"))
                    row = [t['id_str'], 'False', tweet_created_at, user_created_at, t['retweeted'], t['text'], t['retweet_count'], t['user']['followers_count'], t['user']['friends_count'], len(t['entities']['user_mentions']),  len(t['entities']['urls']),  len(t['entities']['hashtags']), t['user']['favourites_count']]
                    #print row
                    insert_row(row)
            else:
                print 'No user'




