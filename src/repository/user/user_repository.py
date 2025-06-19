from typing import Optional
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor
from domain.models.user import User
from domain.repositories.user_repository_interface import IUserRepository
from repository.user.user_queries import UserQueries


class UserRepository(IUserRepository):
    def __init__(self, conn: connection):
        self.conn = conn

    def add(self, user: User) -> None:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                UserQueries.INSERT,
                {
                    "name": user.name,
                    "email": user.email,
                    "password_hash": user.password_hash,
                    "phone": user.phone,
                    "date_of_birth": user.date_of_birth,
                    "address": user.address,
                    "city": user.city,
                    "state": user.state,
                    "country": user.country,
                    "zip_code": user.zip_code,
                    "is_active": user.is_active,
                },
            )
            result = cursor.fetchone()
            if result is not None:
                user.id = result["id"]
            self.conn.commit()

    def get_by_id(self, user_id: int) -> Optional[User]:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(UserQueries.GET_BY_ID, {"id": user_id})
            row = cursor.fetchone()
            if not row:
                return None
            return self._to_domain(row)

    def get_by_email(self, email: str) -> Optional[User]:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(UserQueries.GET_BY_EMAIL, {"email": email.lower()})
            row = cursor.fetchone()
            if not row:
                return None
            return self._to_domain(row)

    def update(self, user: User) -> None:
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                UserQueries.UPDATE,
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "password_hash": user.password_hash,
                    "phone": user.phone,
                    "date_of_birth": user.date_of_birth,
                    "address": user.address,
                    "city": user.city,
                    "state": user.state,
                    "country": user.country,
                    "zip_code": user.zip_code,
                    "is_active": user.is_active,
                },
            )
            self.conn.commit()

    def _to_domain(self, row) -> User:
        return User(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            password="",
            phone=row["phone"],
            date_of_birth=row["date_of_birth"],
            address=row["address"],
            city=row["city"],
            state=row["state"],
            country=row["country"],
            zip_code=row["zip_code"],
            is_active=row["is_active"],
        )
