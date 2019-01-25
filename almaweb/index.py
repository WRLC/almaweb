# route and controller for homepage
from flask import Blueprint, flash, render_template, request, session, url_for

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')

