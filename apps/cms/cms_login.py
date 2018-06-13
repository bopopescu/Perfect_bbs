@bp.route('/')
@login_required
def index():
    return 'cms index'