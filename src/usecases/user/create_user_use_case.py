from domain.enums.HttpStatus import HttpStatusCode
from domain.models.response import Response
from domain.repositories.user_repository_interface import IUserRepository
from usecases.user.create_user_input import CreateUserInput
from domain.models.user import User
from crosscutting.security.hash_service import HashHelper
from typing import Optional
from datetime import datetime

class CreateUserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, input_data: CreateUserInput) -> Response:
        try:
            existing_user: Optional[User] = self.user_repository.get_by_email(input_data.email)
            if existing_user:
                return Response.error(HttpStatusCode.BAD_REQUEST, [ "Email já existe" ])

            password_hash = HashHelper.hash_password(input_data.password)

            date_of_birth = None
            if input_data.date_of_birth:
                date_of_birth = datetime.combine(input_data.date_of_birth, datetime.min.time())

            user = User(
                name=input_data.name,
                email=input_data.email,
                password=password_hash,
                phone=input_data.phone,
                date_of_birth=date_of_birth,
                address=input_data.address,
                city=input_data.city,
                state=input_data.state,
                country=input_data.country,
                zip_code=input_data.zip_code,
                is_active=True
            )

            self.user_repository.add(user)

            return Response.success(HttpStatusCode.CREATED, {
                "id": user.id,
                "name": user.name
            })
        except Exception as e:
            return Response.error(HttpStatusCode.INTERNAL_ERROR, [ "Erro ao criar usuário", str(e) ]) 