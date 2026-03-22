#
# {
#     'id': 9223372036854775807,
#  'name': 'doggie',
#  'photoUrls': ['string'],
#  'tags': []
#  }

from pydantic import BaseModel

class PetResponse(BaseModel):
    id: int
    name: str
    photoUrls: list
    tags: list