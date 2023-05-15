from flask import render_template, flash, redirect, url_for, g
from flask_login import current_user, login_required
from . import bp

from app.models import User, Hero
from app.forms import CreateHeroForm

@bp.route('/create_hero', methods=["GET","POST"])
@login_required
def create_hero():
    form = CreateHeroForm()
    if form.validate_on_submit():
        h = Hero(hero_name=form.hero.data, power=form.power.data, hero_lore=form.lore.data)
        h.user_id = current_user.user_id
        h.commit()
        flash('Hero Created!', 'success')
        return redirect(url_for('social.user_page',username=current_user.username))
    return render_template('create_hero.jinja', form = form, user_search_form= g.user_search_form)

@bp.route('/userpage/<username>')
@login_required
def user_page(username):   
    user = User.query.filter_by(username=username).first()
    return render_template('user_page.jinja', title=username, user=user, user_search_form= g.user_search_form)

@bp.post('/user-search')
@login_required
def user_search():
    if g.user_search_form.validate_on_submit:
        return redirect(url_for('social.user_page', username=g.user_search_form.user.data))
    return redirect(url_for('main.home'))