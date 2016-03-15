import logging

from django.http import Http404, HttpResponseRedirect

# from aawaz_panel.models import permissions_model, roles_model

logger = logging.getLogger(__name__)


class Acl:
    def __init__(self):
        pass

    def process_request(self, request):
        try:
            role = request.session.get('role', "guest")
            request_path = request.path
            logger.debug(request_path)
            # path_id = permissions_model.fetch_pemission_url(request_path)
            # role_permissions = roles_model.get_roles_permissions(role)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            ip = None
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            logger.info(request.path + " by " + ip)
            return None
            # if role == 'user':
            #     return None
            # if str(path_id['_id']) in role_permissions['permissions']:
            #     request.session['current_url'] = request_path
            #     return None
            if role == "guest":
                return HttpResponseRedirect('/')
            else:
                raise Http404
        except TypeError as e:
            logger.error("Error in ACL" + str(e))
        raise Http404