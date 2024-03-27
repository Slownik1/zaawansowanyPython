class Brawery:
    def __init__(self, data):
        self.id =data['id']
        self.name=data['name']
        self.brewery_type=data['brewery_type']
        self.address_1=data['address_1']
        self.address_2=data['address_2']
        self.address_3=data['address_3']
        self.city=data['city']
        self.state_province=data['state_province']
        self.postal_code=data['postal_code']
        self.country=data['country']
        self.longitude=data['longitude']
        self.latitude=data['latitude']
        self.phone=data['phone']
        self.website_url=data['website_url']
        self.state=data['state']
        self.street=data['street']


    def __str__(self):
        return (f"All data: {self.id}, {self.name} "
                f"{self.brewery_type}, {self.address_1}, {self.address_2}, {self.address_3} "
                f"{self.city}, {self.state_province}, {self.postal_code}, {self.country}"
                f"{self.longitude}, {self.latitude}, {self.phone}, {self.website_url}"
                f"{self.street}, {self.state}")
