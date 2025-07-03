from sqlalchemy.orm import sessionmaker
from model.base_model import create_db_and_tables, SessionLocal

from model.product import Product
from model.item import Item
from model.user import User

# Example of how to use it
if __name__ == "__main__":
    create_db_and_tables()
    session = SessionLocal()

    # Create some dummy data
    user1 = User(session, name="Alice", email="alice1@example.com")
    user1.save()
    user2 = User(session, name="Bob", email="bob1@example.com")
    user2.save()
    print("Create 2 user with name Alice , Bob")
    print("")
    # Example usage of the methods

    product1 = Product(session, name="Nametest1", description="Text Description", owner_id=1, harga=20000, variation=["Blue", "Red"])
    product1.save()

    product2 = Product(session, name="OtherTest", description="Text Description", owner_id=1, harga=120000, variation=["Blue", "White", "Greem"])
    product2.save()
    print("Create 2 Product with name Nametest1 , OtherTest")
    print("")

    Item1 = Item(session, title="Nametest", description="Text Description", owner_id=1, attribute={"color": "blue", "volume": 35, "harga": 20000, "features": ["lightweight", "waterproof"] } )
    Item1.save()

    Item2 = Item(session, title="Othername", description="Text Description", owner_id=1, attribute={"color": "red", "volume": 88, "harga": 120000, "features": ["heavy", "waterproof"] } )
    Item2.save()
    print("Create 2 Item with name Nametest , Othername")
    print("")

    print("Fetch ALL USER")
    all_users = User.all(session)
    print("All Users:", all_users)
    print("")

    print("Where condition of User with name = Bob")
    user_bob = User.where(session, User.name == "Bob").first()
    print("User Bob:", user_bob)
    print("")

    print("Where condition of User id = 1")
    user_1 = User.get(session, 1)
    print("User with ID 1:", user_1)
    print("")

    print("Fetch ALL Product")
    all_products = Product.all(session)
    print("All all_products :")
    for product in all_products:
        print(product)
    print("")

    print("Where condition of array of string(variation) which contains Blue")
    search_prod = Product.where_contains(session, Product.variation, "Blue").all()
    print("Search all_products with variation Blue :")
    for product in search_prod:
        print(product)
    print("")

    print("Where condition of array of string(variation) which contains Black")
    search_prod = Product.where_contains(session, Product.variation, "Black").all()
    print("Search all_products with variation Black :")
    for product in search_prod:
        print(product)
    print("")

    print("Where condition product harga > 30000")
    search_prod = Product.where_raw(session, "harga > 30000").all()
    print("Search all_products with harga more than 30000 :")
    for product in search_prod:
        print(product)
    print("")

    print("Fetch ALL Item")
    all_Item = Item.all(session)
    print("All all_Item :")
    for itemo in all_Item:
        print(itemo)
    print("")


    grouped_users = User.groupByRaw(session, "name").with_entities(User.name).all()
    print("Grouped User Names:", grouped_users)
    print("")

    raw_grouped_counts = User.selectRaw(session, "SELECT name, count(*) FROM public.user Group By name")
    print("Raw Grouped Counts:", raw_grouped_counts)
    print("")


    session.close()
