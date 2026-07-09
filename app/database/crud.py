from sqlalchemy.orm import Session

from app.models.call import Call


def create_call(
    db: Session,
    call: Call
):
    """
    Save a call into database.
    """

    db.add(call)
    db.commit()
    db.refresh(call)

    return call