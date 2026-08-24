from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from app.models import TenderStatus

class TenderCreate(BaseModel):
    title: str = Field(..., max_length=255)
    description: str | None = None

class TenderUpdateStatus(BaseModel):
    new_status: TenderStatus
    reason: str | None = None

class TenderResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    status: TenderStatus
    created_at: datetime
    updated_at: datetime | None
    created_by: str

class HistoryResponse(BaseModel):
    id: UUID
    tender_id: UUID
    old_status: TenderStatus | None
    new_status: TenderStatus
    changed_by: str
    reason: str | None
    changed_at: datetime