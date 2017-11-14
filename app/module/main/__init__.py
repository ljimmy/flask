from flask import Blueprint
bp = Blueprint('main', __name__)
route = bp.route

def api(rule, **options):
    def decorator(view, pk='id', pk_type='int'):
        view_func = view.as_view(view.__name__)
        bp.add_url_rule(rule, defaults={pk: None},
                        view_func=view_func, methods=['GET',])
        bp.add_url_rule(rule, view_func=view_func, methods=['POST',])
        bp.add_url_rule('%s<%s:%s>' % (rule, pk_type, pk), view_func=view_func,
                        methods=['GET', 'PUT', 'DELETE'])
        return view
    return decorator


from . import passport
from . import user
