from typing import Optional
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        id: Optional[int] = None,
        phone: Optional[str] = None,
        date_of_birth: Optional[datetime] = None,
        address: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        country: Optional[str] = None,
        zip_code: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        is_active: bool = True
    ):
        self.id = id
        self.name = name
        self.email = email.lower()
        self.password_hash = generate_password_hash(password)
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.is_active = is_active

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def set_password(self, new_password: str):
        self.password_hash = generate_password_hash(new_password)

    def update(self, **kwargs):
        allowed_fields = {
            'name', 'email', 'phone', 'date_of_birth', 'address', 'city',
            'state', 'country', 'zip_code', 'is_active'
        }
        for key, value in kwargs.items():
            if key in allowed_fields and value is not None:
                setattr(self, key, value)
        self.updated_at = datetime.utcnow()
