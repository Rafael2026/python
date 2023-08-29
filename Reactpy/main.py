from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def HelloWorld():
  return html.div('Hello World')


app = FastAPI()
configure(app, HelloWorld)