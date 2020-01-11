import graphene
from graphene import relay, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from product.models import Product
from workorder.models import WorkOrder
from serialnumber.models import SerialNumber
from operation.models import Operation
from routing.models import Routing,RoutingDetail


class RoutingType(DjangoObjectType):
    class Meta:
        model = Routing
        # interfaces = (relay.Node, )

class RoutingDetailType(DjangoObjectType):
    class Meta:
        model = RoutingDetail
        # interfaces = (relay.Node, )

class OperationType(DjangoObjectType):
    class Meta:
        model = Operation
        interfaces = (relay.Node, )

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ['name', 'slug']
        interfaces = (relay.Node, )

class WorkOrderType(DjangoObjectType):
    class Meta:
        model = WorkOrder
        interfaces = (relay.Node, )

class SerialNumberType(DjangoObjectType):
    # currentOperation = graphene.String()
    class Meta:
        model = SerialNumber
        interfaces = (relay.Node,)
    # def resolve_currentOperation(self, info):
    #     return self.current_operation
# ------------------------------------------------

class Query(graphene.ObjectType):  
    # Operation
    operation     = graphene.Field(OperationType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                slug=graphene.String())
    operations    = graphene.List(OperationType)#DjangoFilt,erConnectionField(ProductType)#
    def resolve_operation(self, info, **kwargs):
          id    = kwargs.get('id')
          name  = kwargs.get('name')
          slug  = kwargs.get('slug')
          if id is not None:
              return Operation.objects.get(pk=id)
          if name is not None:
              return Operation.objects.get(name=name)
          if slug is not None:
              return Operation.objects.get(slug=slug)
          return None
    def resolve_operations(self,info,**kwargs):
        return Operation.objects.all()

    # Routing
    routing     = graphene.Field(RoutingType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                slug=graphene.String())
    routings    = graphene.List(RoutingType)#DjangoFilt,erConnectionField(ProductType)#
    def resolve_routing(self, info, **kwargs):
          id    = kwargs.get('id')
          name  = kwargs.get('name')
          slug  = kwargs.get('slug')
          if id is not None:
              return Routing.objects.get(pk=id)
          if name is not None:
              return Routing.objects.get(name=name)
          if slug is not None:
              return Routing.objects.get(slug=slug)
          return None
    def resolve_routings(self,info,**kwargs):
        return Routing.objects.all()


    # RoutingDetail
    routingdetail     = graphene.Field(RoutingDetailType,
                                route=graphene.String(),
                                operation=graphene.String())
    routingdetails    = graphene.List(RoutingDetailType,
                                route=graphene.String())#DjangoFilt,erConnectionField(ProductType)#
    def resolve_routingdetail(self, info, **kwargs):
          route  = kwargs.get('route')
          operation  = kwargs.get('operation')
          if route is not None and operation is not None :
              return RoutingDetail.objects.get(routing=route,operation=operation)
          return None
    def resolve_routingdetails(self,info,**kwargs):
        route  = kwargs.get('route')
        if route is not None:
            return RoutingDetail.objects.filter(routing=route)
        return None



  # Product
    product     = graphene.Field(ProductType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                slug=graphene.String())
    products    = graphene.List(ProductType)#DjangoFilt,erConnectionField(ProductType)#
    def resolve_product(self, info, **kwargs):
          id    = kwargs.get('id')
          name  = kwargs.get('name')
          slug  = kwargs.get('slug')
          if id is not None:
              return Product.objects.get(pk=id)
          if name is not None:
              return Product.objects.get(name=name)
          if slug is not None:
              return Product.objects.get(slug=slug)
          return None
    def resolve_products(self,info,**kwargs):
        return Product.objects.all()

# WorkOrder
    workorder   = graphene.Field(WorkOrderType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                slug=graphene.String())
    workorders    = graphene.List(WorkOrderType)
    def resolve_workorder(self, info, **kwargs):
          id    = kwargs.get('id')
          name  = kwargs.get('name')
          slug  = kwargs.get('slug')
          if id is not None:
              return WorkOrder.objects.get(pk=id)
          if name is not None:
              return WorkOrder.objects.get(name=name)
          if slug is not None:
              return WorkOrder.objects.get(slug=slug)
          return None
    def resolve_workorders(self,info,**kwargs):
        return WorkOrder.objects.all()

# Serial number
    serialnumber   = graphene.Field(SerialNumberType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                slug=graphene.String())
    serialnumbers    = graphene.List(SerialNumberType,
                                workorder = graphene.String() )
    def resolve_serialnumber(self, info, **kwargs):
          id    = kwargs.get('id')
          name  = kwargs.get('name')
          slug  = kwargs.get('slug')
          if id is not None:
              return SerialNumber.objects.get(pk=id)
          if name is not None:
              return SerialNumber.objects.get(name=name)
          if slug is not None:
              return SerialNumber.objects.get(slug=slug)
          return None
    def resolve_serialnumbers(self,info,**kwargs):
        wo  = kwargs.get('workorder')
        if wo is not None:
              return SerialNumber.objects.filter(workorder=wo)
        return SerialNumber.objects.all()