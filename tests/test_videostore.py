class Statement(object):
    def __init__(self):
        self.header = "Rental Record for {customer_name}\n"
        self.body = "{video}  {cost}\n"
        self.total = "You owe {total}\n"
        self.footer = "You earned {frequent_renter_points} frequent renter points"


class GetStatement(object):
    def __init__(self):
        self.statement = Statement()

    @staticmethod
    def check_video_category(video):
        videos = [
            {'name': "Crazynotes", 'category': "Regular"},
            {'name': "Teeth", 'category': "Regular"},
            {'name': "The Web", 'category': "New"},
            {'name': "Snow White", 'category': "Children"}
        ]
        category = next((item['category'] for item in videos if item['name'] == video), None)
        return category

    @staticmethod
    def check_video_cost(category, number_of_days):
        categories = [
                {'category': "Regular", 'first_day': "2.0", 'extra_days': "1.5"},
                {'category': "New", 'first_day': "3.0", 'extra_days': "3.0"},
                {'category': "Children", 'first_day': "1.5", 'extra_days': "1.5"}
        ]
        first_day = next((item['first_day'] for item in categories if item['category'] == category), None)
        extra_days = next((item['extra_days'] for item in categories if item['category'] == category), None)
        if number_of_days == 1:
            cost = first_day
        elif number_of_days == 2:
            cost = first_day + extra_days
        return cost

    @staticmethod
    def check_frequent_renter_points(category):
        categories = [
            {'category': "Regular", 'points': "1"},
            {'category': "New", 'points': "1"},
            {'category': "Children", 'points': "1"}
        ]
        frp = next((item['points'] for item in categories if item['category'] == category), None)
        return frp

    def execute(self, customer_name, videos, number_of_days):
        header = self.statement.header.format(customer_name=customer_name)
        frequent_renter_points = 0
        total = 0
        full_body = ""
        for video in videos:
            category = self.check_video_category(video)
            cost = self.check_video_cost(category, number_of_days)
            total += float(cost)
            frp = self.check_frequent_renter_points(category)
            frequent_renter_points += int(frp)
            body = self.statement.body.format(video=video, cost=cost)
            full_body += body

        total = self.statement.total.format(total=total)
        footer = self.statement.footer.format(frequent_renter_points=frequent_renter_points)
        return header + full_body + total + footer


def test_user_name_is_displayed_on_statement():
    statement = GetStatement()
    customer_name = "Duncan Bell"
    videos = []
    number_of_days = 1
    expected_statement = """Rental Record for {customer_name}
You owe 0
You earned 0 frequent renter points""".format(customer_name=customer_name)
    assert statement.execute(customer_name, videos, number_of_days) == expected_statement


def test_hire_videos_for_one_day():
    statement = GetStatement()
    customer_name = "Duncan Bell"
    videos = ["Crazynotes", "Teeth", "The Web"]
    number_of_days = 1
    expected_statement = """Rental Record for {customer_name}
Crazynotes  2.0
Teeth  2.0
The Web  3.0
You owe 7.0
You earned 3 frequent renter points""".format(customer_name=customer_name)
    assert statement.execute(customer_name, videos, number_of_days) == expected_statement


def test_hire_one_children_video_for_one_day():
    statement = GetStatement()
    customer_name = "Duncan Bell"
    videos = ["Snow White"]
    number_of_days = 1
    expected_statement = """Rental Record for {customer_name}
Snow White  1.5
You owe 1.5
You earned 1 frequent renter points""".format(customer_name=customer_name)
    assert statement.execute(customer_name, videos, number_of_days) == expected_statement
