# accounts/tasks.py
from celery import shared_task
from accounts.utils import send_confirmation_emails
from accounts.models import SubOrder

@shared_task(bind=True, ignore_result=True, max_retries=3, default_retry_delay=60)
def send_confirmation_emails_task(self, suborder_id):
    try:
        suborder = (SubOrder.objects
                    .select_related("main_order", "seller")
                    .prefetch_related("items__product")
                    .get(id=suborder_id))
        send_confirmation_emails(suborder)
    except Exception as e:
        raise self.retry(exc=e)

