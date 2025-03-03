from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaning_staff: str,
        movie_name: str) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaning_staff)
    customers_list = []

    for customer_in_customers in customers:
        customer = Customer(name=customer_in_customers["name"],
                            food=customer_in_customers["food"])
        customers_list.append(customer)
        cinema_bar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie_name, customers_list, cleaner)
