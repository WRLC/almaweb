# routes/controllers for item operations
from flask import Blueprint, flash, render_template, request, session, url_for
from almaweb.utils import get_message

bp = Blueprint('item', __name__, url_prefix='/item')


@bp.route('/')
def item_root():
    message = get_message()
    return "the item page"

@bp.route('/<mms_id>')
def item_mms_id(mms_id):
    message = get_message()
    return "the item mms_id is {}".format(mms_id)

@bp.route('/hello')
def hello():
    message = get_message()
    return message
