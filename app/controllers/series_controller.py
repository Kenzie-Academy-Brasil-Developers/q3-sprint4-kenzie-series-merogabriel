from flask import jsonify, request
from app.models.series_model import Serie


def series():
    series = Serie.get_series()

    if not series:
        return jsonify(series), 200

    serialized_series = [Serie.serialize(serie) for serie in series]

    return jsonify(serialized_series), 200


def select_by_id(serie_id: str):
    serie = Serie.get_serie_by_id(serie_id)

    if not serie:
        return {}, 404

    serialized_serie = Serie.serialize(serie[0])

    return jsonify(serialized_serie), 200


def create():
    data = request.get_json()

    serie = Serie(**data)

    inserted_serie = serie.create_serie()

    serialized_serie = Serie.serialize(inserted_serie)

    return serialized_serie, 201

    