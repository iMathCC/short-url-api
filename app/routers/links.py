from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, HttpUrl
from app.database import SessionLocal
from app.services import link_service

router = APIRouter()

# Dependência do Banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class LinkCreate(BaseModel):
    url: HttpUrl

@router.post("/shorten")
def create_link(payload: LinkCreate, db: Session = Depends(get_db)):
    link = link_service.create_short_link(db, str(payload.url))
    return {
        "short_url": f"http://localhost:8000/{link.short_code}",
        "original_url": link.original_url,
        "short_code": link.short_code
    }

@router.get("/{short_code}")
def redirect_link(short_code: str, db: Session = Depends(get_db)):
    link = link_service.get_link_by_code(db, short_code)
    if not link:
        raise HTTPException(status_code=404, detail="Link não encontrado")
    # 307 preserva o método, ideal para redirecionamento simples
    return RedirectResponse(url=link.original_url, status_code=307)