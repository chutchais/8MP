import graphene
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from product.models import Product
from workorder.models import WorkOrder

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ['name', 'slug']
        interfaces = (relay.Node, )

class WorkOrderType(DjangoObjectType):
    class Meta:
        model = WorkOrder
# ------------------------------------------------

class Query(graphene.ObjectType):
    product     = graphene.Field(ProductType,
                                id=graphene.Int(),
                                name=graphene.String())
    products    = graphene.List(ProductType)#DjangoFilterConnectionField(ProductType)#
    def resolve_product(self, info, **kwargs):
          id    = kwargs.get('id')
          name  = kwargs.get('name')
          if id is not None:
              return Product.objects.get(pk=id)
          if name is not None:
              return Product.objects.get(name=name)
          return None
    def resolve_products(self,info,**kwargs):
        return Product.objects.all()
    
    workorder   = graphene.Field(WorkOrderType,
                                id=graphene.Int(),
                                name=graphene.String())
    workorders    = graphene.List(WorkOrderType)
    def resolve_workorder(self, info, **kwargs):
          id    = kwargs.get('id')
          name  = kwargs.get('name')
          if id is not None:
              return WorkOrder.objects.get(pk=id)
          if name is not None:
              return WorkOrder.objects.get(name=name)
          return None
    def resolve_workorders(self,info,**kwargs):
        return WorkOrder.objects.all()