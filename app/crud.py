from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID
from app import models, schemas

def create_tender(db: Session, tender_data: schemas.TenderCreate, user_id: str) -> models.Tender:
    db_tender = models.Tender(
        title=tender_data.title,
        description=tender_data.description,
        created_by=user_id,
        status=models.TenderStatus.draft,
    )
    db.add(db_tender)
    db.commit()
    db.refresh(db_tender)
    return db_tender

def get_tender(db: Session, tender_id: UUID) -> models.Tender | None:
    return db.execute(select(models.Tender).where(models.Tender.id == tender_id)).scalar_one_or_none()

def update_tender_status(db: Session, tender_id: UUID, new_status: models.TenderStatus, user_id: str, reason: str | None = None):
    tender = get_tender(db, tender_id)
    if not tender:
        return None
    old_status = tender.status
    if old_status == new_status:
        return tender
    tender.status = new_status
    db.commit()
    db.refresh(tender)
    from app.history import log_status_change
    log_status_change(db, tender_id, old_status, new_status, user_id, reason)
    return tender

def get_tenders(db: Session, skip: int = 0, limit: int = 100, status: models.TenderStatus | None = None):
    query = select(models.Tender)
    if status:
        query = query.where(models.Tender.status == status)
    query = query.offset(skip).limit(limit)
    return db.execute(query).scalars().all()

def get_tender_history(db: Session, tender_id: UUID, skip: int = 0, limit: int = 100):
    query = select(models.TenderStatusHistory).where(
        models.TenderStatusHistory.tender_id == tender_id
    ).order_by(models.TenderStatusHistory.changed_at.desc()).offset(skip).limit(limit)
    return db.execute(query).scalars().all()