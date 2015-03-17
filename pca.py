import numpy as np
from sklearn.decomposition import PCA

import MySQLdb as mdb

#np.seterr(divide='ignore', invalid='ignore')
N=7

def pca():
    try:
        con = mdb.connect('localhost', 'xsiena', 'xsiena', 'pretweet');

        cur = con.cursor()
        cur.execute("Select * from tweets")

        rows = cur.fetchall()
        #print len(rows)
        p = np.empty((0,N))
        #p = np.zeros(7)
        #p = np.array([1,1,1,1,1,1,1])
        #p = np.array([1,1,1,1,1,1,1])
        print p
        count = 0
        rowlist = []
        for row in rows:
            #print row
            #arr = np.array([i for i in row[6:]])
            #print arr
            #p = np.append(p, arr)
            #p = np.vstack([p, arr])
            #p = np.vstack([p, row[6:]])
            rowlist.append(row[6:])
            count += 1
            if count%10000 == 0:
                print "appended ", count
            #p = np.concatenate((p, arr), axis=0)
        #p = np.reshape(p, (len(p)/N, N) )
        print "converting list to nparray"
        p = np.asarray(rowlist, dtype=int)
        print "converted"
        print "dimentions:", p.shape
        pca = PCA(n_components=N)
        print pca.fit(p)
        print "Variances:"
        print(pca.explained_variance_ratio_)
        print(pca.components_)

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        #sys.exit(1)
    finally:        
        if con:    
            con.close()


if __name__ == "__main__":
    pca()
