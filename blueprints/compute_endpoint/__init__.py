from flask import abort, Blueprint, jsonify, request

from scraping import scraping
from compute.tf_idf import TfIdf
from utils.utils import get_articles_file

compute_blueprint = Blueprint("api", __name__, url_prefix="/")

tf_idf = TfIdf(get_articles_file())


@compute_blueprint.route("/v1/tfidf", methods=["GET"])
def tfidf():
    if request.method == "GET":
        url = request.args.get("url")
        limit = request.args.get("limit")
        if not validate_params(url, limit):
            abort(400, description="Missing parameters url or limit!")

        res = scraping.process_text(url)
        tf_idfv = tf_idf.compute_tfidf(res, int(limit))
        return jsonify(build_response(tf_idfv))


@compute_blueprint.errorhandler(400)
def not_found(error):
    return {"code": 100, "desc": error.description}, 400


@compute_blueprint.errorhandler(404)
def not_found(error):
    return {"code": 100, "desc": error.description}, 404


@compute_blueprint.errorhandler(405)
def not_allowed(error):
    return {"code": 100, "desc": error.description}, 405


def build_response(tfidf_dict):
    res_list = []
    for elem_set in tfidf_dict:
        res_list.append({"term": elem_set[0], "tf-idf": str(elem_set[1])})
    return {"terms": res_list}


def validate_params(url, limit):
    if url and limit:
        return True
    return False
