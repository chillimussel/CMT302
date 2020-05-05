"""
Commands used during development
"""
import click
from flask.cli import with_appcontext
from flask import current_app
from app import db
from app.blueprints.auth.models import User
from app.blueprints.shop.models import Item
from pathlib import Path

def init_app(app):
    app.cli.add_command(init_db)
    app.cli.add_command(feed_data)


@click.command('init-db')
@with_appcontext
def init_db(): 
    """Create Database Tables"""
    db.reflect() 
    db.drop_all() # drop all tables for preventing polluting new data
    db.create_all()
    click.echo('Successfully Create All DB Tables!')

@click.command('feed-data')
@with_appcontext
def feed_data():
    """feed preserved data into database"""
    from .data import items_data, users_data
    for user in users_data:
        db.session.add(User(username=user.username,password=user.password))
    inventory = 20
    for item in items_data:
        db.session.add(Item(
            name=item.name,
            price=item.price,
            desc=item.desc,
            image=item.image,
            inventory=inventory
        ))
    db.session.commit()
    click.echo('import succeed')
    
