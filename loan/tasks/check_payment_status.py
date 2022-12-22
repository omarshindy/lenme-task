from celery import shared_task
from loan.models import LoanPayments, Loan
from loan.helpers import LoanPaymentStatusChoices


@shared_task(bind=True)
def check_payment_status(self, *args, **kwargs):
    payment = LoanPayments.objects.get(pk = kwargs["payment_id"])
    loan = Loan.objects.get(pk = payment.loan.id)
    if payment.status == LoanPaymentStatusChoices.Paid:
        loan.processed_installments += 1
        loan.save()
    else:
        payment.status = LoanPaymentStatusChoices.Default
        payment.save()