from sqlalchemy.orm import Session
from uuid import UUID
from app import models

def log_status_change(db: Session, tender_id: UUID, old_status: models.TenderStatus | None,
                      new_status: models.TenderStatus, changed_by: str, reason: str | None = None):
    history_entry = models.TenderStatusHistory(
        tender_id=tender_id,
        old_status=old_status,
        new_status=new_status,
        changed_by=changed_by,
        reason=reason,
    )
    db.add(history_entry)
    db.commit()