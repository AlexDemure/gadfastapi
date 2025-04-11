import pydantic

from src.databases.postgres.tables import Table


class Model(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True, extra="allow")

    @classmethod
    def to_dict(cls, table: Table) -> dict:
        return {k: v for k, v in table.__dict__.items() if not k.startswith("_")}

    @classmethod
    def to_model(cls, table: Table) -> "Model":
        model = Model.model_validate(cls.to_dict(table))

        for key, value in model.model_extra.items():
            if isinstance(value, Table.__bound__):
                setattr(model, key, cls.to_model(value))

        return model

    @classmethod
    def from_orm(cls, table: Table) -> "Model":
        model = cls.model_validate(cls.to_dict(table))

        for key, value in model.model_extra.items():
            if isinstance(value, Table.__bound__):
                setattr(model, key, cls.to_model(value))

        return model

    @classmethod
    def init(cls, *args, **kwargs) -> dict:
        raise NotImplementedError
