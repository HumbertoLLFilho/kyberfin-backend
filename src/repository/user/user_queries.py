class UserQueries:
    GET_BY_ID = """
        SELECT * FROM users WHERE id = %(id)s;
    """

    GET_BY_EMAIL = """
        SELECT * FROM users WHERE email = %(email)s;
    """

    INSERT = """
        INSERT INTO users (
            name, email, password_hash, phone, date_of_birth, address,
            city, state, country, zip_code, is_active
        ) VALUES (
            %(name)s, %(email)s, %(password_hash)s, %(phone)s, %(date_of_birth)s, %(address)s,
            %(city)s, %(state)s, %(country)s, %(zip_code)s, %(is_active)s
        ) RETURNING id;
    """

    UPDATE = """
        UPDATE users SET
            name = %(name)s,
            email = %(email)s,
            password_hash = %(password_hash)s,
            phone = %(phone)s,
            date_of_birth = %(date_of_birth)s,
            address = %(address)s,
            city = %(city)s,
            state = %(state)s,
            country = %(country)s,
            zip_code = %(zip_code)s,
            is_active = %(is_active)s,
            updated_at = NOW()
        WHERE id = %(id)s;
    """
