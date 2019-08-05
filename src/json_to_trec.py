# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
#import urllib.request 
import urllib2


with open("testqueries.txt", "r") as ins:
    array = []
    myFlag = True;
    
    for line in ins:

        # change the url according to your own corename and query
        if myFlag == True:
            line = line[3:len(line)]
            myFlag = False
        line = line.strip()
        
        print line
        inurl = 'http://localhost:8983/solr/VSM/select?q=' + line +'&defType=dismax&qf=tweet_urls^0.0%20+tweet_hashtags^0.5%20+text_en^2.0%20+%20text_de^2.0%20+%20text_ru^2.0&fl=id%2Cscore&wt=json&indent=true&rows=20'
        print inurl
        outfn = 'path_to_your_file64.txt'


        # change query id and IRModel name accordingly
        qid = line[0:3]
        print qid
        IRModel='VSM'
        outf = open(outfn, 'a+')
        data = urllib2.urlopen(inurl)
        # if you're using python 3, you should use
        # data = urllib.request.urlopen(inurl)

        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            rank += 1
        outf.close()
