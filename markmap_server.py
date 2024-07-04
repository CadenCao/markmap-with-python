# -*- coding:utf-8 -*-
# Author:Canden Cao 
# time：2024-06-28

from flask import Flask,request,render_template
import argparse 

app = Flask(__name__)

@app.route('/markmap',methods=['GET'])
def markmap_show():
    markdown=request.args.get('markdown')
    return render_template('markmap_child.html',markdown=markdown)


def argumentParser():
    parser=argparse.ArgumentParser()
    parser.add_argument('--host',default='0.0.0.0',type=str,help='The host of generating markmap')
    parser.add_argument('--port',default=5094,type=int,help='The port of generating markmap')
    args=parser.parse_args()
    return args

if __name__ == "__main__":
    args=argumentParser()
    app.run(host=args.host, port=args.port,debug=True)


