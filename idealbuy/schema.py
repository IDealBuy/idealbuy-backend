# idealbuy/schema.py

import graphene
from graphene_django import DjangoObjectType
from testdb.models import Products, Prices, Supermarket

class ProductsType(DjangoObjectType):
    class Meta:
        model = Products
        fields = ('id', 'product_name', 'product_unit', 'category')

class SupermarketType(DjangoObjectType):
    class Meta:
        model = Supermarket
        fields = ('id', 'super_name', 'active')

class PricesType(DjangoObjectType):
    class Meta:
        model = Prices
        fields = ('id', 'price', 'products_id', 'super_id')

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductsType)

    all_super = graphene.List(SupermarketType)

    all_prices = graphene.List(PricesType)

    def resolve_all_products(root, info):
        return Products.objects.all()
    
    def resolve_all_super(root, info):
        return Supermarket.objects.all()

    def resolve_all_prices(root, info):
        return Prices.objects.all()

    

schema = graphene.Schema(query=Query)

