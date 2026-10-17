import string
import random
from sqlalchemy.orm import Session
from app.models.link import Link

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

def create_short_link(db: Session, original_url: str):
    # Gera código e verifica se já existe
    short_code = generate_short_code()
    while db.query(Link).filter(Link.short_code == short_code).first():
        short_code = generate_short_code()
    
    new_link = Link(original_url=original_url, short_code=short_code)
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link

def get_link_by_code(db: Session, short_code: str):
    link = db.query(Link).filter(Link.short_code == short_code).first()
    if link:
        link.clicks += 1
        db.commit()
    return link