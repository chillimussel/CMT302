"""
all operations with shop, which is the main site, are done here.
Like browse items, purchase items, add items to wish list, checkout, etc.
"""
from flask import (
    Blueprint, request, render_template, views, redirect, url_for, session, flash
)
from pathlib import Path
from flask_login import current_user, login_required # current_user is the proxy for current user
from app.blueprints.auth.models import User
from app import db
from .models import Item, Wish

bp = Blueprint('shop',__name__)

@bp.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html',items=items)

@bp.route('/cart/',methods=['GET','POST'])
@login_required
def cart(): # handling cart operation with session
    if request.method == 'GET':
        items_id = session.get('cart',{})
        items = []
        total_price = 0
        for id,count in items_id.items():
            item = Item.query.filter_by(id=int(id)).first()
            items.append((item,int(count)))
            total_price += int(count) * item.price
        total_price = round(total_price,2)
        return render_template('cart.html', items=items, total_price=total_price)
    if request.method == 'POST':
        item_id = request.form['item_id']
        if 'cart' in session:
            if item_id in session['cart']:
                session['cart'][item_id] += 1
            else:
                session['cart'][item_id] = 1
        else:
            session['cart']={item_id:1}
        flash('Successfully Add the Item To Cart!')
        return redirect(request.referrer)


@bp.route('/cart/delete/',methods=['POST','GET'])
@login_required
def delete_cart(): # delete cart
    if request.method == 'GET':
        session.pop('cart')
        return redirect(request.referrer)
    if request.method == 'POST':
        item_id = request.form['item_id']
        if 'cart' in session:
            if item_id in session['cart']:
                session['cart'].pop(item_id)
                flash('Successfully Delete the Item!')
        return redirect(request.referrer)
                
@bp.route('/item/<int:item_id>/')
def item(item_id=None): # handle item details
    item = Item.query.filter_by(id=int(item_id)).first()
    return render_template('item.html',item=item)

@bp.route('/wish/',methods=['GET','POST'])
@bp.route('/wish/<int:wish_id>/',methods=['POST'])
@login_required
def wish(wish_id=None): # handle wish list CURD 
    if request.method == 'GET':
        wishes = Wish.query.filter_by(user_id=current_user.id).all()
        return render_template('wish.html',wishes=wishes)
    if request.method == 'POST':
        if not wish_id:
            item_id = int(request.form['item_id'])
            if db.session.query(
                Wish.query.filter_by(item_id=item_id).exists()
            ).scalar():
                flash('This item already exists in your wish list!','warning')
                return redirect(request.referrer)
            db.session.add(Wish(
                item_id=item_id,
                user_id=current_user.id
            ))
            db.session.commit()
            flash('Successfully Add the Item to Whish List!','warning')
            return redirect(request.referrer)
        else:
            w = Wish.query.filter_by(id=wish_id).first()

            db.session.delete(w)
            db.session.commit()
            flash('Successfully Delete the Item from Whish List!','warning')
            return redirect(request.referrer)

@bp.route('/wish/delete/')
def delete_wish():
    for w in Wish.query.filter_by(user_id=current_user.id).all():
        db.session.delete(w)
    db.session.commit()
    flash('Successfully Delete All Items in the Wish List!')
    return redirect(request.referrer)

@bp.route('/checkout/')
@login_required
def checkout(): # checkout 
    items_id = session.get('cart',{})
    items = []
    total_price = 0
    for id,count in items_id.items():
        item = Item.query.filter_by(id=int(id)).first()
        items.append((item,int(count)))
        total_price += int(count) * item.price
    total_price = round(total_price,2)
    return render_template('checkout.html', items=items,total_price=total_price)

