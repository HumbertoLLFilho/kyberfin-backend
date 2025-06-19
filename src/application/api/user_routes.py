from flask import Blueprint, request, jsonify
from usecases.user.create_user_use_case import CreateUserUseCase
from usecases.user.create_user_input import CreateUserInput
from application.helpers.response_helper import ResponseHelper


def build_user_routes(user_repository):
    user_bp = Blueprint('user', __name__, url_prefix='/users')

    @user_bp.route('/', methods=['POST'])
    def create_user():
        data = request.get_json()
        input_data = CreateUserInput(**data)

        usecase = CreateUserUseCase(user_repository)
        response = usecase.execute(input_data)

        return ResponseHelper.to_http(response)

    return user_bp
