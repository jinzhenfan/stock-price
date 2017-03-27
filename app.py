from flask import Flask, render_template, request, redirect

from bokeh.io import push_notebook, show, output_notebook

from bokeh.layouts import row

from bokeh.plotting import figure

from bokeh.embed import components

from bokeh.util.string import encode_utf8

import quandl

quandl.ApiConfig.api_key = 'Bc6FchAnNSq7zxfjpZGR'



app = Flask(__name__)



@app.route('/')

def main():

  return redirect('/index')

@app.route('/index')

def index():
    return render_template('index.html')
  

@app.route('/graph',methods = ['POST', 'GET'])
def graph():
    if request.method == 'POST':
          #a=request.args.get('a',0,type=str)
          a = request.form['text']
          print a
          data = quandl.get_table('WIKI/PRICES', ticker = a)  
          #output_notebook()
          print (data.head(5))
          p=figure(title=a, plot_height=300, plot_width=600,x_axis_label='date',x_axis_type='datetime')
          r=p.line(data.tail(30).date,data.tail(30).close,color="#2222aa",line_width=3)
          #html = file_html(p, CDN, "my plot")
          script,div=components(p)
          html = render_template('graph.html',script=script, div=div)
          return encode_utf8(html) #render_template('index.html')



#@app.route('/graph')
#def graph():
  #data = quandl.get_table('WIKI/PRICES', ticker = 'GOOG')
  #p=figure(title="close price", plot_height=300, plot_width=600)
  #r=p.line(range(30),data.tail(30).close,color="#2222aa",line_width=3)
  #script,div=components(p)
 # html = render_template('graph.html',script=script, div=div)
  #return encode_utf8(html) #render_template('index.html')


if __name__ == '__main__':

  #app.run(port=33507)

  app.run(port=33507)




