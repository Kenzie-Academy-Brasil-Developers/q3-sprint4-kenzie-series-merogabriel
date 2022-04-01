from flask import Blueprint
from app.controllers import series_controller

bp = Blueprint('series', __name__, url_prefix='/series')

bp.get('')(series_controller.series)
bp.get('<serie_id>')(series_controller.select_by_id)
bp.post('')(series_controller.create)
