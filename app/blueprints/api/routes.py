from flask import request, jsonify

from . import bp
from app.models import Hero, User
from app.blueprints.api.helpers import token_required

# Recieve All Heros
@bp.get('/create_hero')
@token_required
def api_heros(user):
    result = []
    heros = Hero.query.all()
    for hero in heros:
        result.append({
            'id':hero.hero_id,
            'name':hero.hero_name, 
            'power':hero.power, 
            'lore':hero.hero_lore,
            'creator':hero.user_id,
            'timestamp':hero.creation_date
            })
    return jsonify(result), 200

# Recieve Heros created by Single User
@bp.get('/create_hero/<username>')
@token_required
def user_heros(user, username):
    user = User.query.filter_by(username=username).first()
    if user:
      return jsonify([{
            'id':hero.hero_id,
            'name':hero.hero_name, 
            'power':hero.power, 
            'lore':hero.hero_lore,
            'creator':hero.user_id,
            'timestamp':hero.creation_date
            } for hero in user.heros]), 200
    return jsonify([{'message':'Invalid Username'}]), 404 

#Search single hero
@bp.get('/create_hero/<hero_id>')
@token_required
def get_hero(user, hero_id):
    try:
      hero = Hero.query.get(hero_id)
      return jsonify([{
            'id':hero.hero_id,
            'name':hero.hero_name, 
            'power':hero.power, 
            'lore':hero.hero_lore,
            'creator':hero.user_id,
            'timestamp':hero.creation_date
            }])
    except: 
      return jsonify([{'message':'Invalid Hero Id'}]), 404
    
#Create Hero
@bp.post('/create_hero')
@token_required
def create_hero(user):
    try:
        content = request.json
        hero = Hero(hero_name=content.get('hero_name'), power=content.get('power'), hero_lore=content.get('hero_lore'), user_id=user.user_id)
        hero.commit()
        return jsonify([{'message':'Hero Created!','name':hero.hero_name}])
    except:
       jsonify([{'message':'invalid form data'}]), 401