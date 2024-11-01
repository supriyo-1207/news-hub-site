from config.constant import Constants
from flask import (
    Flask,Blueprint,render_template, request,session,redirect,url_for,flash,jsonify
)
from model.auth_model import Auth
from database.db_connection import db
import os
import requests

from utility_function.utility import dec_fun

page=Blueprint('page',__name__)

apikey=os.getenv( "NEWS_API_KEY" )

@page.route('/home')
@dec_fun()
def home():
    return render_template('index.html',title='Home Page')



@page.route('/get_breaking_news')
def get_breaking_news():
    try:
        url=f'{Constants.BASE_URL}/top-headlines?country=us&apiKey={apikey}'
        response = requests.get(url)
        
        if response.status_code == 200:
            news_data = response.json()
            top_news_data = news_data['articles'][:3]  # Get only the top 3 articles
            print(top_news_data)
            return jsonify({"top_news": top_news_data}), 200
        else:
            return jsonify({"error": "Failed to retrieve news data"}), 500
        
    except Exception as e: 
        print(str(e))
        return jsonify({"error": "An error occurred"}), 500



@page.route('/get_articals')
def get_articals():

    try:
        url=f'{Constants.BASE_URL}/top-headlines?country=us&apiKey={apikey}'
        response = requests.get(url)
        
        if response.status_code == 200:
            news_data = response.json()
            return jsonify(news_data=news_data), 200
        else:
            return jsonify({"error": "Failed to retrieve news data"}), 500
        
    except Exception as e: 
        print(str(e))
        return jsonify({"error": "An error occurred"}), 500


@page.route('/blog')
@dec_fun()
def blog():
    
    # Render the blog page template with empty news data
    return render_template('blog.html',title='Blog Page')


@page.route('/get_news')
def get_news():

    try:
        url = f"{Constants.BASE_URL}everything?q=all&apiKey={apikey}"
        response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            return jsonify(news_data=news_data), 200
        else:
            return jsonify({"error": "Failed to retrieve news data"}), 500
    except Exception as e:
        print(str(e))
        return jsonify({"error": "An error occurred"}), 500


# contact page --------------------------------------------------------

@page.route('/contact')
@dec_fun()
def contact():
    return render_template('contact.html',title='Contact Page')


@page.route('/contact-message',methods=['POST'])
def contact_message():
    form_data=request.get_json()
    print("form_data",form_data)