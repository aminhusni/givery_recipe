from main import db, Recipe
from datetime import datetime

db.create_all()
created_at_1 = datetime.strptime('2016-01-10 12:10:12', '%Y-%m-%d %H:%M:%S')
updated_at_1 = datetime.strptime('2016-01-10 12:10:12', '%Y-%m-%d %H:%M:%S')
created_at_2 = datetime.strptime('2016-01-11 13:10:12', '%Y-%m-%d %H:%M:%S')
updated_at_2 = datetime.strptime('2016-01-11 13:10:12', '%Y-%m-%d %H:%M:%S')
chicken_curry = Recipe(id=1, title='Chicken Curry', making_time='45 min', serves='4 people', ingredients='onion, chicken, seasoning', cost=1000, created_at=created_at_1, updated_at=updated_at_1)
rice_omu = Recipe(id=2, title='Rice Omelette', making_time='30 min', serves='2 people', ingredients='onion, egg, seasoning, soy sauce', cost=700, created_at=created_at_2, updated_at=updated_at_2)
db.session.add(chicken_curry)
db.session.add(rice_omu)
db.session.commit()


