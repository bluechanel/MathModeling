# -*- encoding: utf-8 -*-

from app import db


class Common(db.Model):
    __abstract__ = True    # 设置这个值，才能被当成MODEL继承
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()