######
#useful videos on this topic:
# basic classes: https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# Python Objects (4 Parts): https://www.youtube.com/watch?v=u9xZE5t9Y30
# Part 4 goes into the concept of inheritance which is also used here
# abstract classes: https://www.youtube.com/watch?v=PDMe3wgAsWg

from abc import ABCMeta, abstractmethod

# this code was there:
class Book(object, metaclass=ABCMeta): # create class
    def __init__(self,title,author):
        self.title=title # assign title to title
        self.author=author # assign author to author
    @abstractmethod
    def display(): pass # this means that we HAVE TO implement a display method
    # into the subclass MyBook

# this code is new:
#Write MyBook class
class MyBook(Book): # this includes the above class Book (Inheritance)
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self): # don't forget the "self" in parantheses!
        print("Title: " + title + "\nAuthor: " + author + "\nPrice: " + str(price))



###
#this code was there:
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
