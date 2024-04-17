from . import db, Blueprint
from .routeBuilder import makeBaseRoutes
from ..models.usuario import Usuario


usuario_bp = Blueprint('usuario', __name__)

makeBaseRoutes(Usuario,usuario_bp)

