class Ticket:
    def __init__(self, event_id, price):
        self.event_id = event_id
        self.price = price
        self.sold = False

class TicketSales:
    def __init__(self):
        self.sales = {}

    def add_ticket(self, event_id, price):
        if event_id not in self.sales:
            self.sales[event_id] = []
        self.sales[event_id].append(Ticket(event_id, price))

    def sell_ticket(self, event_id):
        for ticket in self.sales.get(event_id, []):
            if not ticket.sold:
                ticket.sold = True
                return True
        return False

    def delete_ticket(self, event_id, index):
        if event_id in self.sales and 0 <= index < len(self.sales[event_id]):
            del self.sales[event_id][index]

    def analyze_sales(self, event_id):
        tickets = self.sales.get(event_id, [])
        total_sold = sum(t.sold for t in tickets)
        avg_price = sum(t.price for t in tickets) / len(tickets) if tickets else 0
        return {
            "total_sold": total_sold,
            "average_price": avg_price,
            "sold_percentage": (total_sold / len(tickets) * 100) if tickets else 0
        }

import unittest

class TestTicketSales(unittest.TestCase):
    def setUp(self):
        self.ticket_sales = TicketSales()
        self.event_id = "E001"
        self.ticket_sales.add_ticket(self.event_id, 100)
        self.ticket_sales.add_ticket(self.event_id, 150)

    def test_sales(self):
        print("Initial tickets:")
        for i, ticket in enumerate(self.ticket_sales.sales[self.event_id]):
            print(f"Ticket {i+1}: Price={ticket.price}, Sold={ticket.sold}")

        print("\nSelling a ticket...")
        self.assertTrue(self.ticket_sales.sell_ticket(self.event_id))
        print("Tickets after selling one:")
        for i, ticket in enumerate(self.ticket_sales.sales[self.event_id]):
            print(f"Ticket {i+1}: Price={ticket.price}, Sold={ticket.sold}")

        print("\nAnalyzing sales...")
        sales_data = self.ticket_sales.analyze_sales(self.event_id)
        print(f"Total sold: {sales_data['total_sold']}")
        print(f"Average price: {sales_data['average_price']}")
        print(f"Sold percentage: {sales_data['sold_percentage']}%")

        print("\nDeleting a ticket...")
        self.ticket_sales.delete_ticket(self.event_id, 0)
        print("Tickets after deleting one:")
        for i, ticket in enumerate(self.ticket_sales.sales[self.event_id]):
            print(f"Ticket {i+1}: Price={ticket.price}, Sold={ticket.sold}")

if __name__ == '__main__':
    unittest.main()