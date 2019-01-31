# routes/controllers for item operations
from flask import abort, Blueprint, flash, render_template, request, session, url_for
from almaweb.utils import alma_get, pprint_xml
from almaweb.settings import *
import requests

bp = Blueprint('item', __name__, url_prefix='/item')


@bp.route('/', methods=['GET', 'POST'])
def item():
    if request.method == 'GET':
        return render_template('get_item.html')
    else:
        barcode = request.form['barcode']
        try:
            item_req = alma_get(API_HOST + GET_BY_BARCODE.format(barcode),
                                BIBS_API_KEY, fmt='xml')
            #return item_req.url
            record_pretty = pprint_xml(item_req.content)
            return render_template('show_item.html',
                                   record=record_pretty)
        except requests.exceptions.HTTPError:
            abort(404, "could not retrieve item {}".format(barcode))

@bp.route('/<mms_id>', methods=['GET', 'POST'])
def item_mms_id(mms_id):
    return "the item mms_id is {}".format(mms_id)

@bp.route('/hello')
def hello():
    return API_HOST

