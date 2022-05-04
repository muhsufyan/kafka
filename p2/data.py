from faker import Faker


fake = Faker()

# generate dummy data
def create_data():
    return{
        "name": fake.name(),
        "address": fake.address(),
        "create_at":fake.year()
    }

if __name__=="__main__":
    print(create_data())