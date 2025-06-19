from flask import jsonify
from domain.models.response import Response

class ResponseHelper:
    @staticmethod
    def to_http(response: Response):
        return jsonify(response.to_dict()), response.code
