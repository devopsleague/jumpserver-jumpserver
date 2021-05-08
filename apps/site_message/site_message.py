from django.db.models import Q

from users.models import User
from .models import SiteMessage, SiteMessageUsers


class Client:
    def send_msg(self, text, user_ids=None, group_ids=None, is_broadcast=False):
        site_msg = SiteMessage.objects.create(text=text, is_broadcast=is_broadcast)

        if not is_broadcast:
            if user_ids:
                site_msg.users.add(user_ids)
            if group_ids:
                site_msg.groups.add(group_ids)

    def _associate_msgs(self, user_id):
        group_ids = User.get_group_ids_by_user_id(user_id)
        site_msg_ids = SiteMessage.objects.filter(
            Q(is_broadcast=True) | Q(groups__id__in=group_ids)
        ).filter(users__id__isnull=True).values_list(id, flat=True)

        if not site_msg_ids:
            return

        to_created = []
        for msg_id in site_msg_ids:
            to_created.append(SiteMessageUsers(
                sitemessage_id=msg_id,
                user_id=user_id
            ))
        SiteMessageUsers.objects.bulk_create(to_created)

    def get_user_all_msgs(self, user_id):
        self._associate_msgs(user_id)

    def get_user_all_msgs_count(self, user_id):
        pass

    def get_user_unread_msgs(self, user_id):
        self._associate_msgs(user_id)

    def get_user_unread_msgs_count(self, user_id):
        pass