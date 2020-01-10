# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request 
# import urllib2


#read from queries.txt
f = open('test_queries.txt','r',encoding="utf8")
# print(f.readline())
while True:
    line_text = f.readline()
    if not line_text :  #If line is empty then end of file reached
        break;
    else:
        # process queries one by one--------------------------------
        query = ''
        words = line_text.split()
        qid = words[0]
        for word in words[1:]:
            query = query + word + ' '
        query_args = {'q':query}
        encoded_args = urllib.parse.urlencode(query_args)    

        # change the url according to your own corename and query
        inurl = 'http://18.188.227.39:8983/solr/IRF19P3_dfr/select?defType=edismax&fl=id%2Cscore&' + encoded_args + '&qf=text_en%20text_ru%20text_de&rows=20&wt=json&ps=3'
        # outfn = 'output_bm25_1.txt'
        # outfn = 'output_lm_1.txt'
        outfn = 'output_dfr_1.txt'

        # change query id and IRModel name accordingly
        # IRModel ='default'
        # IRModel ='LM'
        IRModel ='DFR'
        
        outf = open(outfn, 'a+')
        # data = urllib2.urlopen(inurl)
        # if you're using python 3, you should use
        data = urllib.request.urlopen(inurl)

        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            rank += 1
        outf.close()
f.close()