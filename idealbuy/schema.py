# idealbuy/schema.py
import graphene
from graphene import relay, ObjectType
from django import forms
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from testdb.models import Products, Prices, Supermarket
from graphene_django.forms.mutation import DjangoModelFormMutation

class ProductsType(DjangoObjectType):
    class Meta:
        model = Products
        fields = ('product_name', 'product_unit', 'category')

class SupermarketType(DjangoObjectType):
    class Meta:
        model = Supermarket
        fields = ('id', 'super_name', 'active')

class PricesType(DjangoObjectType):
    class Meta:
        model = Prices
        fields = ('id', 'price', 'products_id', 'super_id')

class PricesNode(DjangoObjectType):
    class Meta:
        model = Prices
        filter_fields = {
            'price':['exact'], 
            'products_id__product_name':['exact','icontains', 'istartswith'], 
            'super_id':['exact'],
        }
        interfaces = (relay.Node,)

class ProductsNode(DjangoObjectType):
    class Meta:
        model = Products
        filter_fields = {
            'product_name': ['exact', 'icontains', 'istartswith'],
            'product_unit': ['exact', 'icontains', 'istartswith'],
            'category': ['exact']
        }
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    products=relay.Node.Field(ProductsNode)
    all_filter_products = DjangoFilterConnectionField(ProductsNode)

    all_products = graphene.List(ProductsType)
    all_super = graphene.List(SupermarketType)
    all_prices = graphene.List(PricesType)

    def resolve_all_products(root, info):
        return Products.objects.all()
    
    def resolve_all_super(root, info):
        return Supermarket.objects.all()

    def resolve_all_prices(root, info):
        return Prices.objects.all()

    price = relay.Node.Field(PricesNode)
    all_filter_prices = DjangoFilterConnectionField(PricesNode)



class CreateProduct(graphene.Mutation):

    product = graphene.Field(ProductsType)
    
    class Arguments:
        product_name = graphene.String()
        product_unit = graphene.String()
        category = graphene.Int()    

    ok = graphene.Boolean()
     
    def mutate(self, info, product_name,product_unit, category):
        product = Products(product_name=product_name, product_unit=product_unit, category=category)
        ok = True
        product.save()
        return CreateProduct(product=product, ok=ok)

class UpdateProduct(graphene.Mutation):
    price = graphene.Field(PricesType)
    
    class Arguments:
        id = graphene.ID()
        new_price = graphene.Int()    


    ok = graphene.Boolean()
     
    def mutate(self, info, id, new_price):
        price = Prices.objects.get(pk=id)
        price.price = new_price
        price.save()
        ok = True
        return UpdateProduct(price=price, ok=ok)
    
class Mutations(graphene.ObjectType):
    create_prod = CreateProduct.Field()
    update_prod = UpdateProduct.Field()
    
"""
class Mutation(ObjectType):
    create_product = CreateProduct.Field() 


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_unit', 'category']




class CreateProduct(DjangoModelFormMutation):
    products = graphene.Field(ProductType)
    class Meta:
        form_class = ProductForm
    



    def resolve_create_products(self, info, **kwargs):
        return self.products


    def mutate(self, info, product_name, product_unit, category):
        products = Products.objects.get(pk=id)
        products.product_name = product_name
        products.product_unit = product_unit
        products.category = category
        products.save()
        return CreateProduct(products=products)
"""


schema = graphene.Schema(query=Query, mutation=Mutations)

