from celery import shared_task
from loan.models import LoanPayments, Loan
from loan.helpers import LoanPaymentStatusChoices, LoanStatusChoices


@shared_task(bind=True)
def check_loan_status(self, *args, **kwargs):
    loan = Loan.objects.get(pk = kwargs["loan_id"])
    if loan.period == loan.processed_installments:
        loan.status = LoanStatusChoices.Completed
    else:
        loan.status = LoanStatusChoices.Default
    loan.save()