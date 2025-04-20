from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CheckoutAPIView(APIView):
    def post(self, request):
        try:
            # Get raw string directly from body
            item_string = request.body.decode('utf-8').strip()

            pricing_rules = {
                'A': {'unit': 50, 'deal_qty': 3, 'deal_price': 130},
                'B': {'unit': 30, 'deal_qty': 2, 'deal_price': 45},
                'C': {'unit': 20},
                'D': {'unit': 15}
            }

            total = 0
            item_counts = {}

            for item in item_string:
                if item in pricing_rules:
                    item_counts[item] = item_counts.get(item, 0) + 1

            for item, count in item_counts.items():
                rule = pricing_rules[item]
                if 'deal_qty' in rule:
                    total += (count // rule['deal_qty']) * rule['deal_price']
                    total += (count % rule['deal_qty']) * rule['unit']
                else:
                    total += count * rule['unit']

            # Return the total price as plain text
            return Response(f"total Price: {total}", status=status.HTTP_200_OK)

        except Exception as e:
            return Response('Invalid input or format', status=status.HTTP_400_BAD_REQUEST)
