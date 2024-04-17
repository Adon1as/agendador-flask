
from sqlalchemy import exc

def baseSQLAlchemyErrorHandler(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exc.SQLAlchemyError as e:
                return {"message":e.args}
            except Exception as e:
                return {"message":e.args}
        return wrapper

def allSQLAlchemyErrorHandler(cls):
    for nome, metodo in vars(cls).items():
        if callable(metodo):
            setattr(cls, nome, baseSQLAlchemyErrorHandler(metodo))
    return cls