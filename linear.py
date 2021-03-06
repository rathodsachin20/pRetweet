from sklearn import linear_model
import numpy as np
import MySQLdb as mdb

from sklearn.preprocessing import scale

N=6

def linear():
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
#        cur.execute("Select * from tweets where retweet_count>0")
        cur.execute("Select * from tweets LIMIT 20000")

        rows = cur.fetchall()
        #print len(rows)
        #p = np.empty((0,7))
        #p = np.zeros(7)
        #p = np.array([1,1,1,1,1,1,1])
        #p = np.array([1,1,1,1,1,1])
        #p = np.ones(6)
        #target = np.ones(1)
        p = np.empty((0,N))
        target = np.empty((0,1))
        print p
        rowlist = []
        targetlist = []
        rowlist.append((0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
        targetlist.append(0.0)
        for row in rows:
            #print row
            #arr = np.array([i for i in row[7:]])
            #print arr
            #p = np.append(p, arr)
            rowlist.append(row[7:])
            #target = np.append(target, row[6])
            targetlist.append(row[6])
            #p = np.concatenate((p, arr), axis=0)
        #p = np.reshape(p, (len(p)/N, N) )
        rowlist = scale(rowlist)
        targetlist = scale(targetlist)
        print "converting list to nparray"
        p = np.asarray(rowlist, dtype=int)
        target = np.asarray(targetlist, dtype=int)
        col = ["followers_count","friends_count","user_mentions","urls_count","hashtags_count","favourites_count"]
        print "converted"
        print "dimentions:", p.shape
        clf = linear_model.LinearRegression()
        #target = np.reshape(target, len(target), 1)
        print p.shape
        print target.shape
        print target
        clf.fit (p, target)
        print "Factors:" , col
        print "Coeff:", clf.coef_

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
    finally:        
        if con:    
            con.close()


if __name__ == "__main__":
    linear()
