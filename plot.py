from sklearn import linear_model
import numpy as np
import MySQLdb as mdb
import plotly.plotly as ply
from plotly.graph_objs import *

ply.sign_in('rathodsachin20', 'z83geaui8i')

N=7

def plot():
    try:
        con = mdb.connect('localhost', 'root', '', 'pretweet');

        cur = con.cursor()
        cur.execute("Select * from tweets where retweet_count>0")

        rows = cur.fetchall()
        #print len(rows)
        px = np.empty((0,1))
        py = np.empty((0,1))
        #p = np.zeros(7)
        #p = np.array([1,1,1,1,1,1,1])
        #p = np.array([1,1,1,1,1,1])
        #p = np.ones(6)
        #print p
        for row in rows:
            #print row
            #arr = np.array([i for i in row[6:]])
            #print arr
            px = np.append(px, row[7])
            py = np.append(py, row[6])
            #p = np.concatenate((p, arr), axis=0)
        
        for i in xrange(10):
            print px[i], ":", py[i]
        data = Data([Histogram( x=px, y=py )])
        layout = Layout(title='#Followers and retweets', xaxis=XAxis(title='#followers' ), yaxis=YAxis( title='#retweets') )
        fig = Figure(data=data, layout=layout)

        plot_url = ply.plot(fig, filename='horizontal-histogram')


    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
    finally:        
        if con:    
            con.close()


if __name__ == "__main__":
    plot()
