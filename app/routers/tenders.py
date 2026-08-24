from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from uuid import UUID
from app import schemas, crud, models
from app.database import get_db
from app.dependencies import get_current_user_id

router = APIRouter(prefix="/tenders", tags=["tenders"])

@router.post("/", response_model=schemas.TenderResponse, status_code=status.HTTP_201_CREATED)
def create_tender(
    tender_in: schemas.TenderCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id)
):
    tender = crud.create_tender(db, tender_in, user_id)
    return tender

@router.get("/{tender_id}", response_model=schemas.TenderResponse)
def get_tender(tender_id: UUID, db: Session = Depends(get_db)):
    tender = crud.get_tender(db, tender_id)
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    return tender

@router.put("/{tender_id}/status", response_model=schemas.TenderResponse)
def update_tender_status(
    tender_id: UUID,
    update_data: schemas.TenderUpdateStatus,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id)
):
    tender = crud.update_tender_status(db, tender_id, update_data.new_status, user_id, update_data.reason)
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    return tender

@router.get("/", response_model=list[schemas.TenderResponse])
def list_tenders(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    status: models.TenderStatus | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_tenders(db, skip=skip, limit=limit, status=status)

@router.get("/{tender_id}/history", response_model=list[schemas.HistoryResponse])
def get_history(
    tender_id: UUID,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    # проверяем, существует ли тендер
    tender = crud.get_tender(db, tender_id)
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    return crud.get_tender_history(db, tender_id, skip=skip, limit=limit)