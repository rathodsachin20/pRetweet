from sklearn import linear_model
import numpy as np
import MySQLdb as mdb

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

N=7

def plot():
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
        
        cur.execute("Select count(*) from tweets")
        count = long(cur.fetchone()[0])

        cur.execute("Select avg(retweet_count), followers_count from tweets group by followers_count")

        rows = cur.fetchall()
        #print len(rows)
        px = np.empty((0,1))
        py = np.empty((0,1))
        #p = np.zeros(7)
        #p = np.array([1,1,1,1,1,1,1])
        #p = np.array([1,1,1,1,1,1])
        #p = np.ones(6)
        #print p
        xlist = []
        ylist = []
        for row in rows:
            #print row
            #arr = np.array([i for i in row[6:]])
            #print arr
            #px = np.append(px, row[7])
            #py = np.append(py, row[6])
            xlist.append(row[1])
            ylist.append(row[0])
            #p = np.concatenate((p, arr), axis=0)

        px = np.asarray(xlist, dtype=int)
        py = np.asarray(ylist, dtype=int)

#        for i in xrange(10):
#            print px[i], ":", py[i]

        plt.plot(px, py, marker='x', linestyle='..')

        plt.ylabel('#AvgRetweets')
        plt.xlabel('#Followers')
        plt.title('#AvgRetweets vs #Followers')
        txt = "Total #Tweets: " + str(count)
        plt.text(1,1, txt)
        #plt.show()
        plt.savefig('./retweets-followers.png')

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
    finally:        
        if con:    
            con.close()


if __name__ == "__main__":
    plot()
