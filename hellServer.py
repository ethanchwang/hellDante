from pywebio import *
import gensim
from gensim import models
from gensim.models import Word2Vec
import numpy as np
import csv
import hell

def main():
    confession = input.input("confess now!")
    confessionList = confession.split()
    c = hell.finalScore(hell.sim(confessionList, hell.circles))
    output.put_text(f"You have been banished to circle {c} of hell!")

start_server(main, port=8080, debug=True)