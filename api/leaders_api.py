from api import api_bp
from database import get_top_5_leaders_db


# polucheniya spiska liderov
@api_bp.route('/leaders/<int:level>', methods=['GET'])
def get_top_5(level: int = 0):
    result = get_top_5_leaders_db(level)
    leaders = []

    # prohodim po kajdomu onjectu v spiske
    for leader in result:
        leaders.append({leader.user_fk.name: leader.score})

    return {'level': level, 'leaders': None}