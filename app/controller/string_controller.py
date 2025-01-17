from app.services.string_splitjoin import split_and_join
from app.core.config import YearRequest,StringRequest
from app.utils.util import validate_string

async def string_split_join(request: StringRequest):
    validate_string(request.string)
    result = await split_and_join(request.string)
    return {"result": result}