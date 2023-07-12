from sqlalchemy import null
from market import app
from flask import render_template, redirect, url_for, flash,get_flashed_messages, request
from market.models import User, db, Item
from market.forms import Purchase_Item, RegistrationForm, LoginForm, CartForm, SellForm, AgreementForm,DisagreementForm
from market.buffer import predict, represent, represent_bar
from flask_login import current_user, login_user, logout_user, login_required
db.create_all()
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = Purchase_Item()
    if request.method == "POST":
        purchased_item = request.form.get('purchase_form')
        p = Item.query.filter_by(name=purchased_item).first()
        user = User.query.filter_by(id=current_user.id).first()
        if p:
            # p.owner = current_user.id
                current_user.cart = current_user.cart + str(p.id) + ","
                flash(f'{p.name} added successfully',category='success')
                db.session.add(user)
                db.session.commit()
    items = Item.query.all()
    return render_template('market.html', items=items, purchase_form=purchase_form)


@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = form.username.data
        user = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Account successfully created!!',category='success')
        flash(f'logged in as {user}', category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f'Error occurred: {str(msg)}', category='danger')
    return render_template('register.html',form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit:
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user:
            if attempted_user.check_password_correction(attempted_password=form.password.data):
                login_user(attempted_user)
                flash(f"You have logged in as {attempted_user.username}!", category="success")
                return redirect(url_for('market_page'))
            else:
                flash("Attempted User and password don't match", category='danger')
        else:
            flash("No such user exists", category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash("Logout successful", category='info')
    return redirect(url_for('home_page'))
@app.route('/cart',methods=['GET','POST'])
@login_required
def cart_page():
    item = Item()
    cart_form = CartForm()
    if request.method == "POST":
        removed_item = request.form.get('cart_form')
        p = Item.query.filter_by(name=removed_item).first()
        if p:
            p.owner = None
            flash(f"Cart updated! {p.name} removed successfully",category='info')
            db.session.commit()
    items = item.query.filter_by(owner=current_user.id)
    return render_template('cart.html',items=items,cart_form=cart_form)

@app.route('/sell',methods=['GET','POST'])
@login_required
def sell_page():
    form = SellForm()
    if form.validate_on_submit():
        # pred = predict(int(form.price.data), str(form.name.data), current_user.id)
        # print(form.name.data)
        # print(pred)
        # if pred:
        # represent(str(form.name.data))
        # represent_bar(str(form.name.data))
        item = Item(name=form.name.data, price=form.price.data,
                    description=form.description.data, owner = current_user.id)
        db.session.add(item)
        db.session.commit()
        flash("Item added successfully!", category="success")
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for msg in form.errors.values():
            flash(f'Error occurred: {str(msg)}', category='danger')
    return render_template('sell.html',form=form)