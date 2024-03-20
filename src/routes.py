from src import app
from flask import Flask, request, jsonify, render_template, redirect, flash, url_for

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/missions", methods=["GET"])
def mission():
    return render_template("missions.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/conferences", methods=["GET"])
def conferences():
    return render_template("conferences.html")


@app.route("/proposals", methods=["GET"])
def proposals():
    return render_template("proposals.html")


@app.route("/tools", methods=["GET"])
def tools():
    return render_template("tools.html")