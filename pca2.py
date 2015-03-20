import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import RandomizedPCA
from sklearn.preprocessing import scale

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import MySQLdb as mdb

#np.seterr(divide='ignore', invalid='ignore')
N=7

def pca():
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
        cur.execute("Select * from tweets LIMIT 20000")

        rows = cur.fetchall()
        #print len(rows)
        p = np.empty((0,N))
        #p = np.zeros(7)
        #p = np.array([1,1,1,1,1,1,1])
        #p = np.array([1,1,1,1,1,1,1])
        print p
        count = 0
        rowlist = []
        rowlist.append((0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
        for row in rows:
            #print row
            #arr = np.array([i for i in row[6:]])
            #print arr
            #p = np.append(p, arr)
            #p = np.vstack([p, arr])
            #p = np.vstack([p, row[6:]])
            rowlist.append(row[6:])
            count += 1
            if count%100000 == 0:
                print "appended ", count
            #p = np.concatenate((p, arr), axis=0)
        for i in xrange(10):
            print rowlist[i]
        rowlist = scale(rowlist)
        for i in xrange(10):
            print rowlist[i]
        print "converting list to nparray"
        p = np.asarray(rowlist, dtype=int)
        print "converted"
        print "dimentions:", p.shape
        #pca = PCA(n_components=N)
        #pca = RandomizedPCA(n_components=3)
        pca =PCA(n_components=3)
        pca.fit(p)
        print "Variances:"
        print(pca.explained_variance_ratio_)
        print "PCA components:"
        print(pca.components_)


        col = np.asarray(["retweet_count","followers_count","friends_count","user_mentions","urls_count","hashtags_count","favourites_count"])
        px = np.asarray(pca.components_[0], dtype=float)
        py = np.asarray(pca.components_[1], dtype=float)
        pz = np.asarray(pca.components_[2], dtype=float)
        
        #plt.subplot(2, 1, 1)
        """
        plt.plot(px, py, marker='x', linestyle='..')
        ax = plt.axes()
        for x, y, c in zip(px,py,col):
            ax.arrow(0, 0, x, y, head_width=0.01, head_length=0.05, fc='k', ec='k', label=c)
            plt.annotate(c, xy=(x, y), xytext=(x, y), arrowprops=dict(facecolor='black', shrink=0.05),)
        plt.savefig('./pca-0vs1.png')
        """

        #plt.subplot(2, 1, 2)
        plt.plot(px, pz, marker='o', linestyle='..')
        ax = plt.axes()
        for x, z, c in zip(px,pz,col):
            ax.arrow(0, 0, x, z, head_width=0.01, head_length=0.05, fc='k', ec='k', label=c)
            plt.annotate(c, xy=(x, z), xytext=(x, z), arrowprops=dict(facecolor='black', shrink=0.05),)
        plt.savefig('./pca-0vs2.png')


    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        #sys.exit(1)
    finally:        
        if con:    
            con.close()


if __name__ == "__main__":
    pca()
