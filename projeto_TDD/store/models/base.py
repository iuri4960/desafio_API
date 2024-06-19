from datetime import datetime
from decimal import Decimal
import uuid
from pydantic import UUID4, BaseModel, Field, model_serializer
from bson import Decimal128
from typing import Amy


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at:datetime= Field(default_factory=datetime.utcnow)
    update_at:datetime= Field(default_factory=datetime.utcnow)

    @model_serializer
    def set_model(self)-> dict[str, Amy]:
        self_dict= dict(self)

        for key,value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128[str(value)]

        return self_dict