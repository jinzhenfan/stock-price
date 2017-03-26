from flask import Flask, render_template, request, redirect
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure
from bokeh.embed import components

import quandl
quandl.ApiConfig.api_key = 'Bc6FchAnNSq7zxfjpZGR'

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/_ticker_input')
def ticker_input():
  a=request.args.get('a',0,type='str')
  print a
  data = quandl.get_table('WIKI/PRICES', ticker = a)
  #output_notebook()
  print (data.head(5))
  p=figure(title="close price", plot_height=300, plot_width=600)
  r=p.line(range(30),data.tail(30).close,color="#2222aa",line_width=3)
  #html = file_html(p, CDN, "my plot")
  script,div=components(p)
  return render_template('grpah.html',script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)
