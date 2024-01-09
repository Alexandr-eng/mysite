from rest_framework.routers import DefaultRouter

from shop.views import UserModelViewSet, CategoryModelViewSet, \
    WarhouseModelViewSet, ProductModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('categories', CategoryModelViewSet)
router.register('warhouses', WarhouseModelViewSet)
router.register('products', ProductModelViewSet)

urlpatterns = [


]
urlpatterns.extend(router.urls)