from django.http import HttpResponse


class StripeWebhookHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def payment_intent_succeeded(self, event):
        """Handle the payment_intent_succeeded Stripe webhook"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def payment_intent_failed(self, event):
        """Handle the payment_intent_failed Stripe webhook"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
