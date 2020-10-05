# idealbuy/schema.py
import graphene
from graphene import relay, ObjectType
from django import forms
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from testdb.models import Products, Prices, Supermarket, User, Boss
from graphene_django.forms.mutation import DjangoModelFormMutation

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id','username', 'user_mail', 'role', 'active','user_photo','user_firebase')

class BossType(DjangoObjectType):
    class Meta:
        model = Boss
        fields = ('id','admin_name', 'mail', 'role', 'active')

class ProductsType(DjangoObjectType):
    class Meta:
        model = Products
        fields = ('id','product_name', 'product_unit', 'category', 'product_photo')

class SupermarketType(DjangoObjectType):
    class Meta:
        model = Supermarket
        fields = ('id', 'super_name', 'active','super_photo', 'role')

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
            'products_id__id': ['exact'],
            'super_id__super_name':['exact', 'icontains', 'istartswith'],
            'super_id__id':['exact'],
        }
        interfaces = (relay.Node,)

class ProductsNode(DjangoObjectType):
    class Meta:
        model = Products
        filter_fields = {
            'product_name': ['exact', 'icontains', 'istartswith'],
            'product_unit': ['exact', 'icontains', 'istartswith'],
            'product_photo': ['exact'],
            'category': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
class SupermarketNode(DjangoObjectType):
    class Meta:
        model = Supermarket
        filter_fields = {
            'super_name':['exact','icontains', 'istartswith'], 
            'super_photo':['exact'],
        } 
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    products=relay.Node.Field(ProductsNode)
    all_filter_products = DjangoFilterConnectionField(ProductsNode)

    price = relay.Node.Field(PricesNode)
    all_filter_prices = DjangoFilterConnectionField(PricesNode)
    
    super_name = relay.Node.Field(SupermarketNode)
    all_supers_name = DjangoFilterConnectionField(SupermarketNode)
    
   
    all_bosses = graphene.List(BossType)
    all_users = graphene.List(UserType)
    all_products = graphene.List(ProductsType)
    all_super = graphene.List(SupermarketType)
    all_prices = graphene.List(PricesType)

    def resolve_all_products(root, info):
        return Products.objects.all()
    
    def resolve_all_super(root, info):
        return Supermarket.objects.all()

    def resolve_all_prices(root, info):
        return Prices.objects.all()
    
    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_all_bosses(root,info):
        return Boss.objects.all()

class CreateUser(graphene.Mutation):
    new_user = graphene.Field(UserType)
    class Arguments:
        username = graphene.String()
        user_mail= graphene.String()
        user_photo = graphene.String()
    ok = graphene.Boolean()
    
    def mutate(self,info,username,user_mail, user_photo):
        new_user = User(username=username,user_mail=user_mail,user_photo=user_photo,role='usr')
        new_user.save()
        ok = True
        return CreateUser(new_user=new_user, ok=ok)

class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductsType)
    
    class Arguments:
        product_name = graphene.String()
        product_unit = graphene.String()
        category = graphene.String()  
          

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

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        username = graphene.String()
        active = graphene.Boolean()

    ok = graphene.Boolean()

    def mutate(self,info,username,active):
        user = User.objects.get(username=username)
        user.active = active
        user.save()
        ok = True
        return UpdateUser(user=user, ok=ok)
        


class Mutations(graphene.ObjectType):
    create_prod = CreateProduct.Field()
    update_prod = UpdateProduct.Field()
    update_user = UpdateUser.Field()
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)

