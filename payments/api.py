from ninja import Router
from .schemas import TransactionSchema
from django.shortcuts import get_object_or_404
from users.models import User
from rolepermissions.checkers import has_permission
from django.db import transaction as django_transaction
import requests
from django.conf import settings
from .models import Transaction
from django_q.tasks import async_task
from .tasks import send_notification


payments_router = Router()

@payments_router.post('/', response={200: TransactionSchema, 400: dict, 403: dict})
def trasaction(request, transaction: TransactionSchema):
    payer = get_object_or_404(User, id=transaction.payer)
    payee = get_object_or_404(User, id=transaction.payee)
    
    if payer.amount < transaction.amount:
        return 400, {'error': 'Saldo insuficiente'}
    
    if not has_permission(payer, 'make_transfer'):
        return 403, {'error': 'Você não possui permissão para realizar tranferência'}
    
    if not has_permission(payee, 'receive_transfer'):
        return 403, {'error': 'O usuário não pode receber tranferências'}
    
    with django_transaction.atomic():
        payer.pay(transaction.amount)
        payer.recive(transaction.amount)
        
        transact = Transaction(
           amount = transaction.amount,
           payer_id = transaction.payer,
           payee_id = transaction.payee 
        )
        payer.save()
        payee.save()
        transact.save()
        
        response = requests.get(settings.AUTHORIZE_TRANSFER_ENDPOINT).json()
        if response.get('status') != "authorizad":
            raise Exception()
        
    async_task(send_notification, payer.first_name, payee.first_name, transaction.amount)   
    return 200, {'transaction_id': 1}