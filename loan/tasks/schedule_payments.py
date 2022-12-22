# tasks.py
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from django_celery_beat.models import PeriodicTask, ClockedSchedule
from loan.models import Loan, Offers, LoanPayments
import json

@shared_task()
def schedule_payments(loan_id, offer_id):
    loan = Loan.objects.get(pk=loan_id)
    offer = Offers.objects.filter(id = offer_id).first()
    payment_amount = loan.return_amount / loan.period
    for i in range(1,loan.period + 1):
        due_date = timezone.now() + timedelta(minutes=i)
        loan_payments = LoanPayments.objects.create(loan=loan, investor= offer.investor ,amount=payment_amount, due_date= due_date)
        loan_payments.refresh_from_db()
        schedule, created = ClockedSchedule.objects.get_or_create(clocked_time=due_date)
        PeriodicTask.objects.create(
            name=f"Payment Status at {schedule}",
            clocked=schedule,
            task="loan.tasks.check_payment_status.check_payment_status",
            one_off=True,
            args=json.dumps([]),
            kwargs=json.dumps({
                "payment_id": loan_payments.id
            })
        )
        
        if i == loan.period:
            PeriodicTask.objects.create(
                name=f"Loan Status at {schedule}",
                clocked=schedule,
                task="loan.tasks.check_loan_status.check_loan_status",
                one_off=True,
                args=json.dumps([]),
                kwargs=json.dumps({
                    "loan_id": loan.id
                })
            ) 

        