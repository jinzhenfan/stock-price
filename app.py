from flask import Flask, render_template, request, redirect
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure
import quandl
quandl.ApiConfig.api_key = 'Bc6FchAnNSq7zxfjpZGR'

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

def ticker_input():
  a=request.args.get('a',0,type='str')
  data = quandl.get_table('WIKI/PRICES', ticker = a)
  output_notebook()
  p=figure(title="close price", plot_height=300, plot_width=600)
  r=p.line(range(30),data.tail(30).close,color="#2222aa",line_width=3)
  show(p)
  return p

if __name__ == '__main__':
  app.run(port=33507)
