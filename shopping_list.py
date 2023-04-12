shopping_list = {"piekarnia": ["chleb", "bułki", "rogale"],
                 "warzywniak": ["brokuł", "ogórki", "szczypiorek"]}
for shop, product in shopping_list.items():
    print(f"Idę do {shop.title()} i kupuję tam {str(product).title()}")

products = 0
for values in shopping_list.values():
    products += len(values)
