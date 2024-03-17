from engine.core.lib.thingspeaks_response import ThingSpeaksRequestResponse
from engine.core.enums.http_status import HttpStatus
from engine.core.lib.engine_response import EngineResponse
from engine.core.database import db_handler, db_model
from flask import Request

from functools import lru_cache as memoized
"""
Author: Francis Benjamin Zavaleta, Eng
Copyright © fbzavaleta. All rights reserved.
"""

class ThingSpeaksService:
    def __init__(self, request: Request=None) -> None:
        self.engine_response = EngineResponse(request)

    @property
    @memoized(maxsize=1)
    def ingest_channel_description(self) -> dict:
        channel_description = self._get_channel_description
        if channel_description:
            db_handler.MysqlEngine().insert_row(db_model.Channel, channel_description)
            return jsonify({'status': HttpStatus.OK, 'message': 'Channel description ingested'})
        return jsonify({'status': HttpStatus.NOT_FOUND, 'message': 'Channel not found'})

    @property
    @memoized(maxsize=1)
    def _get_channel_feed(self):
        return self.request_response.get_channel_response
